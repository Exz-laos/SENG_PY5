
# システム制御演習 期末試験対策 復習ノート

## 演習(6): 応答と伝達関数

### 問題2: 単位ステップ応答（インディシャル応答）の導出
単位ステップ入力 $U(s) = \frac{1}{s}$ を各伝達関数 $G(s)$ に掛けた出力 $Y(s) = G(s)U(s)$ を計算し、部分分数分解後に逆ラプラス変換により時間応答 $y(t)$ を求めます。

**(a) 比例要素 $G(s) = K$**
$$ Y(s) = K \cdot \frac{1}{s} = \frac{K}{s} $$
逆ラプラス変換により：
$$ y(t) = K $$

**(b) 1次遅れ系 $G(s) = \frac{1}{1+Ts}$**
$$ Y(s) = \frac{1}{1+Ts} \cdot \frac{1}{s} = \frac{1}{s(1+Ts)} $$
部分分数分解を行います：
$$ Y(s) = \frac{1}{s} - \frac{T}{1+Ts} = \frac{1}{s} - \frac{1}{s + \frac{1}{T}} $$
逆ラプラス変換により：
$$ y(t) = 1 - e^{-\frac{t}{T}} $$

**(c) 伝達関数 $G(s) = \frac{1+0.5s}{(1+s)(1+2s)}$**
$$ Y(s) = \frac{1+0.5s}{(1+s)(1+2s)} \cdot \frac{1}{s} = \frac{1+0.5s}{s(1+s)(1+2s)} $$
部分分数分解 $Y(s) = \frac{A}{s} + \frac{B}{1+s} + \frac{C}{1+2s}$ を行います：
$$ Y(s) = \frac{1}{s} + \frac{0.5}{1+s} - \frac{3}{1+2s} = \frac{1}{s} + \frac{0.5}{s+1} - \frac{1.5}{s+0.5} $$
逆ラプラス変換により：
$$ y(t) = 1 + 0.5e^{-t} - 1.5e^{-0.5t} $$

**(d) 伝達関数 $G(s) = \frac{1-5s}{(1+s)(1+2s)}$**
$$ Y(s) = \frac{1-5s}{(1+s)(1+2s)} \cdot \frac{1}{s} = \frac{1-5s}{s(1+s)(1+2s)} $$
部分分数分解を行います：
$$ Y(s) = \frac{1}{s} + \frac{6}{1+s} - \frac{14}{1+2s} = \frac{1}{s} + \frac{6}{s+1} - \frac{7}{s+0.5} $$
逆ラプラス変換により：
$$ y(t) = 1 + 6e^{-t} - 7e^{-0.5t} $$

---

### 問題3: ステップ応答からの伝達関数の導出
システムのステップ応答 $y(t) = 5e^{-t} + 5e^{-7t}$ が与えられているとき、伝達関数 $G(s)$ を求めます。

1. $y(t)$ をラプラス変換して出力 $Y(s)$ を求めます。
$$ Y(s) = \frac{5}{s+1} + \frac{5}{s+7} = \frac{5(s+7) + 5(s+1)}{(s+1)(s+7)} = \frac{10s+40}{(s+1)(s+7)} $$

2. ステップ入力 $U(s) = \frac{1}{s}$ であるため、$Y(s) = G(s)U(s) = G(s)\frac{1}{s}$ より、$G(s) = sY(s)$ を計算します。
$$ G(s) = s \cdot \frac{10s+40}{(s+1)(s+7)} = \frac{10s^2+40s}{(s+1)(s+7)} $$

---

### 問題4: インパルス応答とステップ応答
システム $G(s) = \frac{2}{s^2+3s+2} = \frac{2}{(s+1)(s+2)}$ の応答を求めます。

**(a) インパルス応答**
入力 $U(s) = 1$ であるため、$Y(s) = G(s)$ となります。
$$ Y(s) = \frac{2}{(s+1)(s+2)} = \frac{2}{s+1} - \frac{2}{s+2} $$
逆ラプラス変換により：
$$ y(t) = 2e^{-t} - 2e^{-2t} $$

**(b) ステップ応答**
入力 $U(s) = \frac{1}{s}$ であるため、$Y(s) = G(s)\frac{1}{s}$ となります。
$$ Y(s) = \frac{2}{s(s+1)(s+2)} = \frac{1}{s} - \frac{2}{s+1} + \frac{1}{s+2} $$
逆ラプラス変換により：
$$ y(t) = 1 - 2e^{-t} + e^{-2t} $$

---

## 演習(7): 安定性判別と根軌跡

### 問題1: ナイキスト線図を用いた安定判別
フィードバック制御系の安定条件は **$P = R$** です。
*   $P$: 一巡伝達関数が右半平面に持つ極の数（不安定な極の数）
*   $R$: ナイキスト線図が点 $(-1+j0)$ のまわりを反時計回りに回る回数（時計回りは負とする）

**(b) 図1(b) の判別**
*   図より $P = 2$ が与えられています。
*   $(-1+j0)$ の周りを、反時計回りに1回（+1）、時計回りに1回（-1）回っているため、$R = 1 - 1 = 0$ となります。
*   $P \neq R \implies 2 \neq 0$ であるため、この系は **不安定** です。

**(c) 図1(c) の判別**
*   図より $P = 0$ が与えられています。
*   $(-1+j0)$ の周りを時計回りに1回（-1）回っているため、$R = -1$ となります。
*   $P \neq R \implies 0 \neq -1$ であるため、この系は **不安定** です。

---

### 問題3: 根軌跡の描画（一巡伝達関数 $G(s)H(s) = \frac{K}{s(s+1)}$ の場合）
特性方程式 $1 + G(s)H(s) = 0$ から根軌跡を求めます。

$$ 1 + \frac{K}{s(s+1)} = 0 \implies s^2 + s + K = 0 $$
二次方程式の解の公式より、根は以下のように求まります。
$$ s = \frac{-1 \pm \sqrt{1-4K}}{2} $$
*   $K=0$ のとき、根は開ループ極である $s=0, -1$ となります。
*   漸近線と実軸の交点 $\sigma_c$ は、$\sigma_c = \frac{\sum(\text{極}) - \sum(\text{零点})}{n-m} = \frac{(0 + (-1)) - 0}{2} = -0.5$ となります。
*   したがって、軌跡は実軸上の $0$ と $-1$ から出発し、$-0.5$ で衝突した後、虚軸に平行に上下($\pm j\infty$)へと伸びていきます。

---

## 演習(8): 定常偏差

### 定常偏差の基本公式
外部入力信号 $R(s)$ から制御偏差 $E(s)$ までの関係は以下の通りです。
$$ E(s) = \frac{1}{1+G(s)H(s)}R(s) $$
最終値の定理より、定常偏差 $e(\infty)$ は次のように求められます。
$$ e(\infty) = \lim_{s \to 0} s E(s) = \lim_{s \to 0} \frac{s}{1+G(s)H(s)}R(s) $$

---

### 問題1・2: 0形システム（原点に極を持たない）の場合
一巡伝達関数: $G(s)H(s) = \frac{40(s+5)}{s^3+7s^2+18s+24}$

**問題1: 目標値が大きさ5のステップ入力 $R(s) = \frac{5}{s}$ の定常偏差**
$$ \lim_{s \to 0} G(s)H(s) = \frac{40 \times 5}{24} = \frac{200}{24} = \frac{25}{3} $$
$$ e(\infty) = \lim_{s \to 0} \frac{s \cdot \frac{5}{s}}{1+G(s)H(s)} = \frac{5}{1 + \frac{25}{3}} = \frac{15}{3+25} = \frac{15}{28} \approx 0.536 $$

**問題2: 目標値が傾き2のランプ入力 $R(s) = \frac{2}{s^2}$ の定常偏差**
$$ e(\infty) = \lim_{s \to 0} s \cdot \frac{1}{1+G(s)H(s)} \cdot \frac{2}{s^2} = \lim_{s \to 0} \frac{2}{s + sG(s)H(s)} $$
ここで、$\lim_{s \to 0} sG(s)H(s) = 0$ となるため、
$$ e(\infty) = \frac{2}{0 + 0} = \infty $$
（※0形システムはランプ入力に追従できず、定常偏差は無限大になります。）

---

### 問題3・4: 1形システム（原点に極を1つ持つ）の場合
一巡伝達関数: $G(s)H(s) = \frac{40(s+3)}{s(s+2)(s+4)(s+5)}$

**問題3: 目標値が大きさ5のステップ入力 $R(s) = \frac{5}{s}$ の定常偏差**
原点に極 $s$ を持つため、$\lim_{s \to 0} G(s)H(s) = \infty$ となります。
$$ e(\infty) = \frac{5}{1 + \infty} = 0 $$
（※1形システムはステップ入力に対して完全に追従します。）

**問題4: 目標値が傾き2のランプ入力 $R(s) = \frac{2}{s^2}$ の定常偏差**
速度偏差定数 $K_v$ を求めます。
$$ K_v = \lim_{s \to 0} s G(s)H(s) = \lim_{s \to 0} \frac{40(s+3)}{(s+2)(s+4)(s+5)} = \frac{40 \times 3}{2 \times 4 \times 5} = \frac{120}{40} = 3 $$
定常偏差は、
$$ e(\infty) = \frac{2}{K_v} = \frac{2}{3} \approx 0.667 $$



# システム制御演習 期末試験対策 復習ノート（過去問統合版）

## 演習(6): 応答と伝達関数

### 演習問題2: 単位ステップ応答（インディシャル応答）の導出
単位ステップ入力 $U(s) = \frac{1}{s}$ を各伝達関数 $G(s)$ に掛けた出力 $Y(s) = G(s)U(s)$ を計算し、部分分数分解後に逆ラプラス変換により時間応答 $y(t)$ を求めます。

**(a) 比例要素 $G(s) = K$**
$$ Y(s) = K \cdot \frac{1}{s} = \frac{K}{s} \implies y(t) = K $$

**(b) 1次遅れ系 $G(s) = \frac{1}{1+Ts}$**
$$ Y(s) = \frac{1}{1+Ts} \cdot \frac{1}{s} = \frac{1}{s} - \frac{T}{1+Ts} = \frac{1}{s} - \frac{1}{s + \frac{1}{T}} $$
$$ y(t) = 1 - e^{-\frac{t}{T}} $$

**(c) 伝達関数 $G(s) = \frac{1+0.5s}{(1+s)(1+2s)}$**
$$ Y(s) = \frac{1+0.5s}{s(1+s)(1+2s)} = \frac{1}{s} + \frac{0.5}{s+1} - \frac{1.5}{s+0.5} $$
$$ y(t) = 1 + 0.5e^{-t} - 1.5e^{-0.5t} $$

**(d) 伝達関数 $G(s) = \frac{1-5s}{(1+s)(1+2s)}$**
$$ Y(s) = \frac{1-5s}{s(1+s)(1+2s)} = \frac{1}{s} + \frac{6}{s+1} - \frac{7}{s+0.5} $$
$$ y(t) = 1 + 6e^{-t} - 7e^{-0.5t} $$

---
> 📝 **【過去問】問題1 （類似: 演習6 問題2(b) 1次遅れ系）**
> **問題:** 1次遅れ系 $G(s) = \frac{K}{Ts+1}$ 但し、$T>0, K>0$ について、インディシャル応答を求めよ。
> 
> **解答:**
> インディシャル応答なので $U(s) = \frac{1}{s}$
> $$ Y(s) = G(s)U(s) = \frac{K}{s(Ts+1)} $$
> 部分分数分解を行います。
> $$ Y(s) = \frac{K}{s} - \frac{K \cdot T}{Ts+1} = \frac{K}{s} - \frac{K}{s + \frac{1}{T}} $$
> 逆ラプラス変換により：
> $$ y(t) = K - Ke^{-\frac{t}{T}} = K(1 - e^{-\frac{t}{T}}) $$
---

### 演習問題3: ステップ応答からの伝達関数の導出
システムのステップ応答 $y(t) = 5e^{-t} + 5e^{-7t}$ から伝達関数 $G(s)$ を求めます。

1. $y(t)$ をラプラス変換します。
$$ Y(s) = \frac{5}{s+1} + \frac{5}{s+7} = \frac{10s+40}{(s+1)(s+7)} $$
2. $G(s) = \frac{Y(s)}{U(s)} = sY(s)$ を計算します。
$$ G(s) = \frac{10s^2+40s}{(s+1)(s+7)} $$

---

### 演習問題4: インパルス応答とステップ応答
システム $G(s) = \frac{2}{s^2+3s+2} = \frac{2}{(s+1)(s+2)}$ の応答を求めます。

**(a) インパルス応答** ($U(s) = 1$)
$$ Y(s) = G(s) = \frac{2}{s+1} - \frac{2}{s+2} \implies y(t) = 2e^{-t} - 2e^{-2t} $$

**(b) ステップ応答** ($U(s) = \frac{1}{s}$)
$$ Y(s) = G(s)\frac{1}{s} = \frac{1}{s} - \frac{2}{s+1} + \frac{1}{s+2} \implies y(t) = 1 - 2e^{-t} + e^{-2t} $$

---
> 📝 **【過去問】問題2 （類似/同一: 演習6 問題4 インパルス応答）**
> **問題:** $G_1(s) = \frac{1}{s^2+3s+2}, G_2(s) = \frac{s+1}{s^2+5s+4}$ について、(a) 極と零点を求めよ。(b) インパルス応答を求めよ。
> ※注意: $G_1(s)$ は演習6問題4とほぼ同じですが、分子が2ではなく1です。
> 
> **解答:**
> **【$G_1(s)$ について】**
> (a) 極と零点: $G_1(s) = \frac{1}{(s+1)(s+2)}$ より、**極: $s=-1, -2$**、**零点: なし**。
> (b) インパルス応答: $Y_1(s) = G_1(s) \cdot 1 = \frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2}$
> 逆ラプラス変換して、**$y_1(t) = e^{-t} - e^{-2t}$**
> 
> **【$G_2(s)$ について】**
> (a) 極と零点: $G_2(s) = \frac{s+1}{(s+1)(s+4)} = \frac{1}{s+4}$ より、**極: $s=-4$**、**零点: なし**。
> (b) インパルス応答: $Y_2(s) = G_2(s) \cdot 1 = \frac{1}{s+4}$
> 逆ラプラス変換して、**$y_2(t) = e^{-4t}$**
---


## 演習(7): 安定性判別と根軌跡

### 演習問題1: ナイキスト線図を用いた安定判別
フィードバック系の安定条件は **$P = R$**（$P$: 右半平面の極の数、$R$: -1+j0を反時計回りに回る回数）
*   **(b) 図1(b)**: $P = 2$、$R = 1 - 1 = 0$。$P \neq R$ のため **不安定**。
*   **(c) 図1(c)**: $P = 0$、$R = -1$。$P \neq R$ のため **不安定**。

---
> 📝 **【過去問】問題3 （関連: 安定性判別 - フルビッツの安定判別法）**
> **問題:** パラメータ$K$を含む特性方程式が $s^3+5s^2+6s+K=0$ であるとき、フルビッツの安定判別法を用いて、この系が安定な$K$の範囲を求めよ。
> ※演習7はナイキストですが、過去問では同じ安定性評価としてフルビッツが出題されています。
>
> **解答:**
> 特性方程式 $a_3s^3 + a_2s^2 + a_1s + a_0 = 0$ と比較します。
> 安定条件1: 全係数が正であること $\implies K > 0$
> 安定条件2: フルビッツ行列式 $\Delta_2 > 0$ であること
> $$ \Delta_2 = \begin{vmatrix} a_2 & a_0 \\ a_3 & a_1 \end{vmatrix} = \begin{vmatrix} 5 & K \\ 1 & 6 \end{vmatrix} = (5 \times 6) - (1 \times K) = 30 - K $$
> $30 - K > 0 \implies K < 30$
> 以上より、安定なKの範囲は **$0 < K < 30$** です。
---

### 演習問題3: 根軌跡の描画
一巡伝達関数 $G(s)H(s) = \frac{K}{s(s+1)}$ の根軌跡。
*   根は $s = \frac{-1 \pm \sqrt{1-4K}}{2}$
*   漸近線と実軸の交点 $\sigma_c = \frac{(0 + (-1)) - 0}{2} = -0.5$
*   軌跡は実軸上の $0$ と $-1$ から出発し、$-0.5$ で衝突して上下に分岐する。

---
> 📝 **【過去問】問題4 （類似: 演習7 問題3 根軌跡の描画）**
> **問題:** $G(s) = \frac{K}{s^2+2s}$ の根軌跡を描く。
> (a) 漸近線と実軸の交点 $\sigma$ を求めよ。(b) 漸近線の傾き $\theta_N$ を求めよ。(c) 軌跡が実軸から離れる点を求めよ。(d) 根軌跡を描け。
> 
> **解答:**
> 開ループ伝達関数 $G(s) = \frac{K}{s(s+2)}$。極は $s=0, -2$ (極の数 $n=2$)。零点はなし (零点の数 $m=0$)。
> 
> **(a) 漸近線と実軸の交点 $\sigma$**
> $$ \sigma = \frac{\sum P - \sum Z}{n - m} = \frac{(0 - 2) - 0}{2 - 0} = \frac{-2}{2} = -1 $$
> 
> **(b) 漸近線の傾き $\theta_N$**
> $$ \theta_N = \frac{N}{n - m}\pi \quad (N=1,3,5...) = \frac{1}{2}\pi, \frac{3}{2}\pi $$
> （つまり $\pm 90^\circ$ 方向）
> 
> **(c) 実軸から離れる点（分岐点）**
> 特性方程式 $1 + G(s) = 0 \implies s^2 + 2s + K = 0 \implies K = -(s^2 + 2s)$
> $K$ を $s$ で微分して0とおきます。
> $$ \frac{dK}{ds} = -(2s + 2) = 0 \implies s = -1 $$
>
> **(d) 根軌跡**
> 実軸上の極 $s=0$ と $s=-2$ から軌跡が出発し、分岐点 $s=-1$ で衝突。その後、$\pm 90^\circ$ の漸近線（虚軸に平行）に沿って上下($\pm j\infty$)に伸びる十字型の図形となります。
---


## 演習(8): 定常偏差

### 基本公式
定常偏差 $e(\infty) = \lim_{s \to 0} \frac{s}{1+G(s)H(s)}R(s)$

### 問題1・2: 0形システム（原点に極を持たない）
$G(s)H(s) = \frac{40(s+5)}{s^3+7s^2+18s+24}$
*   **問題1（ステップ入力 $R(s)=\frac{5}{s}$）:**
    $\lim_{s \to 0} G(s)H(s) = \frac{25}{3}$
    $e(\infty) = \frac{5}{1 + 25/3} = \frac{15}{28} \approx 0.536$
*   **問題2（ランプ入力 $R(s)=\frac{2}{s^2}$）:**
    $s \to 0$ で分母が0になるため、$e(\infty) = \infty$ （追従不可）

### 問題3・4: 1形システム（原点に極を1つ持つ）
$G(s)H(s) = \frac{40(s+3)}{s(s+2)(s+4)(s+5)}$
*   **問題3（ステップ入力 $R(s)=\frac{5}{s}$）:**
    原点極により $\lim G(s)H(s) = \infty$ となるため、$e(\infty) = \frac{5}{1+\infty} = 0$ （完全追従）
*   **問題4（ランプ入力 $R(s)=\frac{2}{s^2}$）:**
    速度偏差定数 $K_v = \lim_{s \to 0} s G(s)H(s) = \frac{40 \times 3}{2 \times 4 \times 5} = 3$
    $e(\infty) = \frac{2}{K_v} = \frac{2}{3} \approx 0.667$




Here is the reconstructed exam:

---

# 【システム制御演習】(前期・定期試験) 2023年8月2日
**(Reconstructed Exam Questions)**

### 問題1 (Problem 1: Nyquist Stability)
以下の(1)～(4)のフィードバック制御系のナイキスト線図（または周回数 $R$ と右半平面の極の数 $P$ の条件）が与えられている。ナイキストの安定判別法を用いて、各システムの安定性を「安定」または「不安定」で答えよ。
*(Note: The original exam likely provided 4 Nyquist plots, or just gave the P and R values directly as follows)*
(1) $R=2, P=2$ のとき
(2) $R=0, P=0$ のとき
(3) $R=0, P=4$ のとき
(4) $R=2, P=4$ のとき

### 問題2 (Problem 2: Poles and Hurwitz Stability)
以下のシステムについて、安定性を判別せよ。
+ (1) 一巡伝達関数が $G(s) = \frac{1}{s^2+2s-3}$ で与えられるシステムについて、極を求め、システムの安定性を判別せよ。
+ (2) 特性方程式の係数が ( すなわち $s^2+3s+2=0$）で与えられるシステムの安定性を判別せよ。
+ (3) 特性方程式が $s^4+2s^3+4s^2+2s+2=0$ で与えられるシステムについて、フルビッツの安定判別法（Hurwitz matrix）を用いて安定性を判別せよ。

### 問題3 (Problem 3: Root Locus)
一巡伝達関数が $L(s) = \frac{K}{(s+1)(s+7)(s+8)}$ で与えられるフィードバック制御系の根軌跡を描く。以下の問いに答えよ。
(1) 極と零点を求めよ。また、極の数 $n$ と零点の数 $m$ を答えよ。
(2) 軌跡の漸近線と実軸の交点 $\delta$ を求めよ。
(3) 実軸との漸近線のなす角度 $\theta_N$ を求めよ。
(4) 軌跡が実軸から離れる点（分岐点）を求めよ。
(5) 根軌跡を描け。

### 問題4 (Problem 4: Frequency Response & Gain Margin)
開ループ伝達関数が $L(s) = \frac{K}{s^3+5s^2+7s+3}$ で与えられる系について、以下の問いに答えよ。
(1) $s = j\omega$ を代入し、位相が $-180^\circ$（虚数部が0）となる位相交差周波数 $\omega_{cp}$ [rad/s] を求めよ。
(2) $K=8$ のとき、ゲイン余裕 $g_m$ [dB] を求めよ。
(3) ゲイン余裕が $0$ dB ($g_m = 0$) となる、すなわち限界ゲインとなる $K$ の値を求めよ。

---

## 🎯 Commentary: What is similar to THIS YEAR's test?

Based on our conversation history and the exercises you have been assigned recently (`演習⑦`, `演習⑧`, and the other `過去問1.pdf`), here is how this past exam aligns with your upcoming test:

**1. Problem 1 (Nyquist): HIGHLY SIMILAR 🔥**
This exact concept ($P = R \rightarrow$ Stable) is what we practiced in **Exercise 7, Problem 1**. You will almost certainly have a question where you need to count encirclements ($R$) and compare them to unstable poles ($P$). 

**2. Problem 2 (Hurwitz): HIGHLY SIMILAR 🔥**
We discussed calculating Hurwitz determinants in the other Past Exam (Problem 3, finding the range of $K$). You must know how to set up the Hurwitz matrix and check if $H_1, H_2, H_3 > 0$. Problem 2(1) is also a basic check of poles—remember that any positive pole (like $s=1$) means immediate instability!

**3. Problem 3 (Root Locus): EXTREMELY SIMILAR 🔥🔥**
This is a 1-to-1 match with **Exercise 7 Problem 3(b)** and the **other Past Exam Problem 4**. Notice how the teacher breaks it down into the exact same steps: (1) Poles, (2) $\delta$ (Centroid), (3) $\theta_N$ (Angles), (4) $dK/ds = 0$ (Breakaway point), and (5) Drawing. *Master Method 2 (Root Locus Rules), and you will guarantee these points.*

**4. Problem 4 (Gain Margin): NEW / DIFFERENT ⚠️**
We have *not* discussed Gain Margin ($g_m$), Phase Crossover Frequency ($\omega_{cp}$), or Bode plots in our recent conversations. If this topic was covered in your recent lectures (perhaps in Chapter/Exercise 6?), you should review the formula $g_m = -20 \log_{10} |L(j\omega_{cp})|$. 
*(Note: Problem 4(1) uses the exact same trick we talked about for finding where the root locus crosses the imaginary axis: substitute $s = j\omega$ and set the imaginary part to 0!)*

**🚨 CRITICAL MISSING TOPIC: Steady-State Error (定常偏差) 🚨**
Notice that this 2023 exam does **not** have a question about Steady-State Error (Final Value Theorem, Type 0 vs Type 1 systems, Ramp vs Step inputs). However, you just spent a lot of time studying **Exercise 8 (Problems 1-4)**. I highly suspect the teacher might replace Problem 4 from this past exam with a Steady-State Error question this year. **Do not forget to study Exercise 8!**


Here is the complete, step-by-step solution for **Problem 2 (Poles and Hurwitz Stability)** based directly on the provided teacher's solution manual and handwritten notes. I have formatted everything clearly in Markdown code block as you requested.


# 問題2 (Problem 2: Poles and Hurwitz Stability) - Solution

### 🇯🇵 日本語での解答と解説 (Solution in Japanese)

**(1) 一巡伝達関数 $G(s) = \frac{1}{s^2+2s-3}$ について、極を求め、安定性を判別せよ。**
*   **極を求める:** 分母を $0$ とおいて特性方程式を解きます。
    $$ s^2 + 2s - 3 = 0 $$
    $$ (s - 1)(s + 3) = 0 $$
    よって、極は **$s = 1, -3$** となります。
*   **安定性の判別:** 極の1つ（$s = 1$）が $0$ 以上（複素平面の右半平面に存在）であるため、このシステムは **不安定 (Unstable)** です。

**(2) 特性方程式が $s^2+3s+2=0$ で与えられるシステムの安定性を判別せよ。**
*   **安定性の判別:** 2次方程式の係数 $$ に着目します。係数がすべて同じ符号（すべて正）であり、符号の変化がないため、このシステムは **安定 (Stable)** です。
    *(※補足: 実際に解を求めても $(s+1)(s+2)=0 \implies s=-1, -2$ となり、すべての極が左半平面にあるため安定であることがわかります。)*

**(3) 特性方程式 $s^4+2s^3+4s^2+2s+2=0$ について、フルビッツを用いて安定性を判別せよ。**
*   **ステップ1: 係数の確認**
    $a_0=1, a_1=2, a_2=4, a_3=2, a_4=2$
*   **ステップ2: フルビッツ行列 $H$ を立てる**
    $$ H = \begin{pmatrix} a_1 & a_3 & 0 & 0 \\ a_0 & a_2 & a_4 & 0 \\ 0 & a_1 & a_3 & 0 \\ 0 & a_0 & a_2 & a_4 \end{pmatrix} = \begin{pmatrix} 2 & 2 & 0 & 0 \\ 1 & 4 & 2 & 0 \\ 0 & 2 & 2 & 0 \\ 0 & 1 & 4 & 2 \end{pmatrix} $$
*   **ステップ3: 首座行列式 ($H_1 \sim H_4$) を計算する**
    *   $H_1 = |2| = \mathbf{2 > 0}$
    *   $H_2 = \begin{vmatrix} 2 & 2 \\ 1 & 4 \end{vmatrix} = (2 \times 4) - (2 \times 1) = \mathbf{6 > 0}$
    *   $H_3 = \begin{vmatrix} 2 & 2 & 0 \\ 1 & 4 & 2 \\ 0 & 2 & 2 \end{vmatrix} = 2\begin{vmatrix} 4 & 2 \\ 2 & 2 \end{vmatrix} - 2\begin{vmatrix} 1 & 2 \\ 0 & 2 \end{vmatrix} = 2(8 - 4) - 2(2 - 0) = 8 - 4 = \mathbf{4 > 0}$
    *   $H_4 = \begin{vmatrix} 2 & 2 & 0 & 0 \\ 1 & 4 & 2 & 0 \\ 0 & 2 & 2 & 0 \\ 0 & 1 & 4 & 2 \end{vmatrix} = 2 \times H_3 = 2 \times 4 = \mathbf{8 > 0}$
*   **結論:** すべての行列式が正 ($H_1, H_2, H_3, H_4 > 0$) であるため、このシステムは **安定 (Stable)** です。

---

### 🇬🇧 English Explanation and Solution

**(1) For the open-loop transfer function $G(s) = \frac{1}{s^2+2s-3}$, find the poles and determine stability.**
*   **Find the Poles:** Set the denominator to $0$.
    $$ s^2 + 2s - 3 = 0 \implies (s - 1)(s + 3) = 0 $$
    The poles are **$s = 1, -3$**.
*   **Determine Stability:** Because there is a pole that is greater than $0$ ($s = 1$), which means it lies in the right-half of the complex plane, the system is **Unstable**.

**(2) Determine the stability of the system with the characteristic equation $s^2+3s+2=0$.**
*   **Determine Stability:** Look at the coefficients of the polynomial: $$. Because all coefficients have the exact same sign (all positive) and there are no missing terms, the system is automatically **Stable**. 

**(3) Determine the stability of the system with the characteristic equation $s^4+2s^3+4s^2+2s+2=0$ using the Hurwitz matrix.**
*   **Step 1: Identify coefficients**
    $a_0=1, a_1=2, a_2=4, a_3=2, a_4=2$.
*   **Step 2: Set up the Hurwitz Matrix ($H$)**
    $$ H = \begin{pmatrix} 2 & 2 & 0 & 0 \\ 1 & 4 & 2 & 0 \\ 0 & 2 & 2 & 0 \\ 0 & 1 & 4 & 2 \end{pmatrix} $$
*   **Step 3: Calculate the principal minor determinants ($H_1$ to $H_4$)**
    *   $H_1 = 2 \implies \mathbf{2 > 0}$
    *   $H_2 = (2)(4) - (2)(1) = 8 - 2 = \mathbf{6 > 0}$
    *   $H_3 = 2[(4)(2)-(2)(2)] - 2[(1)(2)-(2)(0)] = 2(4) - 2(2) = \mathbf{4 > 0}$
    *   $H_4 = 2 \times H_3 = 2 \times 4 = \mathbf{8 > 0}$
*   **Conclusion:** Because all principal minors are strictly greater than zero ($H_n > 0$), the system satisfies the Hurwitz stability criterion and is **Stable**.



Here is the complete, step-by-step solution for **Problem 3 (Root Locus)** from the 2023 past exam (`more 過去問.pdf`), formatted in a Markdown code block with both Japanese and English explanations!


# 問題3 (Problem 3: Root Locus) - Solution

### 🇯🇵 日本語での解答と解説 (Solution in Japanese)

与えられた一巡伝達関数は $L(s) = \frac{K}{(s+1)(s+7)(s+8)}$ です。これを用いて根軌跡を描くための各ステップを計算します。

**(1) 極と零点を求めよ。また、極の数 $n$ と零点の数 $m$ を答えよ。**
*   **極 (Poles):** 分母が $0$ になる $s$ の値です。
    $s = -1, -7, -8$ 
    極の数は **$n = 3$** です。
*   **零点 (Zeros):** 分子に $s$ が含まれていないため、**「なし」** です。
    零点の数は **$m = 0$** です。

**(2) 軌跡の漸近線と実軸の交点 $\delta$ を求めよ。**
漸近線の交点（重心）の公式 $\delta = \frac{\sum P - \sum Z}{n - m}$ を使います。
$$ \delta = \frac{(-1 - 7 - 8) - 0}{3 - 0} = \mathbf{-\frac{16}{3}} \quad (\approx -5.33) $$

**(3) 実軸との漸近線のなす角度 $\theta_N$ を求めよ。**
漸近線の角度の公式 $\theta_N = \frac{N}{n-m}\pi$ を使います。
$n - m = 3$ なので、$N = 1, 3, 5$ の3つの角度を求めます。
*   $N=1$ のとき: $\theta_1 = \mathbf{\frac{1}{3}\pi}$ （$60^\circ$）
*   $N=3$ のとき: $\theta_3 = \frac{3}{3}\pi = \mathbf{\pi}$ （$180^\circ$）
*   $N=5$ のとき: $\theta_5 = \mathbf{\frac{5}{3}\pi}$ （$300^\circ$ または $-60^\circ$）
*答え: $\theta_N = \frac{1}{3}\pi, \pi, \frac{5}{3}\pi$*

**(4) 軌跡が実軸から離れる点（分岐点）を求めよ。**
特性方程式 $1 + L(s) = 0$ から $K$ を $s$ の式で表し、$\frac{dK}{ds} = 0$ を解きます。
$$ 1 + \frac{K}{(s+1)(s+7)(s+8)} = 0 $$
$$ K = -(s+1)(s+7)(s+8) = -(s^3 + 16s^2 + 71s + 56) $$
これを $s$ で微分します。
$$ \frac{dK}{ds} = -(3s^2 + 32s + 71) = 0 $$
二次方程式の解の公式を使って $s$ を求めます。
$$ s = \frac{-16 \pm \sqrt{16^2 - 3 \times 71}}{3} = \frac{-16 \pm \sqrt{256 - 213}}{3} = \frac{-16 \pm \sqrt{43}}{3} $$
ここで、軌跡は実軸上の奇数区間（$-1$ と $-7$ の間、および $-8$ から $-\infty$ の間）にのみ存在します。
$s = \frac{-16 - \sqrt{43}}{3} \approx -7.51$ は軌跡が存在しない区間（$-7$ と $-8$ の間）にあるため不適です。
よって、$-1$ と $-7$ の間にある解が正しい分岐点となります。
*答え:* **$s = \frac{-16 + \sqrt{43}}{3}$** *($\approx -3.15$)*

**(5) 根軌跡を描け。**
1. 実軸上の $-1, -7, -8$ に極（×印）を打つ。
2. 軌跡は $-1$ と $-7$ の間で衝突し、(4)で求めた $s \approx -3.15$ の点から上下（$60^\circ$ と $300^\circ$ の方向）に分かれて発散する。
3. $-8$ にある極からの軌跡は、そのまま実軸上を左（$-\infty$ の方向、$180^\circ$）へ真っ直ぐ進む。
4. (2)で求めた $\delta \approx -5.33$ を中心に、漸近線を点線で引いておく。

---

### 🇬🇧 English Explanation and Solution

Given the open-loop transfer function $L(s) = \frac{K}{(s+1)(s+7)(s+8)}$, we will follow the rules to sketch the root locus.

**(1) Find the poles and zeros. Also, state the number of poles ($n$) and zeros ($m$).**
*   **Poles:** Set the denominator to $0$. 
    $s = -1, -7, -8$. 
    Number of poles **$n = 3$**.
*   **Zeros:** There are no $s$ terms in the numerator.
    **None**. 
    Number of zeros **$m = 0$**.

**(2) Find the intersection of the asymptotes and the real axis ($\delta$).**
Use the centroid formula: $\delta = \frac{\sum P - \sum Z}{n - m}$.
$$ \delta = \frac{(-1 - 7 - 8) - 0}{3 - 0} = \mathbf{-\frac{16}{3}} \quad (\approx -5.33) $$

**(3) Find the angles of the asymptotes with the real axis ($\theta_N$).**
Use the angle formula: $\theta_N = \frac{N}{n-m}\pi$.
Since $n - m = 3$, we must calculate exactly three angles using $N = 1, 3, 5$.
*   $N=1$: $\theta_1 = \mathbf{\frac{1}{3}\pi}$ ($60^\circ$)
*   $N=3$: $\theta_3 = \frac{3}{3}\pi = \mathbf{\pi}$ ($180^\circ$)
*   $N=5$: $\theta_5 = \mathbf{\frac{5}{3}\pi}$ ($300^\circ$)
*Answer: $\theta_N = \frac{1}{3}\pi, \pi, \frac{5}{3}\pi$*

**(4) Find the breakaway point where the locus leaves the real axis.**
Set up the characteristic equation $1 + L(s) = 0$ and solve for $K$.
$$ K = -(s+1)(s+7)(s+8) = -(s^3 + 16s^2 + 71s + 56) $$
Take the derivative and set it to $0$:
$$ \frac{dK}{ds} = -(3s^2 + 32s + 71) = 0 $$
Using the quadratic formula, we get:
$$ s = \frac{-16 \pm \sqrt{16^2 - 3(71)}}{3} = \frac{-16 \pm \sqrt{43}}{3} $$
By Rule 4 of the root locus, the locus on the real axis only exists between $-1$ and $-7$, and from $-8$ to $-\infty$. 
The root $s = \frac{-16 - \sqrt{43}}{3} \approx -7.51$ falls in the empty space between $-7$ and $-8$, so it is invalid. We must choose the root that falls between $-1$ and $-7$.
*Answer:* **$s = \frac{-16 + \sqrt{43}}{3}$** *($\approx -3.15$)*

**(5) Draw the root locus.**
1. Mark the poles at $-1, -7$, and $-8$ with an 'x'.
2. The roots starting at $-1$ and $-7$ move towards each other, crash at the breakaway point ($-3.15$), and split upwards and downwards following the $60^\circ$ and $300^\circ$ asymptotes.
3. The root starting at $-8$ moves indefinitely to the left ($-\infty$) following the $180^\circ$ asymptote.


Here is the complete step-by-step solution for **Exercise 7 Problem 2**, formatted as Markdown code just as you requested!


# 演習⑦ 問題2 (Exercise 7 Problem 2) - Solution

### 🇯🇵 日本語での解答と解説 (Solution in Japanese)

**① 根軌跡とは何かを説明せよ。**
フィードバック制御系において、開ループ伝達関数のゲイン $K$ を $0$ から $\infty$ まで変化させたときに、閉ループ系の極（特性方程式の根）が複素平面上を移動する軌跡のことです。

**② この制御対象の伝達関数 $G(s)$ を推定せよ。**

**ステップ1: グラフから極と零点を読み取る**
図3のグラフから、$K=0$ の出発点（×印、極）と $K=\infty$ の到達点（○印、零点）を読み取ります。
*   **極 (Poles, $K=0$):** $s = -9, -12, -3 \pm 4j$。
*   **零点 (Zeros, $K=\infty$):** $s = -6$。

**ステップ2: 伝達関数の式を立てる**
先生の板書にあるように、読み取った極を分母に、零点を分子に配置して式を作ります。
$$ G(s) = \frac{s - (-6)}{\{s - (-9)\}\{s - (-12)\}\{s - (-3 + j4)\}\{s - (-3 - j4)\}} $$

**ステップ3: 式を展開して整理する**
複素数の部分 $(s+3-j4)(s+3+j4)$ を展開します。
$(s+3)^2 - (j4)^2 = s^2 + 6s + 9 - (-16) = s^2 + 6s + 25$ となります。
これらを組み合わせて、最終的な伝達関数が完成します。

**【答え】**
$$ G(s) = \frac{s + 6}{(s + 9)(s + 12)(s^2 + 6s + 25)} $$

---

### 🇬🇧 English Explanation and Solution

**① Explain what a root locus is.**
A root locus is a graph in the complex plane showing how the roots of the characteristic equation (the closed-loop poles) move as a system parameter, like the open-loop gain $K$, is varied from $0$ to $\infty$.

**② Estimate the transfer function $G(s)$ of this controlled object.**

**Step 1: Identify poles and zeros from the graph**
From Figure 3, we identify the starting points ($K=0$, marked with 'x') as poles and the ending point ($K=\infty$, marked with 'o') as a zero.
*   **Poles ($K=0$):** $s = -9, -12$, and $-3 \pm 4j$.
*   **Zeros ($K=\infty$):** $s = -6$.

**Step 2: Set up the transfer function equation**
Place the zero in the numerator and the poles in the denominator.
$$ G(s) = \frac{s - (-6)}{\{s - (-9)\}\{s - (-12)\}\{s - (-3 + j4)\}\{s - (-3 - j4)\}} $$

**Step 3: Expand and simplify the equation**
Expand the complex conjugate terms: 
$(s+3-j4)(s+3+j4) = (s+3)^2 - (j4)^2 = s^2 + 6s + 9 - (-16) = s^2 + 6s + 25$.

Combine them all together to get the final transfer function.

**【Answer】**
$$ G(s) = \frac{s + 6}{(s + 9)(s + 12)(s^2 + 6s + 25)} $$


Here is the solution to Question 3, followed by the English explanation, cross-references to your materials, and a summary of the formulas you need to know.

### 🇯🇵 問3 の解答 (Solution in Japanese)

**問題:** 問2のシステムの可制御性を調べよ。

（※問2のシステム: $\frac{d}{dt}\boldsymbol{x}(t) = \begin{bmatrix} -5 & -4 \\ 4 & 1 \end{bmatrix}\boldsymbol{x}(t) + \begin{bmatrix} 1 \\ -1 \end{bmatrix}u(t)$）

**解答:**
与えられたシステムの行列を $A = \begin{bmatrix} -5 & -4 \\ 4 & 1 \end{bmatrix}$、入力ベクトルを $\boldsymbol{b} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ とおきます。

**手順 1: $A\boldsymbol{b}$ を計算する**
$A\boldsymbol{b} = \begin{bmatrix} -5 & -4 \\ 4 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} (-5 \times 1) + (-4 \times -1) \\ (4 \times 1) + (1 \times -1) \end{bmatrix} = \begin{bmatrix} -5 + 4 \\ 4 - 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 3 \end{bmatrix}$

**手順 2: 可制御性行列 (Controllability Matrix) $\mathcal{U}_c$ を作る**
$\mathcal{U}_c = [\boldsymbol{b}, A\boldsymbol{b}]$ であるため、求めたベクトルを並べます。
$\mathcal{U}_c = \begin{bmatrix} 1 & -1 \\ -1 & 3 \end{bmatrix}$

**手順 3: 行列式 $|\mathcal{U}_c|$ を計算する**
$|\mathcal{U}_c| = (1 \times 3) - (-1 \times -1) = 3 - 1 = 2$

**結論:**
$|\mathcal{U}_c| = 2 \neq 0$ であるため、このシステムは**可制御である（可制御性が有る）**。

---

### 🇬🇧 English Explanation

**Controllability (可制御性)** asks a simple question: *Can we force the system's state to move from any initial position to any target position within a finite amount of time using only the input $u(t)$?* 

To find out, we construct the **Controllability Matrix** $\mathcal{U}_c = [\boldsymbol{b}, A\boldsymbol{b}]$. 
1. You take the input vector $\boldsymbol{b}$ as your first column.
2. You multiply matrix $A$ by vector $\boldsymbol{b}$ to get the second column.
3. You put them together to form a 2x2 matrix.

Finally, you calculate the **determinant** of this new matrix. 
*   If the determinant is **not zero** ($|\mathcal{U}_c| \neq 0$), the matrix is "full rank" and the system is **controllable (可制御)**. 
*   If the determinant **is zero** ($|\mathcal{U}_c| = 0$), the system is **uncontrollable (不可制御)**. 
Because our determinant is 2, this system is completely controllable.

---

### 🗂 Cross-References to Your Materials

Yes, this exact concept is heavily featured in both your notes and the past exam!

**1. In your note ("5I システム制御理論　I.pdf"):**
*   **Where:** In the whiteboard photos (specifically around the section covering state feedback and canonical forms).
*   **Problem Sentence/Context:** There is a specific heading that says **"可制御かどうかを調べる方法"** (How to check if it's controllable). 
    It defines **"可制御性行列"** (Controllability Matrix) as $\mathcal{U}_c = [\boldsymbol{b}, A\boldsymbol{b}]$. 
    The notes provide a very similar example: $Ab = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}\begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\ -4 \end{bmatrix}$, resulting in $|\mathcal{U}_c| = \begin{vmatrix} -1 & 2 \\ 2 & -4 \end{vmatrix} = 0$, which is marked as **"不可制御" (Uncontrollable)**.

**2. In the past exam ("システム制御理論期末試験過去問.pdf"):**
*   **Where:** On the **2023 Exam paper**, as **問題 4 (Question 4), Part ②**.
*   **Problem Sentence:** 
    > **"問題 4 システム $\frac{d}{dt}\boldsymbol{x}(t) = \begin{bmatrix} -2 & 1 \\ 2 & -3 \end{bmatrix}\boldsymbol{x}(t) + \begin{bmatrix} 1 \\ 0 \end{bmatrix}u(t)$ について、... ② 可制御性を調べよ。"**
*   **Solution in Exam:** The handwritten answer key for the 2023 exam shows the exact same steps we used: calculating $A\boldsymbol{b} = \begin{bmatrix} -2 \\ 2 \end{bmatrix}$, building $\mathcal{U}_c = \begin{bmatrix} 1 & -2 \\ 0 & 2 \end{bmatrix}$, and checking the determinant $|\mathcal{U}_c| = 2 \neq 0 \Rightarrow$ **可制御**.

---

### 📝 Summary of Knowledge and Formulas

To solve controllability problems on your exam, memorize these core steps:

*   **The Controllability Matrix (可制御性行列):** 
    For a 2nd-order system (2x2 matrix $A$), the formula is:
    $$\mathcal{U}_c = [\boldsymbol{b}, A\boldsymbol{b}]$$
*   **Matrix Multiplication:** 
    Remember how to multiply a 2x2 matrix by a 2x1 vector to find $A\boldsymbol{b}$.
    $$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} ax + by \\ cx + dy \end{bmatrix}$$
*   **Determinant Check for Controllability:**
    $$|\mathcal{U}_c| = (row1,col1 \times row2,col2) - (row1,col2 \times row2,col1)$$
    *   If $|\mathcal{U}_c| \neq 0 \longrightarrow$ **可制御 (Controllable)**.
    *   If $|\mathcal{U}_c| = 0 \longrightarrow$ **不可制御 (Uncontrollable)**.



    Here is the problem and solution for Question 2 from the 2025 past exam, formatted with clear formulas and minimal text as requested.


**【問題 2】**
$A = \begin{bmatrix} -7 & 10 \\ -5 & 8 \end{bmatrix}, \boldsymbol{b} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, C =$ について、可制御正準系を求めよ。

---

**【解答】**

**1. 特性方程式と係数 $a_1, a_2$**
$$|sI - A| = \begin{vmatrix} s+7 & -10 \\ 5 & s-8 \end{vmatrix}= (s+7)(s-8) - (-50) = s^2 - s - 56 + 50 = s^2 - s - 6 = 0$$

基本形 $s^2 + a_2s + a_1 = 0$ と比較：
$$a_1 = -6, \quad a_2 = -1$$

**2. 可制御性行列 $V_c$**
$$A\boldsymbol{b} = \begin{bmatrix} -7 & 10 \\ -5 & 8 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} -7 \\ -5 \end{bmatrix} -->V_c = [\boldsymbol{b}, A\boldsymbol{b}] = \begin{bmatrix} 1 & -7 \\ 0 & -5 \end{bmatrix}$$

**3. 変換行列 $T$**
$$W = \begin{bmatrix} a_2 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} -1 & 1 \\ 1 & 0 \end{bmatrix} -->T = V_c W = \begin{bmatrix} 1 & -7 \\ 0 & -5 \end{bmatrix} \begin{bmatrix} -1 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} -8 & 1 \\ -5 & 0 \end{bmatrix}$$

**4. 可制御正準系 $\tilde{A}, \tilde{\boldsymbol{b}}, \tilde{C}$**
$$\tilde{A} = \begin{bmatrix} 0 & 1 \\ -a_1 & -a_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 6 & 1 \end{bmatrix} ;\tilde{\boldsymbol{b}} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

$$\tilde{C} = CT = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} -8 & 1 \\ -5 & 0 \end{bmatrix} = \begin{bmatrix} -8 & 1 \end{bmatrix}$$

---

**【最終解答 (状態方程式)】**
$$\begin{bmatrix} \dot{z}_1 \\ \dot{z}_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 6 & 1 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix}u $$
$$ y = \begin{bmatrix} -8 & 1 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \end{bmatrix}$$



Here is the problem and solution for Question 2 from the 2023 past exam, formatted in a `.md` code block with clear formulas and reduced text explanation.


**【問題 2 (2023年)】**
システム $\frac{d}{dt}\begin{bmatrix}x_1(t)\\x_2(t)\end{bmatrix} = \begin{bmatrix}-1 & 1 \\ 2 & 0\end{bmatrix} \begin{bmatrix}x_1(t)\\x_2(t)\end{bmatrix} + \begin{bmatrix}1 \\ 2\end{bmatrix} u(t)$ について、
① 固有値 $\lambda_1, \lambda_2$、対応する固有ベクトル $\boldsymbol{v}_1, \boldsymbol{v}_2$ を求めよ。
② 対角正準系への変換行列 $T = [\boldsymbol{v}_1, \boldsymbol{v}_2]$ を求めよ。
③ 対角正準形式 $\tilde{A} = T^{-1}AT, \tilde{\boldsymbol{b}} = T^{-1}\boldsymbol{b}$ を求めよ。

---

**【解答】**

**① 固有値と固有ベクトル**
特性方程式 $|sI - A| = 0$ を解く：
$$|sI - A| = \begin{vmatrix} s+1 & -1 \\ -2 & s \end{vmatrix} = s(s+1) - (-1)(-2)= s^2 + s - 2 = (s-1)(s+2) = 0$$
固有値: $\lambda_1 = 1, \quad \lambda_2 = -2$

$\lambda_1 = 1$ のときの固有ベクトル $\boldsymbol{v}_1$：
$$A\boldsymbol{v}_1 = \lambda_1\boldsymbol{v}_1 \implies \begin{bmatrix} -1 & 1 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix} = 1 \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix}$$
上の行より: $-v_{11} + v_{12} = v_{11} \implies v_{12} = 2v_{11}$
$v_{11} = 1$ とすると $v_{12} = 2 \implies \boldsymbol{v}_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$

$\lambda_2 = -2$ のときの固有ベクトル $\boldsymbol{v}_2$：
$$A\boldsymbol{v}_2 = \lambda_2\boldsymbol{v}_2 \implies \begin{bmatrix} -1 & 1 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} v_{21} \\ v_{22} \end{bmatrix} = -2 \begin{bmatrix} v_{21} \\ v_{22} \end{bmatrix}$$
上の行より: $-v_{21} + v_{22} = -2v_{21} \implies v_{22} = -v_{21}$
$v_{21} = 1$ とすると $v_{22} = -1 \implies \boldsymbol{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$


**② 変換行列 $T$**
$$T = [\boldsymbol{v}_1, \boldsymbol{v}_2] = \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix}$$


**③ 対角正準形式 $\tilde{A}, \tilde{\boldsymbol{b}}$**
まず逆行列 $T^{-1}$ を計算：
$$|T| = (1)(-1) - (1)(2) = -3$$
$$T^{-1} = \frac{1}{-3} \begin{bmatrix} -1 & -1 \\ -2 & 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix}$$

対角行列 $\tilde{A}$ (固有値が対角に並ぶ)：
$$\tilde{A} = T^{-1}AT = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix}$$

入力行列 $\tilde{\boldsymbol{b}}$：
$$\tilde{\boldsymbol{b}} = T^{-1}\boldsymbol{b} = \frac{1}{3} \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} (1\times1) + (1\times2) \\ (2\times1) + (-1\times2) \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 3 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$



Here is the problem and solution for Question 4 from the 2023 past exam, formatted in a `.md` code block with clear formulas and reduced text explanation.


**【問題 4 (2023年)】**
システム $\frac{d}{dt}\begin{bmatrix}x_1(t)\\x_2(t)\end{bmatrix} = \begin{bmatrix}-2 & 1 \\ 2 & -3\end{bmatrix} \begin{bmatrix}x_1(t)\\x_2(t)\end{bmatrix} + \begin{bmatrix}1 \\ 0\end{bmatrix} u(t)$ について、

① 特性多項式 $|sI - A|$ を求めよ。
② 可制御性を調べよ。
③ 可制御正準系への変換行列 $T = [\boldsymbol{b}, A\boldsymbol{b}]\begin{bmatrix}a_2 & 1 \\ 1 & 0\end{bmatrix}$ を求めよ。
④ 可制御正準形式 $\tilde{A}, \tilde{\boldsymbol{b}}$ を求めよ。

---

**【解答】**

**① 特性多項式**
$$|sI - A| = \begin{vmatrix} s+2 & -1 \\ -2 & s+3 \end{vmatrix}= (s+2)(s+3) - (-1)(-2)= s^2 + 5s + 6 - 2= s^2 + 5s + 4$$

基本形 $s^2 + a_2s + a_1$ と比較して、係数：
$$a_1 = 4, \quad a_2 = 5$$

**② 可制御性**
$$A\boldsymbol{b} = \begin{bmatrix} -2 & 1 \\ 2 & -3 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} -2 \\ 2 \end{bmatrix}$$

可制御性行列 $\mathcal{U}_c$ :
$$\mathcal{U}_c = [\boldsymbol{b}, A\boldsymbol{b}] = \begin{bmatrix} 1 & -2 \\ 0 & 2 \end{bmatrix}--->|\mathcal{U}_c| = (1 \times 2) - (-2 \times 0) = 2$$
$|\mathcal{U}_c| \neq 0$ であるため、**可制御である**。

**③ 変換行列 $T$**
$$T = \mathcal{U}_c \begin{bmatrix} a_2 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & -2 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 5 & 1 \\ 1 & 0 \end{bmatrix}= \begin{bmatrix} (1\times 5)+(-2\times 1) & (1\times 1)+(-2\times 0) \\ (0\times 5)+(2\times 1) & (0\times 1)+(2\times 0) \end{bmatrix}= \begin{bmatrix} 3 & 1 \\ 2 & 0 \end{bmatrix}$$

**④ 可制御正準形式 $\tilde{A}, \tilde{\boldsymbol{b}}$**
（※過去問解答用紙では $T^{-1}$ を求め $\tilde{A} = T^{-1}AT, \tilde{\boldsymbol{b}} = T^{-1}\boldsymbol{b}$ を計算していますが、公式でも直接導出可能です）

$$\tilde{A} = \begin{bmatrix} 0 & 1 \\ -a_1 & -a_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -4 & -5 \end{bmatrix}$$

$$\tilde{\boldsymbol{b}} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$



Based on the whiteboard images in your notes (`5I システム制御理論 I.pdf`) from **23/06/2026** and the pages immediately following it (dated **30/06** and **07/07/2026**), your teacher goes through a very detailed example of a system using the matrix $A = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}$. 

They use this exact matrix to teach **four different topics**: State Variable Diagrams, Transfer Functions, Diagonalization, and Controllability. Because your teacher spent so much time on this specific example, it is highly likely you will see these exact steps on your exam!

Here are **3 Possible Exam Problems** based exactly on the examples from those pages, complete with the solutions written out just like your teacher did on the board. I have put them in a `.md` code block so you can easily copy and study them.


# 📝 Possible Exam Practice Problems (Based on Notes 23/06 - 07/07)

## 【Practice Problem 1: Diagrams & Transfer Functions】
**問題 (Problem):**
システム $\dot{\boldsymbol{x}} = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}\boldsymbol{x} + \begin{bmatrix} -1 \\ 2 \end{bmatrix}u, \quad y = \begin{bmatrix} 1 & 1 \end{bmatrix}\boldsymbol{x}$ について、以下の問いに答えよ。
① 状態方程式と出力方程式を展開し、状態変数線図 (State Variable Diagram) を描け。
② 特性方程式 $|sI - A| = 0$ を解き、システムの極（固有値）$\lambda_1, \lambda_2$ を求めよ。

**【解答 (Solution)】**
**① 状態変数線図:**
行列を展開すると以下の式になる。
$\dot{x}_1 = x_2 - u$
$\dot{x}_2 = 2x_1 - x_2 + 2u$
$y = x_1 + x_2$
*(※図の描き方: 2つの積分器を置き、$u$ から $x_1$ 側の加算点へ [-1]、$x_2$ 側の加算点へ のゲインを繋ぐ。ノートの23/06の次のページにある複雑な交差した図を参照)*

**② 特性方程式と極:**
$|sI - A| = \begin{vmatrix} s & -1 \\ -2 & s+1 \end{vmatrix}$
$= s(s+1) - (-1)(-2)$
$= s^2 + s - 2 = 0$
$(s-1)(s+2) = 0$
**極 (Poles): $\lambda_1 = 1, \quad \lambda_2 = -2$**

---

## 【Practice Problem 2: Diagonal Canonical Form (対角化)】
**問題 (Problem):**
システム $\dot{\boldsymbol{x}} = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}\boldsymbol{x} + \begin{bmatrix} 0 \\ 1 \end{bmatrix}u, \quad y = \begin{bmatrix} 1 & 0 \end{bmatrix}\boldsymbol{x}$ について、対角正準系を求めよ。
*(※注意: 先生はノートで入出力を少し変えて $b=\begin{bmatrix}0\\1\end{bmatrix}, c=$ としています)*

**【解答 (Solution)】**
**① 固有ベクトルと変換行列 $T$:**
$\lambda_1 = 1$ のとき:
$\begin{bmatrix} -1 & 1 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies v_{12} = v_{11}$
$v_{11} = 1$ とすると $v_{12} = 1 \implies \boldsymbol{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$

$\lambda_2 = -2$ のとき:
$\begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} v_{21} \\ v_{22} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies v_{22} = -2v_{21}$
$v_{21} = 1$ とすると $v_{22} = -2 \implies \boldsymbol{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$

変換行列 $T = [\boldsymbol{v}_1, \boldsymbol{v}_2] = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}$

**② 逆行列 $T^{-1}$:**
$|T| = (1)(-2) - (1)(1) = -3$
$T^{-1} = \frac{1}{-3} \begin{bmatrix} -2 & -1 \\ -1 & 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}$

**③ 対角正準系 $\tilde{A}, \tilde{\boldsymbol{b}}, \tilde{\boldsymbol{c}}$:**
$\tilde{A} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix}$

$\tilde{\boldsymbol{b}} = T^{-1}\boldsymbol{b} = \frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1/3 \\ -1/3 \end{bmatrix}$

$\tilde{\boldsymbol{c}} = \boldsymbol{c}T = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \end{bmatrix}$

---

## 【Practice Problem 3: Controllability (可制御性)】
**問題 (Problem):**
システム $\dot{\boldsymbol{x}} = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}\boldsymbol{x} + \begin{bmatrix} -1 \\ 2 \end{bmatrix}u$ について、可制御性を調べよ。

**【解答 (Solution)】**
**① $A\boldsymbol{b}$ の計算:**
$A\boldsymbol{b} = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} (0\times-1)+(1\times 2) \\ (2\times-1)+(-1\times 2) \end{bmatrix} = \begin{bmatrix} 2 \\ -4 \end{bmatrix}$

**② 可制御性行列 $\mathcal{U}_c$:**
$\mathcal{U}_c = [\boldsymbol{b}, A\boldsymbol{b}] = \begin{bmatrix} -1 & 2 \\ 2 & -4 \end{bmatrix}$

**③ 行列式の判定:**
$|\mathcal{U}_c| = (-1 \times -4) - (2 \times 2) = 4 - 4 = 0$
$|\mathcal{U}_c| = 0$ であるため、このシステムは **不可制御 (Uncontrollable)** である。





You are absolutely right! In your notes from **23/06/2026**, the whiteboard clearly includes finding the transfer function $G(s)$ alongside the characteristic equation and the state variable diagram. 

Here is the fully updated **Practice Problem 1**, including all three of those specific questions and their complete step-by-step solutions, formatted in a clean `.md` code block for you to study!


**【Practice Problem 1: Transfer Functions & Diagrams (Updated)】**

**問題 (Problem):**
システム $\dot{\boldsymbol{x}} = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}\boldsymbol{x} + \begin{bmatrix} -1 \\ 2 \end{bmatrix}u, \quad y = \begin{bmatrix} 1 & 1 \end{bmatrix}\boldsymbol{x}$ について、以下の問いに答えよ。

① 入出力の伝達関数 $G(s)$ を求めよ。
② 特性方程式 $|sI - A| = 0$ を解き、システムの極（固有値）$\lambda_1, \lambda_2$ を求めよ。
③ 状態方程式と出力方程式を展開し、状態変数線図 (State Variable Diagram) を描け。

---

**【解答 (Solution)】**

**① 伝達関数 $G(s)$**
伝達関数の公式 $G(s) = \boldsymbol{c}(sI - A)^{-1}\boldsymbol{b}$ を用いる。
まず、$(sI - A)$ を求める。
$$sI - A = \begin{bmatrix} s & 0 \\ 0 & s \end{bmatrix} - \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix} = \begin{bmatrix} s & -1 \\ -2 & s+1 \end{bmatrix}$$

次に、逆行列 $(sI - A)^{-1}$ を計算する。行列式は $|sI - A| = s(s+1) - 2 = s^2 + s - 2$ である。
$$(sI - A)^{-1} = \frac{1}{s^2+s-2} \begin{bmatrix} s+1 & 1 \\ 2 & s \end{bmatrix}$$

これに $\boldsymbol{c}$ と $\boldsymbol{b}$ を掛ける。
$$G(s) = \begin{bmatrix} 1 & 1 \end{bmatrix} \left( \frac{1}{s^2+s-2} \begin{bmatrix} s+1 & 1 \\ 2 & s \end{bmatrix} \right) \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \frac{1}{s^2+s-2} \begin{bmatrix} s+3 & s+1 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \end{bmatrix}= \frac{1}{s^2+s-2} \{ -(s+3) + 2(s+1) \}$$
$$G(s) = \frac{1}{s^2+s-2} \{ -s - 3 + 2s + 2 \}  = \frac{s - 1}{s^2 + s - 2}$$

分母を因数分解して約分すると、最終的な伝達関数が求まる。
$$G(s) = \frac{s - 1}{(s-1)(s+2)} = \frac{1}{s+2}$$

**② 特性方程式と極（固有値）**
特性方程式は分母が $0$ になる条件であるため、
$$|sI - A| = s^2 + s - 2 = 0$$
$$(s-1)(s+2) = 0$$
**極 (固有値): $\lambda_1 = 1, \quad \lambda_2 = -2$**

**③ 状態変数線図**
行列計算を展開して、個別の状態方程式と出力方程式を導く。
$\dot{x}_1 = x_2 - u$
$\dot{x}_2 = 2x_1 - x_2 + 2u$
$y = x_1 + x_2$

**(※作図の手順):**
1. $x_1, x_2$ を作るために、積分器（$\int dt$）を2つ配置する。
2. **$\dot{x}_1$ の加算点:** 入力 $u$ からゲイン $[-1]$ を通して加算点へ。$x_2$ からそのままフィードバックして加算点へ。
3. **$\dot{x}_2$ の加算点:** 入力 $u$ からゲイン $$ を通して加算点へ。$x_1$ からゲイン $$ でフィードバック。$x_2$ からゲイン $[-1]$ でフィードバック。
4. **出力 $y$:** $x_1$ と $x_2$ の出力をそのまま足し合わせる。
*(ノートの23/06/2026に描かれている複雑な交差線図が正解となります)*



You are completely right! Breaking it down into those 4 specific sub-questions matches your teacher's exact teaching style on the whiteboard perfectly. 

*(Small note: You mentioned $c=$, but looking closely at the whiteboard photos from **30/06** and **07/07**, the teacher wrote **$c=$**. I will use $c=$ so the math matches your notes exactly!)*

Here is the fully updated problem and step-by-step solution, formatted in a clean `.md` code block with clear formulas.


**【Practice Problem 2: Diagonal Canonical Form (Full Version)】**

**問題 (Problem):**
システム $\dot{\boldsymbol{x}} = \begin{bmatrix} 0 & 1 \\ 2 & -1 \end{bmatrix}\boldsymbol{x} + \begin{bmatrix} 0 \\ 1 \end{bmatrix}u, \quad y = \begin{bmatrix} 1 & 0 \end{bmatrix}\boldsymbol{x}$ について、以下の問いに答えよ。

① 固有値 $\lambda$、固有ベクトル $\boldsymbol{v}$ と変換行列 $T$ を求めよ。
② 逆行列 $T^{-1}$ を求めよ。
③ 対角正準系 $\tilde{A}, \tilde{\boldsymbol{b}}, \tilde{\boldsymbol{c}}$ を求めよ。
④ 状態方程式と出力方程式を展開し、状態変数線図 (State Variable Diagram) を描け。

---

**【解答 (Solution)】**

**① 固有値・固有ベクトル・変換行列 $T$**
特性方程式 $|sI - A| = 0$ より：
$$|sI - A| = \begin{vmatrix} s & -1 \\ -2 & s+1 \end{vmatrix} = s(s+1) - 2 = s^2 + s - 2 = (s-1)(s+2) = 0$$
固有値: **$\lambda_1 = 1, \quad \lambda_2 = -2$**

$\lambda_1 = 1$ のときの固有ベクトル $\boldsymbol{v}_1$：
$$\begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies v_{12} = v_{11}$$
$v_{11} = 1$ とすると $v_{12} = 1 \implies \boldsymbol{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$

$\lambda_2 = -2$ のときの固有ベクトル $\boldsymbol{v}_2$：
$$\begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} v_{21} \\ v_{22} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies v_{22} = -2v_{21}$$
$v_{21} = 1$ とすると $v_{22} = -2 \implies \boldsymbol{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$

変換行列 $T$:
$$T = [\boldsymbol{v}_1, \boldsymbol{v}_2] = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}$$


**② 逆行列 $T^{-1}$**
行列式 $|T| = (1)(-2) - (1)(1) = -3$
$$T^{-1} = \frac{1}{-3} \begin{bmatrix} -2 & -1 \\ -1 & 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}$$


**③ 対角正準系 $\tilde{A}, \tilde{\boldsymbol{b}}, \tilde{\boldsymbol{c}}$**
$$\tilde{A} = T^{-1}AT = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix}$$

$$\tilde{\boldsymbol{b}} = T^{-1}\boldsymbol{b} = \frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1/3 \\ -1/3 \end{bmatrix}$$

$$\tilde{\boldsymbol{c}} = \boldsymbol{c}T = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \end{bmatrix}$$


**④ 状態方程式と状態変数線図**
求めた行列から、新しい状態方程式を展開する：
$$\dot{z}_1 = z_1 + \frac{1}{3}u$$
$$\dot{z}_2 = -2z_2 - \frac{1}{3}u$$
$$y = z_1 + z_2$$

**(※作図の手順):**
1. 積分器（$\int dt$ または $1/s$）を上下に2つ並行に配置する。
2. **上段 ($z_1$ のループ):**
   * 入力 $u$ からゲイン $[1/3]$ を通り加算点 $\oplus$ へ。
   * $z_1$ からゲイン $$ を通り加算点 $\oplus$ へ戻る（フィードバック）。
   * 積分器の出力 $z_1$ はそのまま（またはゲイン $$ を通って）最終出力 $y$ の加算点へ。
3. **下段 ($z_2$ のループ):**
   * 入力 $u$ からゲイン $[-1/3]$ を通り別の加算点 $\oplus$ へ。
   * $z_2$ からゲイン $[-2]$ を通り加算点 $\oplus$ へ戻る（フィードバック）。
   * 積分器の出力 $z_2$ はそのまま（またはゲイン $$ を通って）最終出力 $y$ の加算点へ。
4. **出力 $y$:** 上段と下段の出力を足し合わせる。
*(※この図はノートの「07/07/2026」のページに描かれている、完全に上下に分離した並列の図と一致します)*
