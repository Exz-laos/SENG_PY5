# --- 情報技術概論 中間試験 過去問題・予想問題 (Total: 35 Problems) ---

# ==========================================
# Question Variables
# ==========================================

q_1 = """1. 2進小数 0.101を10進小数に基数変換しなさい。"""

q_2 = """2. 4桁の2進整数1000を10進数に基数変換しなさい。ただし、2の補数で負数が表現されているとする。"""

q_3 = """3. 4桁の2進整数1000を2ビット算術右シフトした後の数を4桁の2進数で答えなさい。ただし、2の補数で負数が表現されているとする。"""

q_4 = """4. 10進数75を16進数で表しなさい。"""

q_5 = """5. 全体の1%が罹っている病気がある。この病気を調べる検査があり、その検査精度は右表の通りである（本当に病気の人に検査をすると90%は陽性と出るが、10%は陰性と出る。本当に病気でない健康な人に検査をすると90%は陰性と出るが、10%は陽性と出る）。
このとき、病気かどうか分からない人がこの検査を受けて陽性と出た。この人が本当に病気に罹っている確率をベイズの定理で求めたい。以下の問いに答えなさい。
(1) 検査で陽性が出る事象をAとするとき、その確率P(A)を答えなさい。
(2) 病気に罹っている事象をBとするとき、その確率P(B)を答えなさい。
(3) 病気の人が検査で陽性と出る条件付き確率P(A|B)を答えなさい。
(4) 検査で陽性と出た人が病気に罹っている確率P(B|A)を答えなさい。"""

q_6 = """6. 通常の表記による計算式 (a+(b*c))-d を逆ポーランド表記法で表記なさい。"""

q_7 = """7. 空の状態のスタックとキューの2つのデータ構造がある。これらに以下の同じデータ {1, 2, 3, 4} を同じ順番で入れた後にデータを取り出すとき、次の問いに答えなさい。
(1) スタックから2番目に取り出されるデータを答えなさい。
(2) キューから2番目に取り出されるデータを答えなさい。"""

q_8 = """8. 次の探索アルゴリズムの時間計算量をオーダー記法 (O(?)) で答えなさい。
(1) 線形探索法
(2) 2分探索法
(3) ハッシュ表を用いる方法 (ハッシュ値は衝突しない場合)"""

q_9 = """9. 次の整列(ソート) アルゴリズムの時間計算量をオーダー記法 (O(?)) で答えなさい。
(1) クイックソート
(2) バブルソート
(3) 選択ソート"""

q_10 = """10. コンピュータの高速化技術の一つであるメモリインタリーブに関する記述として、適切なものはどれか。
ア: 主記憶と入出力装置、又は主記憶同士のデータの受渡しをCPU経由でなく直接やり取りする方式
イ: 主記憶にデータを送り出す際に、データをキャッシュに書き込み、キャッシュがあふれたときに主記憶へ書き込む方式
ウ: 主記憶のデータの一部をキャッシュにコピーすることによって、レジスタと主記憶とのアクセス速度の差を縮める方式
エ: 主記憶を複数の独立して動作するグループに分けて、各グループに並列にアクセスする方式"""

q_11 = """11. 数値を2進数で格納するレジスタがある。このレジスタに正の整数xを設定した後、レジスタの値を2ビット左にシフトして、xを加える操作を行うと、レジスタの値はxの何倍になるか。ここで、あふれ(オーバーフロー)は発生しないものとする。"""

q_12 = """12. 以下の説明に最も合うマークアップ言語を HTML、SGML、XML、UML の中から選んで答えなさい。
(1) 企業間の電子商取引の文書標準化に利用される、文書の標準化やデータ交換を目的とした言語。
(2) WWWのホームページの記述に使われる言語
(3) 電子文書交換のために国際規格として標準化された文書定義言語"""

q_13 = """13. 1GHzのクロックで動作するCPUがある。このCPUのCPI (Clock Cycles per Instruction)が2のとき、次の問いに答えなさい。
(1) このCPUの平均命令実行時間を答えなさい。
(2) このCPUのMIPS数を答えなさい。"""

q_14 = """14. 次の説明に最も合うメモリを SRAM、DRAM、ROM、フラッシュメモリ から1つ選んで答えなさい。
(1) 書き込みおよび消去を一括またはブロック単位で行う不揮発性メモリ。
(2) データを保持するためのリフレッシュ操作が不要な揮発性メモリ。
(3) 電源が遮断された状態でも、記憶した情報を保持することができる。
(4) メモリセル構造が単純で高集積化できビット単価も安いため、パソコン等のメインメモリによく使われる。"""

q_15 = """15. キャッシュメモリのアクセス時間は1ナノ秒、メインメモリのアクセス時間は10ナノ秒、キャッシュのヒット率は80%のとき、実効アクセス時間はいくらか。"""

q_16 = """16. アナログ音声信号をサンプリング周波数8kHz、量子化ビット数8ビットでデジタルデータ化して伝送するとき、その伝送速度はいくらか。
【ア 1.5M bit/秒   イ 256k bit/秒   ウ 64k bit/秒   エ 8k bit/秒】"""

q_17 = """17. 次のBNFで定義される<変数名>に合致するものはどれか
【ア _B39   イ 246   ウ 3E5   エ F5_1】
<数字> ::= 0|1|2|3|4|5|6|7|8|9
<英字> ::= A|B|C|D|E|F
<英数字> ::= <英字>|<数字>|_
<変数名> ::= <英字>|<変数名><英数字>"""

q_18 = """18. 処理装置を構成する要素のうち、分岐命令の実行によって更新されるものはどれか、次の中から選びなさい。
【ア インデックスレジスタ   イ 汎用レジスタ   ウ プログラムレジスタ (プログラムカウンタ)   エ 命令レジスタ】"""

q_19 = """19. 複数のプロセスから同時に呼び出されたときに、互いに干渉することなく並行して動作することができるプログラムの性質を表すものはどれか。次の中から選びなさい。
【ア リエントラント   イ リカーシブ   ウ リユーザブル   エ リロケータブル】"""

q_20 = """20. X・Y・Z + X̅・Y・Z と等価な論理式はどれか。次の中から選びなさい。ここで「・」は論理積、「+」は論理和、「X̅」はXの否定を表す。
【ア X・Y・Z   イ X̅・(Y+Z)   ウ Y・Z   エ Y+Z】"""

q_21 = """21. サブルーチンへの引数の渡し方のうち、変数を引数として渡してもサブルーチンの実行後にその変数の値が変更されないことが補償されているものはどれか。
【ア 値渡し(値呼出し)   イ 結果渡し(結果呼出し)   ウ 参照渡し(参照呼出し)   エ 名前渡し(名前呼出し)】"""

q_22 = """22. ある試験の点数は、平均70点、標準偏差5の分布となった。この試験で60点の偏差値はいくらか。"""

q_ex_1 = """予想1. 10個から3つ選び順に並べた場合の数(順列)を答えよ。"""

q_ex_2 = """予想2. 10個から3つ選ぶ場合の数(組合せ)を答えよ。"""

q_ex_3 = """予想3. コインを3回投げて裏表を調べる。1回目が表のとき、表が2回でる条件付き確率を求めよ。(※講義資料の修正に基づく)"""

q_ex_4 = """予想4. スタックとキューの最も大きな違いを簡潔に説明せよ。"""

q_ex_5 = """予想5. 10, 9, 8, 7, 6, 5, 4のデータが格納された2分探索木を図で描きなさい(根の数字と配置ルールを答えよ)。"""

q_ex_6 = """予想6. 問5の2分探索木で「5」を探索する時、見つかるまでの繰返し回数(比較の回数)は何回か。"""

q_ex_7 = """予想7. 単方向リストに昇順にデータが格納されているとするとき、指定されたデータがリストのどこに格納されているかを探索する処理の計算量を答えなさい。"""

q_ex_8 = """予想8. 16進数の9個のデータ 1A, 35, 3B, 54, 8E, A1, AF, B2, B3 をこの順にハッシュ表に入れる。ハッシュ値としてデータを8で割った余りとするとき、最初に衝突が起こるデータを答えよ。"""

q_ex_9 = """予想9. 文字サイズなど文書の体裁を記述する言語を以下から選べ。
【DTD, CSS, XSL, SOAP, SVG】"""

q_ex_10 = """予想10. C++言語に対してJava言語の最も大きな利点は何か。"""

q_ex_11 = """予想11. webサーバからダウンロードされWebブラウザ上で動作するJavaプログラムを何と言うか下記から選べ。
【Java servlet, Java applet, Java VM, Javaアプリケーション】"""

q_ex_12 = """予想12. すべての命令が5サイクルで完了するパイプライン制御のコンピュータでは、20命令を実行するには何サイクル必要か。"""

q_ex_13 = """予想13. コンピュータの5大装置を答えよ。"""


# ==========================================
# Flashcard Data (Japanese)
# ==========================================

flashcard_data = {
    q_1: """Answer: 0.625

Explanation: 2進数の小数を10進数に変換するには、各桁に重み(2のマイナスn乗)を掛け合わせます。
・小数第1位: 1 * 0.5 = 0.5
・小数第3位: 1 * 0.125 = 0.125
合計: 0.5 + 0.125 = 0.625
Reference: <<joho1.pdf, p11-12>>""",

    q_2: """Answer: -8

Explanation: 2の補数表現では、最上位ビット(MSB)が1の場合、負の数です。絶対値を求めるためにビットを反転して1を足します。1000を反転すると0111、これに1を足すと1000(10進数で8)。負数なので-8となります。
Reference: <<joho1.pdf, p23-24>>



""",

    q_3: """Answer: 1110

Explanation: 算術右シフトとは、符号ビット(MSB)の値を保持したまま右にビットをずらす演算です。1000を右に2ビットシフトし、空いた左側の2ビットに元の符号ビット(1)を入れるため1110になります。
Reference: <<joho2.pdf, p7>>

กฎ 2 ข้อของการเลื่อนบิตทางขวาแบบคณิตศาสตร์ (Arithmetic Right Shift):

ทิ้งบิตขวาสุด — ทุกครั้งที่เลื่อน บิตที่อยู่ขวาสุดจะหายไป
เติมบิตซ้ายสุดด้วย sign bit (1) — เนื่องจากเป็นจำนวนลบ ช่องว่างทางซ้ายที่เกิดขึ้นจะต้องใส่ 1 เสมอ (ถ้าใส่ 0 จะกลายเป็นจำนวนบวกแทน!)


การเลื่อนบิตทางซ้ายแบบคณิตศาสตร์ (Arithmetic Left Shift)
กฎ 2 ข้อ:

ทิ้งบิตซ้ายสุด — ทุกครั้งที่เลื่อน บิตที่อยู่ซ้ายสุด (MSB) จะหายไป
เติมบิตขวาสุดด้วย 0 เสมอ — ช่องว่างทางขวาที่เกิดขึ้นจะใส่ 0 เสมอ (ไม่ว่าจะเป็นบวกหรือลบ)

""",

    q_4: """Answer: 4B

Explanation: 10進数を16進数に変換するには16で割り算を行います。75 / 16 = 4 余り 11。16進数で11は「B」なので、答えは4Bとなります。
Reference: <<joho1.pdf, p13>>
Step 1 — Memorize the hex digits
Dec  10 11 12 13 14 15
Hex  A  B  C  D  E  F
Step 2 — Keep dividing by 16

Divide the number by 16
Record the remainder each time

Stop when the quotient = 0

Step 3 — Read remainders bottom to top
The first remainder = least significant digit (right side), the last remainder = most significant digit (left side).

Memory trick for the division:

"16 × ? ≤ my number" — find the biggest multiple of 16 that fits, the leftover is your remainder.

For 75: 16 × 4 = 64, so quotient = 4, remainder = 75 − 64 = 11 = B

Quick sanity check:Always verify by converting back:

hex digit1×16+hex digit0=original number\text{hex digit}_1 \times 16 + \text{hex digit}_0 = \text{original number}hex digit1​×16+hex digit0​=original number
4×16+11=64+11=75✓4 \times 16 + 11 = 64 + 11 = 75 ✓4×16+11=64+11=75✓

例題: 10進数 255 を16進数に変換
255 ÷ 16 = 15 … 余り 15 → F
15 ÷ 16 = 0 … 余り 15 → F
余りを逆順に読む →　255(10)=FF(16)

例題: 10進数 100 を16進数に変換
100 ÷ 16 = 6 … 余り 4
6 ÷ 16 = 0 … 余り 6
余りを逆順に読む → 100(10)=64(16)

例題: 10進数 1000 を16進数に変換
1000 ÷ 16 = 62 … 余り 8
62 ÷ 16 = 3 … 余り 14 → E
3 ÷ 16 = 0 … 余り 3
余りを逆順に読む → 1000(10)=3E8(16)

例題: 10進数 16 を16進数に変換
16 ÷ 16 = 1 … 余り 0
1 ÷ 16 = 0 … 余り 1
余りを逆順に読む → 16(10)=10(16)
16(10)​=10(16)​​


""",

    q_5: """Answer: 
(1) 0.108
(2) 0.01
(3) 0.9
(4) 0.083

Explanation: ベイズの定理を用いて条件付き確率を求めます。
(1) P(A) = (0.01 * 0.9) + (0.99 * 0.1) = 0.108
(4) P(B|A) = (0.9 * 0.01) / 0.108 = 0.083
Reference: <<joho2.pdf, p25-26>>, <<joho4.pdf, p27>>

前提整理

病気の有病率：1% → P(B) = 0.01
病気の人が陽性：90% → P(A|B) = 0.90
健康な人が陽性：10% → P(A|B̄) = 0.10


(2) P(B) — 病気に罹っている確率
P(B)=0.01\boxed{P(B) = 0.01}P(B)=0.01​

(3) P(A|B) — 病気の人が陽性と出る条件付き確率
P(A∣B)=0.90\boxed{P(A|B) = 0.90}P(A∣B)=0.90​

(1) P(A) — 検査で陽性が出る確率
全確率の法則より：
P(A)=P(A∣B)⋅P(B)+P(A∣Bˉ)⋅P(Bˉ)P(A) = P(A|B)\cdot P(B) + P(A|\bar{B})\cdot P(\bar{B})P(A)=P(A∣B)⋅P(B)+P(A∣Bˉ)⋅P(Bˉ)
=0.90×0.01+0.10×0.99= 0.90 \times 0.01 + 0.10 \times 0.99=0.90×0.01+0.10×0.99
=0.009+0.099= 0.009 + 0.099=0.009+0.099
P(A)=0.108\boxed{P(A) = 0.108}P(A)=0.108​

(4) P(B|A) — 陽性だった人が本当に病気の確率
ベイズの定理より：
P(B∣A)=P(A∣B)⋅P(B)P(A)P(B|A) = \frac{P(A|B)\cdot P(B)}{P(A)}P(B∣A)=P(A)P(A∣B)⋅P(B)​
=0.90×0.010.108= \frac{0.90 \times 0.01}{0.108}=0.1080.90×0.01​
=0.0090.108= \frac{0.009}{0.108}=0.1080.009​
P(B∣A)=112≈0.0833≈8.3%\boxed{P(B|A) = \frac{1}{12} \approx 0.0833 \approx 8.3\%}P(B∣A)=121​≈0.0833≈8.3%​
""",

    q_6: """Answer: a b c * + d -

Explanation: 逆ポーランド記法(後置記法)では、演算子を被演算子の後ろに配置します。
1. b*c -> b c *
2. a+(b c *) -> a b c * +
3. (a b c * +)-d -> a b c * + d -
Reference: <<joho3.pdf, p23>>, <<joho4.pdf, p28>>
Example 1: a + b
Step 1 → a b +
Answer: a b +

Example 2: a + b - c
Step 1 — a + b → a b +
Step 2 — (a b +) - c → a b + c -
Answer: a b + c -

Example 3: (a + b) * (c - d)
Step 1 — a + b → a b +
Step 2 — c - d → c d -
Step 3 — (a b +) * (c d -) → a b + c d - *
Answer: a b + c d - *

Example 4: a * b + c * d
Step 1 — a * b → a b *
Step 2 — c * d → c d *
Step 3 — (a b *) + (c d *) → a b * c d * +
Answer: a b * c d * +

Example 5: (a + b) * c - d / e
Step 1 — a + b → a b +
Step 2 — d / e → d e /
Step 3 — (a b +) * c → a b + c *
Step 4 — (a b + c *) - (d e /) → a b + c * d e / -
Answer: a b + c * d e / -
""",

    q_7: """Answer: 
(1) 3
(2) 2

Explanation: 
スタックはLIFO(後入れ先出し)なので、取り出す順は 4 -> 3 -> 2 -> 1。よって2番目は3。
キューはFIFO(先入れ先出し)なので、取り出す順は 1 -> 2 -> 3 -> 4。よって2番目は2。
Reference: <<joho4.pdf, p8-9>>""",

    q_8: """Answer: 
(1) O(n)
(2) O(log n)
(3) O(1)

Explanation: 線形探索はデータ数に比例。2分探索は半分ずつ絞り込むため対数時間。ハッシュ表は直接場所を計算するため一定時間です。
Reference: <<joho4.pdf, p26>>""",

    q_9: """Answer: 
(1) O(n log n)
(2) O(n^2)
(3) O(n^2)

Explanation: クイックソートは基準値で分割していくため高速。バブルソートと選択ソートは繰り返し比較を行うため計算量が多くなります。
Reference: <<joho4.pdf, p31>>""",

    q_10: """Answer: エ

Explanation: メモリインタリーブは、メインメモリを「バンク」と呼ばれる複数の領域に分割し、並列アクセスすることでデータ転送の高速化を図る技術です。
Reference: <<joho6.pdf, p31>>""",

    q_11: """Answer: 5倍

Explanation: 2進数を左に2ビットシフトすると値は2^2 = 4倍になります(4x)。これに元の値xを加算するので 4x + x = 5x となり、5倍になります。
Reference: <<joho2.pdf, p5, p9>>""",

    q_12: """Answer: 
(1) XML
(2) HTML
(3) SGML

Explanation: XMLはデータ交換や独自のタグ定義が可能。HTMLはWebページ作成用。SGMLはISO標準化されたマークアップ言語の元祖です。
Reference: <<joho5.pdf, p23-24>>""",

    q_13: """Answer: 
(1) 2n秒 (2ナノ秒)
(2) 500 MIPS

Explanation: 1GHz = 1クロック1ナノ秒(1ns)。CPIが2なので 1命令あたり 2 * 1ns = 2ns。MIPSは1秒間に実行できる命令数(百万単位)なので 1 / (2 * 10^-9) = 500 * 10^6 で500 MIPS。
Reference: <<joho6.pdf, p19-20>>


前提
クロック周波数 f = 1 GHz = 10⁹ Hz
CPI = 2（1命令あたり2クロックサイクル）

(1) 平均命令実行時間
クロック周期 = 1 ÷ 10⁹ = 1 ns
命令実行時間 = CPI × クロック周期 = 2 × 1 ns
答え：2 ns

(2) MIPS数
MIPS = f ÷ (CPI × 10⁶) = 10⁹ ÷ (2 × 10⁶) = 1000 ÷ 2
答え：500 MIPS

まとめ
クロック周期 → 1 ns
平均命令実行時間 → 2 ns
MIPS → 500 MIPS
""",

    q_14: """Answer: 
(1) フラッシュメモリ
(2) SRAM
(3) ROM (またはフラッシュメモリ)
(4) DRAM

Explanation: フラッシュメモリはブロック単位の消去が特徴。SRAMはリフレッシュ不要。DRAMはリフレッシュが必要ですが大容量化が容易です。
Reference: <<joho6.pdf, p25-26>>""",

    q_15: """Answer: 2.8n秒

Explanation: 実効アクセス時間 = (キャッシュアクセス時間 * ヒット率) + (メインモリアクセス時間 * (1 - ヒット率))
(1ns * 0.8) + (10ns * 0.2) = 0.8 + 2.0 = 2.8ns
Reference: <<joho6.pdf, p29>>""",

    q_16: """Answer: ウ

Explanation: 伝送速度 = サンプリング周波数 * 量子化ビット数。 8,000Hz * 8bit = 64,000bit/秒 = 64kbps。
Reference: <<joho3.pdf, p22>>""",

    q_17: """Answer: エ

Explanation: <変数名>の定義により、変数の先頭文字は必ず<英字>(A〜F)でなければなりません。選択肢の中で先頭が英字なのはF5_1のみです。
Reference: <<joho3.pdf, p22>>""",

    q_18: """Answer: ウ

Explanation: プログラムレジスタ(プログラムカウンタ)は次に実行する命令のアドレスを記憶しており、分岐(ジャンプ)命令によってこのアドレス値が更新されます。
Reference: <<joho6.pdf, p8>>""",

    q_19: """Answer: ア

Explanation: リエントラント(再入可能)は、手続き部分とデータ部分が分離されており、複数のプロセスが同時に実行してもデータが競合しないプログラムの性質です。
Reference: <<joho5.pdf, p16>>""",

    q_20: """Answer: ウ

Explanation: 分配則を使ってY・Zでくくると (X + X̅)・YZ となります。相補性の法則により X + X̅ = 1 なので、結果は Y・Z です。
Reference: <<joho2.pdf, p16-17>>""",

    q_21: """Answer: ア

Explanation: 値渡し(Call by Value)は、変数の「値のコピー」だけを渡すため、サブルーチン内で値を変更しても呼び出し元の元の変数には影響しません。
Reference: <<joho5.pdf, p20>>""",

    q_22: """Answer: 30

Explanation: 偏差値の公式 50 + 10 * ((得点 - 平均点) / 標準偏差) に当てはめます。50 + 10 * ((60 - 70) / 5) = 50 - 20 = 30。
Reference: <<joho3.pdf, p11-12>>, <<joho4.pdf, p28>>""",

    q_ex_1: """Answer: 720

Explanation: 順列(Permutation)の計算です。順番を気にして選ぶため、10P3 = 10 * 9 * 8 = 720 通りとなります。
Reference: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>""",

    q_ex_2: """Answer: 120

Explanation: 組合せ(Combination)の計算です。順番を気にせず選ぶため、10C3 = (10 * 9 * 8) / (3 * 2 * 1) = 720 / 6 = 120 通りとなります。
Reference: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>""",

    q_ex_3: """Answer: 1/2

Explanation: 条件付き確率。1回目が表の事象(Y)は4通り。そのうち表が合計2回出る事象(X∩Y)は2通り。P(X|Y) = 2/4 = 1/2 となります。
Reference: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>""",

    q_ex_4: """Answer: スタックはLIFO、キューはFIFO

Explanation: スタック(Stack)は Last-In First-Out(後入れ先出し)。キュー(Queue)は First-In First-Out(先入れ先出し)です。
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>""",

    q_ex_5: """Answer: 根は「7」。ルールは「左の子 < 親 < 右の子」

Explanation: 2分探索木(Binary Search Tree)は中央値である7を根(Root)にし、左側に小さい数字、右側に大きい数字を配置します。
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>""",

    q_ex_6: """Answer: 2回

Explanation: 1回目の比較: 根の「7」と比較(左へ)。 2回目の比較: 次の節の「5」と比較して一致(探索終了)。
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>""",

    q_ex_7: """Answer: O(n)

Explanation: 単方向リスト(Singly Linked List)では、先頭からポインタをたどって順番に探す(線形探索)必要があるため、データ数に比例する O(n) の時間がかかります。
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p4>>""",

    q_ex_8: """Answer: B2

Explanation: 1A(10進数26) / 8 の余りは2。 B2(10進数178) / 8 の余りも2となり、同じ場所に格納しようとして衝突します。
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p4>>""",

    q_ex_9: """Answer: CSS

Explanation: CSS(Cascading Style Sheets)は、HTMLなどのマークアップ言語で書かれた文書のデザインやレイアウトを指定するための言語です。
Reference: <<joho5.pdf, p26>>, <<joho6.pdf, p3>>""",

    q_ex_10: """Answer: コンパイル済みプログラムでも異なるコンピュータで実行可能

Explanation: Java仮想マシン(JVM)の上で動作するため、OS環境が異なっても同じコンパイル済みプログラムを実行できます(Write once, run anywhere)。
Reference: <<joho5.pdf, p27>>, <<joho6.pdf, p4>>""",

    q_ex_11: """Answer: Java applet

Explanation: クライアント側(ブラウザ側)で動作する小さなJavaプログラムを Java applet と呼びます。サーバ側は Java servlet です。
Reference: <<joho5.pdf, p27>>, <<joho6.pdf, p4>>""",

    q_ex_12: """Answer: 24サイクル

Explanation: 最初の1命令目は完了するのにそのまま5サイクルかかりますが、残りの19命令は1サイクルごとに次々と完了します。 5 + (20-1) * 1 = 24サイクル。
Reference: <<joho6.pdf, p37>>, <<joho7.pdf, p5>>""",

    q_ex_13: """Answer: 制御装置、演算装置、記憶装置、入力装置、出力装置

Explanation: コンピュータを構成する必須の5要素です。
Reference: <<joho6.pdf, p37>>, <<joho7.pdf, p5>>"""
}


# ==========================================
# English Translations
# ==========================================

english_translations = {
    q_1: {
        "question": """1. Convert the binary fraction 0.101 to a decimal fraction.""",
        "answer": """Answer: 0.625

Explanation: To convert a binary fraction to a decimal, multiply each digit by its weight (2 to the power of -n).
- 1st decimal place: 1 * 0.5 = 0.5
- 3rd decimal place: 1 * 0.125 = 0.125
Total: 0.5 + 0.125 = 0.625
Reference: <<joho1.pdf, p11-12>>"""
    },
    q_2: {
        "question": """2. Convert the 4-digit binary integer 1000 to a decimal number. Assume negative numbers are represented in 2's complement.""",
        "answer": """Answer: -8

Explanation: In 2's complement representation, if the Most Significant Bit (MSB) is 1, it's a negative number. To find the absolute value, invert the bits and add 1. Inverting 1000 gives 0111, adding 1 gives 1000 (which is 8 in decimal). Since it's negative, the answer is -8.
Reference: <<joho1.pdf, p23-24>>"""
    },
    q_3: {
        "question": """3. What is the 4-digit binary result of applying a 2-bit arithmetic right shift to the 4-digit binary integer 1000? Assume negative numbers are in 2's complement.""",
        "answer": """Answer: 1110

Explanation: An arithmetic right shift moves bits to the right while preserving the sign bit (MSB). Shifting 1000 right by 2 bits leaves the 2 leftmost bits empty, which are then filled with the original sign bit (1), resulting in 1110.
Reference: <<joho2.pdf, p7>>"""
    },
    q_4: {
        "question": """4. Express the decimal number 75 in hexadecimal.""",
        "answer": """Answer: 4B

Explanation: To convert decimal to hexadecimal, divide by 16. 75 / 16 = 4 with a remainder of 11. In hexadecimal, 11 is represented by 'B', so the answer is 4B.
Reference: <<joho1.pdf, p13>>"""
    },
    q_5: {
        "question": """5. 1% of the population has a certain disease. The test accuracy is: 90% positive if sick, 10% negative; 90% negative if healthy, 10% positive. 
If a person tests positive, use Bayes' theorem to find:
(1) P(A): Probability of testing positive.
(2) P(B): Probability of having the disease.
(3) P(A|B): Probability of testing positive given the person is sick.
(4) P(B|A): Probability of having the disease given a positive test result.""",
        "answer": """Answer: 
(1) 0.108
(2) 0.01
(3) 0.9
(4) 0.083

Explanation: Using Bayes' theorem for conditional probability.
(1) P(A) = (0.01 * 0.9) + (0.99 * 0.1) = 0.108
(4) P(B|A) = (0.9 * 0.01) / 0.108 = 0.083
Reference: <<joho2.pdf, p25-26>>, <<joho4.pdf, p27>>"""
    },
    q_6: {
        "question": """6. Express the mathematical formula (a+(b*c))-d in Reverse Polish Notation.""",
        "answer": """Answer: a b c * + d -

Explanation: In Reverse Polish Notation (postfix), operators are placed after their operands. Evaluating from the innermost parentheses:
1. b*c -> b c *
2. a+(b c *) -> a b c * +
3. (a b c * +)-d -> a b c * + d -
Reference: <<joho3.pdf, p23>>, <<joho4.pdf, p28>>"""
    },
    q_7: {
        "question": """7. For an empty stack and an empty queue, data {1, 2, 3, 4} is inserted in that order. When retrieving data, answer the following:
(1) What is the 2nd piece of data retrieved from the stack?
(2) What is the 2nd piece of data retrieved from the queue?""",
        "answer": """Answer: 
(1) 3
(2) 2

Explanation: 
Stack is LIFO (Last-In First-Out), so retrieval order is 4 -> 3 -> 2 -> 1. The 2nd is 3.
Queue is FIFO (First-In First-Out), so retrieval order is 1 -> 2 -> 3 -> 4. The 2nd is 2.
Reference: <<joho4.pdf, p8-9>>"""
    },
    q_8: {
        "question": """8. Give the time complexity in Big-O notation (O(?)) for the following search algorithms:
(1) Linear search
(2) Binary search
(3) Hash table (assuming no hash collisions)""",
        "answer": """Answer: 
(1) O(n)
(2) O(log n)
(3) O(1)

Explanation: Linear search is proportional to the number of data items. Binary search halves the search space each time, giving logarithmic time. Hash tables calculate the location directly, taking constant time.
Reference: <<joho4.pdf, p26>>"""
    },
    q_9: {
        "question": """9. Give the time complexity in Big-O notation (O(?)) for the following sorting algorithms:
(1) Quick sort
(2) Bubble sort
(3) Selection sort""",
        "answer": """Answer: 
(1) O(n log n)
(2) O(n^2)
(3) O(n^2)

Explanation: Quick sort divides the array by a pivot, making it fast. Bubble sort and selection sort require repeated comparisons, resulting in a quadratic time complexity.
Reference: <<joho4.pdf, p31>>"""
    },
    q_10: {
        "question": """10. Which statement correctly describes memory interleaving, a computer speed-up technique?
A: Direct data transfer between main memory and I/O devices without going through the CPU.
B: Writing data to cache first, then to main memory when the cache overflows.
C: Copying part of main memory data to cache to reduce the access speed gap with registers.
D: Dividing main memory into multiple independently operating groups accessed in parallel.""",
        "answer": """Answer: D

Explanation: Memory interleaving divides the main memory into multiple areas called "banks" and allows parallel access to speed up data transfer.
Reference: <<joho6.pdf, p31>>"""
    },
    q_11: {
        "question": """11. A register stores a positive binary integer x. If its value is shifted left by 2 bits and x is added to it, by what multiple does the register's value increase? (Assume no overflow).""",
        "answer": """Answer: 5 times

Explanation: Shifting a binary number left by 2 bits multiplies its value by 2^2 = 4 (making it 4x). Adding the original value x gives 4x + x = 5x.
Reference: <<joho2.pdf, p5, p9>>"""
    },
    q_12: {
        "question": """12. Choose the markup language that best fits each description from [HTML, SGML, XML, UML]:
(1) Used for document standardization and data exchange in B2B electronic commerce.
(2) Used to describe WWW homepages.
(3) A document definition language standardized as an international standard for electronic document exchange.""",
        "answer": """Answer: 
(1) XML
(2) HTML
(3) SGML

Explanation: XML allows custom tags and is used for data exchange. HTML is for creating web pages. SGML is the ISO-standardized ancestor of markup languages.
Reference: <<joho5.pdf, p23-24>>"""
    },
    q_13: {
        "question": """13. A CPU operates at a 1GHz clock speed with a CPI (Clock Cycles per Instruction) of 2. 
(1) What is the average instruction execution time?
(2) What is the MIPS rating of this CPU?""",
        "answer": """Answer: 
(1) 2 ns (2 nanoseconds)
(2) 500 MIPS

Explanation: 1GHz means 1 clock cycle is 1 nanosecond (1ns). With a CPI of 2, one instruction takes 2 * 1ns = 2ns. MIPS (Millions of Instructions Per Second) is calculated as 1 / (2 * 10^-9) = 500 * 10^6, which is 500 MIPS.
Reference: <<joho6.pdf, p19-20>>"""
    },
    q_14: {
        "question": """14. Choose the memory type that best fits each description from [SRAM, DRAM, ROM, Flash memory]:
(1) Non-volatile memory where writing and erasing are done in bulk or block units.
(2) Volatile memory that does not require a refresh operation to retain data.
(3) Can retain stored information even when the power is turned off.
(4) Commonly used as main memory in PCs because of its simple cell structure, high density, and low cost per bit.""",
        "answer": """Answer: 
(1) Flash memory
(2) SRAM
(3) ROM (or Flash memory)
(4) DRAM

Explanation: Flash memory erases in block units. SRAM is fast and requires no refresh. DRAM uses capacitors and requires refreshing but is easily manufactured with large capacities.
Reference: <<joho6.pdf, p25-26>>"""
    },
    q_15: {
        "question": """15. If the cache memory access time is 1 ns, the main memory access time is 10 ns, and the cache hit rate is 80%, what is the effective access time?""",
        "answer": """Answer: 2.8 ns

Explanation: Effective access time = (Cache access time * Hit rate) + (Main memory access time * (1 - Hit rate)).
(1ns * 0.8) + (10ns * 0.2) = 0.8 + 2.0 = 2.8ns.
Reference: <<joho6.pdf, p29>>"""
    },
    q_16: {
        "question": """16. When an analog audio signal is digitized at a sampling frequency of 8kHz and a quantization bit rate of 8 bits and then transmitted, what is the transmission speed?
[A: 1.5M bit/s, B: 256k bit/s, C: 64k bit/s, D: 8k bit/s]""",
        "answer": """Answer: C (64k bit/s)

Explanation: Transmission speed = Sampling frequency * Quantization bits. 8,000 Hz * 8 bits = 64,000 bits/sec = 64 kbps.
Reference: <<joho3.pdf, p22>>"""
    },
    q_17: {
        "question": """17. Which of the following matches the <variable_name> defined by the given BNF?
[A: _B39, B: 246, C: 3E5, D: F5_1]
<digit> ::= 0|1|2|3|4|5|6|7|8|9
<letter> ::= A|B|C|D|E|F
<alphanumeric> ::= <letter>|<digit>|_
<variable_name> ::= <letter>|<variable_name><alphanumeric>""",
        "answer": """Answer: D (F5_1)

Explanation: According to the definition of <variable_name>, the first character must always be a <letter> (A-F). Among the choices, only F5_1 starts with a letter.
Reference: <<joho3.pdf, p22>>"""
    },
    q_18: {
        "question": """18. Among the components of a processing unit, which one is updated by the execution of a branch instruction?
[A: Index register, B: General-purpose register, C: Program register (Program counter), D: Instruction register]""",
        "answer": """Answer: C (Program register / Program counter)

Explanation: The program register (program counter) stores the address of the next instruction to be executed. A branch (jump) instruction updates this address value.
Reference: <<joho6.pdf, p8>>"""
    },
    q_19: {
        "question": """19. Which program property allows it to operate concurrently without interference when called simultaneously by multiple processes?
[A: Reentrant, B: Recursive, C: Reusable, D: Relocatable]""",
        "answer": """Answer: A (Reentrant)

Explanation: A reentrant program separates its procedure and data parts, preventing data conflicts even when multiple processes execute it simultaneously.
Reference: <<joho5.pdf, p16>>"""
    },
    q_20: {
        "question": """20. Which logical expression is equivalent to X・Y・Z + X̅・Y・Z? (Where '・' is logical AND, '+' is logical OR, and 'X̅' is NOT X).
[A: X・Y・Z, B: X̅・(Y+Z), C: Y・Z, D: Y+Z]""",
        "answer": """Answer: C (Y・Z)

Explanation: By factoring out Y・Z using the distributive law, you get (X + X̅)・YZ. By the law of complementarity, X + X̅ = 1, so the result is Y・Z.
Reference: <<joho2.pdf, p16-17>>"""
    },
    q_21: {
        "question": """21. Among the methods of passing arguments to a subroutine, which one guarantees that the value of the variable will not be changed after the subroutine executes?
[A: Call by value, B: Call by result, C: Call by reference, D: Call by name]""",
        "answer": """Answer: A (Call by value)

Explanation: Call by value only passes a "copy of the value," so any modifications made inside the subroutine do not affect the original variable in the caller.
Reference: <<joho5.pdf, p20>>"""
    },
    q_22: {
        "question": """22. The scores of an exam formed a distribution with a mean of 70 and a standard deviation of 5. What is the deviation score (T-score) of a score of 60 on this exam?""",
        "answer": """Answer: 30

Explanation: Apply the T-score formula: 50 + 10 * ((Score - Mean) / Standard Deviation). 50 + 10 * ((60 - 70) / 5) = 50 - 20 = 30.
Reference: <<joho3.pdf, p11-12>>, <<joho4.pdf, p28>>"""
    },
    q_ex_1: {
        "question": """Expected 1. How many ways are there to choose 3 items from 10 and arrange them in order (Permutation)?""",
        "answer": """Answer: 720

Explanation: This is a permutation calculation. Since order matters, 10P3 = 10 * 9 * 8 = 720 ways.
Reference: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>"""
    },
    q_ex_2: {
        "question": """Expected 2. How many ways are there to choose 3 items from 10 (Combination)?""",
        "answer": """Answer: 120

Explanation: This is a combination calculation. Order doesn't matter, so 10C3 = (10 * 9 * 8) / (3 * 2 * 1) = 720 / 6 = 120 ways.
Reference: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>"""
    },
    q_ex_3: {
        "question": """Expected 3. A coin is tossed 3 times. If the first toss is heads, what is the conditional probability of getting exactly 2 heads in total?""",
        "answer": """Answer: 1/2

Explanation: Conditional probability. Event Y (1st is heads) has 4 outcomes. Event X∩Y (1st is heads AND exactly 2 heads total) has 2 outcomes. P(X|Y) = 2/4 = 1/2.
Reference: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>"""
    },
    q_ex_4: {
        "question": """Expected 4. Briefly explain the biggest difference between a stack and a queue.""",
        "answer": """Answer: Stack is LIFO, Queue is FIFO

Explanation: A Stack uses Last-In First-Out (LIFO), retrieving the most recently stored data first. A Queue uses First-In First-Out (FIFO), retrieving the oldest data first.
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>"""
    },
    q_ex_5: {
        "question": """Expected 5. What is the root number and the placement rule for a binary search tree storing the data 10, 9, 8, 7, 6, 5, 4?""",
        "answer": """Answer: Root is 7. Rule: Left child < Parent < Right child

Explanation: A binary search tree places the median value (7) at the root, smaller values on the left branches, and larger values on the right branches.
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>"""
    },
    q_ex_6: {
        "question": """Expected 6. When searching for '5' in the binary search tree from Question 5, how many comparisons (repetitions) are made until it is found?""",
        "answer": """Answer: 2 times

Explanation: 1st comparison: compare with root '7' (move left). 2nd comparison: compare with node '5' and it matches (search ends).
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>"""
    },
    q_ex_7: {
        "question": """Expected 7. If data is stored in ascending order in a singly linked list, what is the time complexity of the process to search for the location of specified data?""",
        "answer": """Answer: O(n)

Explanation: In a singly linked list, you cannot jump directly to a location; you must follow pointers from the head one by one (linear search), taking time proportional to the number of elements, O(n).
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p4>>"""
    },
    q_ex_8: {
        "question": """Expected 8. Nine hexadecimal data items (1A, 35, 3B, 54, 8E, A1, AF, B2, B3) are inserted into a hash table in this order. If the hash value is the remainder of the data divided by 8, which data item causes the first collision?""",
        "answer": """Answer: B2

Explanation: The remainder of 1A (decimal 26) / 8 is 2. The remainder of B2 (decimal 178) / 8 is also 2. They attempt to store at the same location, causing a collision.
Reference: <<joho4.pdf, p33>>, <<joho5.pdf, p4>>"""
    },
    q_ex_9: {
        "question": """Expected 9. Choose the language that describes the format of a document, such as font size, from the following: [DTD, CSS, XSL, SOAP, SVG]""",
        "answer": """Answer: CSS

Explanation: CSS (Cascading Style Sheets) is a language used to specify the design and layout (font size, color, positioning, etc.) of documents written in markup languages like HTML.
Reference: <<joho5.pdf, p26>>, <<joho6.pdf, p3>>"""
    },
    q_ex_10: {
        "question": """Expected 10. What is the biggest advantage of the Java language compared to the C++ language?""",
        "answer": """Answer: Compiled programs can be executed on different computers.

Explanation: Because Java runs on the Java Virtual Machine (JVM), the same compiled program can be executed regardless of the OS or hardware environment ("Write once, run anywhere").
Reference: <<joho5.pdf, p27>>, <<joho6.pdf, p4>>"""
    },
    q_ex_11: {
        "question": """Expected 11. What is a Java program downloaded from a web server and executed on a web browser called? Choose from below:
[Java servlet, Java applet, Java VM, Java application]""",
        "answer": """Answer: Java applet

Explanation: Small Java programs that run on the client side (in the browser) are called Java applets. Programs running on the server side are called Java servlets.
Reference: <<joho5.pdf, p27>>, <<joho6.pdf, p4>>"""
    },
    q_ex_12: {
        "question": """Expected 12. In a pipeline-controlled computer where all instructions complete in 5 cycles, how many cycles are required to execute 20 instructions?""",
        "answer": """Answer: 24 cycles

Explanation: The first instruction takes a full 5 cycles to complete, but the remaining 19 instructions complete consecutively 1 cycle at a time. 5 + (20 - 1) * 1 = 24 cycles.
Reference: <<joho6.pdf, p37>>, <<joho7.pdf, p5>>"""
    },
    q_ex_13: {
        "question": """Expected 13. Name the 5 major components of a computer.""",
        "answer": """Answer: Control unit, Arithmetic unit, Memory unit, Input device, Output device.

Explanation: These are the five essential elements that make up a computer.
Reference: <<joho6.pdf, p37>>, <<joho7.pdf, p5>>"""
    }
}


# ==========================================
# Thai Translations
# ==========================================

thai_translations = {
    q_1: {
        "question": """1. จงแปลงเลขฐานสองทศนิยม 0.101 เป็นเลขฐานสิบทศนิยม""",
        "answer": """คำตอบ: 0.625

คำอธิบาย: การแปลงเลขฐานสองทศนิยมเป็นฐานสิบ ให้นำแต่ละหลักไปคูณกับค่าน้ำหนัก (2 ยกกำลัง -n)
- ทศนิยมตำแหน่งที่ 1: 1 * 0.5 = 0.5
- ทศนิยมตำแหน่งที่ 3: 1 * 0.125 = 0.125
รวม: 0.5 + 0.125 = 0.625
อ้างอิง: <<joho1.pdf, p11-12>>"""
    },
    q_2: {
        "question": """2. จงแปลงจำนวนเต็มฐานสอง 4 หลัก 1000 เป็นเลขฐานสิบ โดยสมมติว่ามีการแทนจำนวนลบด้วย 2's complement""",
        "answer": """คำตอบ: -8

คำอธิบาย: ในการแทนแบบ 2's complement หากบิตนัยสำคัญสูงสุด (MSB) เป็น 1 แสดงว่าเป็นจำนวนลบ การหาค่าสัมบูรณ์ทำได้โดยสลับบิตและบวก 1 สลับบิต 1000 จะได้ 0111 บวก 1 จะได้ 1000 (ซึ่งคือ 8 ในฐานสิบ) เนื่องจากเป็นค่าลบ คำตอบจึงเป็น -8
อ้างอิง: <<joho1.pdf, p23-24>>"""
    },
    q_3: {
        "question": """3. จงหาผลลัพธ์ของการเลื่อนบิตทางขวาแบบเลขคณิต (arithmetic right shift) 2 บิตของจำนวนเต็มฐานสอง 4 หลัก 1000 ในรูปเลขฐานสอง 4 หลัก โดยสมมติว่าใช้ 2's complement สำหรับจำนวนลบ""",
        "answer": """คำตอบ: 1110

คำอธิบาย: การเลื่อนบิตทางขวาแบบเลขคณิตจะเลื่อนบิตไปทางขวาโดยคงค่าบิตเครื่องหมาย (MSB) ไว้ การเลื่อน 1000 ไปทางขวา 2 บิตทำให้มีพื้นที่ว่าง 2 บิตทางซ้าย ซึ่งจะถูกเติมด้วยบิตเครื่องหมายเดิม (1) ทำให้ได้ 1110
อ้างอิง: <<joho2.pdf, p7>>"""
    },
    q_4: {
        "question": """4. จงแสดงเลขฐานสิบ 75 ในรูปเลขฐานสิบหก""",
        "answer": """คำตอบ: 4B

คำอธิบาย: แปลงฐานสิบเป็นฐานสิบหกโดยการหารด้วย 16 75 / 16 = 4 เศษ 11 ในฐานสิบหก 11 แทนด้วย 'B' ดังนั้นคำตอบคือ 4B
อ้างอิง: <<joho1.pdf, p13>>"""
    },
    q_5: {
        "question": """5. 1% ของประชากรเป็นโรคชนิดหนึ่ง การตรวจมีความแม่นยำดังนี้: ผู้ป่วยจริงตรวจพบผลบวก 90% ผลลบ 10%; ผู้ที่แข็งแรงตรวจพบผลลบ 90% ผลบวก 10% 
หากบุคคลหนึ่งรับการตรวจและได้ผลบวก จงหาความน่าจะเป็นโดยใช้ทฤษฎีบทของเบส์ (Bayes' Theorem):
(1) P(A): ความน่าจะเป็นที่จะตรวจพบผลบวก
(2) P(B): ความน่าจะเป็นที่เป็นโรค
(3) P(A|B): ความน่าจะเป็นที่จะตรวจพบผลบวกเมื่อเป็นโรค
(4) P(B|A): ความน่าจะเป็นที่จะเป็นโรคจริงเมื่อผลตรวจเป็นบวก""",
        "answer": """คำตอบ: 
(1) 0.108
(2) 0.01
(3) 0.9
(4) 0.083

คำอธิบาย: ใช้ทฤษฎีบทของเบส์หาความน่าจะเป็นแบบมีเงื่อนไข
(1) P(A) = (0.01 * 0.9) + (0.99 * 0.1) = 0.108
(4) P(B|A) = (0.9 * 0.01) / 0.108 = 0.083
อ้างอิง: <<joho2.pdf, p25-26>>, <<joho4.pdf, p27>>"""
    },
    q_6: {
        "question": """6. จงเขียนสมการ (a+(b*c))-d ให้อยู่ในรูป Reverse Polish Notation (สัญกรณ์โปแลนด์ย้อนกลับ)""",
        "answer": """คำตอบ: a b c * + d -

คำอธิบาย: ใน Reverse Polish Notation (postfix) ตัวดำเนินการจะถูกวางไว้หลังตัวถูกดำเนินการ เริ่มจากวงเล็บในสุด:
1. b*c -> b c *
2. a+(b c *) -> a b c * +
3. (a b c * +)-d -> a b c * + d -
อ้างอิง: <<joho3.pdf, p23>>, <<joho4.pdf, p28>>"""
    },
    q_7: {
        "question": """7. มีสแต็ก (Stack) และคิว (Queue) ว่างๆ อย่างละหนึ่งรายการ หากใส่ข้อมูล {1, 2, 3, 4} ตามลำดับ จงตอบคำถามต่อไปนี้เมื่อดึงข้อมูลออก:
(1) ข้อมูลลำดับที่ 2 ที่ถูกดึงออกจากสแต็กคืออะไร?
(2) ข้อมูลลำดับที่ 2 ที่ถูกดึงออกจากคิวคืออะไร?""",
        "answer": """คำตอบ: 
(1) 3
(2) 2

คำอธิบาย: 
สแต็กทำงานแบบ LIFO (เข้าหลังออกก่อน) ดังนั้นลำดับการดึงคือ 4 -> 3 -> 2 -> 1 ลำดับที่สองคือ 3
คิวทำงานแบบ FIFO (เข้าก่อนออกก่อน) ดังนั้นลำดับการดึงคือ 1 -> 2 -> 3 -> 4 ลำดับที่สองคือ 2
อ้างอิง: <<joho4.pdf, p8-9>>"""
    },
    q_8: {
        "question": """8. จงบอกความซับซ้อนของเวลา (Time Complexity) ในรูป Big-O notation (O(?)) ของอัลกอริทึมการค้นหาต่อไปนี้:
(1) Linear search (ค้นหาแบบเชิงเส้น)
(2) Binary search (ค้นหาแบบทวิภาค)
(3) Hash table (ตารางแฮช - กรณีไม่มีการชนกันของค่าแฮช)""",
        "answer": """คำตอบ: 
(1) O(n)
(2) O(log n)
(3) O(1)

คำอธิบาย: การค้นหาเชิงเส้นแปรผันตามจำนวนข้อมูล การค้นหาแบบทวิภาคแบ่งครึ่งข้อมูลทีละรอบทำให้เป็นลอการิทึม ตารางแฮชคำนวณตำแหน่งโดยตรงจึงใช้เวลาคงที่
อ้างอิง: <<joho4.pdf, p26>>"""
    },
    q_9: {
        "question": """9. จงบอกความซับซ้อนของเวลา (Time Complexity) ในรูป Big-O notation (O(?)) ของอัลกอริทึมการจัดเรียง (Sorting) ต่อไปนี้:
(1) Quick sort
(2) Bubble sort
(3) Selection sort""",
        "answer": """คำตอบ: 
(1) O(n log n)
(2) O(n^2)
(3) O(n^2)

คำอธิบาย: Quick sort แบ่งอาร์เรย์ด้วยค่าหลัก (pivot) ทำให้เร็ว Bubble sort และ Selection sort ต้องมีการเปรียบเทียบซ้ำๆ ทำให้ใช้เวลาแปรผันยกกำลังสอง
อ้างอิง: <<joho4.pdf, p31>>"""
    },
    q_10: {
        "question": """10. ข้อใดอธิบายเกี่ยวกับ memory interleaving (เทคนิคเพิ่มความเร็วคอมพิวเตอร์) ได้ถูกต้องที่สุด?
A: โอนถ่ายข้อมูลระหว่างหน่วยความจำหลักและ I/O โดยตรงโดยไม่ผ่าน CPU
B: เขียนข้อมูลลงแคชก่อน หากแคชเต็มจึงเขียนลงหน่วยความจำหลัก
C: คัดลอกข้อมูลส่วนหนึ่งจากหน่วยความจำหลักลงแคชเพื่อลดความต่างความเร็วการเข้าถึง
D: แบ่งหน่วยความจำหลักเป็นกลุ่มที่ทำงานอิสระต่อกัน และเข้าถึงแต่ละกลุ่มแบบขนาน""",
        "answer": """คำตอบ: D (แบ่งหน่วยความจำหลักเป็นกลุ่มที่ทำงานอิสระต่อกัน และเข้าถึงแต่ละกลุ่มแบบขนาน)

คำอธิบาย: Memory interleaving แบ่งหน่วยความจำหลักออกเป็นพื้นที่ที่เรียกว่า "banks" เพื่อให้สามารถเข้าถึงแบบขนานและเร่งการถ่ายโอนข้อมูล
อ้างอิง: <<joho6.pdf, p31>>"""
    },
    q_11: {
        "question": """11. เรจิสเตอร์หนึ่งเก็บจำนวนเต็มบวก x จากนั้นถูกเลื่อนบิตไปทางซ้าย 2 บิต และบวกค่า x กลับเข้าไป ค่าในเรจิสเตอร์จะเป็นกี่เท่าของ x? (สมมติว่าไม่มีโอเวอร์โฟลว์)""",
        "answer": """คำตอบ: 5 เท่า

คำอธิบาย: การเลื่อนบิตเลขฐานสองไปทางซ้าย 2 บิตทำให้ค่าเพิ่มเป็น 2^2 = 4 เท่า (กลายเป็น 4x) การบวกค่าดั้งเดิม x เข้าไปคือ 4x + x = 5x
อ้างอิง: <<joho2.pdf, p5, p9>>"""
    },
    q_12: {
        "question": """12. จงเลือกภาษามาร์กอัปที่ตรงกับคำอธิบายจากตัวเลือก [HTML, SGML, XML, UML]:
(1) ใช้สำหรับการวางมาตรฐานเอกสารและการแลกเปลี่ยนข้อมูลในอีคอมเมิร์ซแบบ B2B
(2) ใช้สำหรับอธิบายหน้าโฮมเพจบน WWW
(3) ภาษาการกำหนดเอกสารที่ได้มาตรฐานสากลเพื่อการแลกเปลี่ยนเอกสารอิเล็กทรอนิกส์""",
        "answer": """คำตอบ: 
(1) XML
(2) HTML
(3) SGML

คำอธิบาย: XML อนุญาตให้สร้างแท็กเองและใช้แลกเปลี่ยนข้อมูล HTML ใช้สร้างเว็บเพจ SGML เป็นมาตรฐาน ISO ดั้งเดิมของภาษามาร์กอัป
อ้างอิง: <<joho5.pdf, p23-24>>"""
    },
    q_13: {
        "question": """13. CPU ทำงานที่สัญญาณนาฬิกา 1GHz มี CPI (Clock Cycles per Instruction) เท่ากับ 2:
(1) เวลาเฉลี่ยในการรันคำสั่ง (Average instruction execution time) คือเท่าใด?
(2) ค่า MIPS ของ CPU นี้คือเท่าใด?""",
        "answer": """คำตอบ: 
(1) 2 ns (2 นาโนวินาที)
(2) 500 MIPS

คำอธิบาย: 1GHz หมายถึง 1 ไซเคิลสัญญาณนาฬิกาคือ 1 นาโนวินาที (1ns) ด้วย CPI 2 หนึ่งคำสั่งจะใช้เวลา 2 * 1ns = 2ns MIPS (ล้านคำสั่งต่อวินาที) คำนวณเป็น 1 / (2 * 10^-9) = 500 * 10^6 หรือ 500 MIPS
อ้างอิง: <<joho6.pdf, p19-20>>"""
    },
    q_14: {
        "question": """14. จงเลือกหน่วยความจำที่ตรงกับคำอธิบายจากตัวเลือก [SRAM, DRAM, ROM, Flash memory]:
(1) หน่วยความจำแบบไม่ลบเลือนที่เขียนและลบข้อมูลเป็นบล็อก
(2) หน่วยความจำแบบลบเลือนที่ไม่ต้องดำเนินการรีเฟรช (refresh) เพื่อเก็บข้อมูล
(3) สามารถเก็บรักษาข้อมูลไว้ได้แม้ในขณะที่ไม่มีไฟเลี้ยง
(4) มีโครงสร้างเซลล์เรียบง่าย ความหนาแน่นสูงและราคาต่อบิตถูก มักใช้เป็นหน่วยความจำหลักใน PC""",
        "answer": """คำตอบ: 
(1) Flash memory
(2) SRAM
(3) ROM (หรือ Flash memory)
(4) DRAM

คำอธิบาย: แฟลชเมมโมรีลบเป็นบล็อก SRAM เร็วและไม่ต้องรีเฟรช DRAM ใช้ตัวเก็บประจุต้องการการรีเฟรชแต่ทำความจุสูงได้ง่าย
อ้างอิง: <<joho6.pdf, p25-26>>"""
    },
    q_15: {
        "question": """15. ถ้าเวลาเข้าถึงแคช (cache access time) คือ 1 ns, หน่วยความจำหลัก (main memory) 10 ns, และอัตราแคชฮิต (cache hit rate) คือ 80% เวลาเข้าถึงที่มีผลจริง (effective access time) คือเท่าใด?""",
        "answer": """คำตอบ: 2.8 ns

คำอธิบาย: เวลาเข้าถึงที่มีผลจริง = (เวลาเข้าถึงแคช * อัตราแคชฮิต) + (เวลาเข้าถึงหน่วยความจำหลัก * (1 - อัตราแคชฮิต))
(1ns * 0.8) + (10ns * 0.2) = 0.8 + 2.0 = 2.8ns
อ้างอิง: <<joho6.pdf, p29>>"""
    },
    q_16: {
        "question": """16. อัตราการส่งข้อมูลจะเป็นเท่าใดเมื่อแปลงสัญญาณเสียงแอนะล็อกด้วยความถี่สุ่ม (sampling frequency) 8kHz และ quantization 8 บิต ก่อนนำไปส่งข้อมูล?
[A: 1.5M bit/s, B: 256k bit/s, C: 64k bit/s, D: 8k bit/s]""",
        "answer": """คำตอบ: C (64k bit/s)

คำอธิบาย: อัตราการส่งข้อมูล = ความถี่สุ่ม * ควอนไตซ์บิต 8,000 Hz * 8 bits = 64,000 bits/sec = 64 kbps
อ้างอิง: <<joho3.pdf, p22>>"""
    },
    q_17: {
        "question": """17. ข้อใดตรงกับ <variable_name> ที่กำหนดโดย BNF ที่ให้มา?
[A: _B39, B: 246, C: 3E5, D: F5_1]
<digit> ::= 0|1|2|3|4|5|6|7|8|9
<letter> ::= A|B|C|D|E|F
<alphanumeric> ::= <letter>|<digit>|_
<variable_name> ::= <letter>|<variable_name><alphanumeric>""",
        "answer": """คำตอบ: D (F5_1)

คำอธิบาย: ตามคำจำกัดความของ <variable_name> ตัวอักษรตัวแรกจะต้องเป็น <letter> (A-F) เสมอ ในตัวเลือกทั้งหมด มีเพียง F5_1 ที่ขึ้นต้นด้วยตัวอักษร
อ้างอิง: <<joho3.pdf, p22>>"""
    },
    q_18: {
        "question": """18. ในองค์ประกอบของหน่วยประมวลผล ส่วนใดที่จะถูกอัปเดตเมื่อมีการรันคำสั่ง branch (คำสั่งกระโดด)?
[A: Index register, B: General-purpose register, C: Program register (Program counter), D: Instruction register]""",
        "answer": """คำตอบ: C (Program register / Program counter)

คำอธิบาย: Program register (หรือ program counter) จะเก็บแอดเดรสของคำสั่งต่อไปที่จะรัน คำสั่ง branch จะอัปเดตค่าแอดเดรสนี้
อ้างอิง: <<joho6.pdf, p8>>"""
    },
    q_19: {
        "question": """19. ข้อใดอธิบายคุณสมบัติของโปรแกรมที่สามารถถูกเรียกใช้งานพร้อมกันจากหลายโปรเซสโดยไม่รบกวนการทำงานซึ่งกันและกัน?
[A: Reentrant, B: Recursive, C: Reusable, D: Relocatable]""",
        "answer": """คำตอบ: A (Reentrant)

คำอธิบาย: โปรแกรมแบบ Reentrant จะแยกส่วนกระบวนการทำงานและส่วนข้อมูลออกจากกัน ทำให้ป้องกันความขัดแย้งของข้อมูลเมื่อโปรเซสหลายอันเรียกใช้พร้อมกัน
อ้างอิง: <<joho5.pdf, p16>>"""
    },
    q_20: {
        "question": """20. นิพจน์ตรรกศาสตร์ใดเทียบเท่ากับ X・Y・Z + X̅・Y・Z ? (โดยที่ '・' คือตรรกะ AND, '+' คือ OR, และ 'X̅' คือ NOT X)
[A: X・Y・Z, B: X̅・(Y+Z), C: Y・Z, D: Y+Z]""",
        "answer": """คำตอบ: C (Y・Z)

คำอธิบาย: โดยใช้กฎการกระจายดึงตัวร่วม Y・Z จะได้ (X + X̅)・YZ ด้วยกฎส่วนเติมเต็ม X + X̅ = 1 ผลลัพธ์จึงเป็น Y・Z
อ้างอิง: <<joho2.pdf, p16-17>>"""
    },
    q_21: {
        "question": """21. วิธีการส่งผ่านอาร์กิวเมนต์ (Arguments) ไปยังซับรูทีน (Subroutine) วิธีใดที่รับประกันว่าค่าของตัวแปรจะไม่เปลี่ยนแปลงหลังจากซับรูทีนทำงานเสร็จสิ้น?
[A: Call by value, B: Call by result, C: Call by reference, D: Call by name]""",
        "answer": """คำตอบ: A (Call by value)

คำอธิบาย: Call by value จะส่งเพียง "สำเนาของค่า" เท่านั้น ดังนั้นการปรับเปลี่ยนภายในซับรูทีนจะไม่ส่งผลต่อตัวแปรต้นฉบับของผู้เรียก
อ้างอิง: <<joho5.pdf, p20>>"""
    },
    q_22: {
        "question": """22. คะแนนสอบมีการแจกแจงโดยมีค่าเฉลี่ย 70 และส่วนเบี่ยงเบนมาตรฐาน (Standard deviation) 5 คะแนนมาตรฐาน (T-score) สำหรับคะแนน 60 ในการสอบนี้คือเท่าใด?""",
        "answer": """คำตอบ: 30

คำอธิบาย: ใช้สูตร T-score: 50 + 10 * ((คะแนนที่ได้ - ค่าเฉลี่ย) / ส่วนเบี่ยงเบนมาตรฐาน) 50 + 10 * ((60 - 70) / 5) = 50 - 20 = 30
อ้างอิง: <<joho3.pdf, p11-12>>, <<joho4.pdf, p28>>"""
    },
    q_ex_1: {
        "question": """ข้อสอบคาดการณ์ 1. มีกี่วิธีในการเลือกสิ่งของ 3 ชิ้นจาก 10 ชิ้นมาจัดเรียงตามลำดับ (Permutation)?""",
        "answer": """คำตอบ: 720

คำอธิบาย: การคำนวณแบบ Permutation ที่ให้ความสำคัญกับลำดับ 10P3 = 10 * 9 * 8 = 720 วิธี
อ้างอิง: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>"""
    },
    q_ex_2: {
        "question": """ข้อสอบคาดการณ์ 2. มีกี่วิธีในการเลือกสิ่งของ 3 ชิ้นจาก 10 ชิ้น (Combination)?""",
        "answer": """คำตอบ: 120

คำอธิบาย: การคำนวณแบบ Combination ที่ไม่สนใจลำดับ 10C3 = (10 * 9 * 8) / (3 * 2 * 1) = 720 / 6 = 120 วิธี
อ้างอิง: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>"""
    },
    q_ex_3: {
        "question": """ข้อสอบคาดการณ์ 3. โยนเหรียญ 3 ครั้ง หากครั้งแรกออกหัว จงหาความน่าจะเป็นแบบมีเงื่อนไข (Conditional probability) ที่จะได้หัวทั้งหมด 2 ครั้งพอดี""",
        "answer": """คำตอบ: 1/2

คำอธิบาย: ความน่าจะเป็นแบบมีเงื่อนไข เหตุการณ์ Y (ครั้งแรกออกหัว) มี 4 วิธี เหตุการณ์ X∩Y (ครั้งแรกออกหัวและรวมได้หัว 2 ครั้งพอดี) มี 2 วิธี P(X|Y) = 2/4 = 1/2
อ้างอิง: <<joho2.pdf, p27>>, <<joho3.pdf, p6>>"""
    },
    q_ex_4: {
        "question": """ข้อสอบคาดการณ์ 4. จงอธิบายข้อแตกต่างที่ใหญ่ที่สุดระหว่างสแต็ก (Stack) และคิว (Queue) สั้นๆ""",
        "answer": """คำตอบ: สแต็กคือ LIFO, คิวคือ FIFO

คำอธิบาย: สแต็กใช้ระบบ Last-In First-Out (ดึงข้อมูลล่าสุดออกก่อน) คิวใช้ระบบ First-In First-Out (ดึงข้อมูลเก่าที่สุดออกก่อน)
อ้างอิง: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>"""
    },
    q_ex_5: {
        "question": """ข้อสอบคาดการณ์ 5. จงระบุหมายเลขที่เป็นราก (Root) และกฎการจัดวางของแผนภาพต้นไม้ค้นหาแบบทวิภาค (Binary search tree) ที่มีข้อมูล 10, 9, 8, 7, 6, 5, 4""",
        "answer": """คำตอบ: ราก (Root) คือ 7 กฎ: โหนดย่อยซ้าย < โหนดแม่ < โหนดย่อยขวา

คำอธิบาย: ต้นไม้ค้นหาแบบทวิภาคจะนำค่ามัธยฐาน (7) วางไว้ที่ราก วางค่าน้อยลงทางกิ่งซ้าย และค่ามากขึ้นทางกิ่งขวา
อ้างอิง: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>"""
    },
    q_ex_6: {
        "question": """ข้อสอบคาดการณ์ 6. เมื่อค้นหา '5' ในต้นไม้ค้นหาแบบทวิภาคจากข้อ 5 จะต้องทำการเปรียบเทียบ (ทำซ้ำ) กี่ครั้งจึงจะพบ?""",
        "answer": """คำตอบ: 2 ครั้ง

คำอธิบาย: การเปรียบเทียบครั้งที่ 1: เทียบกับราก '7' (ไปทางซ้าย) การเปรียบเทียบครั้งที่ 2: เทียบกับโหนด '5' ซึ่งตรงพอดี (สิ้นสุดการค้นหา)
อ้างอิง: <<joho4.pdf, p33>>, <<joho5.pdf, p3>>"""
    },
    q_ex_7: {
        "question": """ข้อสอบคาดการณ์ 7. หากข้อมูลถูกจัดเก็บแบบเรียงลำดับจากน้อยไปมากใน singly linked list ความซับซ้อนของเวลาในกระบวนการค้นหาตำแหน่งของข้อมูลคือเท่าใด?""",
        "answer": """คำตอบ: O(n)

คำอธิบาย: ใน singly linked list ไม่สามารถข้ามไปยังตำแหน่งปลายทางได้ตรงๆ ต้องทำตามพอยน์เตอร์จากส่วนหัวไปทีละตัว (การค้นหาเชิงเส้น) ซึ่งจะแปรผันตามจำนวนข้อมูล O(n)
อ้างอิง: <<joho4.pdf, p33>>, <<joho5.pdf, p4>>"""
    },
    q_ex_8: {
        "question": """ข้อสอบคาดการณ์ 8. นำข้อมูลฐานสิบหก 9 ตัว (1A, 35, 3B, 54, 8E, A1, AF, B2, B3) ใส่ลงตารางแฮชตามลำดับ หากค่าแฮชคือเศษจากการหารข้อมูลด้วย 8 ข้อมูลใดจะเกิดการชนกัน (Collision) เป็นตัวแรก?""",
        "answer": """คำตอบ: B2

คำอธิบาย: เศษของ 1A (ฐานสิบ 26) / 8 คือ 2 ส่วนเศษของ B2 (ฐานสิบ 178) / 8 คือ 2 เช่นกัน เมื่อพยายามเก็บในตำแหน่งเดียวกันจึงเกิดการชน
อ้างอิง: <<joho4.pdf, p33>>, <<joho5.pdf, p4>>"""
    },
    q_ex_9: {
        "question": """ข้อสอบคาดการณ์ 9. จงเลือกภาษาที่ใช้อธิบายรูปแบบของเอกสาร เช่น ขนาดตัวอักษร จากตัวเลือกต่อไปนี้: [DTD, CSS, XSL, SOAP, SVG]""",
        "answer": """คำตอบ: CSS

คำอธิบาย: CSS (Cascading Style Sheets) เป็นภาษาที่ใช้ระบุการออกแบบและเค้าโครง (ขนาดแบบอักษร สี การจัดวาง ฯลฯ) ของเอกสารมาร์กอัปเช่น HTML
อ้างอิง: <<joho5.pdf, p26>>, <<joho6.pdf, p3>>"""
    },
    q_ex_10: {
        "question": """ข้อสอบคาดการณ์ 10. ข้อได้เปรียบที่ใหญ่ที่สุดของภาษา Java เมื่อเทียบกับภาษา C++ คืออะไร?""",
        "answer": """คำตอบ: โปรแกรมที่คอมไพล์แล้วสามารถถูกนำไปรันบนคอมพิวเตอร์ที่ต่างระบบกันได้

คำอธิบาย: เนื่องจาก Java ทำงานบน Java Virtual Machine (JVM) โปรแกรมที่คอมไพล์แล้วจึงทำงานได้โดยไม่ขึ้นอยู่กับระบบปฏิบัติการหรือฮาร์ดแวร์ ("Write once, run anywhere")
อ้างอิง: <<joho5.pdf, p27>>, <<joho6.pdf, p4>>"""
    },
    q_ex_11: {
        "question": """ข้อสอบคาดการณ์ 11. โปรแกรม Java ที่ถูกดาวน์โหลดจากเว็บเซิร์ฟเวอร์และทำงานบนเว็บเบราว์เซอร์เรียกว่าอะไร? เลือกจากด้านล่างนี้:
[Java servlet, Java applet, Java VM, Java application]""",
        "answer": """คำตอบ: Java applet

คำอธิบาย: โปรแกรม Java ขนาดเล็กที่ทำงานทางฝั่งไคลเอนต์ (ในเบราว์เซอร์) เรียกว่า Java applets โปรแกรมทางฝั่งเซิร์ฟเวอร์เรียกว่า Java servlets
อ้างอิง: <<joho5.pdf, p27>>, <<joho6.pdf, p4>>"""
    },
    q_ex_12: {
        "question": """ข้อสอบคาดการณ์ 12. ในคอมพิวเตอร์ควบคุมแบบไปป์ไลน์ (Pipeline) ที่ทุกคำสั่งทำเสร็จสมบูรณ์ใน 5 ไซเคิล (Cycles) จะต้องใช้กี่ไซเคิลในการรันคำสั่ง 20 คำสั่ง?""",
        "answer": """คำตอบ: 24 ไซเคิล

คำอธิบาย: คำสั่งแรกต้องใช้ 5 ไซเคิลเต็มในการทำงาน แต่ 19 คำสั่งที่เหลือจะเสร็จสมบูรณ์ตามลำดับทีละ 1 ไซเคิล 5 + (20 - 1) * 1 = 24 ไซเคิล
อ้างอิง: <<joho6.pdf, p37>>, <<joho7.pdf, p5>>"""
    },
    q_ex_13: {
        "question": """ข้อสอบคาดการณ์ 13. จงบอกองค์ประกอบหลัก 5 ประการของคอมพิวเตอร์ (5 Major components)""",
        "answer": """คำตอบ: หน่วยควบคุม, หน่วยคำนวณและตรรกะ, หน่วยความจำ, หน่วยรับข้อมูล, หน่วยแสดงผล

คำอธิบาย: องค์ประกอบสำคัญ 5 ประการที่ประกอบกันเป็นคอมพิวเตอร์
อ้างอิง: <<joho6.pdf, p37>>, <<joho7.pdf, p5>>"""
    }
}