
#### 問1 (Systems Reliability Diagram)
システム稼働状態の推移が図のように表されるとき、システムのMTBFとMTTRを表した式はどれか。ここで、$t_i$はシステムの稼働時間、$r_i$はシステムの修理時間を表すものとする。

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
```

*   **選択肢 (Options):**
    *   **ア:** MTBF = $\frac{1}{n} \sum_{i=1}^{n} r_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} t_i$
    *   **イ:** MTBF = $\frac{1}{n} \sum_{i=1}^{n} t_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} r_i$
    *   **ウ:** MTBF = $\frac{1}{n} \sum_{i=1}^{n} t_i$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} (t_i + r_i)$
    *   **エ:** MTBF = $\frac{1}{n} \sum_{i=1}^{n} (t_i + r_i)$ , MTTR = $\frac{1}{n} \sum_{i=1}^{n} r_i$

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **MTBF (Mean Time Between Failures: 平均故障間隔)** は、故障せずに稼動していた時間の平均値（稼働時間の総和を稼働回数で割ったもの）です。したがって、式は $\frac{1}{n} \sum_{i=1}^{n} t_i$ となります。
        *   **MTTR (Mean Time To Repair: 平均修理時間)** は、故障が発生してから修理が完了するまでの平均時間（修理時間の総和を修理回数で割ったもの）です。したがって、式は $\frac{1}{n} \sum_{i=1}^{n} r_i$ となります。
    *   **English:** 
        *   **MTBF (Mean Time Between Failures)** is the average time a system runs without failing, calculated as the sum of operating times divided by the count. Thus, MTBF = $\frac{1}{n} \sum t_i$.
        *   **MTTR (Mean Time To Repair)** is the average time spent repairing failures, calculated as the sum of repair times divided by the count. Thus, MTTR = $\frac{1}{n} \sum r_i$.

---

#### 問2 (MTBF & MTTR Applied Scenario Calculation)
あるシステムの今年度のMTBFは3,000時間、MTTRは1,000時間である。翌年度はMTBFについて今年度の20%分の改善、MTTRについて今年度の10%分の改善を図ると、翌年度の稼働率は何%になるか。

*   **選択肢 (Options):**
    *   **ア:** 69%
    *   **イ:** 73%
    *   **ウ:** 77%
    *   **エ:** 80%

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        1. **翌年度の改善された値の算出:**
           * MTBFの20%改善（長くなる）: $\text{MTBF}_{\text{new}} = 3,000 \times (1 + 0.20) = 3,600 \text{時間}$
           * MTTRの10%改善（短くなる）: $\text{MTTR}_{\text{new}} = 1,000 \times (1 - 0.10) = 900 \text{時間}$
        2. **稼働率 (Availability) の公式への適用:**
           $$\text{稼働率} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
           $$\text{稼働率}_{\text{new}} = \frac{3,600}{3,600 + 900} = \frac{3,600}{4,500} = 0.80 \to 80\%$$
    *   **English:** 
        1. **Calculate the improved metrics for the next year:**
           * MTBF 20% improvement (longer): $\text{MTBF}_{\text{new}} = 3,000 \times 1.20 = 3,600 \text{ hours}$
           * MTTR 10% improvement (shorter): $\text{MTTR}_{\text{new}} = 1,000 \times 0.90 = 900 \text{ hours}$
        2. **Apply to the Availability formula:**
           $$\text{Availability} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} = \frac{3,600}{3,600 + 900} = \frac{3,600}{4,500} = 0.80 \text{ or } 80\%$$

---

#### 問3 (Multiple Systems Availability Calculation)
図のような稼働率 $P$ のシステムで構成された多重化システム全体の稼働率を表す式はどれか。ここで、並列の部分は、どちらか一方が稼働していればよいものとする。

```text
    【多重化システム構成図】
    
                    +----- [ P ] ----- [ P ] -----+
                    |    (Upper Branch: Serial)   |
         -- [ P ] --+                             +--
          (Serial)  |                             |
                    +----- [ P ] ----- [ P ] -----+
                         (Lower Branch: Serial)
```

*   **選択肢 (Options):**
    *   **ア:** $1 - (1 - P)(1 - P^2)^2$
    *   **イ:** $P\{1 - (1 - P)^4\}$
    *   **ウ:** $P\{1 - (1 - P)^2\}^2$
    *   **エ:** $P\{1 - (1 - P^2)^2\}$

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        1. 左側の独立した「直列システムP」の稼働率は $P$ です。
        2. 右側の並列部分（Upper Branch と Lower Branch）について考えます。
           * 各ブランチは「稼働率Pの機器が2台直列」であるため、各ブランチの稼働率は $P \times P = P^2$ です。
           * いずれかのブランチが故障する確率は $1 - P^2$ です。
           * 並列構造のため、両方のブランチが「同時に故障する確率」は $(1 - P^2) \times (1 - P^2) = (1 - P^2)^2$ です。
           * したがって、並列部分全体の稼働率は $1 - (1 - P^2)^2$ となります。
        3. 左側の直列部分と右側の並列部分を直列結合すると、全体の稼働率は：
           $$\text{全体稼働率} = P \times \{1 - (1 - P^2)^2\}$$
    *   **English:** 
        1. The operating rate of the standalone serial component $P$ on the left is $P$.
        2. Analyze the parallel block on the right (Upper and Lower branches):
           * Operating rate of each individual serial branch (2 units of $P$ in series) is $P \times P = P^2$.
           * Probability of failure for one branch is $1 - P^2$.
           * Since they are in parallel, both branches fail simultaneously with probability $(1 - P^2)^2$.
           * Thus, the operating rate of the parallel block is $1 - (1 - P^2)^2$.
        3. Combine the left series component with the right parallel block:
           $$\text{Overall Availability} = P \times \{1 - (1 - P^2)^2\}$$

---

#### 問4 (Full Adder Gate Logic)
図に示す全加算器の入力 $x$ に 1，$y$ に 0，$z$ に 1 を入力したとき，出力となる $c$(けた上げ数)，$s$(和)の値の組合せとして，正しいものはどれか。

```text
    【全加算器 ブロック図】
    
                 +-------------------+
         x (1) --|                   |-- c (1) (けた上げ数 / Carry-out)
         y (0) --|     全加算器      |
         z (1) --|    (Full Adder)   |-- s (0) (和 / Sum)
                 +-------------------+
```

*   **選択肢 (Options):**
    *   **ア:** $c = 0, s = 0$
    *   **イ:** $c = 0, s = 1$
    *   **ウ:** $c = 1, s = 0$
    *   **エ:** $c = 1, s = 1$

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   全加算器は、1桁の2進数3入力（$x, y, z$）を足し合わせ、2進数2桁の出力 $(c, s)$ を生成する回路です。
        *   実際の和： $x + y + z = 1 + 0 + 1 = 2_{10}$
        *   10進数「2」を2進数に表すと「$10_2$」になります。
        *   2進数の2桁目が $c$(けた上げ)であり $c = 1$、1桁目が $s$(和)であり $s = 0$ になります。
    *   **English:** 
        *   A Full Adder adds three 1-bit binary inputs ($x, y, z$) and produces a 2-bit binary result $(c, s)$, representing carry ($c$) and sum ($s$).
        *   Mathematical addition: $x + y + z = 1 + 0 + 1 = 2_{10}$
        *   Converting decimal 2 to binary yields $10_2$.
        *   Therefore, the carry digit $c = 1$ and the sum digit $s = 0$.

---

#### 問5 (Preemptive Operating System Scheduling)
優先度に基づくプリエンプティブなスケジューリングを行うリアルタイムOSで，二つのタスクA，Bをスケジューリングする。Aの方がBより優先度が高い場合にリアルタイムOSが行う動作のうち，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** Aの実行中にBに起動がかかると，Aを実行可能状態にしてBを実行する。
    *   **イ:** Aの実行中にBに起動がかかると，Aを待ち状態にしてBを実行する。
    *   **ウ:** Bの実行中にAに起動がかかると，Bを実行可能状態にしてAを実行する。
    *   **エ:** Bの実行中にAに起動がかかると，Bを待ち状態にしてAを実行する。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **プリエンプティブ (Preemptive)** 方式では、OSがCPUの実行権を強制的に切り替えることができます。
        *   優先度が「A ＞ B」であるため、低優先度タスクBが実行されている間に、高優先度タスクAが実行可能になると、OSはBを中断し、「実行可能状態 (READY)」に戻して、AにCPUを割り当てます。
        *   *注意:* 待ち状態 (WAIT) は入出力の終了を待つための状態です。割り込みやCPUの剥奪によって強制中断されたタスクは実行可能状態 (READY) へ遷移するため、選択肢ウが正しい。
    *   **English:** 
        *   In **preemptive** scheduling, the OS manages CPU control based on task priority.
        *   Since Priority A > B, if high-priority task A is activated while lower-priority task B is running, B is preempted (moved back to the READY state, not WAIT), and A is allocated the CPU. Thus, Option ウ is correct.

---

#### 問6 (Open Source Software - OSS Rules)
OSS(Open Source Software)の特徴のうち，適切なものはどれか。ここで，OSSはOSI(Open Source lnitiative)によるOSD(The Open Source Definition)の定義に基づくものとする。

*   **選択肢 (Options):**
    *   **ア:** OSSはフリーウェアと同様に無償で入手できるが商用システムの開発への利用は禁止されている。
    *   **イ:** OSSをパッケージ化したり，自社のソフトウェアを組み合わせたりして，有償で販売することができる。
    *   **ウ:** システム開発で利用できるようにソースコードで入手できるが，利用者がある数以上になるとライセンス料が発生する。
    *   **エ:** 複製と改良は自由にできるが，改良したソフトウェアを再頒布することはできない。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   OSS（オープンソースソフトウェア）の最大の原則は、商用・非商用を問わず自由に使用・再頒布・改造ができることです。自社システムとして商用利用することも認められていますし、自社製品と組み合わせて有償で販売することもライセンスに従う限り自由に行うことができます。したがって、イが正解です。
    *   **English:** 
        *   According to the Open Source Definition (OSD), OSS grants the freedom to redistribute, modify, and use the software for commercial purposes. Therefore, packaging OSS or integrating it with proprietary systems to sell commercially for a fee is entirely permitted under open-source licenses. Thus, Option イ is correct.

---

#### 問7 (Security Threats: Keylogger Definition)
キーロガーの悪用例はどれか。

*   **選択肢 (Options):**
    *   **ア:** 通信を行う2者間の経路上に割り込み，両者が交換する情報を収集し，改ざんする。
    *   **イ:** ネットバンキング利用時に，利用者が入力したパスワードを収集する。
    *   **ウ:** ブラウザでの動画閲覧時に，利用者の意図しない広告を勝手に表示する。
    *   **エ:** ブラウザの起動時に，利用者がインストールしていないツールバーを勝手に表示する。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **キーロガー (Keylogger)** とは、ユーザーがキーボード（またはマウス）に入力した文字や操作内容をそのまま全て傍受して記録するスパイウェアやハードウェアです。
        *   キーボード操作を盗み取るため、ネットバンキングなどでパスワードや暗号キー、暗証番号を入力する操作がそのまま漏えいし、不正送金やなりすましなどの致命的な被害に直結します。
    *   **English:** 
        *   A **Keylogger** is a malicious software or hardware tool that monitors and logs every keystroke made by the user. 
        *   It is heavily abused to harvest confidential credentials, such as online banking passwords, credit card numbers, and pins as the user types them.

---

#### 問8 (Digital Signatures Dual Purposes)
デジタル署名を通信に利用する主な目的は二つある。一つは，メッセージの発信者を受信者が確認することである。もう一つの目的はどれか。

*   **選択肢 (Options):**
    *   **ア:** 署名が行われた後でメッセージに変更が加えられていないかどうかを，受信者が確認すること。
    *   **イ:** 送信の途中でメッセージが不当に解読されていないことを，受信者が確認すること
    *   **ウ:** 発信者のIDを受信者が確認すること
    *   **エ:** 秘密鍵を返信してよいかどうかを受信者が確認すること

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   デジタル署名（Digital Signature）が実現するコアな機能は、**「なりすましの防止（発信元の本人確認）」** と **「改ざんの防止（データの整合性確認）」** の2つです。
        *   ハッシュ関数と公開鍵暗号技術を用いることで、送信されたデータが途中で一切変更（改ざん）されていないかを受信側が厳密に検証することができます。*注意:* デジタル署名自体に「暗号化（メッセージの秘匿化）」機能はないため、盗聴防止（解読されないこと）は目的ではありません。
    *   **English:** 
        *   A **Digital Signature** provides two cryptographic guarantees: **non-repudiation (authenticity of the sender)** and **data integrity (preventing modification)**.
        *   By verifying the signature, the recipient confirms that the message has not been altered or tampered with since it was signed. Thus, Option ア is correct.

---

#### 問9 (Security Attack Steps: Phishing)
次の手順に示すセキュリティ攻撃はどれか。

*   **攻撃手順 (Attack Steps):**
    1. 攻撃者が金融機関の偽のWebサイトを用意する。
    2. 金融機関の社員を装って，偽のWebサイトへ誘導するURLを本文中に含めた電子メールを送信する。
    3. 電子メールの受信者が，その電子メールを信用して本文中のURLをクリックすると，偽のWebサイトに誘導される。
    4. 偽のWebサイトと気付かずに認証情報を入力すると，その情報が攻撃者に渡る。

*   **選択肢 (Options):**
    *   **ア:** DDoS攻撃
    *   **イ:** フィッシング (Phishing)
    *   **ウ:** ボット
    *   **エ:** メールヘッダーインジェクション

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   問題に記載されたフローは典型的な**フィッシング（Phishing）詐欺**のプロセスです。本物に酷似した偽サイトを用意し、メールなどで騙したユーザーにID、パスワード、クレジットカード情報などを入力させて盗み取る攻撃手法です。
    *   **English:** 
        *   The described sequence outlines a textbook **Phishing** attack. 
        *   Attackers create spoofed emails mimicking credible organizations (like banks) and redirect victims to a fraudulent replica website to extract user credentials and personal identifiers.

---

#### 問10 (Network Management: NTP Uses)
NTP(Network Time Protocol)の用途に関する記述として，最も適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** クライアントサーバシステムでの業務プログラムの応答時間を正確に測定する。
    *   **イ:** タイムサーバを利用して，ネットワーク上の各PCの時刻を合わせる。
    *   **ウ:** ファイルサーバに格納されている共用ファイルの更新時刻によって，最新かどうかを判断する。
    *   **エ:** メールサーバで電子メールを受信した時刻を比較して，未読の電子メールを転送する。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **NTP (Network Time Protocol)** は、ネットワークを介してサーバーやクライアントPCといった様々なコンピュータ間の内部時計を同期し、正確な標準時刻（UTC）を維持するために設計された、UDPポート123を使用するプロトコルです。
    *   **English:** 
        *   **NTP (Network Time Protocol)** is utilized to synchronize system clocks across various computer systems over packet-switched, variable-latency data networks. It keeps servers and PCs unified to a single accurate standard time.

---

#### 問11 (Network Addressing: Subnet Host Limit Calculation)
192.168.0.0/23 (サブネットマスク 255.255.254.0) のIPv4ネットワークにおいて，ホストとして使用できるアドレスの個数の上限はどれか。

*   **選択肢 (Options):**
    *   **ア:** 23
    *   **イ:** 24
    *   **ウ:** 254
    *   **エ:** 510

*   **正解 (Correct Answer):** **エ**

*   **詳細計算 (Calculation):**
    *   **日本語:** 
        1. IPv4アドレスは合計 **32ビット** です。
        2. プレフィックス長 `/23` は、先頭から23ビットが「ネットワーク部」であることを示します。
        3. したがって、「ホスト部」として使えるビット数は：
           $$\text{ホスト部ビット数} = 32 - 23 = 9 \text{ビット}$$
        4. 9ビットで表現できるアドレスの総数は $2^9 = 512$ 個です。
        5. アドレスプールの中から、ホストのアドレスとして割り当てできない **2つの特別な用途のアドレス** を除外します：
           * ホスト部がすべて「0」のアドレス：**ネットワークアドレス**
           * ホスト部がすべて「1」のアドレス：**ブロードキャストアドレス**
        6. 使用可能なホストアドレス上限：
           $$512 - 2 = 510 \text{個} \to \text{エ}$$
    *   **English:** 
        1. An IPv4 address contains **32 bits**.
        2. A CIDR suffix `/23` allocates 23 bits to the Network Prefix.
        3. This leaves remaining bits for assigning Host Identifiers:
           $$\text{Host bits} = 32 - 23 = 9 \text{ bits}$$
        4. $2^9 = 512$ represents total possible unique addresses.
        5. Deduct **2 reserved addresses** that cannot be assigned to system hosts:
           * Host portion all 0s: **Network Address**
           * Host portion all 1s: **Broadcast Address**
        6. Total actual hosts supported:
           $$512 - 2 = 510 \text{ hosts } \to \text{Option エ}$$

---

#### 問12 (Information Security: PKI Certificate Authorities)
PKI(公開鍵基盤)の認証局(CA)が果たす役割はどれか。

*   **選択肢 (Options):**
    *   **ア:** 共通鍵を生成する。
    *   **イ:** 公開鍵を利用しデータの暗号化を行う。
    *   **ウ:** 失効したデジタル証明書の一覧を発行する。
    *   **エ:** データが改ざんされていないことを検証する。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **認証局 (CA: Certificate Authority)** は、公開鍵が本人のものであるかを証明するデジタル証明書を発行する第三者機関です。
        *   重要な機能の一つとして、有効期限内に漏えい・紛失などの理由で無効化（失効）された証明書の一覧である **CRL (Certificate Revocation List: 証明書失効リスト)** を発行・公開します。
    *   **English:** 
        *   In **PKI (Public Key Infrastructure)**, the **CA (Certificate Authority)** validates ownership of public keys and issues Digital Certificates.
        *   One of its key duties is generating and publishing the **CRL (Certificate Revocation List)**, which lists digital certificates that have been revoked prior to their scheduled expiration date.

---

#### 問13 (Information Security Safeguards: Laptop Drive Encryption)
情報漏えい対策に該当するものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 送信するデータにチェックサムを付加する。
    *   **イ:** データが保存されるハードディスクをミラーリングする。
    *   **ウ:** データのバックアップ媒体のコピーを遠隔地に保管する。
    *   **エ:** ノート型PCのハードディスクの内容を暗号化する。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   ノートPCを社外に持ち出す際の紛失や盗難によるデータ漏えいを防ぐのに、最も効果的な対策は **ハードディスク（ドライブ）の暗号化** です。暗号化されていれば、PCを紛失してSSD/HDDを取り出されても、パスワードや暗号キーがない限り中身を解読できません。
        *   *他の選択肢について:*
          * ア: 完全性（Integrity）の確保
          * イ、ウ: 可用性（Availability）とディザスタリカバリの確保
    *   **English:** 
        *   Encrypting the hard drive of portable laptop computers is highly effective for protecting sensitive data against exposure when devices are lost or stolen. It ensures that even if physical storage is extracted, data remains unreadable.
        *   *Other options:*
          * Option ア is for data Integrity.
          * Options イ and ウ are for Availability.

---

#### 問14 (Network Protocols: TCP Placement in OSI Reference Model)
TCP/IP階層モデルにおいて，TCPが属する層はどれか。

*   **選択肢 (Options):**
    *   **ア:** アプリケーション層 (Application Layer)
    *   **イ:** インターネット層 (Internet Layer)
    *   **ウ:** トランスポート層 (Transport Layer)
    *   **エ:** データリンク層 (Data Link Layer)

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **TCP (Transmission Control Protocol)** は、再送制御やウィンドウ制御などを持ち、安全かつ信頼性の高いコネクション型のデータ転送を実現するプロトコルであり、**トランスポート層（Layer 4）** に位置します。
    *   **English:** 
        *   **TCP (Transmission Control Protocol)** provides highly reliable, connection-oriented packet streaming with error-correction mechanisms. It operates at the **Transport Layer** of the TCP/IP conceptual stack.

---

#### 問15 (Cryptography: RSA Public-key Principles)
公開鍵暗号方式に関する記述として，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** AESは，NISTが公募した公開鍵暗号方式である。
    *   **イ:** RSAは，素因数分解の計算の困難さを利用した公開鍵暗号方式である。
    *   **ウ:** 公開鍵暗号方式に参加する利用者の数が増えると鍵の配送が煩雑になる。
    *   **エ:** 通信文の内容の秘匿に公開鍵暗号方式を使用する場合は，受信者の復号鍵を公開する。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **RSA暗号** は、巨大な2つの素数の掛け算から、元の素数に分解する（**素因数分解**）ことが極めて困難であるという数学的性質に基づいた、代表的な公開鍵暗号方式です。
        *   *他の選択肢について:*
          * ア: AESは共通鍵暗号方式です。
          * ウ: 鍵管理が複雑化するのは「共通鍵暗号方式」です。
          * エ: 内容の秘匿の際は「受信者の公開鍵」で暗号化し、受信者は自身の「秘密鍵（非公開）」で復号します。
    *   **English:** 
        *   **RSA** is an asymmetric cryptosystem based on the mathematical difficulty of **factoring large prime integers (integer factorization)**.
        *   *Other options:*
          * Option ア: AES is a symmetric-key cryptosystem.
          * Option ウ: Key distribution bottlenecks are a vulnerability of symmetric encryption, not asymmetric.
          * Option エ: Confidential streaming requires encrypting with the recipient's public key, while their decryption private key is strictly kept secret.

---

#### 問16 (Information Security Threats: Backdoors)
情報セキュリティにおいてバックドアに該当するものはどれか。

*   **選択肢 (Options):**
    *   **ア:** アクセスする際にパスワード認証などの正規の手続が必要なWebサイトに，当該手続を経ないでアクセス可能なURL
    *   **イ:** インターネットに公開されているサーバのTCPポートの中からアクティブになっているポートを探して，稼働中のサービスを特定するためのツール
    *   **ウ:** ネットワーク上の通信パケットを取得して通信内容を見るために設けられたスイッチのLANポート
    *   **エ:** プログラムが確保するメモリ領域に，領域の大きさを超える長さの文字列を入力してあふれさせ，ダウンさせる攻撃

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **バックドア (Backdoor: 裏口)** とは、一度不正侵入した攻撃者が、二回目以降に正規の認証をバイパスしてシステムにいつでも再侵入できるように、こっそり設置する通信接続の抜け道です。正規の認証ステップを経ずに直接ログインできるCGIなどをサーバー内に設置する行為が該当します。
        *   *他の選択肢について:*
          * イ: ポートスキャナー（Port Scanner）の説明
          * ウ: ミラーポート（Mirror Port）の説明
          * エ: バッファオーバーフロー（Buffer Overflow）攻撃の説明
    *   **English:** 
        *   A **Backdoor** is a malicious portal planted by hackers into a compromise target to regain future entry bypassing standard administrative credentials. Exposing direct-access script URLs to run file actions without standard authorization exemplifies a backdoor.
        *   *Other options:*
          * Option イ: Port Scanner tools.
          * Option ウ: Mirror Port function.
          * Option エ: Buffer Overflow attack vector.

---

#### 問17 (Object-Oriented Programming: Encapsulation)
オブジェクト指向におけるカプセル化を説明したものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 同じ性質をもつ複数のオブジェクトを抽象化して，整理すること
    *   **イ:** 基底クラスの性質を派生クラスに受け継がせること
    *   **ウ:** クラス間に共通する性質を抽出し，基底クラスを作ること
    *   **エ:** データとそれを操作する手続を一つのオブジェクトにして，データと手続の詳細をオブジェクトの外部から隠蔽すること

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **カプセル化 (Encapsulation)** とは、「データ（属性）」と「それを操作する手続き（メソッド）」を一つのオブジェクト（クラス）としてひとまとめにし、必要最小限のインターフェースだけを外部に開示して、内部データの詳細を隠す（**情報隠蔽**）オブジェクト指向の設計思想です。
        *   *他の選択肢について:*
          * ア: 抽象化（Class Abstraction）
          * イ: 継承（Inheritance）
          * ウ: 汎化（Generalization）
    *   **English:** 
        *   **Encapsulation** bundles properties (attributes) and methods (operations) into a single logical structural class and shields its structural internal mechanisms from external manipulation. This is also called **information hiding**.
        *   *Other options:*
          * Option ア is Abstraction.
          * Option イ is Inheritance.
          * Option ウ is Generalization.

---

#### 問18 (Software Engineering Processes: Reverse Engineering)
ソフトウェアのリバースエンジニアリングの説明はどれか。

*   **選択肢 (Options):**
    *   **ア:** 開発支援ツールなどを用いて，設計情報からソースコードを自動生成する。
    *   **イ:** 外部から見たときの振る舞いを変えずに，ソフトウェアの内部構造を変える。
    *   **ウ:** 既存のソフトウェアを解析し，その仕様や構造を明らかにする。
    *   **エ:** 既存のソフトウェアを分析し理解した上で，ソフトウェア全体を新しく構築し直す。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **リバースエンジニアリング (Reverse Engineering)** は、完成した既存の製品やプログラムを分解・調査し、その動作、内部設計、仕様、ソースコードなどの論理構造を明らかにする技術です。
        *   *他の選択肢について:*
          * ア: フォワードエンジニアリング（CASEツールの自動コード生成など）
          * イ: リファクタリング（Refactoring）
          * エ: リエンジニアリング（Re-engineering）
    *   **English:** 
        *   **Reverse Engineering** investigates already compiled software binaries or physical machines to deduce their source codes, design diagrams, logic pathways, and operational parameters.
        *   *Other options:*
          * Option ア is Forward Engineering.
          * Option イ is Code Refactoring.
          * Option エ is Re-engineering.

---

#### 問19 (Software Testing Methods: Regression Testing)
ソフトウェアの保守に当たり，修正や変更がほかの正常箇所に影響していないことを確認するテストはどれか。

*   **選択肢 (Options):**
    *   **ア:** 性能テスト (Performance Test)
    *   **イ:** 耐久テスト (Load Test)
    *   **ウ:** 退行テスト (Regression Test)
    *   **エ:** 例外処理テスト (Exception Test)

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   プログラムのバグ修正や機能追加、OSアップデートなどの変更を加えた際、その変更が「これまで正常に動いていた既存の機能」に悪影響を及ぼしていないか（バグが復活したり別の箇所が壊れたりしていないか）を確認するテストを **退行テスト（回帰テスト、リグレッションテスト）** と呼びます。
    *   **English:** 
        *   **Regression Testing (退行テスト / 回帰テスト)** verifies that modified source code branches do not unintentionally impact existing validated application operations or reintroduce solved errors elsewhere.

---

#### 問20 (Software Testing: Black-box Test Case Design)
ブラックボックステストにおけるテストケースの設計方法として，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** プログラム仕様書の作成又はコーディングが終了した段階で，仕様書やソースリストを参照して，テストケースを設計する。
    *   **イ:** プログラムの機能仕様やインタフェースの仕様に基づいて，テストケースを設計する。
    *   **ウ:** プログラムの処理手順や内部構造に基づいて，テストケースを設計する。
    *   **エ:** プログラムのすべての条件判定で，真と偽をそれぞれ1回以上実行させることを基準に，テストケースを設計する。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ブラックボックステスト** は、プログラムの中身（ソースコードや分岐構造）を全く考慮せず、外部仕様（入力値と出力される結果）だけに着目して仕様通りに作動するかを確認するテスト手法です。そのため、テストケースは「機能仕様」や「インターフェース仕様」から作成されます。
        *   *他の選択肢について:*
          * ア、ウ、エ: 内部構造に依存してテストケースを組む「ホワイトボックステスト」の手法です。
    *   **English:** 
        *   **Black-box Testing** models test parameters based solely on output results expected from specific inputs, completely ignoring internal logic components or source codes. Test criteria are derived strictly from functional requirements or API interface specifications.
        *   *Other options:*
          * Options ア, ウ, and エ correspond to White-box testing approaches.

---

#### 問21 (Software Testing: Module Unit Test Guidelines)
モジュール単体テストに関する記述として，最も適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 通常はコーディングを行ったプログラマではなく，専任のテスト要員がテストケースを作成し実行する。
    *   **イ:** モジュール間インタフェースは，モジュール単体ではテストできないので，単体テストの対象外となる。
    *   **ウ:** モジュール設計書は，正しいことが検証済みであるので，テスト結果に問題があるときは，テストケース又はモジュールに誤りがある。
    *   **エ:** モジュール設計書を見ながら，原則としてすべてのロジックパスを一度は通るようなテストケースによって，検証を行う。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **単体テスト (Unit Test)** は、プログラムを構成する最小単位であるモジュールごとに正しく設計通り動作するかを確認する工程であり、原則として「すべてのロジックパスを1回は検証する（ホワイトボックス的に網羅する）」ことが推奨されます。
        *   *他の選択肢について:*
          * ア: 単体テストは原則として、そのコードを書いたプログラマ自身が実施します。
          * イ: モジュール単体の段階であっても、その引数（インターフェース）の整合性はテスト対象に含まれます。
          * ウ: モジュール設計書自体が誤っている可能性も大いにあるため、検証が必要です。
    *   **English:** 
        *   **Unit Testing** verifies modules or classes independently. Developers reference internal design sheets and leverage white-box testing strategies to verify that every logical path executes correctly at least once.
        *   *Other options:*
          * Option ア: Unit tests are usually executed by the programmers who authored the code.
          * Option イ: Although interface integration tests are executed during integration tests, interface parameters of a single module are still subject to unit validation.
          * Option ウ: The module design document itself can contain errors.

---

#### 問22 (White-box Testing Coverage Criteria)
図の構造をもつプログラムに対して，ホワイトボックステストのテストケースを設計するとき，少なくとも実施しなければならないテストケース数が最大になるテスト技法はどれか。

```text
    【プログラム判定条件 フローチャート】
    
                     |
                     v
             /----------------            /  A > 0 かつ      \    真 (True)
           <    B = 1 ?         >------------> [ X = X + 1 ]
            \                  /                     |
             \----------------/                      |
                     |                               |
                     | 偽 (False)                     |
                     v                               |
                     +<------------------------------/
                     |
                     v
```

*   **選択肢 (Options):**
    *   **ア:** 条件網羅 (Condition Coverage)
    *   **イ:** 判定条件網羅 (Decision/Branch Coverage)
    *   **ウ:** 複数条件網羅 (Multiple Condition Coverage)
    *   **エ:** 命令網羅 (Statement Coverage)

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   ホワイトボックステストの網羅基準（カバレッジ）には網羅性の高さに違いがあります。
        *   **複数条件網羅 (Multiple Condition Coverage)** は、判定条件内の「個々のすべての条件（$A>0$ と $B=1$）」の真・偽の可能な組み合わせ（$2^n$ 通り。今回は $2^2 = 4$ 通り）を全てテストケースとして設計します。
        *   命令網羅は最低1つ、判定条件網羅・条件網羅は最低2つのテストケースで検証可能であるため、最も多くのテストケースを必要とし、最もカバレッジ基準が厳しい（最大になる）のは **ウ（複数条件網羅）** です。
    *   **English:** 
        *   The flowchart evaluates a compound conditional block consisting of two distinct boolean statements: $A>0$ and $B=1$.
        *   **Multiple Condition Coverage** requires testing every possible logical combination of truth values for these individual sub-conditions ($2^n = 2^2 = 4$ test cases):
          1. $A>0$ (True), $B=1$ (True)
          2. $A>0$ (True), $B=1$ (False)
          3. $A>0$ (False), $B=1$ (True)
          4. $A>0$ (False), $B=1$ (False)
        *   This requires more test cases than Statement, Decision, or standard Condition Coverage. Thus, Option ウ is correct.

---

#### 問23 (Internet Protocols: MIME Definition)
インターネットにおける電子メールの規約で、ヘッダフィールドの拡張を行い、テキストだけでなく、音声、画像なども扱えるようにしたものはどれか。

*   **選択肢 (Options):**
    *   **ア:** HTML
    *   **イ:** MHS
    *   **ウ:** MIME (Multipurpose Internet Mail Extensions)
    *   **エ:** SMTP

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   もともと電子メール（SMTP）は、US-ASCIIコード（英語テキスト）しか送れませんでした。
        *   これに対し、日本語などの多言語文字列、さらには画像、動画、音声、PDFといったバイナリファイルも添付して電子メールで転送できるように、メッセージヘッダーと本文の仕様を拡張した規格が **MIME (Multipurpose Internet Mail Extensions)** です。
    *   **English:** 
        *   Originally, email protocols (SMTP) were limited to sending simple English plain-text (7-bit ASCII).
        *   **MIME (Multipurpose Internet Mail Extensions)** expanded email headers and formats, allowing binary files like audio, video, photos, and localized text characters to be encoded and transmitted over standard mail servers.

---

#### 問24 (Software Testing Definitions: White-box Testing)
テスト手法の1つであるホワイトボックステストの説明として、適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 下位モジュールから上位モジュールへと順次統合してテストする。
    *   **イ:** 上位モジュールから下位モジュールへと順次結合してテストする。
    *   **ウ:** モジュールの内部構造に注目してテストする。
    *   **エ:** モジュールの内部構造を考慮することなく、仕様書どおり機能が作動するかどうかをテストする。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ホワイトボックステスト (White-box Testing)** は、プログラムのソースコード、条件分岐、ループ、制御フローといった **「内部のロジック・構造」** に直接着目してテストケースを設計し、テストを実行する手法です。
        *   *他の選択肢について:*
          * ア: ボトムアップ（Bottom-up）統合テスト
          * イ: トップダウン（Top-down）統合テスト
          * エ: ブラックボックステストの説明
    *   **English:** 
        *   **White-box Testing** is a verification methodology that designs test cases based directly on the program's **internal algorithms, logic execution paths, and source code structure**.
        *   *Other options:*
          * Option ア refers to Bottom-up Integration testing.
          * Option イ refers to Top-down Integration testing.
          * Option エ refers to Black-box testing.

---

#### 問25 (Strategic Management: Core Competence)
コアコンピタンスを説明したものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 経営活動における基本精神や行動指針
    *   **イ:** 事業戦略の遂行によって達成すべき到達目標
    *   **ウ:** 自社を取り巻く環境に関するビジネス上の機会と脅威
    *   **エ:** 他社との競争優位の源泉となる経営資源及び企業能力

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **コアコンピタンス (Core Competence)** とは、企業の活動分野や独自技術において、「他社が容易に真似できない、その企業独自の卓越した強みやコア技術、能力」のことです。コアコンピタンスに基づき、得意な事業領域に経営資源を集中させる経営戦略をコアコンピタンス経営と呼びます。
        *   *他の選択肢について:*
          * ア: 経営理念（Corporate Philosophy）
          * イ: 経営目標（KGI / Corporate Objectives）
          * ウ: SWOT分析における外部要因（機会：O、脅威：T）
    *   **English:** 
        *   **Core Competence** represents unique capabilities, proprietary knowledge, or mastery of technological niches that distinguish a business and make its competitive edge highly difficult for competitors to copy.
        *   *Other options:*
          * Option ア corresponds to Corporate Philosophy.
          * Option イ corresponds to Management Objectives.
          * Option ウ corresponds to Opportunities and Threats in SWOT.

---

### 🟢 Category 2: Exercise Questions NOT on Past Exam (33 Questions)
このセクションでは、授業用の演習問題 `第8回演習問題.pdf` ～ `第13回演習問題.pdf` の中から、期末試験本試験に出題されなかった残り33問を全問網羅して解説しています。本試験の問題作成者はこの演習問題から多数複製しているため、次の試験での出題可能性が最も高い重要なセクションです。

---

#### 📄 第8回演習問題 (3 Questions)

##### 問1 (Turnaround Time Components)
一つのジョブについてのターンアラウンドタイム、CPU時間、入出力時間及び処理待ち時間の4つの時間の関係を表す式はどれか。ここで、他のオーバーヘッド時間は考慮しないものとする。

*   **選択肢 (Options):**
    *   **ア:** 処理待ち時間 ＝ CPU時間 ＋ ターンアラウンドタイム ＋ 入出力時間
    *   **イ:** 処理待ち時間 ＝ CPU時間 － ターンアラウンドタイム ＋ 入出力時間
    *   **ウ:** 処理待ち時間 ＝ ターンアラウンドタイム － CPU時間 － 入出力時間
    *   **エ:** 処理待ち時間 ＝ 入出力時間 － CPU時間 － ターンアラウンドタイム

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ターンアラウンドタイム (TAT: Turnaround Time)** とは、バッチ処理においてジョブをシステムに投入してから、実行され、出力が完了するまでの「全経過時間」です。
        *   ジョブがシステム内にいる時間は、実際にCPUが計算している「CPU処理時間」、周辺機器が動いている「入出力時間」、そして他のジョブがCPUを占有しているためキューで待たされている「処理待ち時間」に分割されます。
        *   等式： $\text{ターンアラウンドタイム} = \text{CPU時間} + \text{入出力時間} + \text{処理待ち時間}$
        *   これを「処理待ち時間」について解くと、選択肢 **ウ** になります。
    *   **English:** 
        *   **Turnaround Time (TAT)** is the total duration a job spends inside the system from submission to output completion.
        *   Since TAT is the sum of operation times and queue latency:
           $$\text{TAT} = \text{CPU Time} + \text{I/O Time} + \text{Wait Time}$$
           $$\text{Wait Time} = \text{Turnaround Time} - \text{CPU Time} - \text{I/O Time}$$

---

##### 問3 (Spooling Multiprogramming Wait-Time Calculation)
ある時間帯でのジョブの処理状況を計測したところ、次の通りであった。どのような状況になっているか。
*   (1) 多重度3でジョブを実行する。
*   (2) ジョブは5分間隔で発生し、実行時間は多重度に依存せず20分である。
*   (3) 各ジョブは実行終了後にスプーリング機能を利用して印刷し、印刷時間は15分である。
*   (4) プリンターは2台使用する。

*   **選択肢 (Options):**
    *   **ア:** 印刷待ちだけが増加している。
    *   **イ:** 実行待ちだけが増加している。
    *   **ウ:** 実行待ちと印刷待ちが増加している。
    *   **エ:** 実行待ちも印刷待ちも発生していない。

*   **正解 (Correct Answer):** **ウ**

*   **詳細計算 (Calculation):**
    *   **日本語:** 
        1. **CPU実行待ちキューの分析:**
           * ジョブは **5分間隔** で絶え間なくシステムに到着します（到着率 = 1件/5分 = 0.20件/分）。
           * システムの実行多重度は「3」（同時に3つのジョブを実行可能）で、1件の処理時間は「20分」です。
           * システム全体のジョブ実行完了能力：
             $$\text{CPU完了能力} = \frac{20 \text{分}}{3 \text{件}} \approx 6.67 \text{分/件}$$
           * 到着間隔（5分）の方が、システムがジョブを完了させる間隔（6.67分）より短いため、ジョブは溜まっていきます（**実行待ちが増加**）。
        2. **印刷（プリンター）待ちキューの分析:**
           * プリンターは **2台** で、1件の印刷時間は **15分** です。
           * システム全体の印刷完了能力：
             $$\text{印刷完了能力} = \frac{15 \text{分}}{2 \text{件}} = 7.5 \text{分/件}$$
           * 印刷要求がプリンター側に渡されるスピードは、CPUの処理完了ペース（約6.67分/件）です。
           * 印刷の到着間隔（6.67分）の方が、プリンターの処理完了能力（7.5分/件）より早いため、印刷データがプールに溜まっていきます（**印刷待ちが増加**）。
        3. したがって、実行待ちと印刷待ちの両方が恒常的に増加する状況（選択肢ウ）になります。
    *   **English:** 
        1. **CPU Queue Bottleneck:**
           * Jobs arrive every **5 minutes** (Arrival rate = 1 job/5 mins).
           * CPU runs with multiprogramming level 3; each job takes 20 mins.
           * Effective CPU throughput rate:
             $$\text{CPU processing rate} = \frac{20 \text{ mins}}{3 \text{ jobs}} \approx 6.67 \text{ mins/job}$$
           * Since jobs arrive faster than the CPU can process them (5 mins < 6.67 mins), the execution queue grows.
        2. **Printer Queue Bottleneck:**
           * There are 2 printers; printing takes 15 mins.
           * Effective printer throughput rate:
             $$\text{Printer rate} = \frac{15 \text{ mins}}{2 \text{ printers}} = 7.5 \text{ mins/job}$$
           * Printing requests enter the printer pool at the rate jobs exit the CPU (6.67 mins/job).
           * Since print requests are generated faster than printers can clear them (6.67 mins < 7.5 mins), the printing queue grows. Thus, Option ウ is correct.

---

##### 問5 (Memory Management: Compaction & Garbage Collection)
記憶領域の動的な割り当て及び解放を繰り返すことによって、どこからも利用されない記憶領域が発生することがある。このような記憶領域を再び利用可能にする処理はどれか。

*   **選択肢 (Options):**
    *   **ア:** ガーベジコレクション (Garbage Collection)
    *   **イ:** スタック (Stack)
    *   **ウ:** ヒープ (Heap)
    *   **エ:** フラグメンテーション (Fragmentation)

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   プログラムの実行中に、メモリの確保と解放をランダムに繰り返すと、メモリ上に小さく断片化された未使用領域（虫食い状態：**フラグメンテーション**）が発生します。
        *   また、参照を失ってどこからもアクセスできなくなったメモリゴミ（ゴミ：**ガーベジ**）を自動的または手動で回収して再度メモリの空き領域として統合し、利用可能にする仕組みを **ガーベジコレクション（Garbage Collection）** と呼びます。
        *   *他の選択肢について:*
          * イ: 後入先出し（LIFO）のデータ構造
          * ウ: 動的に確保できるメモリ領域
          * エ: メモリ領域が虫食い状に断片化する現象そのもの
    *   **English:** 
        *   **Garbage Collection** is an automatic memory management function that identifies and reclaims memory allocated to data structures that are no longer accessible by the software, preventing memory leaks and defragmenting free space.
        *   *Other options:*
          * Option イ: LIFO stack database.
          * Option ウ: Dynamically allocated raw memory.
          * Option エ: De-allocation leading to scattered memory remnants (Fragmentation).

---

#### 📄 第9回演習問題 (7 Questions)

##### 問2 (Dynamic vs. Static Linking)
プログラムを構成するモジュールの結合を，プログラムの実行時に行う方式はどれか。

*   **選択肢 (Options):**
    *   **ア:** インタプリタ
    *   **イ:** オーバーレイ
    *   **ウ:** 静的リンキング (Static Linking)
    *   **エ:** 動的リンキング (Dynamic Linking)

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **リンキング (Linking)** とは、翻訳された個別のオブジェクトコードと標準ライブラリ等を1つにまとめる処理のことです。
        *   **静的リンキング (Static Linking)**：コンパイル・ビルド時にあらかじめプログラム内にモジュールを組み込んで1つの巨大な実行ファイルを生成します。
        *   **動的リンキング (Dynamic Linking)**：プログラムの実行中に、ライブラリが必要になったタイミングでメモリ上に配置され結合します（DLLや共有ライブラリがこれに該当）。モジュールを実行ファイルに含めないため、ファイルサイズやメモリ消費量を抑えることができます。
    *   **English:** 
        *   **Dynamic Linking** deferentially links program modules (such as DLLs or shared libraries) to the executing process in virtual memory during runtime rather than embedding library codes into static build executables beforehand.

---

##### 問3 (OS API Features)
パソコンのOSが提供する機能を利用するためのAPIに関する記述のうち，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** APIで呼び出されるOSの処理モジュールは，あらかじめそれを利用するプログラムに静的にリンクしておく必要がある。
    *   **イ:** OSのAPIが提供されない周辺機器はユーザープログラムから利用又は制御することはできない。
    *   **ウ:** アーキテクチャの異なるCPU間でも，同じOSとそのAPIを使用することによって，プログラムの互換性を高め，移植時の工数を削減することが可能である。
    *   **エ:** 異なるOS間でもAPIは共通であり，APIだけを使用したプログラムであれば，再コンパイルだけでほかのOSへの移植が可能である。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **API (Application Programming Interface)** は、ソフトウェアがOSの標準機能（ファイル操作や描画、通信など）を簡単に利用できるように設計された共通窓口（関数群）です。
        *   アーキテクチャやCPUが異なっていても、同じOS（および同じAPI仕様）を利用していれば、プログラムは全く同じAPI関数（命令）を呼び出して動作します。これにより、ハードウェアを意識せずにソフト開発が可能になり、移植（ポート）時の開発コストを大幅に削減できます。
    *   **English:** 
        *   **APIs** abstract system-level hardware architectures. If different CPU architectures support the same OS and API ecosystem, identical application source structures can compile smoothly, improving portability.

---

##### 問5 (Gate Logic Equivalence ASCII Art)
図に示すデジタル回路と等価な論理式はどれか。ここで，論理式中の "・" は論理積， "＋" は論理和， $\overline{X}$ は $X$ の否定を表す。

```text
    【デジタル論理回路図】
    
        A -----+------------\
               |             )=== [ AND ] ---\
               |   +---\    /                |
               +---|NOT|o--/                 |
                   +---/                     |==== [ OR ] ---- X (出力)
               +---|NOT|o--\                 |
               |   +---/    \                |
               |             )=== [ AND ] ---/
        B -----+------------/
```

*   **選択肢 (Options):**
    *   **ア:** $X = A \cdot B + \overline{A \cdot B}$
    *   **イ:** $X = A \cdot B + \overline{A} \cdot \overline{B}$
    *   **ウ:** $X = A \cdot \overline{B} + \overline{A} \cdot B$
    *   **エ:** $X = (\overline{A} + B) \cdot (A + \overline{B})$

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        1. 回路の上段：入力 $A$ と、入力 $B$ を反転させた $\overline{B}$ がANDゲートに入力されています。したがって上段の出力は $A \cdot \overline{B}$ です。
        2. 回路の下段：入力 $A$ を反転させた $\overline{A}$ と、入力 $B$ がANDゲートに入力されています。したがって下段の出力は $\overline{A} \cdot B$ です。
        3. 最後に、この上段と下段の出力がORゲートに入力され結合されるため、全体の出力 $X$ は：
           $$X = A \cdot \overline{B} + \overline{A} \cdot B$$
           ※これは排他的論理和（XOR）と同じ動作をする論理回路です。
    *   **English:** 
        1. Top branch: The inputs to the top AND gate are $A$ and $\overline{B}$ (the inverted $B$ via NOT gate). Output = $A \cdot \overline{B}$.
        2. Bottom branch: The inputs to the bottom AND gate are $\overline{A}$ (the inverted $A$ via NOT gate) and $B$. Output = $\overline{A} \cdot B$.
        3. The two branch signals combine at the final OR gate, yielding the logical sum:
           $$X = A \cdot \overline{B} + \overline{A} \cdot B$$
           This is the standard expansion for an Exclusive OR (XOR) gate logic.

---

##### 問6 (Software Compilation Pipeline)
図はプログラムを翻訳して実行するまでの流れを示したものである。コンパイラ，リンカ，ローダの入出力の組合せとして，適切なものはどれか。

```text
    【ビルド・ローディング処理パイプライン】
    
    原始プログラム ---> [コンパイラ] ---> [ a ] ---> [ リンカ ] ---> [ c ] ---> [ローダ]
                                                      ^
                                                      |
                                                    [ b ]
```

*   **選択肢 (Options):**
    *   **ア:** a: 目的プログラム, b: ライブラリモジュール, c: ロードモジュール
    *   **イ:** a: ライブラリモジュール, b: ロードモジュール, c: 目的プログラム
    *   **ウ:** a: ロードモジュール, b: 目的プログラム, c: ライブラリモジュール
    *   **エ:** a: ロードモジュール, b: ライブラリモジュール, c: 目的プログラム

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        1. **コンパイラ** は人間の書いた「原始プログラム（ソースプログラム）」を翻訳し、機械語の「**a: 目的プログラム (オブジェクトプログラム)**」を出力します。
        2. **リンカ (Linker)** は、生成された目的プログラム (a) と、あらかじめ用意された「**b: ライブラリモジュール**」を連結して、実行可能な「**c: ロードモジュール**」を生成します。
        3. **ローダ (Loader)** は、ロードモジュール (c) を主記憶装置（実メモリ）にロード（配置）し、実行可能な状態にします。
    *   **English:** 
        1. **Compiler** translates human-readable "Source Program" to machine-readable **[a] Object Program (目的プログラム)**.
        2. **Linker** resolves imports by binding the compiled Object Program (a) with shared **[b] Library Modules (ライブラリモジュール)** to build a stand-alone **[c] Load Module (ロードモジュール)**.
        3. **Loader** maps the Load Module (c) into RAM for CPU execution.

---

##### 問7 (Non-preemptive Task Scheduling)
ノンプリエンプティブなスケジューリング方式の説明として，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 新しいタスクが実行可能状態になるたびに，各タスクの残りの実行時間を評価し，その時間が短いものから順に実行する。
    *   **イ:** 実行状態としたタスクが決められた時間内に待ち状態に遷移しないときに，そのタスクを中断して実行待ち行列にある次のタスクを実行状態とする。
    *   **ウ:** 実行状態としたタスクが自ら待ち状態に遷移するか終了するまで，他のタスクを実行状態とすることができない。
    *   **エ:** タスクが実行可能状態になったときに，そのタスクの優先度と，その時，実行状態であるタスクの優先度とを比較して，優先度が高い方のタスクを実行状態とする。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ノンプリエンプティブ (Non-preemptive)** 方式は、CPUの制御管理をOS側で強制せず、実行中の「アプリケーション（プログラム）自身」に任せる方式です。
        *   一度タスクにCPUが割り当てられると、そのタスクが自ら処理を「終了（ターミネート）」するか、「待ち状態（I/O待ち等）」に入って明示的に実行権を放棄するまで、OSが割込んでタスクを切り替えることはできません。
    *   **English:** 
        *   In **non-preemptive** scheduling, CPU custody cannot be forcefully revoked by the OS. A running task retains CPU dominance until it voluntarily terminates or moves to the WAIT state.

---

##### 問9 (Integrated Development Environments: Eclipse)
オープンソースの統合開発環境であって，アプリケーション開発のためのソフトウェア及び支援ツール類をまとめたものはどれか。

*   **選択肢 (Options):**
    *   **ア:** Eclipse
    *   **イ:** Perl
    *   **ウ:** PHP
    *   **エ:** Ruby

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **Eclipse** は、Javaなどで幅広く用いられているOSSの有名な **統合開発環境（IDE: Integrated Development Environment）** です。コード記述、デバッグ、ビルド、コンパイル、バージョン管理などが1つのアプリ上で完結する開発プラットフォームです。
        *   *他の選択肢について:*
          * イ、ウ、エ: スクリプトプログラミング言語の名称です。
    *   **English:** 
        *   **Eclipse** is a legendary open-source **Integrated Development Environment (IDE)** primarily configured for Java, providing compiler pipelines, code intelligence, and execution debuggers.
        *   *Other options:*
          * Options イ, ウ, and エ are script languages.

---

##### 問10 (Boolean Simplification: Karnaugh Maps ASCII Art)
与えられた回路の出力論理式が $X = A \cdot B + \overline{B}$ であるとする。この論理式をカルノー図で整理した簡略化後の回路（等価回路）はどれか。

```text
    【カルノー図整理表】
    
               A     \overline{A}
            +-----+-----+
         B  |  1  |  0  |
            +-----+-----+
  \overline{B}|  1  |  1  |
            +-----+-----+
```

*   **選択肢 (Options):**
    *   **ア:** $X = A \cdot B$ を表すANDゲート
    *   **イ:** $X = A + \overline{B}$ を表すORゲート構成回路
    *   **ウ:** $X = A + B$ を表すORゲート
    *   **エ:** $X = \overline{A \cdot B}$ を表すNANDゲート

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        1. 与えられた式 $X = A \cdot B + \overline{B}$ の各項をカルノー図上にマッピングします。
           * $A \cdot B = 1$ となる位置（A＝1, B＝1）に「1」
           * $\overline{B} = 1$ となる位置（B＝0。すなわち $A \cdot \overline{B}$ と $\overline{A} \cdot \overline{B}$ 両方）に「1」
        2. カルノー図上で「1」が集まっている部分を、できるだけ大きな隣接ブロック（2の階乗サイズ）で囲みます：
           * 列方向のペア：A＝1の2つのマス（$A \cdot B$ と $A \cdot \overline{B}$）を囲むと、変数Bが相殺されて $A$ が残ります。
           * 行方向のペア：B＝0（$\overline{B}$）の行全体を囲むと、変数Aが相殺されて $\overline{B}$ が残ります。
        3. この二つのブロックを足し合わせることで、簡略化された論理式は：
           $$X = A + \overline{B}$$
           これは入力 $A$ と 入力 $B$ の否定 $\overline{B}$ をOR（論理和）ゲートに入力した回路と同じになります（選択肢イ）。
    *   **English:** 
        1. Given formula: $X = A \cdot B + \overline{B}$. Plot these terms on a 2x2 Karnaugh Map.
           * True cells: $(A, B) = (1, 1)$, $(A, \overline{B}) = (1, 0)$, and $(\overline{A}, \overline{B}) = (0, 0)$.
        2. Loop adjacent 1-cells into 2x1 loops:
           * Vertical loop over $A$ column: simplifies to $A$.
           * Horizontal loop over bottom row $\overline{B}$: simplifies to $\overline{B}$.
        3. Combine loops with OR logic to yield the simplest expression:
           $$X = A + \overline{B}$$
           This corresponds to a logic circuit where $A$ and NOT $B$ are passed to an OR gate (Option イ).

---

#### 📄 第10回演習問題 (6 Questions)

##### 問2 (Communication Delay: Satellite Relay Calculation)
地上から高度約36,000kmの静止軌道衛星を中継して，地上のA地点とB地点で通信をする。衛星とA地点，衛星とB地点の距離がどちらも37,500kmであり，衛星での中継による遅延を10ミリ秒とするとき，Aから送信し始めたデータがBに到達するまでの伝送遅延時間は何秒か。ここで，電波の伝搬速度は $3 \times 10^8$ m／秒とする。

*   **選択肢 (Options):**
    *   **ア:** 0.13
    *   **イ:** 0.26
    *   **ウ:** 0.35
    *   **エ:** 0.52

*   **正解 (Correct Answer):** **イ**

*   **詳細計算 (Calculation):**
    *   **日本語:** 
        1. **総データ伝搬距離の算出:**
           電波は A地点 $\to$ 衛星、その後 衛星 $\to$ B地点 と進むため、合計の移動距離 $D$ は：
           $$D = 37,500 \text{ km} \times 2 = 75,000 \text{ km} = 75,000,000 \text{ m} = 7.5 \times 10^7 \text{ m}$$
        2. **電波の移動時間 $t_{\text{travel}}$ の算出:**
           速度 $V = 3 \times 10^8 \text{ m/秒}$ で進むため：
           $$t_{\text{travel}} = \frac{\text{距離}}{\text{速度}} = \frac{7.5 \times 10^7}{3 \times 10^8} = 0.25 \text{秒}$$
        3. **中継遅延の加算:**
           衛星の内部処理（中継遅延）は $10 \text{ミリ秒}$（$= 0.01 \text{秒}$）です。
           $$\text{総伝送遅延} = t_{\text{travel}} + \text{中継遅延} = 0.25 + 0.01 = 0.26 \text{秒} \to \text{イ}$$
    *   **English:** 
        1. **Determine propagation distance ($D$):**
           The signal travels from $A \to \text{Satellite} \to B$. 
           $$D = 37,500 \text{ km} \times 2 = 75,000 \text{ km} = 7.5 \times 10^7 \text{ m}$$
        2. **Calculate absolute physical propagation time ($t_{\text{travel}}$):**
           Velocity $V = 3 \times 10^8 \text{ m/s}$ is applied:
           $$t_{\text{travel}} = \frac{7.5 \times 10^7 \text{ m}}{3 \times 10^8 \text{ m/s}} = 0.25 \text{ seconds}$$
        3. **Incorporate processing latency:**
           Add the relay processing delay of $10 \text{ ms}$ ($0.01 \text{ s}$):
           $$\text{Total Delay} = 0.25 \text{ s} + 0.01 \text{ s} = 0.26 \text{ seconds} \to \text{Option イ}$$

---

##### 問3 (Security Threats & Mitigation Safeguards)
情報システムヘの脅威とセキュリティ対策の組合せのうち，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** (脅威) 誤操作によるデータの論理的な破壊 --- (対策) ディスクアレイ
    *   **イ:** (脅威) 地震と火災 --- (対策) コンピュータ内で複数の仮想化OSを利用したデータの二重化
    *   **ウ:** (脅威) 伝送中のデータへの不正アクセス --- (対策) HDLC手順のCRC
    *   **エ:** (脅威) メッセージの改ざん --- (対策) 公開鍵暗号方式を応用したデジタル署名

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **エ: 正しい。** 送信中にメッセージが「改ざん」される脅威に対しては、公開鍵暗号技術を用いた「デジタル署名」を付与することで、受信側で厳密に改ざんの有無を検知できます。
        *   *他の不適切な組み合わせについて:*
          * ア: 誤操作による論理的データ消失には「バックアップ」が有効です。ディスクアレイ（RAID）はハード障害（物理故障）対策です。
          * イ: 地震や火災による建物の物理的破壊には「遠隔地バックアップ」が有効です。同一PC内の仮想化による多重化は筐体破損の際に一括消失します。
          * ウ: 伝送中データの「不正アクセス（盗聴）」には「暗号化通信（SSL/TLS）」が有効です。CRC（巡回冗長検査）はデータ誤り検出のみです。
    *   **English:** 
        *   **Option エ is correct.** To prevent message tampering (改ざん), applying a **digital signature** utilizing public-key cryptosystems allows the receiver to verify document integrity.
        *   *Other mismatch details:*
          * Option ア: logical deletions require periodic backups; disk arrays (RAID) secure hardware continuity.
          * Option イ: physical earthquakes require geographical disaster recovery redundancy.
          * Option ウ: interception requires encryption; CRC checks handle transmission frame bit noise.

---

##### 問5 (Symmetric-key vs. Public-key Cryptography Features)
公開鍵暗号方式に関する記述として，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** AESなどの暗号方式がある。
    *   **イ:** RSAや楕円(だえん)曲線暗号などの暗号方式がある。
    *   **ウ:** 暗号化鍵と復号鍵が同一である。
    *   **エ:** 共通鍵の配送が必要である。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **公開鍵暗号方式** は、対となる「公開鍵（誰でも取得可能）」と「秘密鍵（本人のみが管理）」の異なる2つの鍵を利用する暗号方式です。代表的な暗号アルゴリズムに **RSA** や **楕円曲線暗号 (ECC: Elliptic Curve Cryptography)** があります。
        *   *他の選択肢について:*
          * ア、ウ、エ: これらはすべて「共通鍵暗号方式」（同一の鍵で暗号・復号を行うAESなど）の性質を説明したものです。
    *   **English:** 
        *   **Asymmetric (Public-Key) Cryptography** uses dual distinct components (public encryption key and private decryption key). Classical options include **RSA** and **Elliptic Curve Cryptography (ECC)**.
        *   *Other options:*
          * Options ア, ウ, and エ refer to symmetric encryption schemes like AES.

---

##### 問6 (Relational Database Referential Integrity Checks)
関係データベース"注文"表の"顧客番号"は"顧客"表の主キー"顧客番号"に対応する外部キーである。このとき、参照の整合性を損なうデータ操作はどれか。ここで、ア～エの記述におけるデータの並びは、それぞれの表の列の並びと同順とする。

```text
    【データベーステーブル構成図】
    
     [注文 (Orders)] 表                      [顧客 (Customers)] 表
     +----------+----------+                 +----------+----------+
     | 伝票番号 | 顧客番号 | (外部キー)       | 顧客番号 |  顧客名  | (主キー)
     +----------+----------+                 +----------+----------+
     |   0001   |   C005   |                 |   C005   |   福島   |
     |   0002   |   K001   |                 |   D010   |   千葉   |
     |   0003   |   C005   |                 |   K001   |   長野   |
     |   0004   |   D010   |                 |   L035   |   宮崎   |
     +----------+----------+                 +----------+----------+
```

*   **選択肢 (Options):**
    *   **ア:** "顧客"表の行 [ L035, 宮崎 ] を削除する。
    *   **イ:** "注文"表に行 [ 0005, D010 ] を追加する。
    *   **ウ:** "注文"表に行 [ 0006, F020 ] を追加する。
    *   **エ:** "注文"表の行 [ 0002, K001 ] を削除する。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **参照整合性制約 (Referential Integrity Constraint)** とは、外部キーに入力する値は、必ず参照先（親テーブル）の主キーに存在する値でなければならない、というルールです。
        *   "顧客"表（親）の顧客番号主キーには [ C005, D010, K001, L035 ] が定義されています。
        *   選択肢ウのデータ操作は、"注文"表（子）の顧客番号に、親のテーブルに存在しない **F020** を追加しようとしています。これは親テーブルにない不正な顧客への注文を作ることになり、参照整合性を著しく破壊するため不許可となります。
    *   **English:** 
        *   **Referential Integrity Constraints** mandate that values entered in foreign keys must exist within the target table's primary key registry.
        *   Adding a line specifying `F020` as `顧客番号` into the `注文` (Orders) table violates integrity rules because customer identifier `F020` is missing from the parent `顧客` (Customers) table registry.

---

##### 問8 (Multimedia: Video Coding Formats - H.264)
H.264/MPEG-4 AVCに関する記述はどれか。

*   **選択肢 (Options):**
    *   **ア:** インターネットで動画や音声データのストリーミング配信を制御するための通信方式
    *   **イ:** テレビ会議やテレビ電話で双方向のビデオ配信を制御するための通信方式
    *   **ウ:** テレビの電子番組案内で使用される番組内容のメタデータを記述する方式
    *   **エ:** ワンセグやインターネットで用いられる動画データの圧縮符号化方式

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **H.264 / MPEG-4 AVC** は、ワンセグ放送、YouTubeなどのインターネット配信、ブルーレイ、スマホのビデオ撮影に幅広く用いられる極めて普及率の高い高効率な **動画圧縮（符号化）の国際標準規格** です。
        *   *他の選択肢について:*
          * ア: RTSP（Real Time Streaming Protocol）等の通信制御プロトコルの説明。
          * イ: SIP（Session Initiation Protocol）等の双方向配信規格の説明。
          * ウ: EPG（Electronic Program Guide）等の番組ガイドデータの仕様。
    *   **English:** 
        *   **H.264 (MPEG-4 AVC)** is a globally dominant compression video coding format utilized massively in web media platforms (e.g. YouTube), mobile devices, and terrestrial broadcasts (1seg).

---

##### 問10 (Network Mask Structural Rules)
IPv4ネットワークで用いられる可変長サブネットマスクとして，正しいものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 255.255.255.1
    *   **イ:** 255.255.255.32
    *   **ウ:** 255.255.255.64
    *   **エ:** 255.255.255.128

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   サブネットマスク（Subnet Mask）を32ビットの2進数で表したとき、**「先頭から連続して1が並び、途中から連続して0が並ぶ」** という厳しい配置規則があります。途中で1と0が交互に混ざったり、0の後に再び1が現れる並びは絶対に認められません。
        *   各選択肢の第4ビット（末尾）を2進数（8桁）に変換して検証します：
          * ア: .1 $\to$ `00000001` (1が右端に孤立しており、不連続なため不可)
          * イ: .32 $\to$ `00100000` (1が途中に孤立しており、不連続なため不可)
          * ウ: .64 $\to$ `01000000` (1が途中に孤立しており、不連続なため不可)
          * エ: .128 $\to$ `10000000` (左側が全て1の並びの続きであり、右に0が並ぶ「連続した1と0」の条件を満たすため正しい！)
    *   **English:** 
        *   An IPv4 **Subnet Mask** must consist of contiguous binary `1`s from the left (representing the network prefix) followed by contiguous binary `0`s (representing the host portion). No mixed binary bits (e.g., `0` preceding a `1`) are structurally valid.
        *   Evaluating the fourth octet values in binary:
          * Option ア: $1 = 00000001_2$ (invalid disjoint `1`)
          * Option イ: $32 = 00100000_2$ (invalid disjoint `1`)
          * Option ウ: $64 = 01000000_2$ (invalid disjoint `1`)
          * Option エ: $128 = 10000000_2$ (valid continuous string of `1`s ending network portion).

---

#### 📄 第11回演習問題 (4 Questions)

##### 問2 (Network Protocols: Layer Encapsulation Sequence)
1個のTCPパケットをイーサネットに送出したとき，イーサネットフレームに含まれる宛先情報の，送出順序はどれか。

*   **選択肢 (Options):**
    *   **ア:** 宛先IPアドレス，宛先MACアドレス，宛先ポート番号
    *   **イ:** 宛先IPアドレス，宛先ポート番号，宛先MACアドレス
    *   **ウ:** 宛先MACアドレス，宛先IPアドレス，宛先ポート番号
    *   **エ:** 宛先MACアドレス，宛先ポート番号，宛先IPアドレス

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   データが送信されるとき、OSI基本参照モデルの上の階層（アプリケーション層）から下の階層（物理層）へと順に **カプセル化（ヘッダー情報が付加される）** されていきます。
        *   送信パケットは、一番外側（物理層に近い層）から順にケーブルに送り出されます。
          * 1番外側：データリンク層の **MACヘッダー（宛先MACアドレス）** $\to$ 最初に送出される。
          * 2番目：ネットワーク層の **IPヘッダー（宛先IPアドレス）** $\to$ 次に送出される。
          * 3番目：トランスポート層の **TCPヘッダー（宛先ポート番号）** $\to$ 最後に送出される。
        *   したがって、物理回線上を電気信号として流れる順番は **「MACアドレス $\to$ IPアドレス $\to$ ポート番号」** （選択肢ウ）になります。
    *   **English:** 
        *   When packets are placed on physical cables, data is serialized from the outermost Layer 2 frame down to the payload. 
        *   Thus, Layer 2 header elements (**Destination MAC Address**) transmit first on the wire, followed by Layer 3 header elements (**Destination IP Address**), and finally Layer 4 headers (**Destination Port Number**). This yields Option ウ.

---

##### 問3 (Network Management Tools: LAN Analyzer Guidelines)
ネットワーク障害の原因を調べるために，ミラーポートを用意して，LANアナライザーを使用するときに留意することはどれか。

*   **選択肢 (Options):**
    *   **ア:** LANアナライザーがパケットを破棄してしまうので，測定中は測定対象外のコンピュータの利用を制限しておく必要がある。
    *   **イ:** LANアナライザーにはネットワークを通過するパケットを表示できるので，盗聴などに悪用されないように注意する必要がある。
    *   **ウ:** 障害発生に備えて，ネットワーク利用者にLANアナライザーの保管場所と使用方法を周知しておく必要がある。
    *   **エ:** 測定に当たって，LANケーブルを一時的に切断する必要があるので，利用者に対して測定日を事前に知らせておく必要がある。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **LANアナライザー (LAN Analyzer: パケットキャプチャーツール)** は、ネットワーク回線上を流れる全てのフレームを傍受して通信解析を行うツールです（Wiresharkなどが有名）。
        *   暗号化されていない平文のパケット（ID、パスワード、メール内容）をそのまま画面上に可視化できてしまう極めて強力な解析ツールであるため、第三者に悪用されると深刻な「盗聴」ツールと化します。そのため、管理と利用ルールを厳格に制限する必要があります。
    *   **English:** 
        *   A **LAN Analyzer** monitors and records ethernet frames on a network interface. 
        *   Because it reconstructs raw packets, malicious entities can abuse it to sniff plain-text passwords and confidential streams. Hence, strict device storage and secure audit access must be enforced.

---

##### 問7 (Malware Threats: Drive-by Download)
ドライブバイダウンロード攻撃に該当するものはどれか。

*   **選択肢 (Options):**
    *   **ア:** PC内のマルウェアを遠隔操作して，PCのハードディスクドライブを丸ごと暗号化する。
    *   **イ:** 外部ネットワークからファイアウォールの設定の誤りを突いて侵入し，内部ネットワークにあるサーバのシステムドライブにルートキットを仕掛ける。
    *   **ウ:** 公開Webサイトにおいて，スクリプトをWebページ中の入力フィールドに入力し，Webサーバがアクセスするデータベース内のデータを不正にダウンロードする。
    *   **エ:** 利用者が公開Webサイトを閲覧したときに，その利用者の意図にかかわらず，PCにマルウェアをダウンロードさせて感染させる。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ドライブバイダウンロード (Drive-by Download) 攻撃** とは、攻撃者がWebサイト改ざんや不正なバナー広告を通じて悪意のあるスクリプトを埋め込み、**ユーザーがただそのWebサイトにアクセスして閲覧しただけ**で、何の同意も操作もない状態でバックグラウンドでマルウェアをダウンロードさせ、感染させる攻撃です。
        *   *他の選択肢について:*
          * ア: ランサムウェア（Ransomware）の動作。
          * ウ: SQLインジェクションによるデータ侵害。
    *   **English:** 
        *   A **Drive-by Download** occurs when malware is automatically downloaded and executed in the background without any user interaction or confirmation, simply as a result of visiting a compromised web page or clicking an infected ad banner.

---

##### 問9 (Malware Classification: Trojan Horse vs. Worm)
マルウェアについて，トロイの木馬とワームを比較したとき，ワームの特徴はどれか。

*   **選択肢 (Options):**
    *   **ア:** 勝手にファイルを暗号化して正常に読めなくする。
    *   **イ:** 単独のプログラムとして不正な動作を行う。
    *   **ウ:** 特定の条件になるまで活動をせずに待機する。
    *   **エ:** ネットワークやリムーバブルメディアを媒介として自ら感染を広げる。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ワーム (Worm)** は、他の宿主プログラム（ファイル）に寄生しなくても「**単独の実行可能ファイルとして存在できる**」マルウェアです。最大の特徴は、PCネットワークやUSBメモリなどの媒体を介して、自身のコピーを**「自立的に複製・増殖（自己拡散）」**させて他のネットワーク内のPCへ次々に感染を拡大することです。
        *   これに対して、**トロイの木馬** は無害な正規アプリに偽装してユーザーに自発的に実行させ、バックグラウンドで破壊や窃盗、バックドアの作成などを行うマルウェアで、自己拡散能力はありません。
    *   **English:** 
        *   Unlike Trojan Horses which require human installation, a **Worm** is a self-replicating independent program. It spreads automatically across networks and storage drives without binding to host files, utilizing security vulnerabilities to infect downstream endpoints.

---

#### 📄 第12回演習問題 (4 Questions)

##### 問2 (System Modeling: State Transition Diagrams)
要求の分析・設計時に使用する状態遷移図の説明として，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 階層構造の形でプログラムの全体構造を記述する。
    *   **イ:** 時間の経過や制御信号の変化等の状態を変化させるきっかけと変化に伴って実行する動作を記述する。
    *   **ウ:** システムの機能を概要から詳細へと段階的に記述する。
    *   **エ:** 処理間のデータの流れをデータフロー，処理，データストア及び外部の四つの記号で記述する。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **状態遷移図 (State Transition Diagram)** は、イベント（時間の経過、ボタン押下、コマンド受信など）をきっかけとして、システムの状態が「どのように変化（遷移）するか」をモデル化して分かりやすく記述する図式設計手法です。
        *   *他の選択肢について:*
          * ア: プログラム構造図（Structure Chart）の説明
          * ウ: 構造化機能ツリー（Functional Decomposition）等の説明
          * エ: DFD（Data Flow Diagram: データフロー図）の説明
    *   **English:** 
        *   A **State Transition Diagram** charts how a system transitions dynamically between logical states in response to asynchronous stimulus triggers or timers.
        *   *Other options:*
          * Option ア is a Structure Chart.
          * Option エ is a DFD (Data Flow Diagram).

---

##### 問5 (Software Architecture: Module Cohesion & Coupling)
ソフトウェアのモジュール設計において，信頼性，保守性を向上させるためのアプローチとして，望ましいものはどれか。

*   **選択肢 (Options):**
    *   **ア:** モジュール強度を強く，結合度を強くする。
    *   **イ:** モジュール強度を強く，結合度を弱くする。
    *   **ウ:** モジュール強度を弱く，結合度を強くする。
    *   **エ:** モジュール強度を弱く，結合度を弱くする。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   ソフトウェアの「保守性」や「再利用性」を高めるには、モジュールの **独立性** を極限まで高める必要があります。
        *   **モジュール強度 (Cohesion - 結束性 / 強度):** モジュール内部にまとめられた機能同士の結びつきの強さです。これが **「強い（強く）」** ほど、そのモジュールは1つの特定の作業に特化した高純度な部品と言え、望ましい状態です。
        *   **モジュール結合度 (Coupling - 依存度 / 結合度):** 他のモジュールとの依存関係の強さです。これが **「弱い（弱く）」** ほど、他のモジュールのコードを修正したときにバグが連鎖して伝播しないため、望ましい状態です。
        *   よって、アプローチとして最適な設計公式は **「強度を強く、結合度を弱くする」** （選択肢イ）です。
    *   **English:** 
        *   For maximizing reliability and codebase maintainability, software components must demonstrate high independence. This requires two design principles:
          * **High Module Cohesion (強度を強く):** The internal functions inside a single module must serve a singular, focused objective.
          * **Low Module Coupling (結合度を弱く):** Modules should avoid heavy parameters or shared global dependencies to minimize regression risks during updates.

---

##### 問8 (Design Reviews: Walkthrough Method)
設計上の誤りを早期に発見することを目的として，作成者と複数の関係者が設計書をレビューする方法はどれか。

*   **選択肢 (Options):**
    *   **ア:** ウォークスルー (Walkthrough)
    *   **イ:** 机上デバッグ (Dry Run)
    *   **ウ:** トップダウンテスト (Top-down Test)
    *   **エ:** 並行シミュレーション (Parallel Simulation)

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ウォークスルー (Walkthrough)** は、仕様書やプログラムの作成者が、関係する開発者（レビュアー）を集め、設計書やソースコードのロジックを段階的に説明（模擬実行）しながら、誤りや不整合を全員で検証するレビュー手法です。
        *   *特徴:* 責任追及の場にしないため、評価権限のある管理者はあえて同席させず、純粋なバグの早期発見を目的に行われます。
    *   **English:** 
        *   A **Walkthrough** is a peer review process in which the author leads software designers and developers through document logical blocks to discover early configuration defects. Managers are usually excluded to encourage unbiased technical criticism.

---

##### 問10 (Software Testing Tools: Static vs. Dynamic Code Analysis)
ソフトウェアのテストツールの説明のうち，静的テストを支援する静的解析ツールのものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 指定された条件のテストデータや，プログラムの入力ファイルを自動的に生成する。
    *   **イ:** テストの実行結果を基に，命令の網羅率や分岐の網羅率を自動的に計測し，分析する。
    *   **ウ:** プログラム中に文法上の誤りや論理的な誤りなどがあるかどうかを，ソースコードを分析して調べる。
    *   **エ:** モジュールの呼出し回数や実行時間，実行文の実行回数などの，プログラム実行時の動作特性に関するデータを計測する。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **静的解析ツール (Static Analysis Tool)** は、プログラムを **「実行させずに（静的状態のままで）」** ソースコードを分析し、構文エラー、セキュリティーの脆弱性、ルール違反、未使用変数などを検出するデバッグ支援ツール（Linterやコードインスペクターなど）です。
        *   *他の選択肢について:*
          * ア: テストデータジェネレーター（環境設定ツール）
          * イ: カバレッジアナライザー（動的解析ツール）
          * エ: プロファイラー（動的解析ツール）
    *   **English:** 
        *   **Static Analysis Tools** evaluate source code structure, scanning syntax grammar, potential leaks, and style guideline compliance **without running the program** itself (e.g. Linters).
        *   *Other options:*
          * Option ア: Test Data Generators.
          * Option イ: Coverage Monitors (Dynamic tools).
          * Option エ: Profilers checking CPU performance during runtime (Dynamic tools).

---

#### 📄 第13回演習問題 (9 Questions)

##### 問1 (Enterprise Strategy: SWOT Analysis Matrix)
経営戦略策定に用いられるSWOT分析はどれか。

*   **選択肢 (Options):**
    *   **ア:** 競争環境における機会・脅威と事業の強み・弱みを分析する。
    *   **イ:** 競争に影響する要因と，他者の動き，自社の動きを分析する。
    *   **ウ:** 市場に対するマーケティングツールの最適な組合せを分析する。
    *   **エ:** 市場の成長性と占有率の観点から各事業の位置付けを分析する。

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **SWOT分析** は、企業の強みと弱みを評価してビジネス戦略を立てるための王道のフレームワークです。
          * 内部要因： **S**trength（強み）、 **W**eakness（弱み）
          * 外部要因： **O**pportunity（機会）、 **T**hreat（脅威）
        *   *他の選択肢について:*
          * イ: 3C分析（Customer, Competitor, Company）
          * ウ: マーケティングミックス（4P / 4C）
          * エ: PPM（Product Portfolio Management）分析
    *   **English:** 
        *   **SWOT Analysis** categorizes internal operational constraints and external business environments into four blocks: **S**trengths, **W**eaknesses, **O**pportunities, and **T**hreats. This provides a clean corporate strategic overview.

---

##### 問2 (Logistics Management: Supply Chain Management - SCM)
サプライチェーンマネジメントを説明したものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 購買，生産，販売及び物流を結ぶ一連の業務を，企業内，企業間で全体最適の視点から見直し，納期短縮や在庫削減を図る。
    *   **イ:** 個人が持っているノウハウや経験などの知的資産を組織全体で共有して，創造的な仕事につなげていく。
    *   **ウ:** 社員のスキルや行動特性を把握し，人事戦略の視点から適切な人員配置・評価などのマネジメントを行う。
    *   **エ:** 多様なチャネルを通して集められた顧客情報を一元化し，活用することによって，顧客との関係を密接にしていく。

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **SCM (Supply Chain Management)** とは、原材料調達、部品製造、最終製品の組み立て、輸送、店舗販売に至るまでの「一連の供給連鎖（サプライチェーン）」に関係する企業間（調達先、メーカー、運送会社、小売店）で情報をリアルタイムに共有し、在庫を極限まで減らし、納期の短縮を達成する「全体最適」の経営手法です。
        *   *他の選択肢について:*
          * イ: ナレッジマネジメント（Knowledge Management）
          * ウ: 人的資源管理（HRM: Human Resource Management）
          * エ: 顧客関係管理（CRM: Customer Relationship Management）
    *   **English:** 
        *   **SCM (Supply Chain Management)** integrates global logistics databases across vendors, transporters, factories, and retailers to coordinate procurement, optimize inventory buffers, and accelerate delivery turnarounds.

---

##### 問3 (Legal Frameworks: Copyright Exclusions)
著作権法において，保護の対象とならないものはどれか。

*   **選択肢 (Options):**
    *   **ア:** インターネットで公開されたフリーソフトウェア
    *   **イ:** ソフトウェアの操作マニュアル
    *   **ウ:** データベース
    *   **エ:** プログラム言語や規約

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   著作権法では、「プログラムの著作物（ソースコードやオブジェクトコード）」、「マニュアル、説明書（言語の著作物）」、「データベース（データベースの著作物）」は明確に保護対象として定めています。
        *   しかし、以下の3項目は、**アイデアそのものや業界の共通規格**であり、特定の誰かが独占するとIT業界全体の技術開発がストップしてしまうため、**著作権法による保護の対象外**と明確に規定されています。
          1. **プログラム言語**（プログラミングの記述ルール）
          2. **規約**（通信プロトコルやデータフォーマットなどの規格）
          3. **解法**（アルゴリズム：問題を解く手順）
    *   **English:** 
        *   Japanese Copyright Law explicitly excludes three programming foundations from protection to foster open technological growth:
          1. **Programming Languages** (syntax rules).
          2. **Rules / Protocols** (communication protocols).
          3. **Algorithms** (methods/steps to solve calculations).

---

##### 問4 (Privacy Legislation: Personal Identifiable Information Exemptions)
個人情報に該当しないものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 受付に設置した監視カメラに録画された，本人が判別できる映像データ
    *   **イ:** 個人番号の記載がない，社員に交付する源泉徴収票
    *   **ウ:** 指紋認証のための指紋データのバックアップデータ
    *   **エ:** 匿名加工情報に加工された利用者アンケート情報

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **個人情報** とは、生存する個人に関する情報であって、特定の個人を「識別できる（照合できる）」ものを指します。
        *   **匿名加工情報** とは、個人情報を復元不可能な方法で加工し、**特定の個人を一切識別・再識別できないように完全に個人識別子を排除した情報**です。これは個人情報保護法の規制対象外となるため、本人の同意なしにビッグデータ分析やビジネス活用として自由に第三者へ提供することができます。
    *   **English:** 
        *   **Anonymized Data (匿名加工情報)** consists of personal datasets processed through cryptographic hashing or masking to fully prevent re-identification of individuals. Because individuals cannot be decoded, it is legally exempted from standard Privacy Law regulations.

---

##### 問5 (Systems Strategy: Electronic Commerce - EC)
EC(Electronic Commerce)に関する説明として，適切なものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 営業活動にITを活用して営業効率と品質を高め，売上・利益の大幅な増加や，顧客満足度の向上を目指す方法である。
    *   **イ:** 企業がもつ経営資源全体を，総合的かつ一元的に計画・管理し，経営の効率化を図る手法・概念である。
    *   **ウ:** 小売店の売上と利益を伸ばすことによって，卸売業者・メーカーが自社との取引拡大につなげるための小売店の経営活動を支援するシステムである。
    *   **エ:** 消費者向けや企業間の商取引をインターネットなどの電子的なネットワークを活用して行うことである。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **EC (Electronic Commerce: 電子商取引)** とは、インターネットや専用回線といった電子的な通信ネットワークを介して行われる、商品の売買やサービスの商取引そのものを指します。
        *   *他の選択肢について:*
          * ア: SFA（Sales Force Automation）の説明。
          * イ: ERP（Enterprise Resource Planning）の説明。
          * ウ: リテールサポート（Retail Support）の説明。
    *   **English:** 
        *   **EC (Electronic Commerce)** covers any form of business transactions or trade of commodities and digital subscriptions executed over electronic channels like the internet.

---

##### 問7 (Labor Regulations: Dispatch Worker Contracts)
A社で雇用しているオペレータのQ氏を，B社に派遣することになった。労働者派遣法で定められているものはどれか。

*   **選択肢 (Options):**
    *   **ア:** A社は，Q氏がA社を辞めてB社に雇用されることを禁止できる。
    *   **イ:** B社はA社に対して，Q氏を指名して派遣を要請できる。
    *   **ウ:** Q氏の派遣契約期間は，最長1年間である。
    *   **エ:** Q氏は，B社の定められた指揮命令者の下で労働に従事する。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **労働者派遣契約** では、派遣労働者（Q氏）は「派遣元（A社）」と雇用関係を持ちつつ、仕事の現場である「派遣先（B社）」の担当者の **「指揮命令（指示）」** に従って実務に従事します（選択肢エが正しい）。
        *   *違法となる行為について:*
          * ア: 派遣期間終了後に、派遣社員が派遣先企業に自発的に就職することを、派遣元が契約で禁止する行為は違法です。
          * イ: 派遣先企業が特定の労働者を指定（指名）して派遣を要請する「特定目的行為」は、雇用差別を防ぐ観点から労働者派遣法で禁止されています。
    *   **English:** 
        *   Under a **Labor Dispatch Contract**, a dispatched worker is employed officially by the Dispatch Agency (Company A) but operates under the direct **supervision and instruction** of the receiving Host Client (Company B).

---

##### 問8 (Server Architecture: Hosting vs. Housing Services)
ホスティングサービスの特徴はどれか。

*   **選択肢 (Options):**
    *   **ア:** 運用管理面では，サーバの稼働監視，インシデント対応などを全て利用者が担う。
    *   **イ:** サービス事業者が用意したサーバの利用権を利用者に貸し出す。
    *   **ウ:** サービス事業者の高性能なサーバを利用者が専有するような使い方には対応しない。
    *   **エ:** サービス事業者の施設に利用者が独自のサーバを持ち込み，サーバの選定や組合せは自由に行う。

*   **正解 (Correct Answer):** **イ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ホスティングサービス (Hosting Service)** とは、サービス事業者が所有するサーバーマシンの利用権（機能）を、インターネット経由で利用者に有料/無料で貸し出すレンタルサーバーサービスです（選択肢イが正しい）。
        *   *ハウジングサービス（コロケーション）との違い:*
          * **ハウジングサービス (Housing Service):** 利用者自身が自前のサーバーをデータセンターに「持ち込み（エの説明）」、ラックやスペース、電源、回線設備だけを借りるサービスです。
    *   **English:** 
        *   A **Hosting Service** leases ready-made hardware processing resources owned and maintained by the Service Provider to the users. 
        *   *Contrast:* In a **Housing Service** (Colocation), users physically rent secure server rack spaces to install their own proprietary custom equipment (defined in Option エ).

---

##### 問9 (Corporate Finance: Properties of a Balance Sheet)
財務諸表のうち，一定時点における企業の資産，負債及び純資産を表示し，企業の財政状態を明らかにするものはどれか。

*   **選択肢 (Options):**
    *   **ア:** 株主資本等変動計算書
    *   **イ:** キャッシュフロー計算書
    *   **ウ:** 損益計算書
    *   **エ:** 貸借対照表 (Balance Sheet)

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **貸借対照表 (B/S: Balance Sheet)** は、ある「決算期末など **特定の一定時点**」において、会社がどんな財産（資産）を持ち、どんな借金（負債）があり、本当の自分の取り分（純資産）がいくらあるかという、**財政状態**を一覧にした財務諸表です。
        *   *他の財務諸表について:*
          * ウ: **損益計算書 (P/L: Profit and Loss Statement):** 一定の「会計期間」における収益と費用を示し、会社の「経営成績（儲け）」を表す表です。
    *   **English:** 
        *   A **Balance Sheet (B/S: 貸借対照表)** records a company's assets, liabilities, and equity at a **single specific point in time** to reflect its overall financial health. 
        *   *Contrast:* A **Profit and Loss Statement (P/L: 損益計算書)** aggregates revenues and expenses over a whole fiscal **period** to represent business performance.

---

##### 問10 (Consumer Protection: Product Liability Law Limits)
ソフトウェアやデータに欠陥がある場合に，製造物責任法（PL法）の対象となるものはどれか。

*   **選択肢 (Options):**
    *   **ア:** ROM化したソフトウェアを内蔵した組込み機器
    *   **イ:** アプリケーションソフトウェアパッケージ
    *   **ウ:** 利用者がPCにインストールしたOS
    *   **エ:** 利用者によってネットワークからダウンロードされたデータ

*   **正解 (Correct Answer):** **ア**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **製造物責任法（PL法）** における「製造物」は、**「製造又は加工された動産（形のある有形物）」** と定義されています。
        *   そのため、プログラムコードや音楽データ、ダウンロードされた電子データ、サービス、不動産といった「無体物（形のないもの）」は、単体では動産ではないため、原則としてPL法の適用対象外となります。
        *   しかし、欠陥プログラムを内蔵した **ハードウェア（例えば、洗濯機や炊飯器、車といった組み込み機器のROM）** の不具合によって火災や怪我などの被害（拡大損害）が発生した場合は、「動産（機器）そのものに欠陥がある」とみなされるため、PL法の適用対象となります。したがって、アが正解です。
    *   **English:** 
        *   Under **Product Liability Law (PL Law)**, a "product" is strictly defined as a manufactured **tangible movable property (動産)**. 
        *   Intangible digital assets like standalone software files, operating system downloads, or digital streams are excluded. However, if defective firmware is embedded inside physical hardware (**ROM on an embedded system**), the physical hardware is deemed defective, falling under PL liability coverage.

---

### 🔵 Category 3: High-Possibility Sample Questions (7 Questions)
このセクションでは、IPAが公開している『基本情報技術者試験 科目A 公開問題』(`2025r07_fe_kamoku_a_qs.pdf`)から、今回のシステム、ネットワーク、セキュリティ、開発、経営の講義に完全に合致する、期末試験への出題可能性が極めて高い7つの厳選問題を解説します。

---

#### 問4 (Systems Reliability: Projected Availability Calculation)
MTBFは4,000時間，MTTRは1,000時間の装置がある。今後の6年間は，予防保守によってMTBFを前年に比べて毎年100時間ずつ改善し，遠隔保守によってMTTRを前年に比べて毎年100時間ずつ改善していく計画である。6年経過後の稼働率は幾らか。

*   **選択肢 (Options):**
    *   **ア:** 0.88
    *   **イ:** 0.90
    *   **ウ:** 0.92
    *   **エ:** 0.94

*   **正解 (Correct Answer):** **ウ**

*   **詳細計算 (Calculation):**
    *   **日本語:** 
        1. **6年後のMTBFの算出（予防保守による改善：長くなる）:**
           * 毎年100時間「改善」されるため、6年間で加算される時間： $100 \text{時間} \times 6 = 600 \text{時間}$
           * 6年後のMTBF： $\text{MTBF}_{\text{6yr}} = 4,000 + 600 = 4,600 \text{時間}$
        2. **6年後のMTTRの算出（遠隔保守による改善：短くなる）:**
           * 毎年100時間「改善（短縮）」されるため、6年間で減算される時間： $100 \text{時間} \times 6 = 600 \text{時間}$
           * 6年後のMTTR： $\text{MTTR}_{\text{6yr}} = 1,000 - 600 = 400 \text{時間}$
        3. **6年後の稼働率 (Availability) の算出:**
           $$\text{稼働率}_{\text{6yr}} = \frac{\text{MTBF}_{\text{6yr}}}{\text{MTBF}_{\text{6yr}} + \text{MTTR}_{\text{6yr}}}$$
           $$\text{稼働率}_{\text{6yr}} = \frac{4,600}{4,600 + 400} = \frac{4,600}{5,000} = 0.92 \to \text{ウ}$$
    *   **English:** 
        1. **Calculate MTBF after 6 years (preventive maintenance extends it):**
           $$\text{MTBF}_{\text{6yr}} = 4,000 + (100 \times 6) = 4,600 \text{ hours}$$
        2. **Calculate MTTR after 6 years (remote maintenance shortens it):**
           $$\text{MTTR}_{\text{6yr}} = 1,000 - (100 \times 6) = 400 \text{ hours}$$
        3. **Calculate Availability after 6 years:**
           $$\text{Availability}_{\text{6yr}} = \frac{4,600}{4,600 + 400} = \frac{4,600}{5,000} = 0.92 \to \text{Option ウ}$$

---

#### 問7 (Network Performance: Line Utilization Rate Calculation)
1Gバイトの動画データを40Mビット／秒の回線を使用してダウンロードしたところ，5分掛かった。このときの回線利用率はおよそ何％か。ここで，ダウンロード時には動画データに20％の制御情報が付加されるものとする。

*   **選択肢 (Options):**
    *   **ア:** 10%
    *   **イ:** 53%
    *   **ウ:** 67%
    *   **エ:** 80%

*   **正解 (Correct Answer):** **エ**

*   **詳細計算 (Calculation):**
    *   **日本語:** 
        1. **送信データの総ビット数（Byteからbitへの変換とオーバーヘッドの加算）:**
           * 元データ： $1 \text{ GByte} = 10^9 \text{ Bytes}$ （※問題文の慣例による $10^9$ 計算）
           * 20%の制御ヘッダー情報が付加されるため、実際の送信量：
             $$\text{データ量} = 1 \text{ GByte} \times 1.20 = 1.2 \text{ GBytes}$$
           * バイトからビットへ変換（1 Byte = 8 bits）：
             $$\text{総データ量 (bits)} = 1.2 \times 10^9 \text{ Bytes} \times 8 \text{ bits/Byte} = 9.6 \times 10^9 \text{ bits}$$
        2. **実際の転送速度（実効伝送速度）の算出:**
           * 転送にかかった時間： 5分 $= 300 \text{秒}$
           * 1秒あたりの実効速度：
             $$\text{実効速度} = \frac{9.6 \times 10^9 \text{ bits}}{300 \text{秒}} = 3.2 \times 10^7 \text{ bps} = 32 \text{ Mbps}$$
        3. **回線利用率の算出:**
           * 理論上の回線最大速度： $40 \text{ Mbps}$
           * 利用率：
             $$\text{回線利用率} = \frac{\text{実効速度}}{\text{理論上の速度}} = \frac{32 \text{ Mbps}}{40 \text{ Mbps}} = 0.80 \to 80\% \to \text{エ}$$
    *   **English:** 
        1. **Calculate total bits transmitted including the 20% control overhead:**
           $$\text{Data} = 1 \text{ GB} \times 1.20 \text{ overhead} = 1.2 \text{ GB}$$
           $$\text{Convert to bits (1 Byte = 8 bits): } 1.2 \times 10^9 \text{ Bytes} \times 8 = 9.6 \times 10^9 \text{ bits}$$
        2. **Determine effective transmission rate over 5 minutes (300 seconds):**
           $$\text{Effective Speed} = \frac{9.6 \times 10^9 \text{ bits}}{300 \text{ seconds}} = 3.2 \times 10^7 \text{ bps} = 32 \text{ Mbps}$$
        3. **Calculate Line Utilization Rate against the 40 Mbps limit:**
           $$\text{Line Utilization} = \frac{32 \text{ Mbps}}{40 \text{ Mbps}} = 0.80 \to 80\% \to \text{Option エ}$$

---

#### 問8 (Secure Protocols: Advantages of HTTPS Certificates)
HTTPとHTTPSを比較した場合において，HTTPSだけがもつ特徴を示したものはどれか。

*   **選択肢 (Options):**
    *   **ア:** cookieに保存されている情報を用いたセッション管理が可能である。
    *   **イ:** IDとパスワードによって利用者の認証を行うことが可能である。
    *   **ウ:** Webブラウザでキャッシュさせることによって通信量を減らすことが可能である。
    *   **エ:** 通信相手先サーバをサーバ証明書によって確認することが可能である。

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   HTTPS（HTTP over SSL/TLS）は、トランスポート層でデータを暗号化するプロトコルです。
        *   HTTPにない最大の特徴は、**信頼できる認証局（CA）が発行した「サーバー証明書」を用いることで、接続先のWebサーバーが本物であるかを確認できる（なりすましを防止する）** ことです。
        *   *他の選択肢について:* ア、イ、ウは通常のHTTPでも全く同様に実行可能です。
    *   **English:** 
        *   **HTTPS (HTTP Secure)** layers standard HTTP over the secure SSL/TLS protocol. 
        *   It uniquely provides **Server Authentication** via cryptographic **digital server certificates** validated by trusted third-party CAs to prevent spoofing. Thus, Option エ is correct.

---

#### 問9 (Information Security Concepts: Compromise of Cryptography)
暗号の危殆（きたい）化に該当するものはどれか。

*   **選択肢 (Options):**
    *   **ア:** あるCAでデジタル証明書の署名に使っている公開鍵のデジタル証明書の有効期限が切れた。
    *   **イ:** ある暗号アルゴリズムの秘密鍵が不正アクセスによって漏えいした。
    *   **ウ:** あるハッシュ関数においてハッシュ値が同じになるデータの組みを現実的な時間内で発見する方法が見つかった。
    *   **エ:** あるランサムウェアの一種で暗号化されたファイルの復号鍵が公開された。

*   **正解 (Correct Answer):** **ウ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **暗号の危殆化 (Compromise of Cryptography)** とは、技術の進歩や数学的な解読法の発見によって、**暗号アルゴリズムやハッシュ関数そのものの理論的な安全強度（信頼性）が低下または崩壊すること**を指します。
        *   選択肢ウのように、ハッシュ値が衝突するような入力データの組み合わせ（衝突）を現実的な時間で発見できるアルゴリズムが見つかることは、ハッシュ関数の強度の危殆化（MD5やSHA-1で実際に起きた歴史的な歴史的事実）に該当します。*注意:* 秘密鍵の単なる漏えい（イ）は人為的ミスやセキュリティ管理不足によるものであり、アルゴリズム自体の「危殆化」とは呼びません。
    *   **English:** 
        *   **Cryptographic Compromise (危殆化)** refers to the theoretical erosion of cryptographic algorithm strength due to computational breakthroughs. 
        *   Finding a realistic method to generate identical hash values (collisions) in a hash function directly compromises its underlying integrity. Thus, Option ウ is correct.

---

#### 問12 (Object-Oriented Programming: Polymorphism)
オブジェクト指向プログラミングの特徴のうち，異なるクラスのオブジェクトを同一のインタフェースで操作したときに，操作対象クラスに応じた異なる動作を可能にすることを何と呼ぶか。

*   **選択肢 (Options):**
    *   **ア:** 委譲
    *   **イ:** 継承
    *   **ウ:** コンポジション
    *   **エ:** 多相性 (Polymorphism)

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **多相性 (Polymorphism: ポリモーフィズム)** は、オブジェクト指向の3大要素の1つです。
        *   同じメッセージ（関数呼び出し）を送っても、呼び出すオブジェクトの種類（クラス）によって自動的に動作が切り替わる性質です（例えば、同じ `draw()` 命令でも、円なら円を、四角なら四角を描画するような仕組み）。
    *   **English:** 
        *   **Polymorphism (多相性)** is an OOP concept allowing a unified interface to be implemented differently by distinct derived classes (e.g. executing same `print()` triggers custom outputs based on targeted class attributes).

---

#### 問16 (Data Mining: Market Basket Analysis)
データマイニングの手法の一つであって，POSなどの蓄積データから“一緒に買われる商品”の組合せを発見する分析手法はどれか。

*   **選択肢 (Options):**
    *   **ア:** 3C分析
    *   **イ:** ABC分析
    *   **ウ:** コンジョイント分析
    *   **エ:** マーケットバスケット分析 (Market Basket Analysis)

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **マーケットバスケット分析** は、スーパーやコンビニのPOSデータ（レジの売上データ）を解析し、「ビールを買う人は、おむつも一緒に買う傾向がある」といった **「一緒に買われる商品（バスケット）の組み合わせパターン（相関関係）」** をマイニング（採掘）する、小売業界のクラシックな経営分析手法です。
    *   **English:** 
        *   **Market Basket Analysis** parses retail Point-of-Sale (POS) logs to locate purchasing affinities and correlation patterns (e.g. "shoppers purchasing infant diapers frequently purchase beer concurrently").

---

#### 問18 (Enterprise Strategy: E-Commerce Long Tail)
物販事業において，ロングテールをビジネスとして成功させるために必要な施策はどれか。

*   **選択肢 (Options):**
    *   **ア:** 多くの有名ブランド店が出店するショッピングモールの構築
    *   **イ:** 交通の利便性が高い地域に対する，生活必需品を広く浅く取りそろえた出店計画
    *   **ウ:** 店舗で購入した商品を近隣地域に無償で配送するサービスの実施
    *   **エ:** 豊富な品ぞろえと，在庫コストや配送費用を抑えるための大規模な物流センタの構築や活用

*   **正解 (Correct Answer):** **エ**

*   **詳細解説 (Explanation):**
    *   **日本語:** 
        *   **ロングテール (Long Tail)** とは、売れ行きの遅い多数の「マイナーな（売れ筋でない）商品」の売上合計が、少数の「ヒット商品」の売上合計を上回る、ネット通販（Amazonなど）特有の経済モデルです。
        *   成功させるには、リアル店舗のような売り場（棚スペース）の物理的限界がない広大なインターネット上の仮想店舗を用意し、さらに「広大な品揃え」にかかる膨大な在庫保管コストや配送費を徹底的に削減するための、大規模で効率的な **「物流センター（フルフィルメントセンター）」の構築・自動化** が必要不可欠です（選択肢エ）。
    *   **English:** 
        *   The **Long Tail** economic model thrives in online e-commerce environments where non-hit niche items outnumber mainstream hot products. 
        *   To execute this model profitably, firms must operate high-capacity, highly optimized distribution warehouses to mitigate bulk storage fees and scale shipping transactions smoothly (Option エ).

---

### 📝 終わりに (Conclusion)
これで全65問の網羅が完了しました。
計算問題の解法（MTBF改善後の稼働率や、ネットワーク回線利用率のオーバーヘッド加算、CIDRのホスト数計算など）は、公式の組み立て方を含めて完全に自分の手で計算できるように何度も繰り返し復習しましょう。応援しています！
