

### **Problem 1: Basic Knowledge & Commands**

**(1) Google's Public DNS**

* **Japanese:** ネットワークインターフェース（NIC）にIPアドレスを設定した。ISP（Internet Service Provider）からDNSサーバの情報をもらっていない場合や、もらったDNSサーバの情報を使いたくない場合は、パブリックDNSサーバのIPアドレスを指定すれば良い。GoogleによるパブリックDNSサーバのIPアドレスを答えなさい。
* **English:** You configured an IP address on a network interface (NIC). If you did not receive DNS server information from your ISP, or if you do not want to use it, you can specify a public DNS server IP address. What is the IP address of Google's public DNS server?
* **Answer:** **`8.8.8.8`**
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>` *(You used this when setting up the `nameservers` block in your netplan).*

**(2) Administrator Privileges**

* **Japanese:** 一般ユーザでログインしていて、一時的に管理者権限で処理をしたいときに使用するコマンド（通常、実行したいコマンドの先頭に付加するアルファベット4文字）を答えなさい。
* **English:** What is the command (usually 4 alphabetical characters added to the beginning of the command you want to execute) used when logged in as a general user and you want to temporarily process something with administrator privileges?
* **Answer:** **`sudo`**
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>` *(Used constantly throughout all your files, starting with `sudo vi` and `sudo netplan apply`).*

---

**(3) Ubuntu Execution Commands**
*Write the commands to execute the following in Ubuntu. (You can omit the 'sudo' command).*

**(a) List files and directories**

* **Japanese:** 現在のディレクトリにあるファイル・ディレクトリ一覧を表示する
* **English:** Display a list of files and directories in the current directory.
* **Answer:** **`ls`**
* **Reference:** `<<< out of FILE >>>` *(This is a basic Linux command usually taught in earlier prerequisite courses, not explicitly in the Lesson 1-6 setup slides).*

**(b) Copy a file**

* **Japanese:** 現在のディレクトリにあるtest.txtというファイルをtest2.txtというファイルとしてコピーする
* **English:** Copy the file named `test.txt` in the current directory as a file named `test2.txt`.
* **Answer:** **`cp test.txt test2.txt`**
* **Reference:** `<<< out of FILE >>>` *(Also a prerequisite basic Linux command).*

**(c) Edit a file**

* **Japanese:** 現在のディレクトリにあるファイルtest.txtをviコマンドで編集する
* **English:** Edit the file `test.txt` in the current directory using the `vi` command.
* **Answer:** **`vi test.txt`**
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>` *(Introduced when you had to edit your first network config file).*

**(d) Check service status**

* **Japanese:** smbdというサービスが正常に動いているかどうかを確認する
* **English:** Check if the service named `smbd` is running normally.
* **Answer:** **`systemctl status smbd`**
* **Reference:** `<<< out of FILE >>>` *(Note: You learned the `systemctl status` command in your DHCP and DNS files, but the specific service `smbd` is for a Samba file server, which is NOT in Lessons 1-6).*

**(e) Restart a service**

* **Japanese:** isc-dhcp-serverというサービスを再起動する
* **English:** Restart the service named `isc-dhcp-server`.
* **Answer:** **`systemctl restart isc-dhcp-server`**
* **Reference:** `<<< DHCP_server.pdf >>>` *(Used immediately after configuring your DHCP ranges).*

**(f) Install a package**

* **Japanese:** apache2というパッケージをインストールする
* **English:** Install the package named `apache2`.
* **Answer:** **`apt install -y apache2`** * **Reference:** `<<< ネットワーク応用04-1_www導入.pdf >>>` *(The very first step of Lesson 4).*

**(g) Display IP address information**

* **Japanese:** ネットワークインターフェース（NIC）に割り当てられたIPアドレス等の情報を表示する
* **English:** Display information such as the IP address assigned to a network interface (NIC).
* **Answer:** **`ip a`** * **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>` *(Used to verify if your static IP assignment worked).*

**(h) Apply network settings**

* **Japanese:** ディレクトリ/etc/netplanの中にIPアドレス等の設定ファイル（99-nc2.yaml）を作成したので、その内容をシステムに反映したい
* **English:** You created a configuration file for IP addresses, etc. (`99-nc2.yaml`) in the `/etc/netplan` directory, and want to apply its contents to the system.
* **Answer:** **`netplan apply`**
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>` *(Used to finalize your static IP setup).*

---




---

Here is the complete breakdown for Problem 2, formatted exactly as you requested. It includes the full original Japanese question sentences, English translations, answers, detailed explanations of *why* the answer is correct, and the exact file references.

---

### **Problem 2: Network Concepts & Configurations**

**(1) Automatic IP Protocol**

* **Japanese:** 端末がネットワークに接続するためにはIPアドレスが必要である。IPアドレス等のネットワーク接続情報を自動で割り振るためのプロトコルを何というか。
* **English:** A terminal needs an IP address to connect to a network. What is the protocol used to automatically assign network connection information such as IP addresses?
* **Answer:** **DHCP** (Dynamic Host Configuration Protocol)
* **Explanation:** DHCP automates the process of configuring devices on an IP network. Instead of manually typing in an IP address, subnet mask, and DNS server for every single computer, a DHCP server leases this information out automatically.
* **Reference:** `<<< DHCP_server.pdf >>>` *(This definition is the foundational concept introduced at the beginning of your DHCP lab).*

**(2) DHCP Client IP**

* **Japanese:** （1）のサーバとクライアントがIPアドレスの割り振りのやり取りをしている最中に、クライアントは送信元IPアドレスとして何を使っているか。
* **English:** While the server and client in (1) are exchanging IP address assignments, what does the client use as its source IP address?
* **Answer:** **`0.0.0.0`**
* **Explanation:** When a computer first connects to a network, it does not have an IP address yet. To find the DHCP server, it yells a "DHCP Discover" message to everyone on the network. Because it cannot identify itself with a real IP, it uses the temporary placeholder `0.0.0.0` as its source address.
* **Reference:** `<<< out of FILE >>>` *(While you built a DHCP server in the lab files, this specific detail about the packets used in the initial handshake is theoretical network knowledge, likely taught in a previous prerequisite networking class).*

**(3) Network Connectivity Test**

* **Japanese:** IPアドレスが192.168.100.100の端末に対して、パケットを送信し、応答があるかどうかを確認するために実行するコマンドを答えなさい。
* **English:** What command do you execute to send packets to a terminal with the IP address `192.168.100.100` and check if there is a response?
* **Answer:** **`ping 192.168.100.100`**
* **Explanation:** The `ping` command sends ICMP Echo Request packets to the target IP. If the target machine is turned on and connected, it sends an Echo Reply back, proving that your physical network and routing are working.
* **Reference:** `<<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>` *(You used this repeatedly to test if your Host OS could successfully reach your newly configured virtual machines).*

**(4) Enabling an Apache Website**

* **Japanese:** apache2の設定ファイル（/etc/apache2/sites-available/100-nc.conf）を作成した。このファイルを有効化するためのコマンドを答えなさい。
* **English:** You created an Apache2 configuration file (`/etc/apache2/sites-available/100-nc.conf`). What command do you execute to enable this file?
* **Answer:** **`a2ensite 100-nc.conf`**
* **Explanation:** In Ubuntu, Apache stores all available website configurations in a folder called `sites-available`. To actually turn the site "on," you use the **A**pache**2** **En**able **Site** (`a2ensite`) command, which links it to the active system.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf >>>` *(This command is explicitly taught right after you create your custom VirtualHost configuration).*

**(5) Web Server Security (Directory Listing)**

* **Japanese:** Webサーバの設定で、サーバ内のファイル構成を見せるのは良くないと考えられている。その観点で考えたとき、次のapache2.confの記述内容のうち、どの部分を消去すべきか。消去すべき記述のみを答えなさい。
```text
<Directory /var/www/website1>
Options Indexes FollowSymLinks
AllowOverride None
Require all granted
</Directory>

```


* **English:** In Web server settings, it is considered bad practice to show the file structure within the server to the public. From this perspective, which part of the following `apache2.conf` description should be deleted? Answer only the exact word that should be removed.
* **Answer:** **`Indexes`**
* **Explanation:** If a user visits your website folder and you forget to upload an `index.html` file, the `Indexes` option tells Apache to automatically display a list of all your secret backend files and folders. Deleting this word secures your folder by returning a "Forbidden" error instead.
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf >>>` *(This is explicitly taught when configuring the Directory permissions in the Apache setup).*

**(6) Server Package Identification**

* **Japanese:** 次のパッケージは何のサーバを構築するために使用されるか答えなさい。
* **English:** What kind of servers are the following packages used to build?
* **(a) bind9**
* **Answer:** **DNSサーバ** (DNS Server)
* **Explanation:** BIND9 translates human-readable domain names (like `www.oreore.test`) into IP addresses.
* **Reference:** `<<< ネットワーク応用06_dns1.pdf >>>`


* **(b) isc-dhcp-server**
* **Answer:** **DHCPサーバ** (DHCP Server)
* **Explanation:** This package automatically hands out IP addresses to client machines.
* **Reference:** `<<< DHCP_server.pdf >>>`


* **(c) apache2**
* **Answer:** **Webサーバ** (Web Server)
* **Explanation:** This package handles HTTP requests to display HTML web pages to browsers.
* **Reference:** `<<< ネットワーク応用04-1_www導入.pdf >>>`


了解しました。ご提示いただいたすべての設定コード（ApacheのVirtualHostやDNSのゾーンファイルなど）を省略することなく完全に含めた状態で、元の日本語の問題文、英語の翻訳、解答、詳細な解説、そして第1回〜第6回の授業資料に基づいた参照元（ファイル名とおおよその位置）を作成します。

---

### **Problem 3: Advanced Configuration & Routing**

#### **(1) DHCP Server Configuration (`dhcpd.conf`)**

* **Japanese:** （1）isc-dhcp-server パッケージをインストールしてdhcpd.confを編集することにした。IPアドレスの払い出しの設定を次の条件でおこなう。このとき、dhcpd.conf に追記すべき内容を書きなさい（subnet から始める）。
* サーバもクライアントも10.0.120.0/20のネットワークに所属する
* 払い出すIPアドレス数は10個だけとする
* サーバ自身のIPアドレスは 10.0.120.2に手動で設定
* デフォルトゲートウェイとして10.0.120.1のルータを指定
* DNSサーバとして8.8.8.8を使わせる
* なお、払い出すIP アドレスの範囲は回答者が適切に決めること。


* **English:** (1) You decided to install the `isc-dhcp-server` package and edit `dhcpd.conf`. Configure the IP address assignment with the following conditions. Write the contents that should be added to `dhcpd.conf` (starting with `subnet`).
* Both server and client belong to the `10.0.120.0/20` network.
* The number of IP addresses to be assigned is exactly 10.
* The server's own IP address is manually set to `10.0.120.2`.
* Specify the router at `10.0.120.1` as the default gateway.
* Use `8.8.8.8` as the DNS server.
* Note: The respondent should appropriately determine the range of IP addresses to be assigned.


* **Answer:**

```text
subnet 10.0.112.0 netmask 255.255.240.0 {
    option routers 10.0.120.1;
    option domain-name-servers 8.8.8.8;
    range 10.0.120.10 10.0.120.19;
}

```

* **Explanation:** CIDR表記の `/20` はサブネットマスク `255.255.240.0` に変換されます。また、10.0.120.2を含む `/20` ネットワークの正しいネットワークアドレスは `10.0.112.0` となります（※手書き試験の採点基準によっては `subnet 10.0.120.0` でも部分点がもらえる可能性がありますが、厳密な計算では112.0です）。`option routers` と `option domain-name-servers` は条件通りに指定します。IPアドレスは10個払い出す必要があるため、ルータ（.1）とサーバ（.2）を避けた任意の10個（例：`.10`から`.19`）を `range` に指定します。
* **Reference:** `<<< DHCP_server.pdf, 中盤のdhcpd.conf設定スライド >>>`

---

#### **(2) Apache Web Server Document Root**

* **Japanese:** （2）WebサーバのIPアドレスが192.168.0.1で、apache の設定ファイルに次の記述があるとする。このとき、[http://192.168.0.1/index.htmlにアクセスして表示される](http://192.168.0.1/index.htmlにアクセスして表示される) webページはサーバ内のどこに保存されているか。ファイルの絶対パスで答えなさい。

```text
<VirtualHost *:80>
ServerAdmin tfukuda@apps.kct.ac.jp
DocumentRoot /var/www/html/website1/
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/ac.log combined
</VirtualHost>

```

* **English:** (2) Assume the Web server's IP address is 192.168.0.1, and the Apache configuration file has the following description. When accessing `http://192.168.0.1/index.html`, where is the displayed web page stored on the server? Answer with the absolute path of the file.
* **Answer:** `/var/www/html/website1/index.html`
* **Explanation:** Apacheの設定において、`DocumentRoot`（ドキュメントルート）はWebサイトの基本となるディレクトリ（`/`）がハードディスク上のどこにあるかを指定するものです。この設定ではルートが `/var/www/html/website1/` に設定されているため、ブラウザから `index.html` を要求された場合、サーバはこのディレクトリ内に直接保存されているファイルを探しに行きます。
* **Reference:** `<<< ネットワーク応用04-2_www設定.pdf, 終盤のVirtualHost設定スライド >>>`

---

#### **(3) DNS Record Types**

* **Japanese:** （3）DNS の設定において次の情報を示すために使用されるレコード名を答えなさい。
* **English:** (3) Answer the record names used to indicate the following information in DNS settings.
* **(a) Japanese:** IPアドレスに対応するドメイン名やホスト名を定義するもので逆引きに必要な情報
* **(a) English:** Information necessary for reverse lookup, which defines the domain name or host name corresponding to an IP address.
* **Answer:** **PTR** (Pointer Record)
* **Reference:** `<<< out of FILE >>>` *(逆引き（Reverse Lookup）は試験範囲である第7回の授業で扱われますが、現在提供されている第1回〜第6回のPDF資料の中には記述がありません)。*
* **(b) Japanese:** メールサーバを定義するもの
* **(b) English:** Defines the mail server.
* **Answer:** **MX** (Mail Exchange Record)
* **Reference:** `<<< out of FILE >>>` *(メールサーバの構築は第1回〜第6回の範囲外です)。*
* **(c) Japanese:** ネームサーバを定義するもの
* **(c) English:** Defines the name server.
* **Answer:** **NS** (Name Server Record)
* **Reference:** `<<< ネットワーク応用06_dns1.pdf, 中盤のゾーンファイル設定スライド >>>`



---

#### **(4) DNS Zone File Resolution**

* **Japanese:** （4）権威DNSサーバにおいて、nc2.exampleのゾーン情報が次のように設定されている。このとき、ブラウザで次の（a）～（d）の各URLにアクセスした場合、この権威DNSサーバによって名前解決をすることで得られるIPアドレスを答えなさい。ただし、名前解決が失敗する場合は✕を書きなさい。

```text
$TTL 604800
@ IN SOA ns1.nc2.example. root.localhost. (
2; serial
604800; refresh
86400; retry
2419200; expire
604800 ); negative cache ttl
@ IN NS ns1
@ IN A 10.13.64.1
ns1 IN A 10.13.64.101
www IN A 10.13.64.105
www2 IN CNAME www
news IN A 10.13.64.106

```

(a). [http://www.nc2.example](https://www.google.com/search?q=http://www.nc2.example)
(b). [http://www2.nc2.example](https://www.google.com/search?q=http://www2.nc2.example)
(c). [http://www.news.example](https://www.google.com/search?q=http://www.news.example)
(d). [http://nc2.example](https://www.google.com/search?q=http://nc2.example)

* **English:** (4) In the authoritative DNS server, the zone information for `nc2.example` is set as follows. When accessing each of the following URLs (a) to (d) in a browser, answer the IP address obtained by name resolution by this authoritative DNS server. If name resolution fails, write ✕.
* **(a) Answer:** `10.13.64.105`
* **Explanation:** `www IN A 10.13.64.105` のレコードがあるため、そのままこのIPアドレスに解決されます。


* **(b) Answer:** `10.13.64.105`
* **Explanation:** `www2 IN CNAME www` のレコードにより、`www2` は `www` の別名（エイリアス）として定義されています。したがって、`www` と同じIPアドレスに解決されます。


* **(c) Answer:** `✕`
* **Explanation:** これは引っかけ問題です。このゾーンファイルは `nc2.example` というドメインを管理するためのものです。リクエストされた `www.news.example` は全く別のドメイン空間に属しているため、このサーバでは解決できません。（もし `news.nc2.example` だった場合は `.106` になりますが、`www.news` というレコードも存在しません）。


* **(d) Answer:** `10.13.64.1`
* **Explanation:** ゾーンファイル内において `@` 記号は「起点（オリジン）」、つまりこのゾーン自体のドメイン（`nc2.example`）を指します。`@ IN A 10.13.64.1` と記述されているため、ホスト名（wwwなど）が付かないドメイン名単体でのアクセスは、このIPアドレスに解決されます。




* **Reference:** `<<< ネットワーク応用06_dns1.pdf, 中盤のdb.oreore作成スライド >>>` *(あなたが実際に `db.oreore` ファイルを作成したときと全く同じロジックです)。*

---

#### **(5) Gateway & IPTables (NAPT)**

* **Japanese:** （5）端末にNICが3個（名前は enp0s3、 enp0s8、enp0s9）搭載されており、enp0s3に192.168.100.0/24のネットワーク、enp0s8に192.168.110.0/24のネットワーク、enp0s9に10.13.0.0/16のネットワークがつながっている。次のような挙動をさせたい場合、実行するべき iptables コマンドを2個答えなさい。ただし、「管理者権限での実行」を表すアルファベット4文字は省かなくて良い。
* 192.168.100.0/24から来るパケットは10.13.0.0/16 宛に転送したい。
* 192.168.110.0/24から来るパケットは192.168.100.0/24宛に転送したい。


* **English:** (5) A terminal is equipped with 3 NICs (named enp0s3, enp0s8, enp0s9). The 192.168.100.0/24 network is connected to enp0s3, the 192.168.110.0/24 network to enp0s8, and the 10.13.0.0/16 network to enp0s9. When you want to cause the following behavior, answer the 2 `iptables` commands that should be executed. (Note: You do not need to omit the 4-letter alphabet for administrator execution).
* Forward packets coming from 192.168.100.0/24 to the 10.13.0.0/16 destination.
* Forward packets coming from 192.168.110.0/24 to the 192.168.100.0/24 destination.


* **Answer:**
1. `sudo iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o enp0s9 -j MASQUERADE`
2. `sudo iptables -t nat -A POSTROUTING -s 192.168.110.0/24 -o enp0s3 -j MASQUERADE`


* **Explanation:** ルーティングを行うためのNAPT（MASQUERADE）の設定です。
`-s` オプションは**送信元（source）**のネットワークを指定します。
`-o` オプションは**出力インターフェース（out-interface）**、つまりパケットが出ていく側のNICを指定します。
1つ目の条件では、宛先である `10.13.0.0/16` のネットワークにつながっているのは `enp0s9` なので、そこからパケットを出します。
2つ目の条件では、宛先である `192.168.100.0/24` のネットワークにつながっているのは `enp0s3` なので、そこからパケットを出します。
* **Reference:** `<<< ネットワーク応用05-1_GW.pdf, 終盤のiptables設定スライド >>>` *(Isolated Web Serverのネットワークへのルーティングを設定した際と全く同じコマンド構造です)。*