# -*- coding: utf-8 -*-
# data.py - Fundamental Information Technology Engineer Examination Dataset
# This file contains the complete 65 unique questions for exam preparation.

all_questions = [
    {
        "id": 1,
        "category": "Systems Reliability Diagram",
        "question": r"""システム稼働状態の推移が図のように表されるとき、システムのMTBFとMTTRを表した式はどれか。ここで、$t_i$はシステムの稼働時間、$r_i$はシステムの修理時間を表すものとする。

```text
    【システム稼働モデル図】
    
        故障発生          故障発生          故障発生
            |                 |                 |
     +-----+-----+     +-----+-----+     +-----+-----+     +-----+
     |   稼働    |     |   稼働    |     |   稼働    |     | 稼働|
     +-----+-----+     +-----+-----+     +-----+-----+     +-----+
           |   修理  |     |   修理  |     |   修理  |
           +---+-----+     +---+-----+     +---+-----+
               |               |               |
           |<-- t_1 -->|<-- r_1 -->|<-- t_2 -->|<-- r_2 -->|<-- t_3 -->|
```""",
        "options": [
            r"""MTBF = $\frac{1}{n} \sum_{i=1}^{n} r_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} t_i$""",
            r"""MTBF = $\frac{1}{n} \sum_{i=1}^{n} t_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} r_i$""",
            r"""MTBF = $\frac{1}{n} \sum_{i=1}^{n} t_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} (t_i + r_i)$""",
            r"""MTBF = $\frac{1}{n} \sum_{i=1}^{n} (t_i + r_i)$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} r_i$""",
        ],
        "correct_answer": r"""MTBF = $\frac{1}{n} \sum_{i=1}^{n} t_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} r_i$""",
        "explanation": r"""**日本語:** 
* **MTBF (Mean Time Between Failures: 平均故障間隔)** は、故障せずに稼動していた時間の平均値（稼働時間の総和を稼働回数で割ったもの）です。したがって、式は $\frac{1}{n} \sum_{i=1}^{n} t_i$ となります。
* **MTTR (Mean Time To Repair: 平均修理時間)** は、故障が発生してから修理が完了するまでの平均時間（修理時間の総和を修理回数で割ったもの）です。したがって、式は $\frac{1}{n} \sum_{i=1}^{n} r_i$ となります。

**English:** 
* **MTBF (Mean Time Between Failures)** is the average time a system runs without failing, calculated as the sum of operating times divided by the count. Thus, MTBF = $\frac{1}{n} \sum t_i$.
* **MTTR (Mean Time To Repair)** is the average time spent repairing failures, calculated as the sum of repair times divided by the count. Thus, MTTR = $\frac{1}{n} \sum r_i$."""
    },
    {
        "id": 2,
        "category": "MTBF & MTTR Applied Scenario Calculation",
        "question": r"""あるシステムの今年度のMTBFは3,000時間、MTTRは1,000時間である。翌年度はMTBFについて今年度の20%分の改善、MTTRについて今年度の10%分の改善を図ると、翌年度の稼働率は何%になるか。""",
        "options": [
            r"""69%""",
            r"""73%""",
            r"""77%""",
            r"""80%""",
        ],
        "correct_answer": r"""80%""",
        "explanation": r"""**日本語:** 
1. **翌年度の改善された値の算出:**
   * MTBFの20%改善（長くなる）: $\text{MTBF}_{\text{new}} = 3,000 \times (1 + 0.20) = 3,600 \text{時間}$
   * MTTRの10%改善（短くなる）: $\text{MTTR}_{\text{new}} = 1,000 \times (1 - 0.10) = 900 \text{時間}$
2. **稼働率 (Availability) の公式への適用:**
   $$\text{稼働率} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
   $$\text{稼働率}_{\text{new}} = \frac{3,600}{3,600 + 900} = \frac{3,600}{4,500} = 0.80 \to 80\%$$

**English:** 
1. **Calculate the improved metrics for the next year:**
   * MTBF 20% improvement (longer): $\text{MTBF}_{\text{new}} = 3,000 \times 1.20 = 3,600 \text{ hours}$
   * MTTR 10% improvement (shorter): $\text{MTTR}_{\text{new}} = 1,000 \times 0.90 = 900 \text{ hours}$
2. **Apply to the Availability formula:**
   $$\text{Availability} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} = \frac{3,600}{3,600 + 900} = \frac{3,600}{4,500} = 0.80 \text{ or } 80\%$$"""
    },
    {
        "id": 3,
        "category": "Systems Reliability Calculation",
        "question": r"""図のような稼働率Pのシステムで構成された多重化システム全体の稼働率を表す式はどれか。ここで、並列の部分は、どちらか一方が稼働していればよいものとする。

```text
                     +----- [ P ] ----- [ P ] -----+
                     |    (Upper Branch: Serial)   |
          -- [ P ] --+                             +--
           (Serial)  |                             |
                     +----- [ P ] ----- [ P ] -----+
                          (Lower Branch: Serial)
```""",
        "options": [
            r"""$1 - (1 - P)(1 - P^2)^2$""",
            r"""$P\{1 - (1 - P)^4\}$""",
            r"""$P\{1 - (1 - P)^2\}^2$""",
            r"""$P\{1 - (1 - P^2)^2\}$""",
        ],
        "correct_answer": r"""$P\{1 - (1 - P^2)^2\}$""",
        "explanation": r"""**日本語:**
1. **並列部分の各ブランチの稼働率:** 
   * 各ブランチは $P$ が2つ直列に接続されているため、ブランチ単体の稼働率は $P \times P = P^2$ です。
2. **並列部分全体の稼働率:** 
   * この稼働率 $P^2$ のブランチが2つ並列に接続されています。並列接続の「いずれか一方が稼働していればよい」という条件より、並列部全体の稼働率は：
     $$\text{稼働率}_{\text{parallel}} = 1 - (1 - P^2)^2$$
3. **システム全体の稼働率:** 
   * システムの先頭にある直列の $P$ と並列部分が直列に接続されているため、システム全体の稼働率はこれらを掛け合わせます：
     $$\text{システム全体} = P \times \{1 - (1 - P^2)^2\} = P\{1 - (1 - P^2)^2\}$$

**English:**
1. **Reliability of each parallel branch:**
   * Each of the two parallel branches consists of two components $P$ in series. Therefore, the reliability of a single branch is $P \times P = P^2$.
2. **Reliability of the parallel section:**
   * Two such branches are connected in parallel. The reliability of this parallel section is:
     $$\text{Reliability}_{\text{parallel}} = 1 - (1 - P^2)^2$$
3. **Total system reliability:**
   * The first component $P$ is in series with the parallel section. Thus, we multiply them:
     $$\text{Total Reliability} = P \times \{1 - (1 - P^2)^2\} = P\{1 - (1 - P^2)^2\}$$"""
    },
    {
        "id": 4,
        "category": "Hardware & Logic Circuits",
        "question": r"""図に示す全加算器の入力 x に 1，y に 0，z に 1 を入力したとき，出力となる c(けた上げ数)，s(和)の値の組合せとして，正しいものはどれか。

```text
                 +-------------------+
         x (1) --|                   |-- c (けた上げ数 / Carry-out)
         y (0) --|     全加算器      |
         z (1) --|    (Full Adder)   |-- s (和 / Sum)
                 +-------------------+
```""",
        "options": [
            r"""c = 0, s = 0""",
            r"""c = 0, s = 1""",
            r"""c = 1, s = 0""",
            r"""c = 1, s = 1""",
        ],
        "correct_answer": r"""c = 1, s = 0""",
        "explanation": r"""**日本語:**
* 全加算器は、3つの1ビットバイナリ入力（$x$, $y$, $z$）を足し合わせ、和（$s$）と2けた目への繰り上がり（$c$）を出力します。
* 入力を加算すると：
  $$x + y + z = 1 + 0 + 1 = 2_{10}$$
* 10進数の「2」を2進数で表現すると $10_2$ となります。
  * 上位ビット（けた上げ数 $c$） $= 1$
  * 下位ビット（和 $s$） $= 0$

**English:**
* A Full Adder adds three 1-bit binary inputs ($x$, $y$, $z$) and outputs the Sum ($s$) and Carry-out ($c$).
* Adding the inputs:
  $$x + y + z = 1 + 0 + 1 = 2_{10}$$
* The decimal value "2" in binary is $10_2$.
  * The higher-order bit (Carry-out $c$) $= 1$
  * The lower-order bit (Sum $s$) $= 0$"""
    },
    {
        "id": 5,
        "category": "OS & Task Management",
        "question": r"""優先度に基づくプリエンプティブなスケジューリングを行うリアルタイム OS で，二つのタスク A，B をスケジューリングする。A の方が B より優先度が高い場合にリアルタイム OS が行う動作のうち，適切なものはどれか。""",
        "options": [
            r"""A の実行中に B に起動がかかると，A を実行可能状態にして B を実行する。""",
            r"""A の実行中に B に起動がかかると，A を待ち状態にして B を実行する。""",
            r"""B の実行中に A に起動がかかると，B を実行可能状態にして A を実行する。""",
            r"""B の実行中に A に起動がかかると，B を待ち状態にして A を実行する。""",
        ],
        "correct_answer": r"""B の実行中に A に起動がかかると，B を実行可能状態にして A を実行する。""",
        "explanation": r"""**日本語:**
* **プリエンプティブ（Preemptive）方式**では、OSがCPU資源の管理権を持ち、より優先度の高いタスクが起動した際に、実行中のタスクを強制中断して実行を切り替えます。
* 優先度は **A ＞ B** であるため：
  * Aの実行中に優先度の低いBが起動しても、Aは中断されずそのまま実行を継続します。
  * 優先度の低いBの実行中に、優先度の高いAが起動すると、OSはBの実行を強制的に一時停止して「実行可能状態（READY）」に戻し、AにCPUの使用権を与えて実行します。

**English:**
* In a **preemptive multitasking OS**, the OS controls the CPU allocation and will immediately switch processing to a newly activated task if it has a higher priority than the currently running task.
* Since priority is **A > B**:
  * If the high-priority task A is running and task B starts, A continues to run.
  * If the low-priority task B is running and task A starts, the OS preempts B, moves it back to the "Ready" (実行可能) state, and immediately runs task A."""
    },
    {
        "id": 6,
        "category": "Open Source Software",
        "question": r"""OSS (Open Source Software) の特徴のうち，適切なものはどれか。ここで，OSS は OSI (Open Source Initiative) による OSD (The Open Source Definition) の定義に基づくものとする。""",
        "options": [
            r"""OSS はフリーウェアと同様に無償で入手できるが商用システムの開発への利用は禁止されている。""",
            r"""OSS をパッケージ化したり，自社のソフトウェアを組み合わせたりして，有償で販売することができる。""",
            r"""システム開発で利用できるようにソースコードで入手できるが，利用者がある数以上になるとライセンス料が発生する。""",
            r"""複製と改良は自由にできるが，改良したソフトウェアを再頒布することはできない。""",
        ],
        "correct_answer": r"""OSS をパッケージ化したり，自社のソフトウェアを組み合わせたりして，有償で販売することができる。""",
        "explanation": r"""**日本語:**
* OSDの定義に基づき、OSSには以下の特徴があります：
  * **商用利用の自由:** 商用開発への利用は禁止されていません。
  * **再配布の自由 & 有償販売可能:** 自社ソフトとOSSを組み合わせたり、パッケージ化したりして有償で販売することができます。
  * **ライセンス料の制限:** 利用者数によって追加のライセンス料を徴収することは禁止されています。
  * **改良版の配布:** 改良したソフトウェア（派生ソフトウェア）を同じライセンス下で再頒布することが認められています。

**English:**
* According to the Open Source Definition (OSD) by the OSI:
  * Commercial use is fully allowed.
  * You are permitted to combine OSS with proprietary software or bundle it into packages and sell it for a fee.
  * Fees based on user count or deployment size are strictly prohibited.
  * Distributing modified versions (derivative works) is allowed and encouraged under the terms of the original license."""
    },
    {
        "id": 7,
        "category": "Information Security Threats",
        "question": r"""キーロガーの悪用例はどれか。""",
        "options": [
            r"""通信を行う 2 者間の経路上に割り込み，両者が交換する情報を収集し，改ざんする。""",
            r"""ネットバンキング利用時に，利用者が入力したパスワードを収集する。""",
            r"""ブラウザでの動画閲覧時に，利用者の意図しない広告を勝手に表示する。""",
            r"""ブラウザの起動時に，利用者がインストールしていないツールバーを勝手に表示する。""",
        ],
        "correct_answer": r"""ネットバンキング利用時に，利用者が入力したパスワードを収集する。""",
        "explanation": r"""**日本語:**
* **キーロガー (Keylogger)** とは、キーボードからの入力を監視し、ログとして記録するプログラムやハードウェアです。
* 利用者がネットバンキングで入力したログインIDやパスワード、クレジットカード番号などを不正に収集・記録して盗み出すために悪用されます。
* 他の選択肢：
  * ア) 中間者攻撃 (Man-in-the-Middle)
  * ウ) アドウェア (Adware)
  * エ) 不正なブラウザ拡張機能 (Browser Hijacker)

**English:**
* A **Keylogger** is software or hardware designed to monitor and record keystrokes made by a user on a keyboard.
* Malicious actors use it to steal sensitive credentials, such as online banking passwords or credit card numbers, by logging the characters entered.
* Other options:
  * A) Man-in-the-Middle attack
  * C) Adware
  * D) Browser Hijacker"""
    },
    {
        "id": 8,
        "category": "Information Security Cryptography",
        "question": r"""デジタル署名を通信に利用する主な目的は二つある。一つは，メッセージの発信者を受信者が確認することである。もう一つの目的はどれか。""",
        "options": [
            r"""署名が行われた後でメッセージに変更が加えられていないかどうかを，受信者が確認すること。""",
            r"""送信の途中でメッセージが不当に解読されていないことを，受信者が確認すること。""",
            r"""発信者の ID を受信者が確認すること。""",
            r"""秘密鍵を返信してよいかどうかを受信者が確認すること。""",
        ],
        "correct_answer": r"""署名が行われた後でメッセージに変更が加えられていないかどうかを，受信者が確認すること。""",
        "explanation": r"""**日本語:**
* デジタル署名（デジタルしょめい）の主な機能は以下の2点です：
  1. **送信者のなりすまし防止 (Authentication):** 送信元が確かに本人であることを証明する。
  2. **メッセージの改ざん検知 (Integrity):** 送信後にデータが第三者によって変更（改ざん）されていないことを、受信者がハッシュ値の比較によって検証する。
* デジタル署名はデータの「暗号化（秘匿）」は行わないため、解読（盗聴）を防ぐ目的には使用されません。

**English:**
* Digital Signatures provide two core security features:
  1. **Authenticity:** Verifying the actual identity of the sender (anti-spoofing).
  2. **Integrity (改ざん検知):** Ensuring that the message has not been altered or tampered with since the signature was applied.
* Note: A digital signature does not encrypt the content, so it cannot prevent unauthorized reading (eavesdropping) of the plaintext."""
    },
    {
        "id": 9,
        "category": "Information Security Attacks",
        "question": r"""次の手順に示すセキュリティ攻撃はどれか。

(1) 攻撃者が金融機関の偽の Web サイトを用意する。
(2) 金融機関の社員を装って，偽の Web サイトへ誘導する URL を本文中に含めた電子メールを送信する。
(3) 電子メールの受信者が，その電子メールを信用して本文中の URL をクリックすると，偽の Web サイトに誘導される。
(4) 偽の Web サイトと気付かずに認証情報を入力すると，その情報が攻撃者に渡る。""",
        "options": [
            r"""DDoS 攻撃""",
            r"""フィッシング""",
            r"""ボット""",
            r"""メールヘッダーインジェクション""",
        ],
        "correct_answer": r"""フィッシング""",
        "explanation": r"""**日本語:**
* **フィッシング (Phishing)** は、実在する金融機関や有名ブランドになりすました偽メールを送り、本物そっくりの偽Webサイトに誘導して、ID、パスワード、クレジットカード番号などの個人情報を盗む詐欺手法です。
* 他の選択肢：
  * ア) DDoS攻撃：大量のトラフィックを送りつけてシステムをダウンさせる。
  * ウ) ボット：外部から遠隔操作可能な状態にするマルウェア。
  * エ) メールヘッダーインジェクション：メール送信プログラムの脆弱性を突き、偽のヘッダー情報を挿入する。

**English:**
* **Phishing** is a deceptive attack where attackers impersonate reputable financial institutions via fake emails, directing users to replica websites designed to capture credentials and credit card information.
* Other options:
  * A) DDoS Attack: Flooding networks with traffic to crash services.
  * C) Bot: Malware enabling remote execution commands.
  * D) Email Header Injection: Explitting mail-script vulnerabilities to inject malicious headers."""
    },
    {
        "id": 10,
        "category": "Network Protocols",
        "question": r"""NTP (Network Time Protocol) の用途に関する記述として，最も適切なものはどれか。""",
        "options": [
            r"""クライアントサーバシステムでの業務プログラムの応答時間を正確に測定する。""",
            r"""タイムサーバを利用して，ネットワーク上の各 PC の時刻を合わせる。""",
            r"""ファイルサーバに格納されている共用ファイルの更新時刻によって，最新かどうかを判断する。""",
            r"""メールサーバで電子メールを受信した時刻を比較して，未読の電子メールを転送する。""",
        ],
        "correct_answer": r"""タイムサーバを利用して，ネットワーク上の各 PC の時刻を合わせる。""",
        "explanation": r"""**日本語:**
* **NTP (Network Time Protocol)** は、ネットワークを介してコンピュータやサーバーのシステム時計（内部時刻）を、ネットワーク上の「タイムサーバー（時刻同期サーバー）」と同期させるための通信プロトコルです。

**English:**
* **NTP (Network Time Protocol)** is a standard internet protocol used to synchronize the system clocks of computers and networking devices with reliable "time servers" across a network."""
    },
    {
        "id": 11,
        "category": "Network Subnetting Calculation",
        "question": r"""192.168.0.0/23 (サブネットマスク 255.255.254.0) の IPv4 ネットワークにおいて，ホストとして使用できるアドレスの個数の上限はどれか。""",
        "options": [
            r"""23""",
            r"""24""",
            r"""254""",
            r"""510""",
        ],
        "correct_answer": r"""510""",
        "explanation": r"""**日本語:**
1. IPv4アドレスは全部で32ビットです。
2. プレフィックス `/23` は、先頭から23ビットがネットワーク部であることを示します。
3. ホスト部に割り当てられるのは残りのビット数：
   $$\text{ホスト部ビット数} = 32 - 23 = 9 \text{ビット}$$
4. 9ビットで表現できるアドレスの総数は $2^9 = 512$ 個。
5. この中からホストアドレスとして割り当てられない特別なアドレスを2つ差し引く必要があります：
   * ホスト部がすべて「0」のアドレス（ネットワークアドレス）
   * ホスト部がすべて「1」のアドレス（ブロードキャストアドレス）
6. したがって上限値は：
   $$2^9 - 2 = 512 - 2 = 510 \text{個}$$

**English:**
1. An IPv4 address contains 32 bits.
2. The prefix `/23` means the first 23 bits represent the network portion.
3. The remaining bits are designated for the host portion:
   $$\text{Host Bits} = 32 - 23 = 9 \text{ bits}$$
4. Total raw addresses $= 2^9 = 512$.
5. Subtract 2 reserved addresses that cannot be assigned to individual hosts:
   * Network Address (all host bits set to 0)
   * Broadcast Address (all host bits set to 1)
6. Available host address limit $= 512 - 2 = 510$."""
    },
    {
        "id": 12,
        "category": "Information Security PKI",
        "question": r"""PKI (公開鍵基盤) の認証局 (CA) が果たす役割はどれか。""",
        "options": [
            r"""共通鍵を生成する。""",
            r"""公開鍵を利用しデータの暗号化を行う。""",
            r"""失効したデジタル証明書の一覧を発行する。""",
            r"""データが改ざんされていないことを検証する。""",
        ],
        "correct_answer": r"""失効したデジタル証明書の一覧を発行する。""",
        "explanation": r"""**日本語:**
* **認証局 (CA: Certificate Authority)** は、公開鍵証明書（デジタル証明書）を発行・管理する第三者機関です。
* 主な役割として：
  * 申請者の本人確認を行い、身元と公開鍵を保証するデジタル証明書を発行。
  * 有効期限内に破棄された証明書のリストである **CRL (Certificate Revocation List: 証明書失効リスト)** を発行・公開します。
* 他の選択肢は利用側の処理や暗号通信における処理であり、CA固有の役割ではありません。

**English:**
* A **Certificate Authority (CA)** is a trusted entity that issues and manages digital certificates.
* A critical role of the CA is publishing the **CRL (Certificate Revocation List)**, which lists all certificates that have been revoked (invalidated) before their expiration date."""
    },
    {
        "id": 13,
        "category": "Information Security Safeguards",
        "question": r"""ノート型 PC やモバイル端末などにおける情報漏えい対策に該当するものはどれか。""",
        "options": [
            r"""送信するデータにチェックサムを付加する。""",
            r"""データが保存されるハードディスクをミラーリングする。""",
            r"""データのバックアップ媒体のコピーを遠隔地に保管する。""",
            r"""ノート型 PC のハードディスクの内容を暗号化する。""",
        ],
        "correct_answer": r"""ノート型 PC のハードディスクの内容を暗号化する。""",
        "explanation": r"""**日本語:**
* 紛失や盗難に遭うリスクの高いノート型PCやモバイル端末において、データの物理的な抜き取りによる情報漏洩を防ぐためには、**ハードディスクやストレージの暗号化**が極めて有効な対策です。
* 他の選択肢の分類：
  * ア) チェックサム付加：完全性 (Integrity) の確保。
  * イ) ミラーリング：可用性 (Availability) の確保。
  * ウ) バックアップ遠隔保管：可用性 (Availability) や災害対策 (DR)。

**English:**
* To protect laptops and mobile devices against data leakage in case of loss or theft, **encrypting the hard drive / storage volume** is the most effective safeguard.
* Other options:
  * A) Checksum: Ensures data Integrity.
  * B) Disk Mirroring: Promotes system Availability.
  * C) Offsite Backup: Facilitates Disaster Recovery and Availability."""
    },
    {
        "id": 14,
        "category": "Network Architecture Layers",
        "question": r"""TCP/IP 階層モデルにおいて， TCP が属する層はどれか。""",
        "options": [
            r"""アプリケーション層""",
            r"""インターネット層""",
            r"""トランスポート層""",
            r"""データリンク層""",
        ],
        "correct_answer": r"""トランスポート層""",
        "explanation": r"""**日本語:**
* **TCP (Transmission Control Protocol)** は、コネクション確立、エラー訂正、フロー制御を行い、高い信頼性を保証するプロトコルで、**トランスポート層**（OSI参照モデルでは第4層）に属します。
* 他の層の代表例：
  * アプリケーション層：HTTP, SMTP, DNS, FTP
  * インターネット層：IP, ICMP, ARP
  * データリンク層：Ethernet, PPP

**English:**
* **TCP (Transmission Control Protocol)** is a connection-oriented protocol that ensures reliable delivery of data packets. It operates at the **Transport Layer** (Layer 4 of the OSI model).
* Other layers examples:
  * Application Layer: HTTP, SMTP, DNS, FTP
  * Internet (Network) Layer: IP, ICMP, ARP
  * Data Link Layer: Ethernet, PPP"""
    },
    {
        "id": 15,
        "category": "Information Security Cryptography",
        "question": r"""公開鍵暗号方式に関する記述のうち，適切なものはどれか。""",
        "options": [
            r"""AES は，NIST が公募した公開鍵暗号方式である。""",
            r"""RSA は，素因数分解の計算の困難さを利用した公開鍵暗号方式である。""",
            r"""公開鍵暗号方式に参加する利用者の数が増えると鍵の配送が煩雑になる。""",
            r"""通信文の内容の秘匿に公開鍵暗号方式を使用する場合は，受信者の復号鍵を公開する。""",
        ],
        "correct_answer": r"""RSA は，素因数分解の計算の困難さを利用した公開鍵暗号方式である。""",
        "explanation": r"""**日本語:**
* **RSA暗号**は、非常に大きな整数の「素因数分解（Prime Factorization）」が極めて困難であることを安全性の根拠とした、代表的な公開鍵暗号方式です。
* 他の選択肢の誤り：
  * ア) AESは代表的な共通鍵暗号方式（対称暗号）です。
  * ウ) 共通鍵の管理数が爆発的に増えるのは共通鍵暗号方式です（公開鍵暗号方式では、全員が自分の秘密鍵と他者の公開鍵を1つずつ持てばよいため、鍵管理が容易です）。
  * エ) 内容を秘匿する際は、「受信者の公開鍵」で暗号化し、「受信者の秘密鍵（復号鍵）」は絶対に公開しません。

**English:**
* The **RSA** algorithm is a public-key cryptosystem whose mathematical security relies on the immense computational difficulty of factoring large composite prime numbers.
* Misconceptions in other options:
  * A) AES is a symmetric (common-key) standard, not asymmetric.
  * C) The key distribution problem gets exponentially complex as user counts grow in Symmetric encryption, not Public-key systems.
  * D) To encrypt confidential content, you use the recipient's public key; their private decryption key must remain strictly secret."""
    },
    {
        "id": 16,
        "category": "Information Security Vulnerabilities",
        "question": r"""情報セキュリティにおいてバックドアに該当するものはどれか。""",
        "options": [
            r"""アクセスする際にパスワード認証などの正規の手続が必要な Web サイトに，当該手続を経ないでアクセス可能な URL""",
            r"""インターネットに公開されているサーバの TCP ポートの中からアクティブになっているポートを探して，稼働中のサービスを特定するためのツール""",
            r"""ネットワーク上の通信パケットを取得して通信内容を見るために設けられたスイッチの LAN ポート""",
            r"""プログラムが確保するメモリ領域に，領域の大きさを超える長さの文字列を入力してあふれさせ，ダウンさせる攻撃""",
        ],
        "correct_answer": r"""アクセスする際にパスワード認証などの正規の手続が必要な Web サイトに，当該手続を経ないでアクセス可能な URL""",
        "explanation": r"""**日本語:**
* **バックドア (Backdoor: 裏口)** とは、認証などの正規の手続きを経ずに、不正アクセスを容易にするために侵入先システム内に秘密裏に設置される侵入口（仕掛け）のことです。
* 他の選択肢：
  * イ) ポートスキャナー
  * ウ) ミラーポート
  * エ) バッファオーバーフロー攻撃

**English:**
* A **Backdoor** is an undocumented or bypassed access mechanism secretly installed inside a target system, enabling illicit entry without passing through normal authentication (like login screens).
* Other options:
  * B) Port Scanner
  * C) Mirror Port (used for sniffing)
  * D) Buffer Overflow Attack"""
    },
    {
        "id": 17,
        "category": "Object-Oriented Programming",
        "question": r"""オブジェクト指向におけるカプセル化を説明したものはどれか。""",
        "options": [
            r"""同じ性質をもつ複数のオブジェクトを抽象化して，整理すること""",
            r"""基底クラスの性質を派生クラスに受けを受け継がせること""",
            r"""クラス間に共通する性質を抽出し，基底クラスを作ること""",
            r"""データとそれを操作する手続を一つのオブジェクトにして，データと手続の詳細をオブジェクトの外部から隠蔽すること""",
        ],
        "correct_answer": r"""データとそれを操作する手続を一つのオブジェクトにして，データと手続の詳細をオブジェクトの外部から隠蔽すること""",
        "explanation": r"""**日本語:**
* **カプセル化 (Encapsulation)** は、データ（プロパティ）とそのデータに対する処理（メソッド）を一体化して、オブジェクトとしてパッケージ化する概念です。
* オブジェクトの内部データは外部から見えないように保護（情報隠蔽）し、公開されたインタフェース（メソッド）を介してのみ操作を許可します。
* 他の選択肢：
  * ア) 抽象化 (Abstraction)
  * イ) 継承 (Inheritance / インヘリタンス)
  * ウ) 汎化 (Generalization)

**English:**
* **Encapsulation** binds both the state (instance variables/data) and behavior (methods) together as a single autonomous object while hiding internal implementation details from external direct access.
* Other options:
  * A) Abstraction
  * B) Inheritance
  * C) Generalization"""
    },
    {
        "id": 18,
        "category": "Software Engineering",
        "question": r"""ソフトウェアのリバースエンジニアリングの説明はどれか。""",
        "options": [
            r"""開発支援ツールなどを用いて，設計情報からソースコードを自動生成する。""",
            r"""外部から見たときの振る舞いを変えずに，ソフトウェアの内部構造を変える。""",
            r"""既存のソフトウェアを解析し，その仕様や構造を明らかにする。""",
            r"""既存のソフトウェアを分析し理解した上で，ソフトウェア全体を新しく構築し直す。""",
        ],
        "correct_answer": r"""既存のソフトウェアを解析し，その仕様や構造を明らかにする。""",
        "explanation": r"""**日本語:**
* **リバースエンジニアリング (Reverse Engineering)** とは、すでに完成しているシステムやオブジェクトコードを解析・分解することで、その基本設計や仕様、ソースコード構造を特定する技術です。
* 他の選択肢：
  * ア) フォワードエンジニアリング
  * イ) リファクタリング (Refactoring)
  * エ) リエンジニアリング (Re-engineering)

**English:**
* **Reverse Engineering** is the process of examining and analyzing compiled binary executables or physical machinery to deduce their original source code, architectural structure, and technical specification.
* Other options:
  * A) Forward Engineering
  * B) Refactoring
  * D) Re-engineering"""
    },
    {
        "id": 19,
        "category": "Software Testing Types",
        "question": r"""ソフトウェアの保守に当たり，修正や変更がほかの正常箇所に影響していないことを確認するテストはどれか。""",
        "options": [
            r"""性能テスト""",
            r"""耐久テスト""",
            r"""退行テスト""",
            r"""例外処理テスト""",
        ],
        "correct_answer": r"""退行テスト""",
        "explanation": r"""**日本語:**
* **退行テスト (Regression Test: リグレッションテスト、回帰テスト)** とは、システムの一部を修正した後に、その修正が関係のない既存の動作していた機能（他のモジュール）に不具合や悪影響をもたらしていないか（デグレードしていないか）を検証するテストです。

**English:**
* **Regression Testing (退行テスト/回帰テスト)** is run after any modifications, updates, or bug fixes are applied to confirm that unchanged parts of the codebase still behave properly and have not been corrupted (degraded)."""
    },
    {
        "id": 20,
        "category": "Software Testing Methodologies",
        "question": r"""ブラックボックステストにおけるテストケースの設計方法として，適切なものはどれか。""",
        "options": [
            r"""プログラム仕様書の作成又はコーディングが終了した段階で，仕様書やソースリストを参照して，テストケースを設計する。""",
            r"""プログラムの機能仕様やインタフェースの仕様に基づいて，テストケースを設計する。""",
            r"""プログラムの処理手順や内部構造に基づいて，テストケースを設計する。""",
            r"""プログラムのすべての条件判定で，真と偽をそれぞれ 1 回以上実行させることを基準に，テストケースを設計する。""",
        ],
        "correct_answer": r"""プログラムの機能仕様やインタフェースの仕様に基づいて，テストケースを設計する。""",
        "explanation": r"""**日本語:**
* **ブラックボックステスト (Black-Box Testing)** とは、システムの「内部構造やプログラムコード」は見ずに、外部から見た入出力（仕様やインタフェース、機能）に着目してテストケースを設計する技法です。
* 他の選択肢はすべて、内部のソースコードや制御フローに基づいてテストを設計する「ホワイトボックステスト」の説明です。

**English:**
* **Black-Box Testing** designs test scenarios looking strictly at functional specifications and external interfaces without inspecting the inner source code or execution flows.
* The other choices pertain to White-Box testing, which checks inner conditional expressions and block logic."""
    },
    {
        "id": 21,
        "category": "Software Testing Guidelines",
        "question": r"""モジュール単体テストに関する記述として，最も適切なものはどれか。""",
        "options": [
            r"""通常はコーディングを行ったプログラマではなく，専任のテスト要員がテストケースを作成し実行する。""",
            r"""モジュール間インタフェースは，モジュール単体ではテストできないので，単体テストの対象外となる。""",
            r"""モジュール設計書は，正しいことが検証済みであるので，テスト結果に問題があるときは，テストケース又はモジュールに誤りがある。""",
            r"""モジュール設計書を見ながら，原則としてすべてのロジックパスを一度は通るようなテストケースによって，検証を行う。""",
        ],
        "correct_answer": r"""モジュール設計書を見ながら，原則としてすべてのロジックパスを一度は通るようなテストケースによって，検証を行う。""",
        "explanation": r"""**日本語:**
* モジュール単体テスト（単体テスト）は、コーディングを行ったプログラマが実施します。
* プログラム設計図（詳細設計書）を確認しながら、原則としてモジュール内の**すべてのロジックパス（ロジックの経路）を一度は網羅する**ようなテストケースを設計して検証を行います。

**English:**
* Module unit testing (単体テスト) is usually performed directly by the programmer who authored the module.
* Using the detailed module specification sheets, test cases are drafted to ensure that, in principle, every logic path within the module is covered at least once."""
    },
    {
        "id": 22,
        "category": "White-Box Testing Path Coverage",
        "question": r"""右図の構造をもつプログラムに対して，ホワイトボックステストのテストケースを設計するとき，少なくとも実施しなければならないテストケース数が最大になるテスト技法はどれか。

```text
                     |
                     v
             /----------------\
            /  A > 0 かつ      \    真 (True)
           <    B = 1 ?         >------------> [ X = X + 1 ]
            \                  /                     |
             \----------------/                      |
                     |                               |
                     | 偽 (False)                     |
                     v                               |
                     +<------------------------------/
                     |
                     v
```""",
        "options": [
            r"""条件網羅""",
            r"""判定条件網羅""",
            r"""複数条件網羅""",
            r"""命令網羅""",
        ],
        "correct_answer": r"""複数条件網羅""",
        "explanation": r"""**日本語:**
* **複数条件網羅 (Multiple Condition Coverage)** は、最もテストケース数が多くなるホワイトボックステストの技法です。
* 判定条件に含まれる「個々の条件（A > 0, B = 1）」の**真・偽のすべての可能な組み合わせ**をテストします：
  1. `A > 0` = 真, `B = 1` = 真 (全体：真)
  2. `A > 0` = 真, `B = 1` = 偽 (全体：偽)
  3. `A > 0` = 偽, `B = 1` = 真 (全体：偽)
  4. `A > 0` = 偽, `B = 1` = 偽 (全体：偽)
* したがって、最低でも4パターンのテストデータ（テストケース）が必要になり、他の網羅（命令網羅: 1, 判定条件/分岐網羅: 2, 条件網羅: 2）と比較して最大になります。

**English:**
* **Multiple Condition Coverage (複数条件網羅)** is the most thorough white-box path testing method. It tests every combination of logical values for atomic sub-conditions within a decision branch:
  1. `A > 0` (True) and `B = 1` (True)
  2. `A > 0` (True) and `B = 1` (False)
  3. `A > 0` (False) and `B = 1` (True)
  4. `A > 0` (False) and `B = 1` (False)
* This requires 4 distinct test inputs, which is more than instruction coverage (1), decision coverage (2), or basic condition coverage (2)."""
    },
    {
        "id": 23,
        "category": "Email Protocols",
        "question": r"""インターネットにおける電子メールの規約で、ヘッダフィールドの拡張を行い、テキストだけでなく、音声、画像なども扱えるようにしたものはどれか。""",
        "options": [
            r"""HTML""",
            r"""MHS""",
            r"""MIME""",
            r"""SMTP""",
        ],
        "correct_answer": r"""MIME""",
        "explanation": r"""**日本語:**
* **MIME (Multipurpose Internet Mail Extensions)** は、本来ASCIIテキスト文字しか送信できなかったSMTP電子メール（7ビットテキスト制限）を拡張し、日本語などのマルチバイト文字や、画像、音声、PDFなどのバイナリファイルを添付できるようにした仕様です。

**English:**
* **MIME (Multipurpose Internet Mail Extensions)** extends the basic 7-bit ASCII format of simple text emails (SMTP) to enable multi-byte characters, embedded graphics, audio clips, and various application file attachments."""
    },
    {
        "id": 24,
        "category": "White-Box Testing Concept",
        "question": r"""テスト手法の1つであるホワイトボックステストの説明として、適切なものはどれか。""",
        "options": [
            r"""下位モジュールから上位モジュールへと順次結合してテストする。""",
            r"""上位モジュールから下位モジュールへと順次結合してテストする。""",
            r"""モジュールの内部構造に注目してテストする。""",
            r"""モジュールの内部構造を考慮することなく、仕様書どおり機能が作動するかどうかをテストする。""",
        ],
        "correct_answer": r"""モジュールの内部構造に注目してテストする。""",
        "explanation": r"""**日本語:**
* **ホワイトボックステスト (White-Box Testing)** は、プログラムの「中身（制御構造や条件式）」が見える状態で、内部の論理的なパスがすべて正しく実行されるかどうかを検証するテスト手法です。
* 他の選択肢：
  * ア) ボトムアップテスト（結合テスト手法）
  * イ) トップダウンテスト（結合テスト手法）
  * エ) ブラックボックステスト

**English:**
* **White-Box Testing** uses visibility into the program code structure and inner paths to analyze and design test cases based on control flows and decisions.
* Other options:
  * A) Bottom-up testing (integration testing)
  * B) Top-down testing (integration testing)
  * D) Black-Box testing"""
    },
    {
        "id": 25,
        "category": "Business Strategy",
        "question": r"""コアコンピタンスを説明したものはどれか。""",
        "options": [
            r"""経営活動における基本精神や行動指針""",
            r"""事業戦略の遂行によって達成すべき到達目標""",
            r"""自社を取り巻く環境に関するビジネス上の機会と脅威""",
            r"""他社との競争優位の源泉となる経営資源及び企業能力""",
        ],
        "correct_answer": r"""他社との競争優位の源泉となる経営資源及び企業能力""",
        "explanation": r"""**日本語:**
* **コアコンピタンス (Core Competence)** とは、競合他社に真似できない、自社に特有で卓越した技術力や能力、ノウハウ（競争優位の源泉）を指します。
* 他の選択肢：
  * ア) 経営理念 (Corporate Philosophy)
  * イ) 経営目標 (Corporate Objectives / KGI)
  * ウ) SWOT分析における外部要因（機会、脅威）

**English:**
* **Core Competence** represents the unique bundle of technological expertise, institutional knowledge, and operational capabilities owned by an enterprise that competitors cannot easily copy, serving as the fountainhead of its sustainable competitive edge.
* Other options:
  * A) Corporate Philosophy
  * B) Business Objectives / KGI
  * C) SWOT Opportunities and Threats"""
    },
    {
        "id": 26,
        "category": "Lesson 8 - System Performance Indicators",
        "question": r"""一つのジョブについてのターンアラウンドタイム、CPU時間、入出力時間及び処理待ち時間の4つの時間の関係を表す式はどれか。ここで、ほかのオーバーヘッド時間は考慮しないものとする。""",
        "options": [
            r"""処理待ち時間 ＝ CPU時間 ＋ ターンアラウンドタイム ＋ 入出力時間""",
            r"""処理待ち時間 ＝ CPU時間 － ターンアラウンドタイム ＋ 入出力時間""",
            r"""処理待ち時間 ＝ ターンアラウンドタイム － CPU時間 － 入出力時間""",
            r"""処理待ち時間 ＝ 入出力時間 － CPU時間 － ターンアラウンドタイム""",
        ],
        "correct_answer": r"""処理待ち時間 ＝ ターンアラウンドタイム － CPU時間 － 入出力時間""",
        "explanation": r"""**日本語:**
* **ターンアラウンドタイム (TAT: Turnaround Time)** とは、ジョブをコンピュータ（システム）に投入してから、すべての処理結果が出力し終わるまでの**全体の所要時間**です。
* 全体時間 (TAT) は、CPU処理時間、I/O処理時間、およびキューで順番を待っている「処理待ち時間」の和で表されます：
  $$\text{TAT} = \text{CPU時間} + \text{入出力時間} + \text{処理待ち時間}$$
* これを「処理待ち時間」について解くように変形すると：
  $$\text{処理待ち時間} = \text{TAT} - \text{CPU時間} - \text{入出力時間}$$

**English:**
* **Turnaround Time (TAT)** is the total duration from job submission to complete result delivery:
  $$\text{TAT} = \text{CPU Time} + \text{I/O Time} + \text{Wait Time}$$
* Solving for Wait Time:
  $$\text{Wait Time} = \text{TAT} - \text{CPU Time} - \text{I/O Time}$$"""
    },
    {
        "id": 27,
        "category": "Lesson 8 - OS Queue Simulation",
        "question": r"""ジョブ処理能力の計測結果が以下の通りであるシステムにおいて、ジョブの待機状態はどう推移するか。
(1) 多重度3でジョブを並列実行する。
(2) ジョブは5分間隔で発生し、実行時間は20分（多重度に依存しない）である。
(3) 各ジョブは実行終了後にスプーリング機能を利用して印刷し、印刷時間は15分である。
(4) プリンターは2台使用する。""",
        "options": [
            r"""印刷待ちだけが増加している。""",
            r"""実行待ちだけが増加している。""",
            r"""実行待ちと印刷待ちが増加している。""",
            r"""実行待ちも印刷待ちも発生していない。""",
        ],
        "correct_answer": r"""実行待ちと印刷待ちが増加している。""",
        "explanation": r"""**日本語:**
1. **CPU実行待ち(実行待ちキュー)の検証:**
   * 1つのジョブが20分かかり、同時に最大3つのジョブを実行（多重度3）できます。
   * したがって、システムのジョブ完了処理速度は：
     $$\text{実行処理能力} = \frac{20 \text{分}}{3} = 6.66 \text{分/件}$$
   * ジョブは5分間隔で発生するため、発生頻度の方が高く、処理が追いつきません（5分 ＜ 6.66分）。よって、**実行待ちジョブは無限に増加します**。
2. **プリンター印刷待ちの検証:**
   * 1つのジョブの印刷には15分かかり、2台のプリンターで並列印刷できます。
   * したがって、印刷処理能力は：
     $$\text{印刷処理能力} = \frac{15 \text{分}}{2} = 7.5 \text{分/件}$$
   * 印刷要求が来る間隔は、CPUを抜けてくる間隔（＝実行処理能力の6.66分/件）です。
   * 印刷要求間隔（6.66分）のほうがプリンター処理速度（7.5分）よりも速いため、**印刷待ちジョブも無限に増加します**。

**English:**
1. **Analyze CPU Queue:**
   * Multi-programming level is 3, job duration is 20 minutes.
   * System throughput $= \frac{20}{3} = 6.66 \text{ mins/job}$.
   * Since jobs arrive every 5 minutes (5 < 6.66), the arrival rate is faster than the execution capacity. Thus, **the execution queue increases**.
2. **Analyze Print Queue:**
   * 2 printers, each print takes 15 minutes.
   * Printing capacity $= \frac{15}{2} = 7.5 \text{ mins/job}$.
   * Print requests arrive as jobs exit execution (every 6.66 minutes).
   * Since requests arrive faster than printers can process them (6.66 < 7.5), **the print queue also increases**."""
    },
    {
        "id": 28,
        "category": "Lesson 8 - OS Memory Management",
        "question": r"""記憶領域の動的な割り当て及び解放を繰り返すことによって、どこからも利用されない記憶領域が発生することがある。このような散らばった不要な記憶領域を回収し、再び利用可能にする処理はどれか。""",
        "options": [
            r"""ガーベジコレクション""",
            r"""スタック""",
            r"""ヒープ""",
            r"""フラグメンテーション""",
        ],
        "correct_answer": r"""ガーベジコレクション""",
        "explanation": r"""**日本語:**
* **ガーベジコレクション (Garbage Collection: GC)** は、プログラムが動的に確保したメモリ空間のうち、不要になった（参照されなくなった）領域を自動的に検出して解放・回収し、再びメモリ割り当て用に再利用可能にする機能です。
* 他の用語：
  * イ) スタック：後入れ先出し (LIFO) 構造。
  * ウ) ヒープ：動的に確保できるメモリ領域。
  * エ) フラグメンテーション：メモリの断片化。

**English:**
* **Garbage Collection (GC)** is an automatic memory management feature that sweeps through system memory to find, deallocate, and reclaim dynamic memory blocks that are no longer referenced by the program.
* Other terms:
  * B) Stack: A LIFO data structure.
  * C) Heap: The pool of memory dynamically allocated at runtime.
  * D) Fragmentation: Splitting of memory into non-contiguous blocks."""
    },
    {
        "id": 29,
        "category": "Lesson 9 - Language Processors",
        "question": r"""プログラムを構成するモジュールの結合を，プログラムの実行時に行う方式はどれか。""",
        "options": [
            r"""インタプリタ""",
            r"""オーバーレイ""",
            r"""静的リンキング""",
            r"""動的リンキング""",
        ],
        "correct_answer": r"""動的リンキング""",
        "explanation": r"""**日本語:**
* **動的リンキング (Dynamic Linking)** とは、コンパイル時ではなく、プログラムの実行時にモジュール（DLLファイルや共用ライブラリなど）をロードしてメインプログラムと結合・リンクする方式です。これにより実行ファイルのサイズが削減され、メモリを効率的に使用できます。
* 他の用語：
  * ウ) 静的リンキング：実行ファイルを作成する段階で、すべてのモジュールを結合します。

**English:**
* **Dynamic Linking** binds program modules (like .dll or .so shared libraries) together at runtime, rather than statically pre-linking everything during compilation. This saves memory and executable disk space."""
    },
    {
        "id": 30,
        "category": "Lesson 9 - OS Architectures",
        "question": r"""パソコンの OS が提供する機能を利用するための API に関する記述のうち，適切なものはどれか。""",
        "options": [
            r"""API で呼び出される OS の処理モジュールは，あらかじめそれを利用するプログラムに静的にリンクしておく必要がある。""",
            r"""OS の API が提供されない周辺機器はユーザープログラムから利用又は制御することはできない。""",
            r"""アーキテクチャの異なる CPU 間でも，同じ OS とその API を使用することによって，プログラムの互換性を高め，移植時の工数を削減することが可能である。""",
            r"""異なる OS 間でも API は共通であり，API だけを使用したプログラムであれば，再コンパイルだけでほかの OS への移植が可能である。""",
        ],
        "correct_answer": r"""アーキテクチャの異なる CPU 間でも，同じ OS とその API を使用することによって，プログラムの互換性を高め，移植時の工数を削減することが可能である。""",
        "explanation": r"""**日本語:**
* **API (Application Programming Interface)** は、アプリケーション開発を抽象化するインタフェースです。
* 同じOSおよび同一のAPIを使っていれば、CPUアーキテクチャが異なっていても、プログラムコードを変更せずに再ビルド・コンパイルするだけで移植可能となるため、移植コストを大幅に削減できます。

**English:**
* An **API (Application Programming Interface)** isolates software logic from underlying machine changes.
* If different CPUs run the same OS and support the same API, application portability is greatly enhanced because code compiles identically, minimizing porting engineering hours."""
    },
    {
        "id": 31,
        "category": "Lesson 9 - Hardware & Logic Circuits",
        "question": r"""図に示す論理回路と等価な論理式はどれか。ここで，論理式中の"・"は論理積，"＋"は論理和，$\bar{X}$はXの否定を表す。

```text
       A ----+------------------\____ [ AND ] -----\
             |                  /                  \____ [ OR ] ----- X
             |  +-- [ NOT ] ----\____ [ OR  ] -----+                    (out)
             +--|               /                  |
                |  +-- [ NOT ] -+                  /---- [ AND ] -----/
       B -------+--|                               /
                   +------------------------------/
```""",
        "options": [
            r"""$X = A \cdot B + \overline{A \cdot B}$""",
            r"""$X = A \cdot B + \overline{A} \cdot \overline{B}$""",
            r"""$X = A \cdot \overline{B} + \overline{A} \cdot B$""",
            r"""$X = (\overline{A} + B) \cdot (A + \overline{B})$""",
        ],
        "correct_answer": r"""$X = A \cdot \overline{B} + \overline{A} \cdot B$""",
        "explanation": r"""**日本語:**
* 回路の結線を順番に論理式に変換します：
  1. 上側のNOTゲートの入力は $A$ なので、出力は $\overline{A}$ です。
  2. 下側のNOTゲートの入力は $B$ なので、出力は $\overline{B}$ です。
  3. 中央のORゲートはこれら2つのNOT出力を入力とするため、出力は $\overline{A} + \overline{B}$ です。
  4. 上側のANDゲートへの入力は $A$ と中央のOR出力 $\overline{A} + \overline{B}$ なので、出力は：
     $$Y_1 = A \cdot (\overline{A} + \overline{B}) = A \cdot \overline{A} + A \cdot \overline{B} = 0 + A \cdot \overline{B} = A \cdot \overline{B}$$
  5. 下側のANDゲートへの入力は $B$ と中央のOR出力 $\overline{A} + \overline{B}$ なので、出力は：
     $$Y_2 = B \cdot (\overline{A} + \overline{B}) = \overline{A} \cdot B + \overline{B} \cdot B = \overline{A} \cdot B + 0 = \overline{A} \cdot B$$
  6. 最右部のORゲートは $Y_1$ と $Y_2$ を足し合わせるため、全体の出力 $X$ は：
     $$X = A \cdot \overline{B} + \overline{A} \cdot B \text{ (排他的論理和: XOR)}$$

**English:**
* Step-by-step logic gate tracing:
  1. Top NOT gate output is $\overline{A}$, and bottom NOT gate output is $\overline{B}$.
  2. Middle OR gate joins them: $\overline{A} + \overline{B}$.
  3. Top AND gate combines input $A$ and middle OR output:
     $$Y_1 = A \cdot (\overline{A} + \overline{B}) = A \cdot \overline{B}$$
  4. Bottom AND gate combines input $B$ and middle OR output:
     $$Y_2 = B \cdot (\overline{A} + \overline{B}) = \overline{A} \cdot B$$
  5. The outermost OR gate merges $Y_1$ and $Y_2$:
     $$X = A \cdot \overline{B} + \overline{A} \cdot B \text{ (Exclusive OR / XOR)}$$"""
    },
    {
        "id": 32,
        "category": "Lesson 9 - Program Translation Pipeline",
        "question": r"""図はプログラムを翻訳して実行するまでの流れを示したものである。コンパイラ，リンカ，ローダの入出力関係において、a, b, c に入る適切な用語の組合せはどれか。

```text
    [ 原始プログラム ] 
          |
          v
     [ コンパイラ ]
          |
          v
        [ a ] 
          |         [ b ]
          v           |
       [ リンカ ] <---+
          |
          v
        [ c ] 
          |
          v
       [ ローダ ] ---> [ 主記憶上の実行可能イメージ ]
```""",
        "options": [
            r"""a: 目的プログラム, b: ライブラリモジュール, c: ロードモジュール""",
            r"""a: ライブラリモジュール, b: ロードモジュール, c: 目的プログラム""",
            r"""a: ロードモジュール, b: 目的プログラム, c: ライブラリモジュール""",
            r"""a: ロードモジュール, b: ライブラリモジュール, c: 目的プログラム""",
        ],
        "correct_answer": r"""a: 目的プログラム, b: ライブラリモジュール, c: ロードモジュール""",
        "explanation": r"""**日本語:**
* **プログラム開発・ビルドの基本フロー:**
  1. 人間が書いた「原始プログラム（ソースプログラム）」を、**コンパイラ**が翻訳して機械語の**「a: 目的プログラム（オブジェクトモジュール）」**を生成します。
  2. **リンカ（連結編集プログラム）**が、目的プログラムと他の**「b: ライブラリモジュール」**を結合し、実行可能な形式である**「c: ロードモジュール」**を作成します。
  3. **ローダ**が、このロードモジュールを主記憶装置（メインメモリ）にロードして実行可能状態にします。

**English:**
* **Standard compilation build pipeline:**
  1. The **compiler** translates the user's source code into a machine-readable **"a: Object Module (目的プログラム)"**.
  2. The **linker** connects this object module with shared **"b: Library Modules (ライブラリモジュール)"** to output a executable **"c: Load Module (ロードモジュール)"**.
  3. The **loader** copies the load module into primary RAM memory to run."""
    },
    {
        "id": 33,
        "category": "Lesson 9 - OS Task Scheduling",
        "question": r"""ノンプリエンプティブ（Non-preemptive）なタスクスケジューリング方式の説明として，適切なものはどれか。""",
        "options": [
            r"""新しいタスクが実行可能状態になるたびに，各タスクの残りの実行時間を評価し，その時間が短いものから順に実行する。""",
            r"""実行状態としたタスクが決められた時間内に待ち状態に遷移しないときに，そのタスクを中断して実行待ち行列にある次のタスクを実行状態とする。""",
            r"""実行状態としたタスクが自ら待ち状態に遷移するか終了するまで，他のタスクを実行状態とすることができない。""",
            r"""タスクが実行可能状態になったときに，そのタスクの優先度と，その時，実行状態であるタスクの優先度とを比較して，優先度が高い方のタスクを実行状態とする。""",
        ],
        "correct_answer": r"""実行状態としたタスクが自ら待ち状態に遷移するか終了するまで，他のタスクを実行状態とすることができない。""",
        "explanation": r"""**日本語:**
* **ノンプリエンプティブ (Non-preemptive) 方式**は、CPUの使用権管理をOSではなく実行中のプログラム（タスク）自身に委ねるスケジューリング方式です。
* 実行状態になったタスクは、自発的にCPUをOSに返却（I/O待ちなどでスリープ・待ち状態に遷移）するか、処理を完了して終了するまで、他のタスクに邪魔されずにCPUを占有し続けます。

**English:**
* Under **Non-preemptive Scheduling**, running programs keep continuous control of the CPU.
* A task occupies the CPU uninterrupted until it voluntarily yields execution control (moves to the "Wait" state for I/O) or finishes completely."""
    },
    {
        "id": 34,
        "category": "Lesson 9 - Development Tools",
        "question": r"""オープンソースの統合開発環境であって，アプリケーション開発のためのソフトウェア及び支援ツール類をまとめたものはどれか。""",
        "options": [
            r"""Eclipse""",
            r"""Perl""",
            r"""PHP""",
            r"""Ruby""",
        ],
        "correct_answer": r"""Eclipse""",
        "explanation": r"""**日本語:**
* **Eclipse（エクリプス）**は、代表的なオープンソースの**統合開発環境 (IDE: Integrated Development Environment)** です。Javaを筆頭に、C++, PHP, Pythonなど多様なアプリケーション開発を支援するエディタやデバッガを完備しています。
* 他の選択肢はすべて「スクリプト言語」の名称です。

**English:**
* **Eclipse** is a standard, open-source **Integrated Development Environment (IDE)** bundled with editors and debuggers to facilitate application coding.
* Other choices are scripting language processors."""
    },
    {
        "id": 35,
        "category": "Lesson 9 - Logic Optimization",
        "question": r"""次のカルノー図で表される論理回路の出力を最も簡略化した論理式はどれか。

```text
               A    \bar{A}
           +------+------+
        B  |  1   |  0   |
           +------+------+
   \bar{B} |  1   |  1   |
           +------+------+
```""",
        "options": [
            r"""$X = A \cdot B$""",
            r"""$X = A + \overline{B}$""",
            r"""$X = B + \overline{A}$""",
            r"""$X = \overline{A \cdot B}$""",
        ],
        "correct_answer": r"""$X = A + \overline{B}$""",
        "explanation": r"""**日本語:**
1. 与えられたカルノー図の「1」の位置を確認します：
   * $(A, B) = (1, 1)$ に $1$
   * $(A, \overline{B}) = (1, 0)$ に $1$
   * $(\overline{A}, \overline{B}) = (0, 0)$ に $1$
2. これを隣接する2マスのグループで括ります（ループ化）：
   * 縦方向のループ：$(A, B)$ と $(A, \overline{B})$。このグループは $B$ の状態に関係なく $A$ が1のとき1になるため、論理式は **$A$** です。
   * 横方向のループ：$(A, \overline{B})$ と $(\overline{A}, \overline{B})$。このグループは $A$ の状態に関係なく $\overline{B}$ が1のとき1になるため、論理式は **$\overline{B}$** です。
3. 2つのグループを論理和（OR）で結ぶと、最も簡略化された論理式は **$X = A + \overline{B}$** になります。

**English:**
1. Grouping adjacent cells of "1" in the Karnaugh map:
   * Vertical group: $(A, B)$ and $(A, \overline{B})$. This depends only on **$A$**.
   * Horizontal group: $(A, \overline{B})$ and $(\overline{A}, \overline{B})$. This depends only on **$\overline{B}$**.
2. Summing these terms yields the simplified expression:
   $$X = A + \overline{B}$$"""
    },
    {
        "id": 36,
        "category": "Lesson 10 - Satellite Delay Calculation",
        "question": r"""地上から高度約 36,000km の静止軌道衛星を中継して，地上の A 地点と B 地点で通信をする。衛星とA 地点，衛星と B 地点の距離がどちらも 37,500km であり，衛星での中継による遅延を 10 ミリ秒とするとき，A から送信し始めたデータが B に到達するまでの伝送遅延時間は何秒か。ここで，電波の伝搬速度は $3 \times 10^8$ m／秒とする。""",
        "options": [
            r"""0.13""",
            r"""0.26""",
            r"""0.35""",
            r"""0.52""",
        ],
        "correct_answer": r"""0.26""",
        "explanation": r"""**日本語:**
1. **総伝搬距離の算出:**
   * 電波は「A地点 $\to$ 衛星」と「衛星 $\to$ B地点」の経路を走るため、総距離は：
     $$\text{総距離} = 37,500 \text{ km} \times 2 = 75,000 \text{ km} = 7.5 \times 10^7 \text{ m}$$
2. **電波の伝搬時間の算出:**
   * 時間 ＝ 距離 $\div$ 速度 公式を適用します：
     $$\text{伝搬時間} = \frac{7.5 \times 10^7 \text{ m}}{3 \times 10^8 \text{ m/秒}} = 0.25 \text{ 秒}$$
3. **中継処理遅延の加算:**
   * 衛星内部での処理遅延は10ミリ秒（＝0.01秒）です：
     $$\text{総遅延時間} = 0.25 \text{ 秒} + 0.01 \text{ 秒} = 0.26 \text{ 秒}$$

**English:**
1. **Calculate total propagation distance:**
   * The radio signal travels from A to the satellite and then from the satellite to B:
     $$\text{Total Distance} = 37,500 \text{ km} \times 2 = 75,000 \text{ km} = 7.5 \times 10^7 \text{ m}$$
2. **Calculate wave transit time:**
   * Using $\text{Time} = \frac{\text{Distance}}{\text{Speed}}$:
     $$\text{Transit Time} = \frac{7.5 \times 10^7 \text{ m}}{3 \times 10^8 \text{ m/s}} = 0.25 \text{ seconds}$$
3. **Include processing relay delay:**
   * The satellite delay is 10 ms ($0.01$ seconds):
     $$\text{Total transmission delay} = 0.25 + 0.01 = 0.26 \text{ seconds}$$"""
    },
    {
        "id": 37,
        "category": "Lesson 10 - Threats and Security Safeguards",
        "question": r"""情報システムヘの脅威とセキュリティ対策の組合せのうち，適切なものはどれか。""",
        "options": [
            r"""ア) 脅威：誤操作によるデータの論理的な破壊 | 対策：ディスクアレイ (RAID)""",
            r"""イ) 脅威：地震と火災 | 対策：コンピュータ内で複数の仮想化 OS を利用したデータの二重化""",
            r"""ウ) 脅威：伝送中のデータへの不正アクセス | 対策：HDLC 手順の CRC""",
            r"""エ) 脅威：メッセージの改ざん | 対策：公開鍵暗号方式を応用したデジタル署名""",
        ],
        "correct_answer": r"""エ) 脅威：メッセージの改ざん | 対策：公開鍵暗号方式を応用したデジタル署名""",
        "explanation": r"""**日本語:**
* 各選択肢の評価：
  * ア) 誤操作によるファイル削除などの論理的な破壊は、RAID（ハードウェアの物理故障対策）では防げません。バックアップが必要です。
  * イ) 地震や火災（物理的被災）に対しては、同一サーバー内の仮想OS二重化では同時に被災するため意味がありません。遠隔地バックアップやバックアップ電源が必要です。
  * ウ) CRCは伝送中の「電気的なビットエラー（ノイズ）」を検知する技術であり、意図的な不正アクセス（盗聴や漏洩）を防ぐものではありません。
  * エ) 送信メッセージの第三者による改ざんは、ハッシュ値を含む**デジタル署名**を検証することで完全に検知可能です。正しい組み合わせです。

**English:**
* Analysis of security threat-safeguard combinations:
  * A) Logical database deletion cannot be salvaged by hardware disk arrays (RAID). It requires offline backups.
  * B) Natural disasters like fires require physical separation or offsite disaster recovery centers.
  * C) CRC is a cyclic error-detecting checksum for electrical noise errors, not encryption for secure privacy.
  * D) Digital Signatures using asymmetric cryptography guarantee data integrity and successfully flag unauthorized tampering (alteration)."""
    },
    {
        "id": 38,
        "category": "Lesson 10 - Cryptographic Foundations",
        "question": r"""公開鍵暗号方式に関する記述として，適切なものはどれか。""",
        "options": [
            r"""AES などの暗号方式がある。""",
            r"""RSA や楕円(だえん)曲線暗号などの暗号方式がある。""",
            r"""暗号化鍵と復号鍵が同一である。""",
            r"""共通鍵の配送が必要である。""",
        ],
        "correct_answer": r"""RSA や楕円(だえん)曲線暗号などの暗号方式がある。""",
        "explanation": r"""**日本語:**
* **公開鍵暗号方式**には、RSAや楕円曲線暗号（ECC）などのアルゴリズムが存在します。
* 共通鍵暗号方式（AESなど）とは異なり、暗号化と復号に異なるペア鍵を使用するため、あらかじめ秘密の共通鍵を受信者へ安全に送出（鍵配送問題）する必要がありません。

**English:**
* **Public-Key Cryptography** relies on mathematical algorithms like RSA and Elliptic Curve Cryptography (ECC).
* It bypasses the common-key distribution issue because the public encryption key is widely published, while decryption is bound strictly to the private key held by the recipient."""
    },
    {
        "id": 39,
        "category": "Lesson 10 - RDB Referential Integrity",
        "question": r"""関係データベース"注文"表の"顧客番号"は，"顧客"表の主キー"顧客番号"に対応する外部キーである。このとき、参照の整合性を損なうデータ操作はどれか。

```text
    【注文】表                        【顧客】表
+----------+----------+         +----------+----------+
| 伝票番号 | 顧客番号 |         | 顧客番号 |  顧客名  |
+----------+----------+         +----------+----------+
|   0001   |   C005   |         |   C005   |   福島   |
|   0002   |   K001   |         |   D010   |   千葉   |
|   0003   |   C005   |         |   K001   |   長野   |
|   0004   |   D010   |         |   L035   |   宮崎   |
+----------+----------+         +----------+----------+
```""",
        "options": [
            r""""顧客"表の行 [ L035 | 宮崎 ] を削除する。""",
            r""""注文"表に行 [ 0005 | D010 ] を追加する。""",
            r""""注文"表に行 [ 0006 | F020 ] を追加する。""",
            r""""注文"表の行 [ 0002 | K001 ] を削除する。""",
        ],
        "correct_answer": r""""注文"表に行 [ 0006 | F020 ] を追加する。""",
        "explanation": r"""**日本語:**
* **参照整合性制約（外部キー制約）**とは、外部キーに入力する値は、参照先テーブルの主キーに存在する値でなければならないというルールです。
* 「注文」表の「顧客番号」は「顧客」表の「顧客番号」を参照しています。
* 「顧客」表の主キーには `C005`, `D010`, `K001`, `L035` しか存在しません。
* したがって、「注文」表に存在しない顧客番号 `F020` を含む新規注文レコード `[ 0006 | F020 ]` を追加しようとすると、参照整合性制約違反となりシステムに拒否されます。

**English:**
* **Referential Integrity Constraints** dictate that any value written to a Foreign Key column must exist within the referenced Primary Key column.
* The "顧客番号" (Customer ID) field in "注文" (Orders) references "顧客" (Customers).
* Since customer ID `F020` does not exist in the "顧客" primary table, attempting to insert order `[ 0006 | F020 ]` violates integrity constraint and fails."""
    },
    {
        "id": 40,
        "category": "Lesson 10 - Multimedia Standards",
        "question": r"""H.264/MPEG-4 AVC に関する記述として適切なものはどれか。""",
        "options": [
            r"""インターネットで動画や音声データのストリーミング配信を制御するための通信方式""",
            r"""テレビ会議やテレビ電話で双方向のビデオ配信を制御するための通信方式""",
            r"""テレビの電子番組案内で使用される番組内容のメタデータを記述する方式""",
            r"""ワンセグやインターネットで用いられる動画データの圧縮符号化方式""",
        ],
        "correct_answer": r"""ワンセグやインターネットで用いられる動画データの圧縮符号化方式""",
        "explanation": r"""**日本語:**
* **H.264/MPEG-4 AVC** は、ワンセグ放送やインターネット動画配信、Blu-rayディスクなど、モバイル端末向けの低ビットレートからフルHDや4Kに至るまで、極めて広く普及している**動画データの圧縮符号化（ビデオコーデック）規格**です。

**English:**
* **H.264/MPEG-4 AVC** is an industry-standard video compression and encoding codec used for streaming video on smartphones, computers, TV broadcasts, and high-definition media files."""
    },
    {
        "id": 41,
        "category": "Lesson 10 - Subnetting Architectures",
        "question": r"""IPv4 ネットワークで用いられる可変長サブネットマスクの表記として、構造上「正しい」ものはどれか。""",
        "options": [
            r"""255.255.255.1""",
            r"""255.255.255.32""",
            r"""255.255.255.64""",
            r"""255.255.255.128""",
        ],
        "correct_answer": r"""255.255.255.128""",
        "explanation": r"""**日本語:**
* サブネットマスクは32ビットのビット列です。
* ルールとして、**「先頭から連続した1」のあとに「連続した0」**が並ぶ必要があり、途中で0と1が交互に現れることは許されません。
* 選択肢の最右オクテットを2進数展開します：
  * ア) `.1` $= 00000001_2$ (1の前に0があるので不正)
  * イ) `.32` $= 00100000_2$ (不正)
  * ウ) `.64` $= 01000000_2$ (不正)
  * エ) `.128` $= 10000000_2$ (連続した1のあとに0が続くため、構造上**正しい**サブネットマスクです。`/25`を意味します)

**English:**
* An IPv4 subnet mask must be structured as contiguous 1 bits followed by contiguous 0 bits.
* Converting the fourth octet values to binary:
  * A) `.1` $= 00000001_2$ (Invalid)
  * B) `.32` $= 00100000_2$ (Invalid)
  * C) `.64` $= 01000000_2$ (Invalid)
  * D) `.128` $= 10000000_2$ (Valid contiguous bitmask representing a `/25` network)"""
    },
    {
        "id": 42,
        "category": "Lesson 11 - Network Layer Encapsulation",
        "question": r"""1 個の TCP パケットをイーサネットに送出したとき，イーサネットフレームに含まれる宛先情報の，物理メディア（回線上）への送出順序はどれか。""",
        "options": [
            r"""宛先 IP アドレス，宛先 MAC アドレス，宛先ポート番号""",
            r"""宛先 IP アドレス，宛先ポート番号，宛先 MAC アドレス""",
            r"""宛先 MAC アドレス，宛先 IP アドレス，宛先ポート番号""",
            r"""宛先 MAC アドレス，宛先ポート番号，宛先 IP アドレス""",
        ],
        "correct_answer": r"""宛先 MAC アドレス，宛先 IP アドレス，宛先ポート番号""",
        "explanation": r"""**日本語:**
* 送信データのパッケージング（カプセル化）は、上位レイヤーから下位レイヤー（物理層）に向かって順次ヘッダーを包むように行われます。
* しかし、いざ回線上（物理メディア）に電気信号としてパケットを送出する際は、もっとも外側に位置する下位レイヤー（データリンク層）のヘッダーが最初に送出されます：
  1. 最外層（レイヤ2：データリンク層）：**宛先MACアドレス**（スイッチングハブが最初に読み取る）
  2. 中間層（レイヤ3：ネットワーク層）：**宛先IPアドレス**（ルーターが次に読み取る）
  3. 最内層（レイヤ4：トランスポート層）：**宛先ポート番号**（ホストOSがアプリケーションに振り分けるために読み取る）

**English:**
* Data encapsulation builds from the inside out (Layer 4 to Layer 2). However, on the wire, the packet header data is transmitted in physical sequence from the outermost Layer 2 frame:
  1. Layer 2 (Data Link): **Destination MAC Address** (Read first by switches)
  2. Layer 3 (Network): **Destination IP Address** (Read next by routers)
  3. Layer 4 (Transport): **Destination Port Number** (Read last by the destination OS)"""
    },
    {
        "id": 43,
        "category": "Lesson 11 - Network Diagnostic Tools",
        "question": r"""ネットワーク障害の原因を調べるために，スイッチのミラーポートを用意して，LAN アナライザーを使用するときに留意することはどれか。""",
        "options": [
            r"""LAN アナライザーがパケットを破棄してしまうので，測定中は測定対象外のコンピュータの利用を制限しておく必要がある。""",
            r"""LAN アナライザーにはネットワークを通過するパケットを全表示・解析できる機能があるため，パスワード盗聴などに悪用されないよう厳重に注意する必要がある。""",
            r"""障害発生に備えて，ネットワーク利用者に LAN アナライザーの保管場所と使用方法を周知しておく必要がある。""",
            r"""測定に当たって，LAN ケーブルを一時的に切断する必要があるので，利用者に対して測定日を事前に知らせておく必要がある。""",
        ],
        "correct_answer": r"""LAN アナライザーにはネットワークを通過するパケットを全表示・解析できる機能があるため，パスワード盗聴などに悪用されないよう厳重に注意する必要がある。""",
        "explanation": r"""**日本語:**
* **LANアナライザー（パケットキャプチャツール）**は、ネットワークを流れる生データパケット（プレインテキストのIDやパスワードを含む）を収集して、内部情報を詳しく解析・可視化できるツールです。
* ミラーポートに接続して稼働させることで、全通信を傍受できてしまうため、悪意のある盗聴などに悪用されないよう厳重な管理体制（セキュリティ管理）が求められます。

**English:**
* A **LAN Analyzer (packet sniffer)** captures and inspects raw traffic traversing networks.
* Since it displays raw application payloads (including potential unencrypted passwords or sessions), it must be carefully guarded to prevent unauthorized wiretapping and sniffing exploits."""
    },
    {
        "id": 44,
        "category": "Lesson 11 - Drive-by Downloads",
        "question": r"""ドライブバイダウンロード（Drive-by Download）攻撃に該当するものはどれか。""",
        "options": [
            r"""PC 内のマルウェアを遠隔操作して，PC のハードディスクドライブを丸ごと暗号化する。""",
            r"""外部ネットワークからファイアウォールの設定の誤りを突いて侵入し，内部ネットワークにあるサーバのシステムドライブにルートキットを仕掛ける。""",
            r"""公開 Web サイトにおいて，スクリプトを Web ページ中の入力フィールドに入力し，Web サーバがアクセスするデータベース内のデータを不正にダウンロードする。""",
            r"""利用者が公開 Web サイトを通常通り閲覧したときに，その利用者の意図や気づきにかかわらず，PC にマルウェアをサイレントにダウンロードさせて感染させる。""",
        ],
        "correct_answer": r"""利用者が公開 Web サイトを通常通り閲覧したときに，その利用者の意図や気づきにかかわらず，PC にマルウェアをサイレントにダウンロードさせて感染させる。""",
        "explanation": r"""**日本語:**
* **ドライブバイダウンロード攻撃**とは、Webサイトに悪意のあるコードを改ざんなどによって埋め込み、ユーザーがそのWebサイトを「ただ閲覧しただけ」で、本人の意思に関係なくバックグラウンドでマルウェアを自動ダウンロードさせてPCに感染させる攻撃手法です。
* 他の選択肢：
  * ア) ランサムウェア (Ransomware)
  * ウ) SQLインジェクション (SQL Injection)

**English:**
* A **Drive-by Download** attack occurs when malicious script is hidden inside a webpage, automatically running on the browser simply upon loading the site. This causes malware to download and execute in the background without user consent or knowledge.
* Other options:
  * A) Ransomware execution
  * C) SQL Injection"""
    },
    {
        "id": 45,
        "category": "Lesson 11 - Malware Classifications",
        "question": r"""マルウェアについて，トロイの木馬とワームを比較したとき，ワームに特有な顕著な特徴はどれか。""",
        "options": [
            r"""勝手にファイルを暗号化して正常に読めなくする。""",
            r"""単独のプログラム（宿主となるファイルを必要としない）として不正な動作を行う。""",
            r"""特定の条件になるまで活動をせずに待機する。""",
            r"""ネットワークやリムーバブルメディア（USBメモリ等）を自ら媒介して自己複製し、自律的に感染を広げる。""",
        ],
        "correct_answer": r"""ネットワークやリムーバブルメディア（USBメモリ等）を自ら媒介して自己複製し、自律的に感染を広げる。""",
        "explanation": r"""**日本語:**
* **ワーム (Worm)** の最大の特徴は、**「自律的な自己複製（感染拡大）能力」**です。他の正常なプログラムファイルを宿主（感染対象）として必要とせず、単独で稼働し、自ら進んでネットワークやUSBメモリなどの外部メディアを介して、他のPCへ次々と自律的に自己のコピーをばらまき、感染を広げます。
* 一方、トロイの木馬は自己複製を行わず、正規プログラムを偽装してユーザーに実行させることで感染します。

**English:**
* The distinguishing feature of a **Worm** is its capability to **independently self-replicate and propagate autonomous copies** across networks or external media (like USB drives).
* Unlike typical viruses, a worm does not need to latch onto an existing host application, and unlike Trojan Horses, it actively spreads itself automatically."""
    },
    {
        "id": 46,
        "category": "Lesson 12 - Software Engineering Models",
        "question": r"""要求の分析・設計時に使用する状態遷移図の説明として，適切なものはどれか。""",
        "options": [
            r"""階層構造の形でプログラムの全体構造を記述する。""",
            r"""時間の経過や制御信号の変化等の状態を変化させるきっかけと変化に伴って実行する動作を記述する。""",
            r"""システムの機能を概要から詳細へと段階的に記述する。""",
            r"""処理間のデータの流れをデータフロー，処理，データストア及び外部の四つの記号で記述する。""",
        ],
        "correct_answer": r"""時間の経過や制御信号の変化等の状態を変化させるきっかけと変化に伴って実行する動作を記述する。""",
        "explanation": r"""**日本語:**
* **状態遷移図 (State Transition Diagram)** は、事象駆動型（イベントドリブン）システムなどの設計において、時間の経過や何らかの制御イベント、信号の変化によって「システムの状態がどのように移り変わるか（遷移するか）」、およびそれに伴う動作を表現する図法です。
* 他の選択肢：
  * ア) プログラム構造図（構造化チャート）
  * ウ) 機能分割図（機能構造階層図）
  * エ) DFD (Data Flow Diagram: データフロー図)

**English:**
* A **State Transition Diagram** details the behavioral changes inside reactive or event-driven systems over time or when specific command triggers/control events happen, highlighting state shifts and active responses.
* Other options:
  * A) Program Structure Chart
  * C) Functional Decomposition Chart
  * D) DFD (Data Flow Diagram)"""
    },
    {
        "id": 47,
        "category": "Lesson 12 - Module Coupling & Cohesion",
        "question": r"""ソフトウェアのモジュール設計において，信頼性，保守性を向上させるためのモジュール分割のアプローチとして，最も望ましいものはどれか。""",
        "options": [
            r"""モジュール強度を強く，結合度を強くする。""",
            r"""モジュール強度を強く，結合度を弱くする。""",
            r"""モジュール強度を弱く，結合度を強くする。""",
            r"""モジュール強度を弱く，結合度を弱くする。""",
        ],
        "correct_answer": r"""モジュール強度を強く，結合度を弱くする。""",
        "explanation": r"""**日本語:**
* モジュールの品質（保守性・再利用性・信頼性）を向上させる設計の鉄則は**「モジュール強度を強く（Cohesionを高く）、モジュール結合度を弱く（Couplingを低く）する」**ことです：
  * **モジュール強度 (Cohesion):** モジュール内部を構成する処理同士の関連性の強さ。1つのモジュールは1つの固有機能のみを果たすべきであり、これが強いほど高品質です。
  * **モジュール結合度 (Coupling):** モジュール同士がどれだけ依存し合っているか。他のモジュールの影響を受けにくくするため、結合度は弱いほど高品質です。

**English:**
* The core gold-standard principle of robust software architecture design is: **"Strong Module Cohesion (モジュール強度を強く) and Weak Module Coupling (モジュール結合度を弱く)"**:
  * **Cohesion (強度):** Measures how closely related the duties within a module are. High/Strong cohesion indicates a module has one clear, undivided task.
  * **Coupling (結合度):** Measures inter-dependency between modules. Low/Weak coupling minimizes regressions when one module is changed."""
    },
    {
        "id": 48,
        "category": "Lesson 12 - Design Reviews",
        "question": r"""設計上の誤りを早期に発見することを目的として，作成者と複数の関係者が設計書をレビューする方法はどれか。""",
        "options": [
            r"""ウォークスルー""",
            r"""机上デバッグ""",
            r"""トップダウンテスト""",
            r"""並行シミュレーション""",
        ],
        "correct_answer": r"""ウォークスルー""",
        "explanation": r"""**日本語:**
* **ウォークスルー (Walkthrough)** は、仕様書や設計書の作成者が、関係する開発チームのメンバーや設計者を数名集め、作成した成果物を机上で共同レビュー・トレースする手法です。
* **管理者を参加させず**、参加者が事前に資料に目を通し、会議では非難ではなく「単純な誤りの早期発見」に徹することをルールとします。

**English:**
* **Walkthrough (ウォークスルー)** is an informal design review methodology where the author guides peers and technicians through a draft design specification to detect logical flaws, spelling errors, or omissions early in the development lifecycle."""
    },
    {
        "id": 49,
        "category": "Lesson 12 - Static vs. Dynamic Testing",
        "question": r"""ソフトウェアのテストツールの説明のうち，静的テストを支援する「静的解析ツール」のものはどれか。""",
        "options": [
            r"""指定された条件のテストデータや，プログラムの入力ファイルを自動的に生成する。""",
            r"""テストの実行結果を基に，命令の網羅率や分岐の網羅率を自動的に計測し，分析する。""",
            r"""プログラム中に文法上の誤りや論理的な誤りなどがあるかどうかを，実際にコードを実行することなく、ソースコードそのものを分析して調べる。""",
            r"""モジュールの呼び出し回数や実行時間，実行文の実行回数などの，プログラム実行時の動作特性に関するデータを計測する。""",
        ],
        "correct_answer": r"""プログラム中に文法上の誤りや論理的な誤りなどがあるかどうかを，実際にコードを実行することなく、ソースコードそのものを分析して調べる。""",
        "explanation": r"""**日本語:**
* **静的解析ツール (Static Analysis Tool)** は、プログラムを**実際に実行（実行テスト）することなく**、ソースコードの構文チェックやルール違反、メモリリークの可能性などを分析・検出する支援ツールです。
* 他の選択肢：
  * ア) テストデータ生成ツール（環境設定ツール）
  * イ) カバレッジモニター（動的テストツール）
  * エ) プロファイラ（動的解析ツール）

**English:**
* **Static Analysis Tools (静的解析ツール)** scan source program files for syntax compliance, unreachable code, and architectural errors **without executing the program**.
* Other options:
  * A) Test Data Generator (Testbed tool)
  * B) Coverage Monitor (Dynamic testing tool)
  * D) Profiler (Dynamic analysis tool measuring execution runs)"""
    },
    {
        "id": 50,
        "category": "Lesson 13 - Management SWOT Analysis",
        "question": r"""経営戦略策定に用いられる SWOT 分析を説明したものはどれか。""",
        "options": [
            r"""競争環境における機会・脅威と自社事業の強み・弱みをマトリクス形式で分析する。""",
            r"""競争に影響する要因と，他者の動き，自社の動きをゲーム理論に沿って分析する。""",
            r"""市場に対するマーケティングツールの最適な組合せ（マーケティングミックス）を分析する。""",
            r"""市場の成長性と市場シェアの観点から自社の事業ポートフォリオを分析する。""",
        ],
        "correct_answer": r"""競争環境における機会・脅威と自社事業の強み・弱みをマトリクス形式で分析する。""",
        "explanation": r"""**日本語:**
* **SWOT分析 (SWOT Analysis)** は、自社を取り巻く外部環境要因である**「機会 (Opportunities)」「脅威 (Threats)」**と、自社自身の内部環境要因である**「強み (Strengths)」「弱み (Weaknesses)」**を掛け合わせたマトリクスを作成し、最適な経営・事業戦略を策定する手法です。
* 他の選択肢：
  * ウ) マーケティングミックス（4P分析）
  * エ) PPM (Product Portfolio Management: プロダクトポートフォリオマネジメント)

**English:**
* **SWOT Analysis** is a framework that matches internal enterprise factors—**S**trengths (強み) and **W**eaknesses (弱み)—with external environmental conditions—**O**pportunities (機会) and **T**hreats (脅威)—to strategize commercial growth pathways."""
    },
    {
        "id": 51,
        "category": "Lesson 13 - Supply Chain Management",
        "question": r"""サプライチェーンマネジメント (SCM) を説明したものはどれか。""",
        "options": [
            r"""購買，生産，販売及び物流を結ぶ一連の業務を，企業内のみならず企業間で全体最適の視点から見直し，納期短縮や在庫削減を図る。""",
            r"""個人が持っているノウハウや経験などの知的資産を組織全体で共有して，創造的な仕事につなげていく。""",
            r"""社員のスキルや行動特性を把握し，人事戦略の視点から適切な人員配置・評価などのマネジメントを行う。""",
            r"""多様なチャネルを通して集められた顧客情報を一元化し，活用することによって，顧客との関係を密接にしていく。""",
        ],
        "correct_answer": r"""購買，生産，販売及び物流を結ぶ一連の業務を，企業内のみならず企業間で全体最適の視点から見直し，納期短縮や在庫削減を図る。""",
        "explanation": r"""**日本語:**
* **SCM (Supply Chain Management)** とは、原材料の調達から部材加工、製品製造、出荷・物流、小売販売に至る「サプライチェーン（供給の連鎖）」全体に関わる情報を、自社のみならず関連会社間（企業間）でリアルタイムに共有・連動させることで、サプライチェーン全体の在庫過剰や欠品を防ぎ、全体最適化を目指す手法です。
* 他の選択肢：
  * イ) ナレッジマネジメント (Knowledge Management)
  * ウ) HRM (Human Resource Management)
  * エ) CRM (Customer Relationship Management)

**English:**
* **SCM (Supply Chain Management)** optimizes raw component procurement, manufacturing, warehousing, and transportation channels across an integrated ecosystem of partners (inter-enterprise networks) to trim delays and suppress inventory stockpiles.
* Other options:
  * B) Knowledge Management
  * C) HRM (Human Resource Management)
  * D) CRM (Customer Relationship Management)"""
    },
    {
        "id": 52,
        "category": "Lesson 13 - Intellectual Property Law",
        "question": r"""著作権法において，保護の対象とならないものはどれか。""",
        "options": [
            r"""インターネットで公開されたフリーソフトウェア""",
            r"""ソフトウェアの操作マニュアル""",
            r"""データベース""",
            r"""プログラム言語、プロトコル、及びアルゴリズム""",
        ],
        "correct_answer": r"""プログラム言語、プロトコル、及びアルゴリズム""",
        "explanation": r"""**日本語:**
* **著作権法（ちょさくけんほう）**では、「思想や感情を創作的に表現したもの（表現そのもの）」を保護対象としています。
* したがって、プログラムを作るために使用する**「プログラム言語」**、プロトコルを構成する共通ルールである**「規約（プロトコル）」**、および計算手順に過ぎない**「解法（アルゴリズム）」**は、いずれも「表現そのもの」ではないため、著作権法の保護対象外として明記されています。
* フリーソフト、マニュアル、データベースは著作物として保護されます。

**English:**
* Copyright protects the original creative **expression** of thoughts or concepts, not functional systems or tools.
* Under Copyright law, **programming languages** (code grammar specs), **rules/protocols** (規約), and **algorithms (解法)** are specifically excluded from copyright protection. (Free software, manuals, and database indices are copyrightable)."""
    },
    {
        "id": 53,
        "category": "Lesson 13 - Information Law Compliance",
        "question": r"""個人情報の保護に関する法律についてのガイドラインによれば，個人情報に該当しないものはどれか。""",
        "options": [
            r"""受付に設置した監視カメラに録画された，特定の個人を容易に判別できる映像データ""",
            r"""個人番号の記載がない，特定の社員の氏名を含む源泉徴収票""",
            r"""指紋認証システムで使用するための、登録者本人の生体認証バックアップデータ""",
            r"""特定の生存する個人を復元できないように安全に加工された匿名加工情報""",
        ],
        "correct_answer": r"""特定の生存する個人を復元できないように安全に加工された匿名加工情報""",
        "explanation": r"""**日本語:**
* **個人情報 (Personal Information)** は、生存する個人に関する情報であって、氏名、生年月日など、特定の個人を識別できる情報（または個人識別符号を含む情報）を指します。
* **匿名加工情報 (Anonymized Information)** とは、特定の個人を一切識別できないよう（かつ元のデータに戻せないよう）に特別の加工を施した情報のことで、個人情報保護法の適用から除外され、第三者へ自由に販売・提供できるようになります。

**English:**
* Under the Personal Information Protection Act:
  * Camera footage tracking faces, and biometric biometric databases are treated as Personal Information.
  * **Anonymized Information (匿名加工情報)** has been programmatically processed so that specific living individuals can no longer be identified or recovered, excluding it from strict Personal Information constraints."""
    },
    {
        "id": 54,
        "category": "Lesson 13 - E-Commerce",
        "question": r"""EC (Electronic Commerce：電子商取引) に関する説明として，適切なものはどれか。""",
        "options": [
            r"""営業活動に IT を活用して営業効率と品質を高め，売上・利益の大幅な増加や，顧客満足度の向上を目指す方法である。""",
            r"""企業がもつ経営資源全体を，総合的かつ一元的に計画・管理し，経営の効率化を図る手法・概念である。""",
            r"""小売店の売上と利益を伸ばすことによって，卸売業者・メーカーが自社との取引拡大につなげるための小売店の経営活動を支援するシステムである。""",
            r"""消費者向けや企業間の商取引をインターネットなどの電子的なネットワークを活用して行うことである。""",
        ],
        "correct_answer": r"""消費者向けや企業間の商取引をインターネットなどの電子的なネットワークを活用して行うことである。""",
        "explanation": r"""**日本語:**
* **EC (Electronic Commerce: 電子商取引)** とは、BtoB（企業間）、BtoC（企業対消費者）などのあらゆる商品取引を、インターネットを介して電子的・自動的に行う経済活動のことです。
* 他の選択肢：
  * ア) SFA (Sales Force Automation)
  * イ) ERP (Enterprise Resource Planning)
  * ウ) リテールサポート (Retail Support)

**English:**
* **EC (Electronic Commerce)** encompasses any buying, selling, or trade activity involving consumers, companies, or agencies conducted digitally through automated network connections (like the internet).
* Other options:
  * A) SFA (Sales Force Automation)
  * B) ERP (Enterprise Resource Planning)
  * C) Retail Support"""
    },
    {
        "id": 55,
        "category": "Lesson 13 - Business Regulations",
        "question": r"""A 社で雇用しているオペレータの Q 氏を，B 社に派遣することになった。労働者派遣法で定められているルールとして，正しいものはどれか。""",
        "options": [
            r"""A 社は，Q 氏が A 社を辞めて B 社に直接雇用されることを一切禁止できる。""",
            r"""B 社は A 社に対して，Q 氏を「指名」して派遣するよう個別に要請できる。""",
            r"""Q 氏の派遣契約期間は，組織内で最長 1 年間である。""",
            r"""Q 氏は，B 社の定められた「指揮命令者」の指示に従って労働に従事する。""",
        ],
        "correct_answer": r"""Q 氏は，B 社の定められた「指揮命令者」の指示に従って労働に従事する。""",
        "explanation": r"""**日本語:**
* **労働者派遣契約 (Labor Dispatch Contract)** では：
  * 派遣労働者（Q氏）の雇用主は派遣元（A社）ですが、実際の仕事現場における**「指揮命令権」は派遣先（B社）の指揮命令者**にあります。
* 他の選択肢の誤り：
  * ア) 派遣終了後の直接雇用を派遣元が禁止することは法律上禁止されています。
  * イ) 派遣先企業は、事前に履歴書を審査したり、面接をして「特定の人物を指名・選別」することは禁止されています。
  * ウ) 同一組織での派遣期間上限は原則「3年間」です。

**English:**
* In a **Labor Dispatch Arrangement**:
  * The employee (Q) maintains a contract of employment with agency A, but works under the direct control and **day-to-day work supervision (指揮命令者) of the host enterprise (B)**.
  * Choice B is illegal: host companies cannot pre-interview or selectively nominate ("designate") specific dispatch dispatchees."""
    },
    {
        "id": 56,
        "category": "Lesson 13 - Cloud & Hosting Solutions",
        "question": r"""ホスティングサービスの特徴はどれか。""",
        "options": [
            r"""運用管理面では，サーバの稼働監視，インシデント対応などを全て利用者が担う。""",
            r"""サービス事業者が用意・運用しているサーバの「利用権（機能）」を利用者に貸し出す。""",
            r"""サービス事業者の高性能なサーバを利用者が専有するような使い方には対応しない。""",
            r"""サービス事業者のデータセンターに利用者が独自のサーバ機器を持ち込み，設置する。""",
        ],
        "correct_answer": r"""サービス事業者が用意・運用しているサーバの「利用権（機能）」を利用者に貸し出す。""",
        "explanation": r"""**日本語:**
* **ホスティングサービス (Hosting Service)** は、サービス事業者がデータセンター内に設置・管理しているサーバーを、利用者にレンタル（貸し出し）するサービスです（レンタルサーバー）。
* ハードウェアの保守管理や基本的なOSアップデートは事業者が担当するため、利用者の運用負担が低いのがメリットです。
* エ) の説明は「ハウジングサービス（コロケーションサービス）」です。

**English:**
* A **Hosting Service** leases out system server resources owned, maintained, and operated in server farms by the provider to client subscribers.
* Option D describes a Housing (Colocation) service, where clients ship physical computer hardware to run in datacenter racks."""
    },
    {
        "id": 57,
        "category": "Lesson 13 - Accounting Principles",
        "question": r"""財務諸表のうち，一定時点における企業のすべての資産，負債及び純資産を表示し，企業の財政状態を明らかにする財務諸表はどれか。""",
        "options": [
            r"""株主資本等変動計算書""",
            r"""キャッシュフロー計算書""",
            r"""損益計算書""",
            r"""貸借対照表 (B/S)""",
        ],
        "correct_answer": r"""貸借対照表 (B/S)""",
        "explanation": r"""**日本語:**
* **貸借対照表 (B/S: Balance Sheet)** は、一定の決算時点における企業の**「資産（財産）」「負債（借金）」「純資産（自己資本）」**を表示し、企業の「財政状態」を報告するための重要な決算報告書です。
* 他の選択肢：
  * ウ) 損益計算書 (P/L: Income Statement)：一定期間の経営成績（売上や費用、利益）を表す。

**English:**
* The **Balance Sheet (貸借対照表 - B/S)** represents a snapshot of an enterprise's financial standing at a specific point in time, organizing numbers across Assets (資産), Liabilities (負債), and Net Assets (純資産).
* Other options:
  * C) Income Statement (損益計算書 - P/L): Reflects business profit/loss over a given accounting cycle."""
    },
    {
        "id": 58,
        "category": "Lesson 13 - Business Laws",
        "question": r"""ソフトウェアやデータに欠陥がある場合に，製造物責任法 (PL法) の対象となるものはどれか。""",
        "options": [
            r"""機器のROMに焼き込んで一体化した、組込み機器内蔵のソフトウェア""",
            r"""一般に市販されているアプリケーションソフトウェアのパッケージ製品""",
            r"""PC用のインストール済みオペレーティングシステム (OS)""",
            r"""ネットワークからダウンロードしたアプリケーションデータプログラム""",
        ],
        "correct_answer": r"""機器のROMに焼き込んで一体化した、組込み機器内蔵 of ソフトウェア""",
        "explanation": r"""**日本語:**
* **製造物責任法（PL法）**において、対象となる「製造物」は**「製造または加工された動産（物理的なモノ）」**に限定されています。
* したがって、有形物の性質を持たない「無体物（ソフトウェアコード単体、OS、ダウンロードデータなど）」は原則としてPL法の対象外です。
* しかし、**有形物である組み込み機器（ハードウェア）内のROM等にソフトウェアが内蔵され、物理的な機器と一体化して流通している場合**、ソフトウェアのバグによる事故であっても「その組み込み機器（製造物）自体に欠陥がある」とみなされ、PL法の損害賠償対象になります。

**English:**
* The **Product Liability Law (PL Law)** bounds damage claims strictly to "manufactured or processed movable physical goods (動産)".
* Isolated intangible digital properties like downloaded data programs or store software cannot be sued under the PL Act.
* However, if code is **pre-installed on physical ROM chips integrated as part of built-in hardware electronics (組込み機器)**, a code defect that causes physical harm represents an overall defect in the movable hardware, qualifying for product liability claims."""
    },
    {
        "id": 59,
        "category": "High-Possibility Sample Questions - Systems Reliability",
        "question": r"""MTBFは4,000時間，MTTRは1,000時間の装置がある。今後の6年間は，予防保守によってMTBFを前年に比べて毎年100時間ずつ改善し，遠隔保守によってMTTRを前年に比べて毎年100時間ずつ改善していく計画である。6年経過後の稼働率は幾らか。""",
        "options": [
            r"""0.88""",
            r"""0.90""",
            r"""0.92""",
            r"""0.94""",
        ],
        "correct_answer": r"""0.92""",
        "explanation": r"""**日本語:**
1. **6年後のMTBFの算出 (毎年100時間改善＝長くなる):**
   $$\text{MTBF}_{\text{6y}} = 4,000 + (100 \times 6) = 4,600 \text{ 時間}$$
2. **6年後のMTTRの算出 (毎年100時間改善＝短くなる):**
   $$\text{MTTR}_{\text{6y}} = 1,000 - (100 \times 6) = 400 \text{ 時間}$$
3. **6年経過後の稼働率 (Availability) の算出:**
   $$\text{稼働率} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
   $$\text{稼働率}_{\text{6y}} = \frac{4,600}{4,600 + 400} = \frac{4,600}{5,000} = 0.92$$

**English:**
1. **Project improved MTBF after 6 years (100 hours longer per year):**
   $$\text{MTBF}_{\text{6y}} = 4,000 + (100 \times 6) = 4,600 \text{ hours}$$
2. **Project improved MTTR after 6 years (100 hours shorter per year):**
   $$\text{MTTR}_{\text{6y}} = 1,000 - (100 \times 6) = 400 \text{ hours}$$
3. **Calculate Availability:**
   $$\text{Availability} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} = \frac{4,600}{4,600 + 400} = \frac{4,600}{5,000} = 0.92$$"""
    },
    {
        "id": 60,
        "category": "High-Possibility Sample Questions - Network Calculation",
        "question": r"""1Gバイトの動画データを40Mビット／秒の回線を使用してダウンロードしたところ，5分掛かった。このときの回線利用率はおよそ何％か。ここで，ダウンロード時には動画データに20％の制御情報が付加されるものとする。""",
        "options": [
            r"""10%""",
            r"""53%""",
            r"""67%""",
            r"""80%""",
        ],
        "correct_answer": r"""80%""",
        "explanation": r"""**日本語:**
1. **総データ量の算出 (制御情報 20% 付加):**
   $$\text{動画本体} = 1 \text{ GB} = 1 \times 10^9 \text{ バイト}$$
   $$\text{付加制御情報込みの総データ} = 1 \text{ GB} \times (1 + 0.20) = 1.2 \text{ GB} = 1.2 \times 10^9 \text{ バイト}$$
2. **データ単位のバイトからビットへの変換:**
   $$\text{総データ（ビット）} = 1.2 \times 10^9 \text{ バイト} \times 8 \text{ ビット/バイト} = 9.6 \times 10^9 \text{ ビット}$$
3. **ダウンロードにかかった実伝送速度の計算 (5分 ＝ 300秒):**
   $$\text{実効伝送速度} = \frac{9.6 \times 10^9 \text{ ビット}}{300 \text{ 秒}} = 3.2 \times 10^7 \text{ ビット/秒 (bps)} = 32 \text{ Mbps}$$
4. **回線利用率 (Line Utilization) の算出:**
   $$\text{回線利用率} = \frac{\text{実効伝送速度}}{\text{理論回線速度}} = \frac{32 \text{ Mbps}}{40 \text{ Mbps}} = 0.80 \to 80\%$$

**English:**
1. **Calculate total data transmitted (with 20% overhead):**
   $$\text{Total data} = 1 \text{ GB} \times 1.20 = 1.2 \text{ GB} = 1.2 \times 10^9 \text{ bytes}$$
2. **Convert bytes to bits:**
   $$\text{Total bits} = 1.2 \times 10^9 \times 8 = 9.6 \times 10^9 \text{ bits}$$
3. **Calculate actual transfer rate over 5 minutes (300 seconds):**
   $$\text{Actual Speed} = \frac{9.6 \times 10^9 \text{ bits}}{300 \text{ seconds}} = 3.2 \times 10^7 \text{ bps} = 32 \text{ Mbps}$$
4. **Determine line utilization rate against 40 Mbps limit:**
   $$\text{Line Utilization} = \frac{\text{Actual Speed}}{\text{Theoretical Speed}} = \frac{32 \text{ Mbps}}{40 \text{ Mbps}} = 0.80 \text{ or } 80\%$$"""
    },
    {
        "id": 61,
        "category": "High-Possibility Sample Questions - Network Protocols",
        "question": r"""HTTP と HTTPS を比較した場合において，HTTPS だけがもつセキュリティ上の顕著な特徴を示したものはどれか。""",
        "options": [
            r"""cookie に保存されている情報を用いたセッション管理が可能である。""",
            r"""ID とパスワードによって利用者の認証を行うことが可能である。""",
            r"""Web ブラウザでキャッシュさせることによって通信量を減らすことが可能である。""",
            r"""通信相手先サーバをサーバ証明書によって確認することが可能である。""",
        ],
        "correct_answer": r"""通信相手先サーバをサーバ証明書によって確認することが可能である。""",
        "explanation": r"""**日本語:**
* **HTTPS (Hypertext Transfer Protocol Secure)** は、HTTP通信をSSL/TLSプロトコルで暗号化する技術です。
* HTTPS固有の特徴として、信頼できる認証局（CA）が署名した**「サーバー証明書 (Server Certificate)」**を用いることで、接続先サーバーが本物であり、悪意ある第三者によるなりすましサイトではないことを証明・確認できる点が挙げられます。
* その他の機能（クッキー管理、パスワード認証、キャッシュ制御）は、通常のHTTPでも共通して利用可能な機能です。

**English:**
* Compared to plain HTTP, **HTTPS** encrypts internet traffic using SSL/TLS.
* A unique, defining security feature of HTTPS is verifying the authentic identity of the target web server using signed **Server Certificates (サーバ証明書)** issued by a trusted Certificate Authority (CA), preventing server spoofing and phishing clones."""
    },
    {
        "id": 62,
        "category": "High-Possibility Sample Questions - Cryptography Vulnerabilities",
        "question": r"""暗号の危殆化（きたいか）に該当する説明として、適切なものはどれか。""",
        "options": [
            r"""ある CA でデジタル証明書の署名に使っている公開鍵のデジタル証明書の有効期限が切れた。""",
            r"""ある暗号アルゴリズムの秘密鍵が不正アクセスによって外部に漏えいした。""",
            r"""あるハッシュ関数においてハッシュ値が同じになるデータの組みを現実的な時間内で発見する方法が見つかった。""",
            r"""あるランサムウェアの一種で暗号化されたファイルの復号鍵が公開された。""",
        ],
        "correct_answer": r"""あるハッシュ関数においてハッシュ値が同じになるデータの組みを現実的な時間内で発見する方法が見つかった。""",
        "explanation": r"""**日本語:**
* **暗号の危殆化 (Compromise of Cryptography)** とは、秘密鍵の漏洩などといった人為的・物理的なミスではなく、計算能力の向上や新たな解読アルゴリズムの発見により、**「暗号方式やハッシュ関数自体の数学的な安全性・理論的強度が低下し、破られやすくなる」**状態を指します。
* ハッシュ値が衝突する元のデータペア（同じハッシュ値を持つ異なるデータ）を現実的な時間内に算出する解法が見つかることは、ハッシュ関数の数学的安全性が崩壊したことを意味するため、まさに暗号の危殆化に該当します。
* 他の選択肢（鍵漏洩、有効期限切れ等）は運用の不備や鍵のライフサイクル管理に関わる問題であり、暗号アルゴリズム自体の危殆化ではありません。

**English:**
* **Cryptographic Compromise (暗号の危殆化)** occurs when the mathematical security strength of a cryptosystem or hash function decays due to advances in computer hardware speed or discovery of codebreaking algorithms.
* Finding an efficient, realistic way to locate hash collision pairs (discovering different input datasets yielding identical output hash digests) breaches the mathematical integrity of a hashing standard, compromising its security.
* Other choices represent procedural key leaks or expiration lifecycles, not mathematical algorithm compromise."""
    },
    {
        "id": 63,
        "category": "High-Possibility Sample Questions - Object-Oriented Principles",
        "question": r"""オブジェクト指向プログラミングの特徴のうち，異なるクラスのオブジェクトを同一のインタフェースで操作したときに，操作対象クラスに応じた異なる動作を可能にすることを何と呼ぶか。""",
        "options": [
            r"""委譲 (Delegation)""",
            r"""継承 (Inheritance)""",
            r"""コンポジション (Composition)""",
            r"""多相性 (Polymorphism)""",
        ],
        "correct_answer": r"""多相性 (Polymorphism)""",
        "explanation": r"""**日本語:**
* **多相性 (Polymorphism: ポリモーフィズム、多様性)** とは、異なるクラスのオブジェクトが、同じメッセージ（関数呼び出し・インターフェース）を受け取った際、それぞれのオブジェクト自身が定義した固有の動作を実行するオブジェクト指向の特徴です。
* 例えば、`Shape`（図形）という共通インターフェースの `draw()` メソッドを呼び出すと、`Circle` クラスは丸を、`Square` クラスは四角をそれぞれ描画します。
* 他の選択肢：
  * ア) 委譲：あるオブジェクトの処理を別のオブジェクトに肩代わりさせる。
  * イ) 継承：親クラスの属性や手続きを子クラスに引き継ぐ。
  * ウ) コンポジション：オブジェクト内に他のオブジェクトを部品として組み込む。

**English:**
* **Polymorphism (多相性)** enables different classes to interpret and respond to identical function or interface calls in their own customized, native ways (e.g. calling `draw()` outputs a circle on a `Circle` object, but a rectangle on a `Square` object).
* Other options:
  * A) Delegation
  * B) Inheritance
  * C) Composition"""
    },
    {
        "id": 64,
        "category": "High-Possibility Sample Questions - Data Mining",
        "question": r"""データマイニングの手法の一つであって，POS などの蓄積データから“一緒に買われる商品”の組合せを発見する分析手法はどれか。""",
        "options": [
            r"""3C 分析""",
            r"""ABC 分析""",
            r"""コンジョイント分析""",
            r"""マーケットバスケット分析""",
        ],
        "correct_answer": r"""マーケットバスケット分析""",
        "explanation": r"""**日本語:**
* **マーケットバスケット分析 (Market Basket Analysis)** は、小売店のPOS（販売時点情報管理）データなどをデータマイニングして、「買い物かご（バスケット）の中に一緒に並びやすい商品の組み合わせ（相関関係）」を発見する分析手法です。（例：「ビールと紙おむつが同時に買われやすい」など）
* 他の選択肢：
  * ア) 3C分析：マーケティング分析フレームワーク（Customer, Competitor, Company）
  * イ) ABC分析：在庫などの重要度別グループ管理手法（売上高順等で並べ、優先度A, B, Cに分類）
  * ウ) コンジョイント分析：商品スペック（機能や価格など）の組み合わせに対する購買者の好みを定量評価する手法

**English:**
* **Market Basket Analysis** is a classic retail data-mining algorithm executed on transactional POS (Point-of-Sale) databases to find meaningful product associations and purchasing patterns (e.g. "Customers who purchase diapers also frequently buy beer").
* Other options:
  * A) 3C Analysis (Customer, Competitor, Company marketing matrix)
  * B) ABC Analysis (Prioritizing warehouse inventory units by volume/sales value)
  * C) Conjoint Analysis (Statistical product attribute valuation marketing model)"""
    },
    {
        "id": 65,
        "category": "High-Possibility Sample Questions - E-Commerce Strategy",
        "question": r"""物販事業において，ロングテールをビジネスとして成功させるために必要な施策はどれか。""",
        "options": [
            r"""多くの有名ブランド店が出店するショッピングモールの構築""",
            r"""交通の利便性が高い地域に対する，生活必需品を広く浅く取りそろえた出店計画""",
            r"""店舗で購入した商品を近隣地域に無償で配送するサービスの実施""",
            r"""豊富な品ぞろえと，在庫コストや配送費用を抑えるための大規模な物流センタの構築や活用""",
        ],
        "correct_answer": r"""豊富な品ぞろえと，在庫コストや配送費用を抑えるための大規模な物流センタの構築や活用""",
        "explanation": r"""**日本語:**
* **ロングテール (Long Tail)** とは、ネットショップなどにおいて、ヒット商品（売れ筋商品）以外の「たまにしか売れない多種多様なニッチ商品」の販売量をすべて合算すると、ヒット商品の売上合計を上回るという販売理論です。
* これをビジネスとして成功させるためには、無限に近い商品をカバーする「圧倒的な品揃え」を用意しつつ、それらのニッチ商品を低コストで保管・配送できる「大規模な自動化物流センターの構築や物流網の効率化（在庫・流通コストの徹底的な抑制）」が必須要件となります。

**English:**
* The **Long Tail** theory suggests that internet retailers can generate significant cumulative revenue by selling low volumes of hard-to-find, niche products rather than focusing exclusively on high-volume blockbusters.
* To make a Long Tail model profitable, businesses must sustain an extensive, near-infinite online inventory database backed by **highly optimized, large-scale automated fulfillment distribution logistics hubs** to suppress warehousing and distribution overheads."""
    },
]
