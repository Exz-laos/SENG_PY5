import json
import os
import random
import streamlit as st
from data import all_questions  # Directly importing the dataset from data.py

# ---------------------------------------------------------
# Configuration & OK Storage Setup
# ---------------------------------------------------------
st.set_page_config(page_title="English Exam Prep", page_icon="📝", layout="centered")

OK_FILE = "ok_questions.json"

def load_ok_ids():
    """Loads the list of OK'd question IDs from a local file."""
    if os.path.exists(OK_FILE):
        with open(OK_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_ok_ids(ids_list):
    """Saves the list of OK'd question IDs to a local file."""
    with open(OK_FILE, "w", encoding="utf-8") as f:
        json.dump(ids_list, f)

# Initialize Session States
if "ok_ids" not in st.session_state:
    st.session_state.ok_ids = load_ok_ids()

def initialize_quiz(filtered_questions, num_questions):
    """Selects a random sample of questions and stores them in session state."""
    selected_sample = random.sample(
        filtered_questions, min(num_questions, len(filtered_questions))
    )

    quiz_set = []
    for item in selected_sample:
        # Create a copy and shuffle only if options exist
        shuffled_options = list(item.get("options", []))
        if shuffled_options:
            random.shuffle(shuffled_options)

        quiz_set.append(
            {
                "id": item["id"],
                "category": item.get("category", "General"),
                "question": item["question"],
                "options": shuffled_options,
                "correct_answer": item["correct_answer"],
                "explanation": item["explanation"],
            }
        )

    st.session_state.quiz_questions = quiz_set
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answers_submitted = {}
    st.session_state.quiz_finished = False


# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
st.sidebar.header("⚙️ Quiz Settings")

if not all_questions:
    st.error("No questions found in data.py!")
    st.stop()

min_id = min(q["id"] for q in all_questions)
max_id = max(q["id"] for q in all_questions)

id_range = st.sidebar.slider(
    "Select Question ID Range",
    min_value=min_id,
    max_value=max_id,
    value=(min_id, max_id),
)

# Extract all unique categories from the dataset
all_categories = sorted(list(set(q.get("category", "General") for q in all_questions)))

# Add a multi-select box for categories
selected_categories = st.sidebar.multiselect(
    "Select Categories to Study",
    options=all_categories,
    default=all_categories
)

# Option to include or exclude OK'd questions
exclude_ok = st.sidebar.checkbox("Exclude 'OK' questions", value=True)

# Filter questions based on range, category, and OK status
filtered_questions = []
for q in all_questions:
    if id_range[0] <= q["id"] <= id_range[1]:
        # Check if the question's category is selected
        if q.get("category", "General") in selected_categories:
            if exclude_ok and q["id"] in st.session_state.ok_ids:
                continue  # Skip OK'd questions
            filtered_questions.append(q)

st.sidebar.info(f"📚 Available Questions in pool: **{len(filtered_questions)}**")

num_to_test = st.sidebar.number_input(
    "Number of questions to pick",
    min_value=1,
    max_value=max(1, len(filtered_questions)) if filtered_questions else 1,
    value=min(10, max(1, len(filtered_questions))),
)

if st.sidebar.button("🎲 Generate New Quiz", type="primary", use_container_width=True):
    if filtered_questions:
        initialize_quiz(filtered_questions, num_to_test)
    else:
        st.sidebar.error("No questions available! Adjust range, select categories, or uncheck 'Exclude OK'.")

# ---------------------------------------------------------
# OK Manager (Sidebar)
# ---------------------------------------------------------
st.sidebar.divider()
st.sidebar.header("✅ Mastery Progress")

# Global Mastery Progress Bar
total_dataset_q = len(all_questions)
mastered_q = len(st.session_state.ok_ids)
mastery_percentage = (mastered_q / total_dataset_q) if total_dataset_q > 0 else 0

st.sidebar.progress(mastery_percentage)
st.sidebar.caption(f"You have mastered **{mastered_q} / {total_dataset_q}** questions ({(mastery_percentage*100):.1f}%).")

if st.session_state.ok_ids:
    with st.sidebar.expander("View & Cancel OK Status"):
        for q_id in st.session_state.ok_ids:
            # Find the first 30 chars of the question for the label
            q_text = next((q["question"] for q in all_questions if q["id"] == q_id), "Unknown Question")
            st.write(f"**ID {q_id}**: {q_text[:25]}...")
            if st.button(f"❌ Cancel OK for ID {q_id}", key=f"cancel_ok_{q_id}"):
                st.session_state.ok_ids.remove(q_id)
                save_ok_ids(st.session_state.ok_ids)
                st.rerun()
else:
    st.sidebar.info("No questions marked as OK yet.")

# Ensure quiz is initialized on first load
if "quiz_questions" not in st.session_state:
    if filtered_questions:
        initialize_quiz(filtered_questions, num_to_test)
    else:
        st.warning("Please adjust the settings in the sidebar to generate a quiz.")
        st.stop()


# ---------------------------------------------------------
# Main Quiz UI
# ---------------------------------------------------------
st.title("📝 Comprehensive English Exam Prep")
st.divider()

if st.session_state.get("quiz_finished", False):
    # --- RESULT SCREEN ---
    st.balloons()
    st.success("🎉 Quiz Completed!")
    
    final_score = st.session_state.score
    total_q = len(st.session_state.quiz_questions)
    percentage = (final_score / total_q) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Questions", total_q)
    col2.metric("Correct Answers", final_score)
    col3.metric("Final Score", f"{percentage:.1f}%")

    st.divider()
    if st.button("🔄 Start a New Quiz", type="primary", use_container_width=True):
        if filtered_questions:
            initialize_quiz(filtered_questions, num_to_test)
            st.rerun()
        else:
            st.error("No questions left in this pool!")

else:
    # --- QUESTION SCREEN ---
    current_idx = st.session_state.current_index
    questions = st.session_state.quiz_questions
    current_q = questions[current_idx]

    # Progress Bar
    progress_val = (current_idx + 1) / len(questions)
    st.progress(progress_val)
    st.caption(f"Question {current_idx + 1} of {len(questions)} | Category: **{current_q['category']}** | ID: {current_q['id']}")

    # Display Question
    st.markdown(f"### Q{current_idx + 1}. \n\n{current_q['question']}")

    is_submitted = current_idx in st.session_state.answers_submitted

    # Radio options (Disable it if the user already submitted an answer for this question)
    selected_option = st.radio(
        "Choose your answer:",
        options=current_q["options"],
        key=f"q_{current_idx}",
        index=None,
        disabled=is_submitted 
    )

    # Submit Answer Button
    if not is_submitted:
        if st.button("Submit Answer", type="primary"):
            if selected_option is None:
                st.warning("⚠️ Please select an answer before submitting.")
            else:
                st.session_state.answers_submitted[current_idx] = selected_option
                if selected_option == current_q["correct_answer"]:
                    st.session_state.score += 1
                st.rerun()
    else:
        # --- EXPLANATION & FEEDBACK SCREEN ---
        user_choice = st.session_state.answers_submitted[current_idx]
        correct_choice = current_q["correct_answer"]

        if user_choice == correct_choice:
            st.success("✅ **Correct!**")
        else:
            st.error(f"❌ **Incorrect.**")
            st.warning(f"**You selected:** {user_choice}\n\n**Correct Answer:** {correct_choice}")

        with st.expander("📖 View Detailed Explanation", expanded=True):
            st.markdown(current_q['explanation'])

    st.divider()
    
    # ---------------------------------------------------------
    # Navigation & OK Controls (Previous / Mark OK / Next)
    # ---------------------------------------------------------
    nav_col1, nav_col2, nav_col3 = st.columns(3)

    with nav_col1:
        if current_idx > 0:
            if st.button("⬅️ Previous Question", use_container_width=True):
                st.session_state.current_index -= 1
                st.rerun()

    with nav_col2:
        # Check if already marked as OK
        if current_q["id"] not in st.session_state.ok_ids:
            if st.button("🟢 Mark as OK (Too Easy)", use_container_width=True):
                st.session_state.ok_ids.append(current_q["id"])
                save_ok_ids(st.session_state.ok_ids)
                st.toast("Saved! This question will be excluded from future quizzes.")
                st.rerun()
        else:
            st.success("✅ Marked as OK")

    with nav_col3:
        if current_idx < len(questions) - 1:
            # Require the user to submit an answer before proceeding to next
            if is_submitted:
                if st.button("Next Question ➡️", type="primary", use_container_width=True):
                    st.session_state.current_index += 1
                    st.rerun()
            else:
                st.button("Next Question ➡️", disabled=True, use_container_width=True, help="Submit an answer first!")
        else:
            if is_submitted:
                if st.button("🏁 Finish Quiz", type="primary", use_container_width=True):
                    st.session_state.quiz_finished = True
                    st.rerun()
            else:
                st.button("🏁 Finish Quiz", disabled=True, use_container_width=True, help="Submit an answer first!")