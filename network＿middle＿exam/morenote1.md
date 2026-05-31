
This is a highly effective way to study, Exz! Breaking it down presentation by presentation ensures there are zero blind spots. Here are 6 new, high-probability practice questions crafted specifically from `ネットワーク応用02-2_serverのIPアドレス.pdf`, targeting the three exact hints your teacher provided.

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: File Permissions**

* **Japanese:** ネットワーク設定ファイル（`60-netc.yaml`）を、ファイルの所有者（root）だけが読み書きできるように権限を変更するコマンドを答えなさい。
* **English:** What command do you execute to change the permissions of the network configuration file (`60-netc.yaml`) so that only the file owner (root) can read and write to it?
* **Answer:** `sudo chmod 600 60-netc.yaml`
* **Explanation (Japanese/English):** 権限を600にすることで、管理者（root）以外のユーザーが誤って設定を変更したり見たりすることを防ぎます。 / Setting permissions to 600 prevents non-admin users from accidentally viewing or modifying the network settings.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 21 >>>`

**Question 2: Detailed Directory Listing**

* **Japanese:** 現在のディレクトリにある、隠しファイルを含めたすべてのファイルの詳細な一覧を表示するコマンドを答えなさい。
* **English:** What command do you execute to display a detailed list of all files in the current directory, including hidden files?
* **Answer:** `ls -la`
* **Explanation (Japanese/English):** `ls` コマンドに `-a` (すべて表示) と `-l` (詳細表示) のオプションを組み合わせることで、ファイルの権限や所有者も確認できます。 / Combining the `-a` (all) and `-l` (long format) options with the `ls` command allows you to check file permissions and owners.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 14 >>>`

**Question 3: Saving in Vim**

* **Japanese:** `vi` コマンドで設定ファイルを編集した後、入力モードから抜け出して、内容を保存して終了するための一連のキー操作を答えなさい。
* **English:** After editing a configuration file with the `vi` command, what sequence of key presses do you use to exit input mode, save the contents, and quit?
* **Answer:** `[ESC]` を押した後、 `[:][w][q][Enter]`
* **Explanation (Japanese/English):** まず `[ESC]` でコマンドモードに戻り、`w` (write = 保存) と `q` (quit = 終了) を同時に実行します。 / First, press `[ESC]` to return to command mode, then execute `w` (write) and `q` (quit) simultaneously.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 16 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 4: DHCP IPv4 Setting**

* **Japanese:** Netplanの設定ファイルにおいて、`dhcp4: true` という項目はどのような意味を持つか答えなさい。
* **English:** In the Netplan configuration file, what does the item `dhcp4: true` mean?
* **Answer:** DHCPサーバからIPv4アドレスを自動でもらう設定。 / A setting to automatically obtain an IPv4 address from a DHCP server.
* **Explanation (Japanese/English):** この設定が `true` の場合、手動で固定IPアドレスを記述する必要はありません。NATネットワークに繋がる `enp0s3` などで使われます。 / If this setting is `true`, there is no need to manually write a static IP address. It is used on interfaces like `enp0s3` that connect to a NAT network.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 20 >>>`

**Question 5: Permission Number Meaning**

* **Japanese:** `chmod 600` というコマンドにおける設定値「6」は、どのような権限の合計値（数字の足し算）を表しているか答えなさい。
* **English:** In the command `chmod 600`, what is the sum of permissions (addition of numbers) represented by the setting value "6"?
* **Answer:** 4（読み込むことができる）+ 2（書き込むことができる）＝ 6 / 4 (can read) + 2 (can write) = 6.
* **Explanation (Japanese/English):** Linuxのファイル権限は、読み込み(4)、書き込み(2)、実行(1)の数字の足し算で表されます。6は「読み書き可能」を意味します。 / Linux file permissions are represented by adding the numbers for read(4), write(2), and execute(1). 6 means readable and writable.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 21 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 6: Static IP Definition**

* **Japanese:** 内部ネットワーク用のインターフェース `enp0s8` に対して、DHCP機能（v4/v6）を無効にし、静的IPアドレスとして `192.168.100.1/24` を割り当てたい。また、IP設定完了を待たずに起動を進めるようにしたい。このとき、設定ファイルに追記すべき内容を書きなさい（`enp0s8:` から始めること）。
* **English:** For the internal network interface `enp0s8`, you want to disable DHCP functions (v4/v6), assign the static IP address `192.168.100.1/24`, and allow the system to boot without waiting for the IP configuration to complete. Write the content that should be added to the config file (starting with `enp0s8:`).
* **Answer:**

```yaml
enp0s8:
  dhcp4: false
  dhcp6: false
  addresses: [192.168.100.1/24]
  optional: true

```

* **Explanation (Japanese/English):** `dhcp4` と `dhcp6` を `false` にして自動取得を止め、`addresses` に指定のIPアドレスをブラケット `[]` で囲んで記述します。起動を止めない設定は `optional: true` です。YAMLファイルでは空白スペースのインデント（字下げ）が非常に重要です。 / Set `dhcp4` and `dhcp6` to `false` to stop auto-assignment, and write the specified IP address in brackets `[]` under `addresses`. The setting to not halt boot is `optional: true`. Blank space indentation is extremely important in YAML files.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Pages 19-20 >>>`





This is exactly how you ace an exam, Exz! By extracting every single possible question from each specific slide deck, you are building an impenetrable cheat sheet.

I have analyzed `ネットワーク応用04-1_www導入.pdf` (Introduction to WWW Server). This lesson transitions you from basic network routing into actual Web Server deployment.

Here are **7 high-probability practice questions** extracted directly from this specific file, perfectly categorized into your teacher's three hints!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Web Server Installation**

* **Japanese:** WWWサーバの機能を提供するパッケージ（`apache2`）をシステムにインストールするためのコマンドを答えなさい。（管理者権限で実行すること）
* **English:** What command do you execute to install the package that provides WWW server functionality (`apache2`) to the system? (Execute with administrator privileges).
* **Answer:** `sudo apt install apache2` *(Note: `sudo apt install -y apache2` is also correct).*
* **Explanation (Japanese/English):** UbuntuでWebサーバを構築するための最も標準的なソフトウェアであるApacheをインストールします。 / Installs Apache, the most standard software for building a Web server on Ubuntu.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 12 >>>`

**Question 2: Service Verification**

* **Japanese:** インストールした `apache2` サービスが正常に稼働しているか（`active (running)` の状態か）を確認するためのコマンドを答えなさい。
* **English:** What command do you execute to check if the installed `apache2` service is operating normally (in the `active (running)` state)?
* **Answer:** `systemctl status apache2`
* **Explanation (Japanese/English):** サービスが正常に起動しているか、エラーで停止していないかを確認する重要なコマンドです。 / An important command to verify if the service has started normally or if it has stopped due to an error.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 13 >>>`

**Question 3: Navigating to the Web Directory**

* **Japanese:** Webページとして公開されるファイル（`index.html` など）が保存されているデフォルトのディレクトリへ移動するためのコマンドを答えなさい。
* **English:** What command do you execute to navigate to the default directory where files published as Web pages (such as `index.html`) are saved?
* **Answer:** `cd /var/www/html`
* **Explanation (Japanese/English):** Apacheの初期設定では、このディレクトリの中にあるファイルがWebブラウザに送信されます。 / In Apache's default configuration, the files inside this directory are sent to the Web browser.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 14 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 4: The Document Root**

* **Japanese:** Webサーバの設定において、`/var/www/html` というディレクトリパスはネットワーク上においてどのような意味（役割）を持つか答えなさい。
* **English:** In Web server configuration, what is the meaning (role) of the directory path `/var/www/html` on the network?
* **Answer:** Webブラウザからアクセスされた際に表示されるファイル群を置く場所（ドキュメントルート）である。 / It is the location (Document Root) where files to be displayed when accessed by a Web browser are placed.
* **Explanation (Japanese/English):** ユーザーが `http://192.168.200.1` にアクセスしたとき、Apacheは自動的にこのディレクトリの中にある `index.html` を読み込みます。 / When a user accesses `http://192.168.200.1`, Apache automatically reads the `index.html` inside this directory.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 14 >>>`

**Question 5: HTML Structure Tags**

* **Japanese:** Webページを記述する `index.html` ファイルにおいて、`<h1>` ～ `</h1>` というタグで囲まれた部分は、どのような意味を持ってWebブラウザに表示されるか答えなさい。
* **English:** In the `index.html` file that describes a Web page, what meaning does the part enclosed by the `<h1>` ~ `</h1>` tags have when displayed in a Web browser?
* **Answer:** ページ内の一番大きな見出し（Heading 1）として表示される。 / It is displayed as the largest heading (Heading 1) on the page.
* **Explanation (Japanese/English):** HTML言語において、`h1` は最上位の見出しを意味し、通常は太く大きな文字でレンダリングされます。 / In HTML, `h1` means the top-level heading and is usually rendered in bold, large text.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 17 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 6: Static IP Setup for the Isolated Web Server**

* **Japanese:** 新しいWebサーバ（`another_company`）を内部ネットワークに配置するため、IPアドレスを `192.168.200.1/24` に固定したい。 `/etc/netplan/` 配下の設定ファイルの `enp0s8:` の下に追記すべき内容を書きなさい。
* **English:** To place the new Web server (`another_company`) on the internal network, you want to fix the IP address to `192.168.200.1/24`. Write the content that should be added under `enp0s8:` in the config file under `/etc/netplan/`.
* **Answer:**

```yaml
enp0s8:
  dhcp4: false
  addresses: [192.168.200.1/24]

```

* **Explanation (Japanese/English):** `another_company` サーバは隔離されたネットワーク（netc2）に配置するため、DHCPを無効化し、指定されたIPアドレスを手動で割り当てます。 / Because the `another_company` server is placed in an isolated network (netc2), DHCP is disabled, and the specified IP address is manually assigned.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 8 >>>`

**Question 7: Editing the Web Page File**

* **Japanese:** デフォルトのWebページ（`index.html`）を編集し、ブラウザのタブに表示されるタイトルを「Welcome Web」にしたい。`<head>` と `</head>` の間に記述すべき内容を書きなさい。
* **English:** You want to edit the default Web page (`index.html`) so that the title displayed on the browser tab is "Welcome Web". Write the content that should be described between `<head>` and `</head>`.
* **Answer:**

```html
<title>Welcome Web</title>

```

* **Explanation (Japanese/English):** HTMLの `<title>` タグは、Webブラウザのタブやウィンドウの上部に表示されるページ名を定義します。 / The HTML `<title>` tag defines the page name displayed at the top of the Web browser's tab or window.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf, Page 17 >>>`

---

You have fully conquered the `04-1` setup slides! Your cheat sheet is getting incredibly robust. Drop the next PDF whenever you are ready!


This is a massive power move for your exam prep, Exz! You are systematically extracting every single drop of knowledge from these slides.

I have thoroughly analyzed `ネットワーク応用04-2_www設定.pdf` (WWW Server Settings). This lesson is highly technical and focuses entirely on Apache configuration files (`100-nc.conf` and `apache2.conf`).

I made sure to **exclude** the questions that were already on the past exam (like `a2ensite` and deleting `Indexes`). Here are **8 brand-new, high-probability practice questions** extracted directly from this specific file, perfectly categorized into your teacher's three hints!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Disabling a Website**

* **Japanese:** デフォルトのWebサイト設定ファイル（`000-default.conf`）を無効化するためのコマンドを答えなさい。
* **English:** What command do you execute to disable the default website configuration file (`000-default.conf`)?
* **Answer:** `sudo a2dissite 000-default.conf`
* **Explanation (Japanese/English):** `a2ensite` (Enable) の逆で、**A**pache**2** **Dis**able **Site** を意味するコマンドです。新しいサイト（100-nc.conf）を動かすために、古いデフォルト設定をオフにする必要があります。 / The opposite of `a2ensite` (Enable), meaning **A**pache**2** **Dis**able **Site**. To run the new site (100-nc.conf), you must turn off the old default settings.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 9 >>>`

**Question 2: Reloading Configuration Smoothly**

* **Japanese:** Apacheの新しい設定ファイル（サイトの有効化や無効化）をシステムに反映させる際、サービスを完全に停止させずに設定だけを再読み込みさせるコマンドを答えなさい。
* **English:** When applying new Apache configuration files (enabling or disabling sites) to the system, what command do you execute to reload the settings without completely stopping the service?
* **Answer:** `sudo systemctl reload apache2`
* **Explanation (Japanese/English):** `restart` はサーバを一度完全に止めて再起動しますが、`reload` はサーバを動かしたまま設定ファイルだけを読み込み直すため、アクセス中のユーザーに迷惑がかかりません。 / While `restart` completely stops and starts the server, `reload` reads the configuration files again while keeping the server running, causing no disruption to active users.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 10 >>>`

**Question 3: Creating the Document Root**

* **Japanese:** 新しいWebページのデータを保存するために、`/var/www/` の下に `website1` という新しいディレクトリ（フォルダ）を作成するコマンドを答えなさい。
* **English:** What command do you execute to create a new directory (folder) named `website1` under `/var/www/` to store the new Web page data?
* **Answer:** `sudo mkdir /var/www/website1`
* **Explanation (Japanese/English):** `mkdir` (Make Directory) コマンドを使って、Apacheが読みに行くための新しい空のフォルダをハードディスク上に作成します。 / Uses the `mkdir` (Make Directory) command to create a new empty folder on the hard drive for Apache to read from.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 18 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 4: Apache Directory Structure**

* **Japanese:** `/etc/apache2/` ディレクトリの中にある `sites-available` と `sites-enabled` の役割の違いを簡潔に答えなさい。
* **English:** Briefly explain the difference in roles between the `sites-available` and `sites-enabled` directories within `/etc/apache2/`.
* **Answer:** `sites-available` は作成した設定ファイルの「置き場」であり、`sites-enabled` はその中で実際に「有効化された（動いている）」設定ファイルが置かれる場所である。
* **Explanation (Japanese/English):** 設定ファイルを作っただけでは動きません。`a2ensite` コマンドを打つと、`available`（利用可能）から `enabled`（有効化済み）にリンクが張られて初めてWebサーバとして機能します。 / Just creating a config file doesn't make it run. When you use the `a2ensite` command, a link is created from `available` to `enabled`, and only then does it function as a Web server.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 2 >>>`

**Question 5: Log File Directives**

* **Japanese:** VirtualHost設定ファイル（100-nc.confなど）に記述されている `ErrorLog` という項目はどのような役割を持つか答えなさい。
* **English:** What role does the item `ErrorLog` written in the VirtualHost configuration file (like 100-nc.conf) play?
* **Answer:** Webサーバのエラーに関する記録（ログ）を保存するファイルの場所を指定する役割。 / Specifies the location of the file where Web server error records (logs) are saved.
* **Explanation (Japanese/English):** サーバに障害が起きた際、管理者はこの `ErrorLog` で指定されたファイル（通常は `/var/log/apache2/error.log`）を見て原因を調査します。 / When the server crashes, administrators check the file specified by `ErrorLog` to investigate the cause.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 5 >>>`

**Question 6: Security and Access Permissions**

* **Japanese:** `apache2.conf` の `<Directory>` ブロック内に記述される `Require all granted` という項目はどのような意味を持つか答えなさい。
* **English:** What does the item `Require all granted` written within the `<Directory>` block of `apache2.conf` mean?
* **Answer:** すべてのアクセス（すべてのユーザーやIPアドレスからの要求）を許可するという意味。 / It means allowing all access (requests from all users and IP addresses).
* **Explanation (Japanese/English):** この記述があることで、外部のPCやスマートフォンからあなたのWebサーバ内のファイルを見ることができるようになります。逆に制限をかける場合は `Require ip 192.168...` のように書きます。 / This description allows external PCs or smartphones to view the files in your Web server. If you want to restrict it, you would write something like `Require ip...`
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 14 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 7: VirtualHost Administrator Email**

* **Japanese:** `100-nc.conf` （VirtualHost設定ファイル）において、サーバ管理者の連絡先メールアドレスを `student@kct.ac.jp` に設定したい。記述すべき1行を書きなさい。
* **English:** In `100-nc.conf` (VirtualHost configuration file), you want to set the server administrator's contact email address to `student@kct.ac.jp`. Write the single line that should be described.
* **Answer:**

```text
ServerAdmin student@kct.ac.jp

```

* **Explanation (Japanese/English):** Webサーバで重大なエラー画面（500 Internal Server Errorなど）が表示された際、訪問者に表示される管理者の連絡先を指定します。 / Specifies the administrator's contact information shown to visitors when a critical error screen occurs.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 5 & 7 >>>`

**Question 8: Defining Directory Rules (`apache2.conf`)**

* **Japanese:** `apache2.conf` において、`/var/www/website1` というディレクトリに対するアクセス権限等のルールを新たに定義したい。このルールの「開始」と「終了」を表すためのタグ（記述）を2行書きなさい（中身の設定は除く）。
* **English:** In `apache2.conf`, you want to newly define rules such as access permissions for the directory `/var/www/website1`. Write the two lines of tags (descriptions) that indicate the "start" and "end" of this rule (excluding the internal settings).
* **Answer:**

```text
<Directory /var/www/website1>
</Directory>

```

* **Explanation (Japanese/English):** HTMLタグのように、Apacheの設定でも特定のフォルダに対してルールを適用する場合は、`<Directory>` と `</Directory>` でルールブロックを囲む必要があります。 / Just like HTML tags, when applying rules to specific folders in Apache settings, you must enclose the rule block with `<Directory>` and `</Directory>`.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, Page 14 >>>`




This is the perfect way to master the material, Exz! By isolating exactly what happens in each slide deck, you are building a complete mental map of the network.

I have thoroughly analyzed **`ネットワーク応用05-1_GW.pdf` (Gateway Server Preparation)**.

This specific file is all about adding a **3rd Network Interface Card (NIC)** to your `ubuntu_server` so it can physically connect to the new `another_company` network. (Note: The actual *routing/iptables* commands were in `05-2`, so this file strictly focuses on interface setup!).

Here are **6 brand-new, high-probability practice questions** extracted directly from this specific file, perfectly categorized into your teacher's three hints, ensuring we don't repeat the exact phrasing from the past exam!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Identifying New Hardware**

* **Japanese:** VirtualBoxで新しいネットワークアダプタ（Adapter 3）を追加してサーバを起動した後、Ubuntu上でその新しいインターフェースに割り当てられた**論理名（enp0s9など）とMACアドレス**を確認するためのコマンドを答えなさい。
* **English:** After adding a new network adapter (Adapter 3) in VirtualBox and booting the server, what command do you execute in Ubuntu to check the **logical name (like enp0s9) and MAC address** assigned to that new interface?
* **Answer:** `ip a` *(or `ip link`)*
* **Explanation (Japanese/English):** 物理的な設定を終えた後、OSが新しいNICをどう認識しているか（名前は何か）を調べるために必須のステップです。過去問にも出た重要コマンドですが、ここでは「新しいNICの名前を探す」という目的で使われます。 / After finishing physical settings, this step is essential to find out how the OS recognizes the new NIC (what its name is). It's an important command from the past exam, but used here specifically to discover the new NIC's name.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf , Page 9 >>>`

**Question 2: Specific Connectivity Testing**

* **Japanese:** `ubuntu_server` から新しいWebサーバに対して通信確認を行う際、パケットを無限に送り続けるのではなく、**ちょうど4回だけ**送信して自動的に終了させるコマンドを答えなさい（宛先IPは 192.168.200.1 とする）。
* **English:** When performing a connectivity check from `ubuntu_server` to the new Web server, what command do you execute to send **exactly 4 packets** and stop automatically, rather than sending packets infinitely? (Assume the destination IP is 192.168.200.1).
* **Answer:** `ping 192.168.200.1 -c 4`
* **Explanation (Japanese/English):** `-c` (count) オプションは、通信テストをすばやく終わらせるために非常に便利です。 / The `-c` (count) option is extremely useful for finishing a communication test quickly.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf , Page 17 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 3: Netplan Versioning**

* **Japanese:** `/etc/netplan/` 以下の設定ファイル（YAML形式）の一番最後の行に書かれている `version: 2` という記述は、どのような意味を持つか答えなさい。
* **English:** What is the meaning of the `version: 2` description written on the very last line of the configuration file (YAML format) under `/etc/netplan/`?
* **Answer:** Netplan（ネットワーク設定ツール）の設定ファイルの記述ルール（フォーマット）のバージョン2を使用していることを意味する。 / It means that version 2 of the configuration file writing rules (format) for Netplan (the network configuration tool) is being used.
* **Explanation (Japanese/English):** この記述がないと、システムがYAMLファイルを正しく解釈できない場合があります。 / Without this description, the system might not interpret the YAML file correctly.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf , Page 12 >>>`

**Question 4: CIDR Notation Meaning**

* **Japanese:** 新しいインターフェースの設定項目において `addresses: [192.168.200.2/24]` と記述した。この末尾の `/24` はネットワークにおいてどのような意味を持つか、具体的に答えなさい。
* **English:** In the new interface configuration, it is written as `addresses: [192.168.200.2/24]`. What specific meaning does the `/24` at the end have in the network?
* **Answer:** サブネットマスクが24ビット（255.255.255.0）であることを意味している。 / It means that the subnet mask is 24 bits long (255.255.255.0).
* **Explanation (Japanese/English):** IPアドレスのうち、左から24ビット分が「ネットワーク部」であり、残りが「ホスト部」であることをシステムに教えています。 / It tells the system that the first 24 bits from the left of the IP address are the "Network part", and the remainder is the "Host part".
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf , Page 12 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 5: Adding a New Interface Block**

* **Japanese:** `ubuntu_server` に新しいネットワークインターフェース `enp0s9` が追加された。DHCP機能を無効にし、静的IPアドレスとして `192.168.200.2/24` を割り当てたい。また、起動時のネットワーク待ちをスキップする設定も入れたい。既存の `enp0s8` の設定の下に追記すべき内容を正確な字下げ（インデント）で書きなさい。
* **English:** A new network interface `enp0s9` was added to `ubuntu_server`. You want to disable the DHCP function, assign `192.168.200.2/24` as a static IP address, and include the setting to skip waiting for the network during boot. Write the exact content with correct indentation that should be added below the existing `enp0s8` configuration.
* **Answer:**

```yaml
            enp0s9:
              dhcp4: false
              addresses: [192.168.200.2/24]
              optional: true

```

* **Explanation (Japanese/English):** ゲートウェイサーバを構築する際、複数のネットワークカード（NIC）を1つのNetplanファイル内で管理します。`enp0s8` と全く同じインデント階層に揃えて記述することが極めて重要です。 / When building a gateway server, you manage multiple Network Interface Cards (NICs) within a single Netplan file. It is extremely important to write it aligned with the exact same indentation level as `enp0s8`.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf , Page 12 >>>`

**Question 6: Netplan Parent Structure**

* **Japanese:** `enp0s8` や `enp0s9` などの個別のインターフェース設定は、YAMLファイルの階層において、特定の項目の下にぶら下がる形で記述しなければならない。その親となる2つの項目名（階層順）を書きなさい。
* **English:** Individual interface settings like `enp0s8` and `enp0s9` must be described hanging under specific items in the YAML file hierarchy. Write the names of the two parent items (in hierarchical order).
* **Answer:**

```yaml
network:
  ethernets:

```

* **Explanation (Japanese/English):** どんなにインターフェースが増えても、必ず一番上に `network:` があり、その次に有線LANを意味する `ethernets:` が来ます。その下に各NIC（enp0s3, enp0s8, enp0s9...）が並びます。 / No matter how many interfaces you add, `network:` is always at the very top, followed by `ethernets:` (meaning wired LAN). Below that, each NIC (enp0s3, enp0s8, enp0s9...) is listed.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf , Page 12 >>>`

---

These questions target the exact mechanics of preparing your machine to act as a router! Whenever you are ready, throw the next file at me (probably `05-2_GW.pdf`, where the real routing magic happens!).




This is fantastic, Exz! You are systematically extracting the core engineering concepts from each slide deck.

I have deeply analyzed **`ネットワーク応用05-2_GW.pdf` (Gateway Server Packet Forwarding)**. This is a critical lesson where you turned a standard Ubuntu server into an actual network router by manipulating kernel parameters and NAT tables.

The past exam (`中間1ネットワーク.pdf`) asked you to write the full `iptables` command for this section. Because we already covered that, I have extracted **5 brand-new, highly probable questions** that focus on the *other* crucial steps in this specific slide deck that your teacher might test you on!

Here is your custom practice exam strictly from the `05-2_GW.pdf` file.

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Applying Kernel Variables**

* **Japanese:** `/etc/sysctl.conf` を編集してIPv4フォワーディングを有効化した後、システムを再起動せずにその設定を直ちにカーネルに反映させるコマンドを答えなさい。
* **English:** After editing `/etc/sysctl.conf` to enable IPv4 forwarding, what command do you execute to apply the settings immediately to the kernel without rebooting the system?
* **Answer:** `sudo sysctl -p`
* **Explanation (Japanese/English):** 設定ファイルを `vi` で書き換えただけではシステムは動かず、このコマンドを打つことで初めてルータとしての転送機能がメモリに読み込まれます。 / Just rewriting the configuration file with `vi` does not change the system's behavior; running this command is what actually loads the router forwarding function into memory.
* **Reference:** `<<< ネットワーク応用05-2_GW.pdf, Page 8 >>>`

**Question 2: Checking Firewall Status**

* **Japanese:** パケット転送がファイアウォールにブロックされていないか確認するため、Ubuntuの標準ファイアウォール（UFW）が現在有効（active）か無効（inactive）か、動作状態を調べるコマンドを答えなさい。
* **English:** To ensure packet forwarding isn't being blocked by the firewall, what command do you execute to check the operational status of Ubuntu's standard firewall (UFW) to see if it is active or inactive?
* **Answer:** `sudo ufw status`
* **Explanation (Japanese/English):** ネットワークが繋がらないトラブルシューティングの第一歩として、OS内蔵のファイアウォールが邪魔をしていないか確認する重要なコマンドです。 / As a first step in troubleshooting network connectivity, this is an important command to check if the OS's built-in firewall is interfering.
* **Reference:** `<<< ネットワーク応用05-2_GW.pdf, Page 14 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 3: IP Forwarding Meaning**

* **Japanese:** `/etc/sysctl.conf` に記述されている `net.ipv4.ip_forward=1` という設定は、ネットワークにおいてどのような意味（役割）を持つか答えなさい。
* **English:** What is the meaning (role) in the network of the setting `net.ipv4.ip_forward=1` described in `/etc/sysctl.conf`?
* **Answer:** サーバに到着したパケットを、別のネットワークへ転送（ルーティング）する機能を有効にするという意味。 / It means enabling the function to forward (route) packets that arrive at the server to another network.
* **Explanation (Japanese/English):** 通常のPCは自分宛て以外のパケットを受け取ると破棄（ドロップ）しますが、この値を `1`（True）にすることで、パケットを隣のネットワークへ橋渡しする「ルータ」として振る舞うようになります。 / A normal PC discards (drops) packets not destined for itself, but setting this value to `1` (True) makes it behave as a "router" that bridges packets to the adjacent network.
* **Reference:** `<<< ネットワーク応用05-2_GW.pdf, Page 6 & 7 >>>`

**Question 4: IPTables MASQUERADE Action**

* **Japanese:** ゲートウェイ構築のために実行する NAPT設定コマンド（`iptables -t nat ...`）の末尾にある `-j MASQUERADE` という部分は、パケットに対してどのような処理を行う指示か答えなさい。
* **English:** What process does the `-j MASQUERADE` part at the end of the NAPT configuration command (`iptables -t nat ...`) instruct the system to perform on the packets?
* **Answer:** 送信元のIPアドレスを、パケットが出ていくインターフェースのIPアドレスに自動的に書き換える（IPマスカレード/NAPT）指示。 / An instruction to automatically rewrite the source IP address to the IP address of the outgoing interface (IP Masquerade/NAPT).
* **Explanation (Japanese/English):** これを行わないと、Webサーバ（another_company）はパケットの返信先（192.168.100.x）を知らないため、通信が成立しません。MASQUERADEによって、あたかもゲートウェイサーバ自身が通信しているように偽装します。 / Without this, the Web server (another_company) doesn't know where to reply (192.168.100.x), so communication fails. MASQUERADE disguises the packet so it looks like the gateway server itself is communicating.
* **Reference:** `<<< ネットワーク応用05-2_GW.pdf, Page 12 & 15 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 5: Enabling the Router Function**

* **Japanese:** Ubuntuサーバをゲートウェイとして機能させるために、設定ファイル `/etc/sysctl.conf` の中にある特定の行の先頭の `#`（コメントアウト）を削除して有効化しなければならない。その有効化すべき1行を正確に書きなさい。
* **English:** To make the Ubuntu server function as a gateway, you must delete the `#` (comment out) at the beginning of a specific line in the `/etc/sysctl.conf` configuration file to enable it. Write that one exact line that should be enabled.
* **Answer:**

```text
net.ipv4.ip_forward=1

```

* **Explanation (Japanese/English):** 設定ファイルにおいて `#` は「この行は無効なメモである」ことを意味します。`#` を消すことで、システムがこの指示を正式な命令として読み込むようになります。 / In configuration files, `#` means "this line is an inactive memo". By removing the `#`, the system reads this instruction as an official command.
* **Reference:** `<<< ネットワーク応用05-2_GW.pdf, Page 7 >>>`

---

This perfectly wraps up Lesson 5! You now know exactly how to write the NAPT rule (from the past exam) AND exactly how to configure the kernel to allow forwarding (from these new questions).

We have one massive slide deck left: `06_dns1.pdf`. Let me know when you are ready to conquer the final boss of the midterm!



This is the grand finale, Exz! You have reached **Lesson 6 (`ネットワーク応用06_dns1.pdf`)**, which is the most complex configuration of the entire midterm scope.

Because the past exam only scratched the surface of DNS (asking about the `bind9` package name and basic zone file resolution), there is a **massive** amount of highly testable material left in this slide deck.

I have created **8 brand-new, advanced practice questions** extracted directly from the `06_dns1.pdf` file, strictly avoiding the exact questions from the past exam.

Here is your ultimate DNS practice test!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Global Configuration Syntax Check**

* **Japanese:** `named.conf.options` や `named.conf.local` などのBIND9全体の設定ファイルに、構文エラー（タイポやセミコロンの抜けなど）がないかを確認するためのコマンドを答えなさい。
* **English:** What command do you execute to check for syntax errors (like typos or missing semicolons) in the global BIND9 configuration files such as `named.conf.options` and `named.conf.local`?
* **Answer:** `named-checkconf`
* **Explanation (Japanese/English):** DNSサーバは1つの「;（セミコロン）」が抜けているだけで起動しなくなります。サービスを再起動する前に、このコマンドでエラーがないかテストすることが鉄則です。何も表示されなければエラーなし（合格）です。 / A DNS server will fail to start if even a single ";" (semicolon) is missing. It is a strict rule to test for errors with this command before restarting the service. If nothing is printed to the screen, there are no errors (Pass).
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 37 >>>`

**Question 2: Zone File Syntax Check**

* **Japanese:** 作成したゾーンファイル（`db.oreore`）の記述内容が、DNSのルールとして正しいかどうかをチェックするためのコマンドを答えなさい（ドメイン名は `oreore.test` とする）。
* **English:** What command do you execute to check if the contents written in the created zone file (`db.oreore`) are correct according to DNS rules? (Assume the domain name is `oreore.test`).
* **Answer:** `named-checkzone oreore.test /etc/bind/db.oreore`
* **Explanation (Japanese/English):** `named-checkconf` が「全体設定」をチェックするのに対し、こちらは特定の「ゾーンファイルの中身」をチェックします。成功すると `OK` と表示されます。 / While `named-checkconf` checks the "global settings," this command checks the specific "contents of a zone file." If successful, it displays `OK`.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 50 >>>`

**Question 3: Name Resolution Testing**

* **Japanese:** DNSサーバの設定完了後、クライアントマシン（xubuntu_client）から `www.oreore.test` のIPアドレスを問い合わせて、正しく名前解決ができるかテストするためのコマンドを答えなさい。
* **English:** After completing the DNS server setup, what command do you execute from the client machine (xubuntu_client) to query the IP address of `www.oreore.test` and test if name resolution works correctly?
* **Answer:** `dig www.oreore.test` *(Note: `nslookup www.oreore.test` is also acceptable).*
* **Explanation (Japanese/English):** DNSサーバが正しく機能しているかを確認するための最も標準的なコマンドです。ANSWER SECTIONにIPアドレスが返ってくれば成功です。 / This is the most standard command to verify if the DNS server is functioning correctly. If an IP address is returned in the ANSWER SECTION, it is a success.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 51 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 4: Forwarding Unknown Queries**

* **Japanese:** `named.conf.options` に記述する `forwarders { 8.8.8.8; };` という設定は、DNSサーバにおいてどのような挙動を引き起こすか答えなさい。
* **English:** What behavior does the setting `forwarders { 8.8.8.8; };` written in `named.conf.options` cause in the DNS server?
* **Answer:** 自分のゾーンファイルに書かれていないドメイン（google.comなど）の問い合わせを受けた際、その質問を外部のDNSサーバ（この場合はGoogleの8.8.8.8）へ転送して代わりに調べてもらう挙動。 / When receiving a query for a domain not written in its own zone file (like google.com), it forwards the question to an external DNS server (in this case, Google's 8.8.8.8) to look it up on its behalf.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 40 >>>`

**Question 5: Query Access Control**

* **Japanese:** `named.conf.options` に記述する `allow-query { localhost; netc2; };` という項目は、どのようなセキュリティ上の意味を持つか答えなさい。
* **English:** What security meaning does the item `allow-query { localhost; netc2; };` written in `named.conf.options` have?
* **Answer:** このDNSサーバに対して名前解決の質問（クエリ）を送ることができるネットワークを、自分自身（localhost）と内部ネットワーク（netc2）だけに制限するという意味。 / It means restricting the networks that are allowed to send name resolution questions (queries) to this DNS server to only itself (localhost) and the internal network (netc2).
* **Explanation (Japanese/English):** 無関係な外部からのDNS問い合わせを拒否することで、サーバへの攻撃や負荷を防ぐための必須設定です。 / This is an essential setting to prevent attacks and load on the server by rejecting DNS queries from unrelated external sources.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 41 >>>`

**Question 6: The Trailing Dot (FQDN)**

* **Japanese:** ゾーンファイル（`db.oreore`）の中で、`ns1.oreore.test.` のようにドメイン名の最後に付加する「`.` （ドット）」は、DNSにおいてどのような重要な意味を持つか答えなさい。
* **English:** In the zone file (`db.oreore`), what important meaning does the "`.`" (dot) added to the end of a domain name, such as `ns1.oreore.test.`, have in DNS?
* **Answer:** 絶対ドメイン名（FQDN）の終端（ルート）であることを示している。 / It indicates the absolute root (termination) of a Fully Qualified Domain Name (FQDN).
* **Explanation (Japanese/English):** この最後のドットを忘れると、BIND9はそれを「相対名」と勘違いし、自動的に `ns1.oreore.test.oreore.test` のようにお尻に勝手にドメインを付け足してしまい、エラーになります。 / If you forget this trailing dot, BIND9 mistakes it for a "relative name" and automatically appends the domain to the end, resulting in `ns1.oreore.test.oreore.test`, causing an error.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 45 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 7: Declaring the Zone**

* **Japanese:** 新しいドメイン `oreore.test` をこのサーバで管理するために、`/etc/bind/named.conf.local` にゾーンの宣言を追記したい。このゾーンのタイプをマスター（master）とし、ファイルパスを `"/etc/bind/db.oreore"` と指定する記述を正確に書きなさい。
* **English:** To manage the new domain `oreore.test` on this server, you want to add a zone declaration to `/etc/bind/named.conf.local`. Write the exact description that sets the zone type to `master` and specifies the file path as `"/etc/bind/db.oreore"`.
* **Answer:**

```text
zone "oreore.test" {
    type master;
    file "/etc/bind/db.oreore";
};

```

* **Explanation (Japanese/English):** BIND9に「俺はこのドメインの責任者（master）だ。データはこのファイル（file）に書いてあるから読み込んでくれ」と教えるための設定です。括弧の終わりの `;` を忘れると致命的エラーになります。 / This setting tells BIND9, "I am the authority (master) for this domain. The data is written in this file, so read it." Forgetting the `;` at the end of the bracket results in a fatal error.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 31 >>>`

**Question 8: Broadcasting the New DNS via DHCP**

* **Japanese:** 構築したDNSサーバ（IP: `192.168.200.2`）の存在を、クライアントマシンに自動的に教えたい。DHCPサーバの設定ファイル（`/etc/dhcp/dhcpd.conf`）において、既存のGoogle DNS（8.8.8.8）の代わりに、自作のDNSサーバを指定するよう書き換えるべき1行を書きなさい。
* **English:** You want to automatically inform client machines of the existence of the constructed DNS server (IP: `192.168.200.2`). In the DHCP server configuration file (`/etc/dhcp/dhcpd.conf`), write the one line that should be rewritten to specify your own DNS server instead of the existing Google DNS (8.8.8.8).
* **Answer:**

```text
option domain-name-servers 192.168.200.2;

```

* **Explanation (Japanese/English):** 第3回では `8.8.8.8` をクライアントに配っていましたが、今回は自分が作った `192.168.200.2` に質問させるため、DHCPの設定を更新して配布し直す必要があります。 / In Lesson 3, you distributed `8.8.8.8` to clients, but this time you must update the DHCP settings to distribute `192.168.200.2` so clients ask the server you built.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 34 >>>`

---

Exz, you now have a comprehensive, slide-by-slide, command-by-command study guide covering every single lesson. If you print these practice questions out or write the exact config blocks onto your A4 cheat sheet, you are going to destroy this midterm!










I have generated 9 brand-new, high-probability questions strictly focusing on the three hints your teacher gave you.

Here is your custom practice exam.

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Service Installation**

* **Japanese:** DNSサーバの機能をもつパッケージ（bind9と関連ツール）をインストールするコマンドを答えなさい。（管理者権限で実行すること）
* **English:** What command do you execute to install the DNS server package (`bind9` and its utilities)? (Execute with administrator privileges).
* **Answer:** `sudo apt install -y bind9 bind9-utils`
* **Explanation (Japanese/English):** DNSサーバを構築するためのBIND9パッケージ本体と、操作用のツール群をインストールします。 / Installs the core BIND9 package and its management tools to build a DNS server.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 15 >>>`

**Question 2: Specific Network Testing**

* **Japanese:** IPアドレス192.168.200.2に対して、通信確認用のパケットを**ちょうど4回だけ**送信して終了させるコマンドを答えなさい。
* **English:** What command do you execute to send exactly 4 connectivity test packets to the IP address `192.168.200.2` and then stop?
* **Answer:** `ping 192.168.200.2 -c 4`
* **Explanation (Japanese/English):** 通常の `ping` は手動で止める（Ctrl+C）まで続きますが、`-c`（count）オプションを指定することで送信回数を制限できます。 / Standard `ping` runs indefinitely until stopped manually. The `-c` (count) option limits the exact number of packets sent.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf, Page 14 >>>`

**Question 3: Safe Shutdown**

* **Japanese:** ターミナルから仮想マシン（サーバ）を安全にシャットダウンするためのコマンドを答えなさい。（管理者権限で実行すること）
* **English:** What command do you execute from the terminal to safely shut down the virtual machine (server)? (Execute with administrator privileges).
* **Answer:** `sudo shutdown now`
* **Explanation (Japanese/English):** システムを直ちに（now）安全に終了させるコマンドです。 / Safely halts and turns off the system immediately (now).
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 26 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 4: Netplan Configuration**

* **Japanese:** `/etc/netplan` 以下の設定ファイルにある `optional: true` という項目はどのような意味（役割）を持つか答えなさい。
* **English:** What is the meaning (role) of the `optional: true` item written in the configuration files under `/etc/netplan`?
* **Answer:** IPアドレスの設定完了を待たずにシステムの起動を進める設定。 / A setting that allows the system boot process to continue without waiting for the IP address configuration to finish.
* **Explanation (Japanese/English):** これがないと、ネットワークに繋がっていない時にシステムの起動が一時停止してしまい、待ち時間が発生します。 / Without this, the system boot will pause and wait if the network is disconnected, causing long boot delays.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf, Page 20 >>>`

**Question 5: DNS Zone Definitions**

* **Japanese:** `/etc/bind/named.conf.local` において、`type master;` という記述はどのような意味を持つか答えなさい。
* **English:** What does the description `type master;` mean in `/etc/bind/named.conf.local`?
* **Answer:** このサーバが、そのゾーンの情報を管理している大元のファイル（マスターデータ）を持っていることを表す。 / Indicates that this specific server holds the original, authoritative master data file for the zone.
* **Explanation (Japanese/English):** 他のサーバからコピーされた情報（slave）ではなく、このサーバ自身がオリジナルを定義していることを宣言します。 / It declares that the server defines the original data, rather than holding a copied cache (slave) from another server.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 30 >>>`

**Question 6: DNS Security / Interface Binding**

* **Japanese:** `/etc/bind/named.conf.options` において、`listen-on { 192.168.200.1; };` と記述した場合、どのような挙動になるか答えなさい。
* **English:** If you write `listen-on { 192.168.200.1; };` in `/etc/bind/named.conf.options`, what behavior will occur?
* **Answer:** IPv4でのDNSの問い合わせを、192.168.200.1のIPアドレス（インターフェース）だけで待ち受けるようになる。 / The DNS server will only listen for and accept IPv4 DNS queries on the specific `192.168.200.1` IP address interface.
* **Explanation (Japanese/English):** サーバが複数のIPを持っている場合、特定のネットワークからしかDNS要求を受け付けないように制限し、セキュリティを高めます。 / If the server has multiple IPs, this restricts it to only accept requests from a specific network side, improving security.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 41 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 7: Netplan Static IP Addition**

* **Japanese:** `60-netc.yaml` を編集し、新しく追加したインターフェース `enp0s9` に対して、DHCP機能（v4/v6）を無効にし、静的IPアドレスとして `192.168.200.2/24` を割り当てたい。追記すべき内容を書きなさい（`enp0s9:` から始めること）。
* **English:** You want to edit `60-netc.yaml` to disable DHCP (v4/v6) and assign the static IP address `192.168.200.2/24` to the newly added interface `enp0s9`. Write the content that should be added (starting with `enp0s9:`).
* **Answer:**

```yaml
enp0s9:
  dhcp4: false
  dhcp6: false
  addresses: [192.168.200.2/24]

```

* **Explanation (Japanese/English):** インターフェース名の下に、DHCPの無効化指示と、ブラケット `[]` で囲んだCIDR表記のIPアドレスを正確なインデント（空白スペース）で記述します。 / Below the interface name, write the DHCP disable commands and the CIDR IP address wrapped in brackets `[]` using exact space indentation.
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf, Page 12 >>>`

**Question 8: DNS Access Control List (ACL)**

* **Japanese:** `named.conf.options` の冒頭に、`192.168.200.0/24` のネットワークを `netc2` という名前のグループとして定義したい。記述すべき内容を書きなさい。
* **English:** At the beginning of `named.conf.options`, you want to define the `192.168.200.0/24` network as a group named `netc2`. Write the content that should be described.
* **Answer:**

```text
acl "netc2" { 192.168.200.0/24; };

```

* **Explanation (Japanese/English):** `acl` (Access Control List) を使うことで、ネットワークの範囲に変数のような名前をつけることができます。末尾のセミコロン `;` を忘れないように注意してください。 / Using `acl` allows you to give a variable-like name to a network range. Be careful not to forget the trailing semicolons `;`.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 35 >>>`

**Question 9: DNS Aliasing (CNAME)**

* **Japanese:** ゾーンファイル（`db.oreore`）において、`www2`（www2.oreore.test）にアクセスした際、`www`（www.oreore.test）と同じIPアドレスに誘導するための別名（エイリアス）レコードを1行で記述しなさい。
* **English:** In the zone file (`db.oreore`), write a single-line alias record so that when someone accesses `www2` (www2.oreore.test), they are directed to the same IP address as `www` (www.oreore.test).
* **Answer:**

```text
www2    IN    CNAME    www

```

* **Explanation (Japanese/English):** CNAME（Canonical Name）レコードは、別のホスト名へのショートカットを作ります。これによりIPアドレスを重複して書く必要がなくなります。 / The CNAME record creates a shortcut to another hostname, which prevents you from having to write the exact same IP address multiple times.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, Page 27 >>>`



You are building an incredible study resource, Exz! Breaking down `DHCP_server.pdf` guarantees you will be ready for any variation of the DHCP questions your teacher might throw at you.

Since the past exam already asked about the definition of DHCP, the client's `0.0.0.0` IP, the `systemctl restart` command, and writing the full `subnet` block, I have designed **6 brand-new, high-probability questions** that focus on the *other* highly testable details in this slide deck.

Here is your custom practice exam strictly from the `DHCP_server.pdf` file!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Package List Update**

* **Japanese:** パッケージをインストールする前に、システムのパッケージ情報を最新の状態に更新（アップデート）するためのコマンドを答えなさい。
* **English:** Before installing a package, what command do you execute to update the system's package information to the latest state?
* 
**Answer:** `sudo apt update` 


* 
**Explanation (Japanese/English):** ソフトウェアをインストールする前に行う必須の準備コマンドです。 / This is a mandatory preparation command executed before installing software.


* **Reference:** `<<< DHCP_server.pdf, Page 11 >>>`

**Question 2: DHCP Server Installation**

* **Japanese:** DHCPサーバの機能を提供するパッケージ（`isc-dhcp-server`）をインストールするためのコマンドを答えなさい。（管理者権限で実行すること）
* **English:** What command do you execute to install the package that provides DHCP server functionality (`isc-dhcp-server`)? (Execute with administrator privileges).
* 
**Answer:** `sudo apt install -y isc-dhcp-server`  *(Note: omitting `-y` is usually also accepted).*


* 
**Explanation (Japanese/English):** IPアドレスの自動配布を行うためのソフトウェア本体をインターネットからダウンロードしてインストールします。 / Downloads and installs the main software from the internet to automatically distribute IP addresses.


* **Reference:** `<<< DHCP_server.pdf, Page 11 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 3: Gateway Distribution**

* **Japanese:** `dhcpd.conf` に記述する `option routers 192.168.100.1;` という項目は、クライアントに対してどのような情報を配布する役割を持つか答えなさい。
* **English:** What information does the item `option routers 192.168.100.1;` written in `dhcpd.conf` distribute to the clients?
* 
**Answer:** クライアントが外部ネットワークと通信するためのデフォルトゲートウェイ（ルータ）のIPアドレス。 / The IP address of the default gateway (router) that clients use to communicate with external networks.


* 
**Explanation (Japanese/English):** この設定により、クライアントは自分宛て以外の通信をどこに投げればよいか（192.168.100.1）を自動的に学習します。 / This setting allows clients to automatically learn where to send communications not destined for themselves (192.168.100.1).


* **Reference:** `<<< DHCP_server.pdf, Page 16 >>>`

**Question 4: DHCP Port Numbers**

* **Japanese:** DHCPの通信において、DHCPサーバ側が待ち受けているポート番号と、DHCPクライアント側が通信に使用するポート番号をそれぞれ答えなさい。
* **English:** In DHCP communication, what are the port numbers used by the DHCP server to listen, and the port number used by the DHCP client to communicate, respectively?
* 
**Answer:** サーバ: 67番, クライアント: 68番  / Server: Port 67, Client: Port 68.


* 
**Explanation (Japanese/English):** ネットワークの基礎知識として、どのポートを使ってIPアドレスの要求と割り当てが行われるかを示す重要な設定値です。 / As basic network knowledge, these are important setting values that indicate which ports are used to request and assign IP addresses.


* **Reference:** `<<< DHCP_server.pdf, Page 5 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 5: Activating Authoritative Mode**

* **Japanese:** このDHCPサーバをネットワーク内の公式な（権威ある）サーバとして動作させるため、設定ファイル（`dhcpd.conf`）の特定の行にある `#`（コメントアウト）を削除して有効化しなければならない。その有効化すべき1行を正確に書きなさい。
* **English:** To make this DHCP server operate as the official (authoritative) server in the network, you must delete the `#` (comment out) on a specific line in the configuration file (`dhcpd.conf`) to enable it. Write that exact one line that should be enabled.
* **Answer:**

```text
authoritative;

```



* 
**Explanation (Japanese/English):** `#` を消すことで、システムがこの指示をメモではなく正式な設定として読み込むようになります。末尾のセミコロン `;` を忘れないようにしてください。 / By removing the `#`, the system reads this instruction as a formal setting rather than a memo. Do not forget the semicolon `;` at the end.


* **Reference:** `<<< DHCP_server.pdf, Page 14 >>>`

**Question 6: Defining the IP Range**

* **Japanese:** クライアントに自動配布するIPアドレスの範囲を `192.168.100.101` から `192.168.100.150` に設定したい。`dhcpd.conf` の `subnet` ブロック内に記述すべき内容を1行で書きなさい。
* **English:** You want to set the range of IP addresses automatically distributed to clients from `192.168.100.101` to `192.168.100.150`. Write the one line that should be described within the `subnet` block of `dhcpd.conf`.
* **Answer:**

```text
range 192.168.100.101 192.168.100.150;

```



* 
**Explanation (Japanese/English):** 過去問ではブロック全体を書かせましたが、この1行（`range`）だけをピンポイントで問われる可能性も非常に高いです。 / While the past exam asked you to write the whole block, there is a very high probability you will be asked specifically for this single line (`range`).


* **Reference:** `<<< DHCP_server.pdf, Page 16 >>>`





Welcome back, Exz! It is great to see you staying consistent with your midterm preparation. Moving directly into Lesson 7 is a smart move, especially since Reverse DNS (逆引き) introduces some very specific formatting rules that teachers love to test on.

Since you uploaded the new `ネットワーク応用07-1_dns2.pdf` file, I have analyzed the slides and extracted **5 brand-new, high-probability practice questions** focused entirely on the Reverse Lookup concepts.

Here is your custom practice exam for Lesson 7!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Testing Reverse Lookup**

* **Japanese:** クライアントマシンのターミナルから、IPアドレス `192.168.200.1` に対応するホスト名（ドメイン名）を調べる（逆引きをテストする）コマンドを答えなさい。
* **English:** What command do you execute from the client machine's terminal to look up the hostname (domain name) corresponding to the IP address `192.168.200.1` (to test reverse lookup)?
* **Answer:** `nslookup 192.168.200.1`
* **Explanation (Japanese/English):** 正引き（ドメイン名からIPを調べる）も逆引き（IPからドメイン名を調べる）も、同じ `nslookup` または `dig` コマンドでテストできます。引数にIPアドレスを直接渡すのがポイントです。 / Both forward lookup (finding IP from domain) and reverse lookup (finding domain from IP) can be tested using the same `nslookup` or `dig` command. The key is passing the IP address directly as the argument.
* **Reference:** `<<< ネットワーク応用07-1_dns2.pdf, Page 23 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 2: PTR Record Function**

* **Japanese:** DNSのゾーンファイルに記述される `PTR` レコードは、ネットワークにおいてどのような役割を持つか答えなさい。
* **English:** What role does the `PTR` record described in the DNS zone file play in the network?
* **Answer:** IPアドレスからホスト名（ドメイン名）へ変換する「逆引き」の役割を持つ。 / It has the role of "reverse lookup," converting an IP address to a hostname (domain name).
* **Explanation (Japanese/English):** Aレコードの真逆の動きをします。実社会では、迷惑メール（スパム）の送信元が本当に実在する信頼できるサーバかを確かめるためなどに使われます。 / It does the exact opposite of an A record. In the real world, it is often used to verify if the sender of an email (spam check) is a real, trustworthy server.
* **Reference:** `<<< ネットワーク応用07-1_dns2.pdf, Page 7 & 8 >>>`

**Question 3: Reverse Zone Naming Convention**

* **Japanese:** `named.conf.local` に記述するゾーン名が `200.168.192.in-addr.arpa` となっている場合、このゾーンはどのネットワークアドレスに対する逆引きを管理しているか答えなさい。
* **English:** If the zone name written in `named.conf.local` is `200.168.192.in-addr.arpa`, which network address does this zone manage the reverse lookup for?
* **Answer:** `192.168.200.0/24`
* **Explanation (Japanese/English):** 逆引きのゾーン名は、ネットワークアドレスの数字（192.168.200）を逆順（200.168.192）に並べ替え、最後に `.in-addr.arpa` をつけるという特別なルール（慣例）があります。 / Reverse lookup zone names have a special rule (convention) where you take the network address numbers (192.168.200), **reverse their order (200.168.192)**, and append `.in-addr.arpa` to the end.
* **Reference:** `<<< ネットワーク応用07-1_dns2.pdf, Page 14 & 18 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 4: Writing the PTR Record**

* **Japanese:** 逆引き用のゾーンファイル（`db.200.168.192.rev`）において、IPアドレスのホスト部が `1` のマシン（192.168.200.1）のホスト名が `ns1.oreore.test.` であることを定義したい。ファイルに追記すべき1行を書きなさい。
* **English:** In the reverse lookup zone file (`db.200.168.192.rev`), you want to define that the machine with the host part `1` of the IP address (192.168.200.1) has the hostname `ns1.oreore.test.`. Write the one line that should be added to the file.
* **Answer:** 
```text
1 IN PTR ns1.oreore.test.
```

* **Explanation (Japanese/English):** ゾーン名で既にネットワーク部（192.168.200）は宣言されているため、レコードの先頭にはIPアドレスの残り（ホスト部である `1`）だけを書きます。また、末尾の `.`（ドット）を忘れないように注意してください。 / Because the network part (192.168.200) is already declared in the zone name, you only write the remainder of the IP address (the host part, `1`) at the beginning of the record. Also, be careful not to forget the trailing `.` (dot).
* **Reference:** `<<< ネットワーク応用07-1_dns2.pdf, Page 15 >>>`

**Question 5: Registering the Reverse Zone**
* **Japanese:** `192.168.200.0/24` ネットワークの逆引きゾーンを有効にするため、`/etc/bind/named.conf.local` にゾーンの宣言を追記したい。ゾーン名とファイルパス（`/etc/bind/db.200.168.192.rev`）を指定する記述を正確に書きなさい。
* **English:** To enable the reverse lookup zone for the `192.168.200.0/24` network, you want to add a zone declaration to `/etc/bind/named.conf.local`. Write the exact description specifying the zone name and the file path (`/etc/bind/db.200.168.192.rev`).
* **Answer:**
```text
zone "200.168.192.in-addr.arpa" {
    type master;
    file "/etc/bind/db.200.168.192.rev";
};

```

* **Explanation (Japanese/English):** 正引きの時と文法は全く同じですが、ゾーン名が `200.168.192.in-addr.arpa` と長くなるため、スペルミスに気をつけてください。括弧の後の `;` も必須です。 / The syntax is exactly the same as forward lookup, but since the zone name `200.168.192.in-addr.arpa` is long, be careful of spelling mistakes. The `;` after the bracket is also required.
* **Reference:** `<<< ネットワーク応用07-1_dns2.pdf, Page 18 >>>`

---

Here are the high-probability practice questions extracted directly from `ネットワーク応用07-2_cachedns.pdf` (Caching DNS Server). This slide deck focuses on configuring `ubuntu_server` to act as a middleman (cache) for DNS queries.

Since we are wrapping up the midterm material, these questions strictly target the new caching concepts and DHCP modifications not covered in previous sections!

---

### **Section 1: What commands to execute? (◯◯するにはどのようなコマンドを実行？)**

**Question 1: Restarting DHCP to Apply DNS Changes**

* **Japanese:** クライアントに配布するDNSサーバのIPアドレスを変更した後、その新しい設定をシステムに反映させるためにDHCPサービスを再起動するコマンドを答えなさい。
* **English:** What command do you execute to restart the DHCP service to apply the new settings after changing the DNS server IP address distributed to clients?
* **Answer:** `sudo systemctl restart isc-dhcp-server`

* **Explanation (Japanese/English):** `dhcpd.conf` を書き換えただけではクライアントに新しいIPは配られません。このコマンドを実行して初めてキャッシュDNSサーバの情報が有効になります。 / Just rewriting `dhcpd.conf` does not distribute the new IP to clients. The caching DNS server information only becomes effective after executing this command.


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 10 >>>`

**Question 2: Verifying Caching DNS Operation**

* **Japanese:** クライアントマシンのターミナルから `www.oreore.test` の名前解決を行い、キャッシュDNSサーバからの「非権威の回答」が得られるか確認するためのコマンドを答えなさい。
* **English:** What command do you execute from the client machine's terminal to resolve the name `www.oreore.test` and confirm if a "Non-authoritative answer" is obtained from the caching DNS server?
* **Answer:** `nslookup www.oreore.test`

* **Explanation (Japanese/English):** クライアントが正しくキャッシュDNSサーバ（192.168.100.1）に問い合わせを行えているかをテストするための必須コマンドです。 / This is the essential command to test whether the client is correctly querying the caching DNS server (192.168.100.1).


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 13 >>>`

---

### **Section 2: What do the items in the config files mean? (設定ファイルに書いてある項目の意味は？)**

**Question 3: Enabling Recursive Queries**

* **Japanese:** `named.conf.options` における `recursion yes;` という項目はどのような意味を持つか答えなさい。
* **English:** What does the item `recursion yes;` mean in `named.conf.options`?
* **Answer:** 問い合わせの答えがわからないときに別のDNSサーバへ再度問い合わせするかどうか（再帰問い合わせ）を許可する設定。 / A setting that allows the server to query another DNS server again (recursive query) when it does not know the answer to a query.


* **Explanation (Japanese/English):** キャッシュDNSサーバは自分自身で答えを持っていないため、この設定を `yes` にして外部の権威サーバに答えを探しに行かせる必要があります。 / Because a caching DNS server does not have the answers itself, this setting must be `yes` to let it go look for the answer from an external authoritative server.


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 7 >>>`

**Question 4: Understanding "Non-authoritative answer"**

* **Japanese:** クライアントで `nslookup` を実行した際、結果に表示される `Non-authoritative answer:`（非権威の回答）は、ネットワークにおいてどのような事実を示しているか答えなさい。
* **English:** When running `nslookup` on a client, what fact in the network does `Non-authoritative answer:` displayed in the results indicate?
* **Answer:** わたしは権威サーバじゃないけどね！という意味であり、そのドメインの情報を直接管理している権威サーバではなく、キャッシュDNSサーバが代理で回答したことを示している。 / It means "I am not an authoritative server!", indicating that a caching DNS server answered on behalf of the authoritative server that directly manages the domain's information.


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 13 >>>`

**Question 5: Caching DNS Architectural Difference**

* **Japanese:** キャッシュDNSサーバを構築する際、権威DNSサーバの構築とは異なり「作成が不要」となるファイルは何か答えなさい。
* **English:** When building a caching DNS server, what file is "not required to be created" unlike when building an authoritative DNS server?
* **Answer:** ゾーンファイル（`db.oreore` など） / Zone files (like `db.oreore`).


* **Explanation (Japanese/English):** キャッシュDNSサーバは自分でドメイン情報を管理するわけではないため、ゾーンファイルの作成や `named.conf.local` への記述は不要です。 / Because a caching DNS server does not manage domain information itself, creating zone files or writing to `named.conf.local` is unnecessary.


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 6 >>>`

---

### **Section 3: What should be written in the config files? (設定ファイルに何を書く？)**

**Question 6: Changing the DHCP DNS Distribution**

* **Japanese:** DHCPサーバ（`ubuntu_server`）の設定において、クライアントに配布するDNSサーバを、権威サーバからキャッシュDNSサーバ（`192.168.100.1`）に変更したい。`/etc/dhcp/dhcpd.conf` のオプション行をどのように書き換えるべきか書きなさい。
* **English:** In the DHCP server (`ubuntu_server`) settings, you want to change the DNS server distributed to clients from the authoritative server to the caching DNS server (`192.168.100.1`). Write how the option line in `/etc/dhcp/dhcpd.conf` should be rewritten.
* **Answer:**

```text
option domain-name-servers 192.168.100.1;

```

* **Explanation (Japanese/English):** クライアントに「これからは自分自身（192.168.100.1）をDNSとして使いなさい」と教えるための非常に重要な変更です。 / This is a crucial change to tell the clients, "From now on, use me (192.168.100.1) as your DNS."


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 10 >>>`

**Question 7: Setting the Forwarder Destination**

* **Japanese:** キャッシュDNSサーバが、自分ではわからない問い合わせを受けた際、それを権威DNSサーバ（IP: `192.168.200.1`）へ転送して調べてもらうようにしたい。`named.conf.options` に追記すべき内容を書きなさい。
* **English:** When the caching DNS server receives a query it doesn't know, you want it to forward the query to the authoritative DNS server (IP: `192.168.200.1`) to look it up. Write the content that should be added to `named.conf.options`.
* **Answer:**

```text
forwarders {192.168.200.1;};

```

* **Explanation (Japanese/English):** 再帰問い合わせ（Recursion）を行う際の「問い合わせ先」を指定する設定です。 / This setting specifies the "destination to query" when performing recursive queries.


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 7 & 8 >>>`

**Question 8: Restricting Recursive Queries**

* **Japanese:** `named.conf.options` において、内部ネットワーク（`netc1`）と自分自身（`localhost`）からのみ、再帰問い合わせ（代理での問い合わせ）を許可する設定を書きなさい。
* **English:** In `named.conf.options`, write the setting that allows recursive queries (querying on behalf of others) only from the internal network (`netc1`) and itself (`localhost`).
* **Answer:**

```text
allow-recursion {netc1; localhost;};

```

* **Explanation (Japanese/English):** 外部の無関係なネットワークからの再帰問い合わせを許可すると、DNSアンプ攻撃などのサイバー攻撃に悪用される危険があるため、許可する範囲を絞ることが重要です。 / Allowing recursive queries from unrelated external networks poses a risk of being abused for cyberattacks like DNS amplification, so it is important to restrict the allowed scope.


* **Reference:** `<<< ネットワーク応用07-2_cachedns.pdf, Page 7 & 8 >>>`