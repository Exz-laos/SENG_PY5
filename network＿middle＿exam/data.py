q_1_1 = """1. (1) ネットワークインターフェース (NIC) にIPアドレスを設定した。ISP (Internet Service Provider) からDNSサーバの情報をもらっていない場合や、もらったDNSサーバの情報を使いたくない場合は、パブリックDNSサーバのIPアドレスを指定すれば良い。GoogleによるパブリックDNSサーバのIPアドレスを答えなさい。"""

q_1_2 = """1. (2) 一般ユーザでログインしていて、一時的に管理者権限で処理をしたいときに使用するコマンド(通常、実行したいコマンドの先頭に付加するアルファベット4文字)を答えなさい。"""

q_1_3_a = """1. (3)(a) Ubuntu において次のことを実施する場合のコマンドを書きなさい。現在のディレクトリにあるファイル・ディレクトリ一覧を表示する"""

q_1_3_b = """1. (3)(b) Ubuntu において次のことを実施する場合のコマンドを書きなさい。現在のディレクトリにあるtest.txtというファイルをtest2.txtというファイルとしてコピーする"""

q_1_3_c = """1. (3)(c) Ubuntu において次のことを実施する場合のコマンドを書きなさい。現在のディレクトリにあるファイルtest.txtをviコマンドで編集する"""

q_1_3_d = """1. (3)(d) Ubuntu において次のことを実施する場合のコマンドを書きなさい。smbdというサービスが正常に動いているかどうかを確認する"""

q_1_3_e = """1. (3)(e) Ubuntu において次のことを実施する場合のコマンドを書きなさい。isc-dhcp-serverというサービスを再起動する"""

q_1_3_f = """1. (3)(f) Ubuntu において次のことを実施する場合のコマンドを書きなさい。apache2というパッケージをインストールする"""

q_1_3_g = """1. (3)(g) Ubuntu において次のことを実施する場合のコマンドを書きなさい。ネットワークインターフェース (NIC) に割り当てられたIPアドレス等の情報を表示する"""

q_1_3_h = """1. (3)(h) Ubuntu において次のことを実施する場合のコマンドを書きなさい。ディレクトリ/etc/netplanの中にIPアドレス等の設定ファイル (99-nc2.yaml) を作成したので、その内容をシステムに反映したい"""

q_2_1 = """2. (1) 端末がネットワークに接続するためにはIPアドレスが必要である。IPアドレス等のネットワーク接続情報を自動で割り振るためのプロトコルを何というか。"""

q_2_2 = """2. (2) (1) のサーバとクライアントがIPアドレスの割り振りのやり取りをしている最中に、クライアントは送信元IPアドレスとして何を使っているか。"""

q_2_3 = """2. (3) IPアドレスが192.168.100.100の端末に対して、パケットを送信し、応答があるかどうかを確認するために実行するコマンドを答えなさい。"""

q_2_4 = """2. (4) apache2の設定ファイル (/etc/apache2/sites-available/100-nc.conf) を作成した。このファイルを有効化するためのコマンドを答えなさい。"""

q_2_5 = """2. (5) Webサーバの設定で、サーバ内のファイル構成を見せるのは良くないと考えられている。その観点で考えたとき、次のapache2.confの記述内容のうち、どの部分を消去すべきか。消去すべき記述のみを答えなさい。 
```text
<Directory /var/www/website1> 
Options Indexes FollowSymLinks 
AllowOverride None 
Require all granted 
</Directory>
```
"""

q_2_6 = """2. (6) 次のパッケージは何のサーバを構築するために使用されるか答えなさい。
```text
(a) bind9
(b) isc-dhcp-server
(c) apache2
```"""

q_3_1 = """3. (1) isc-dhcp-server パッケージをインストールしてdhcpd.confを編集することにした。IPアドレスの払い出しの設定を次の条件でおこなう。このとき、dhcpd.conf に追記すべき内容を書きなさい (subnet から始める)。 
```text
・ サーバもクライアントも10.0.120.0/20のネットワークに所属する 
・ 払い出すIPアドレス数は10個だけとする 
・ サーバ自身のIPアドレスは10.0.120.2に手動で設定 
・ デフォルトゲートウェイとして10.0.120.1のルータを指定 
・ DNSサーバとして8.8.8.8を使わせる 
```
なお、払い出すIP アドレスの範囲は回答者が適切に決めること。
"""

q_3_2 = """3. (2) WebサーバのIPアドレスが192.168.0.1で、apacheの設定ファイルに次の記述があるとする。このとき、http://192.168.0.1/index.htmlにアクセスして表示される webページはサーバ内のどこに保存されているか。ファイルの絶対パスで答えなさい。 
```text
<VirtualHost *:80> 
ServerAdmin tfukuda@apps.kct.ac.jp 
DocumentRoot /var/www/html/website1/ 
ErrorLog ${APACHE_LOG_DIR}/error.log 
CustomLog ${APACHE_LOG_DIR}/ac.log combined 
</VirtualHost>
```
"""

q_3_3 = """3. (3) DNSの設定において次の情報を示すために使用されるレコード名を答えなさい。 
```text
(a) IPアドレスに対応するドメイン名やホスト名を定義するもので逆引きに必要な情報 
(b) メールサーバを定義するもの 
(c) ネームサーバを定義するもの
```
"""

q_3_4 = """3. (4) 権威DNSサーバにおいて、nc2.exampleのゾーン情報が次のように設定されている。このとき、ブラウザで次の (a) ~ (d) の各URLにアクセスした場合、この権威DNSサーバによって名前解決をすることで得られるIPアドレスを答えなさい。ただし、名前解決が失敗する場合は×を書きなさい。 
```text
$TTL 604800 
@ IN SOA ns1.nc2.example. root.localhost. ( 
2; serial 
604800; refresh 
86400; retry 
2419200; expire 
604800); negative cache ttl 
@ IN NS ns1 
@ IN A 10.13.64.1 
ns1 IN A 10.13.64.101 
www IN A 10.13.64.105 
www2 IN CNAME www 
news IN A 10.13.64.106 
```
```text
(a). http://www.nc2.example 
(b). http://www2.nc2.example 
(c). http://www.news.example 
(d). http://nc2.example
```
"""

q_3_5 = """3. (5) 端末にNICが3個 (名前はenp0s3、enp0s8、enp0s9) 搭載されており、enp0s3に192.168.100.0/24のネットワーク、enp0s8に192.168.110.0/24のネットワーク、enp0s9に10.13.0.0/16のネットワークがつながっている。次のような挙動をさせたい場合、実行するべき iptables コマンドを2個答えなさい。ただし、「管理者権限での実行」を表すアルファベット4文字は省かなくて良い。 
```text
・ 192.168.100.0/24から来るパケットは10.13.0.0/16 宛に転送したい。 
・ 192.168.110.0/24から来るパケットは192.168.100.0/24宛に転送したい。
```
"""

flashcard_data = {
    q_1_1: "Answer: 8.8.8.8\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>",
    q_1_2: "Answer: sudo\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>",
    q_1_3_a: "Answer: ls\n\nReference: <<<< out of FILE >>>",
    q_1_3_b: "Answer: cp test.txt test2.txt\n\nReference: <<<< out of FILE >>>",
    q_1_3_c: "Answer: vi test.txt\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>",
    q_1_3_d: "Answer: systemctl status smbd\n\nReference: <<<<< out of FILE >>>",
    q_1_3_e: "Answer: systemctl restart isc-dhcp-server\n\nReference: <<< DHCP_server.pdf >>>",
    q_1_3_f: "Answer: apt install -y apache2\n\nReference: <<< ネットワーク応用04-1_www導入.pdf >>>",
    q_1_3_g: "Answer: ip a\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>",
    q_1_3_h: "Answer: netplan apply\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>",
    q_2_1: "Answer: DHCP (Dynamic Host Configuration Protocol)\n\nExplanation: DHCPは、手動で入力する代わりに、IPアドレス等の設定を自動で割り振ります。\nReference: <<< DHCP_server.pdf >>>",
    q_2_2: "Answer: 0.0.0.0\n\nExplanation: クライアントはIPアドレスをまだ持っていないため、仮の0.0.0.0を使用します。\nReference: <<<< out of FILE >>>",
    q_2_3: "Answer: ping 192.168.100.100\n\nExplanation: pingコマンドはICMP Echo Requestを送り、ネットワーク接続を確認します。\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>",
    q_2_4: "Answer: a2ensite 100-nc.conf\n\nExplanation: sites-availableにある設定を有効化(a2ensite)します。\nReference: <<< ネットワーク応用04-2_www設定.pdf >>>",
    q_2_5: "Answer: Indexes\n\nExplanation: Indexesオプションを消去することで、ファイル構成が自動で表示されるのを防ぎます。\nReference: <<< ネットワーク応用04-2_www設定.pdf >>>",
    q_2_6: "(a) DNSサーバ (DNS Server)\n(b) DHCPサーバ (DHCP Server)\n(c) Webサーバ (Web Server)\n\nReference: <<< ネットワーク応用06_dns1.pdf >>>, <<< DHCP_server.pdf >>>, <<< ネットワーク応用04-1_www導入.pdf >>>",
    q_3_1: """Answer: 
```text
subnet 10.0.112.0 netmask 255.255.240.0 {
    option routers 10.0.120.1;
    option domain-name-servers 8.8.8.8;
    range 10.0.120.10 10.0.120.19;
}
```

Explanation: /20 はサブネットマスク 255.255.240.0 に変換され、ネットワークアドレスは 10.0.112.0 となります。10個のIPをルータ(.1)とサーバ(.2)を避けてrangeで指定します。
Reference: <<< DHCP_server.pdf >>>""",
    q_3_2: "Answer: /var/www/html/website1/index.html\n\nExplanation: DocumentRoot が /var/www/html/website1/ に設定されているため、サーバはこのディレクトリ内に直接保存されているファイルを探しに行きます。\nReference: <<< ネットワーク応用04-2_www設定.pdf >>>",
    q_3_3: "Answer:\n(a) PTR (Pointer Record)\n(b) MX (Mail Exchange Record)\n(c) NS (Name Server Record)",
    q_3_4: "Answer:\n(a) 10.13.64.105 (www IN A のレコード)\n(b) 10.13.64.105 (www2 IN CNAME www によりwwwと同じ)\n(c) x (news.exampleは全く別のドメイン空間)\n(d) 10.13.64.1 (@ IN A 10.13.64.1 よりドメイン単体でのアクセス)\n\nReference: <<< ネットワーク応用06_dns1.pdf >>>",
    q_3_5: "Answer:\n1. sudo iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o enp0s9 -j MASQUERADE\n2. sudo iptables -t nat -A POSTROUTING -s 192.168.110.0/24 -o enp0s3 -j MASQUERADE\n\nExplanation: -sは送信元ネットワーク、-oは出力インターフェースを指定します。\nReference: <<< ネットワーク応用05-1_GW.pdf >>>"
}

english_translations = {
    q_1_1: {
        "question": "1. (1) You configured an IP address on a network interface (NIC). If you did not receive DNS server information from your ISP, or if you do not want to use it, you can specify a public DNS server IP address. What is the IP address of Google's public DNS server?",
        "answer": "Answer: 8.8.8.8\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>> (You used this when setting up the nameservers block in your netplan)."
    },
    q_1_2: {
        "question": "1. (2) What is the command (usually 4 alphabetical characters added to the beginning of the command you want to execute) used when logged in as a general user and you want to temporarily process something with administrator privileges?",
        "answer": "Answer: sudo\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_3_a: {
        "question": "1. (3)(a) Write the commands to execute the following in Ubuntu. Display a list of files and directories in the current directory.",
        "answer": "Answer: ls\n\nReference: <<<< out of FILE >>>"
    },
    q_1_3_b: {
        "question": "1. (3)(b) Write the commands to execute the following in Ubuntu. Copy the file named test.txt in the current directory as a file named test2.txt.",
        "answer": "Answer: cp test.txt test2.txt\n\nReference: <<<< out of FILE >>>"
    },
    q_1_3_c: {
        "question": "1. (3)(c) Write the commands to execute the following in Ubuntu. Edit the file test.txt in the current directory using the vi command.",
        "answer": "Answer: vi test.txt\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_3_d: {
        "question": "1. (3)(d) Write the commands to execute the following in Ubuntu. Check if the service named smbd is running normally.",
        "answer": "Answer: systemctl status smbd\n\nReference: <<<<< out of FILE >>>"
    },
    q_1_3_e: {
        "question": "1. (3)(e) Write the commands to execute the following in Ubuntu. Restart the service named isc-dhcp-server.",
        "answer": "Answer: systemctl restart isc-dhcp-server\n\nReference: <<< DHCP_server.pdf >>>"
    },
    q_1_3_f: {
        "question": "1. (3)(f) Write the commands to execute the following in Ubuntu. Install the package named apache2.",
        "answer": "Answer: apt install -y apache2\n\nReference: <<< ネットワーク応用04-1_www導入.pdf >>>"
    },
    q_1_3_g: {
        "question": "1. (3)(g) Write the commands to execute the following in Ubuntu. Display information such as the IP address assigned to a network interface (NIC).",
        "answer": "Answer: ip a\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_3_h: {
        "question": "1. (3)(h) Write the commands to execute the following in Ubuntu. You created a configuration file for IP addresses, etc. (99-nc2.yaml) in the /etc/netplan directory, and want to apply its contents to the system.",
        "answer": "Answer: netplan apply\n\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_2_1: {
        "question": "2. (1) A terminal needs an IP address to connect to a network. What is the protocol used to automatically assign network connection information such as IP addresses?",
        "answer": "Answer: DHCP (Dynamic Host Configuration Protocol)\n\nExplanation: DHCP automates the process of configuring devices on an IP network. Instead of manually typing in an IP address, a DHCP server leases this information out automatically.\nReference: <<< DHCP_server.pdf >>>"
    },
    q_2_2: {
        "question": "2. (2) While the server and client in (1) are exchanging IP address assignments, what does the client use as its source IP address?",
        "answer": "Answer: 0.0.0.0\n\nExplanation: When a computer first connects to a network, it does not have an IP address yet. To find the DHCP server, it yells a 'DHCP Discover' message using the temporary placeholder 0.0.0.0 as its source address.\nReference: <<<< out of FILE >>>"
    },
    q_2_3: {
        "question": "2. (3) What command do you execute to send packets to a terminal with the IP address 192.168.100.100 and check if there is a response?",
        "answer": "Answer: ping 192.168.100.100\n\nExplanation: The ping command sends ICMP Echo Request packets to the target IP to test network routing and connectivity.\nReference: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_2_4: {
        "question": "2. (4) You created an Apache2 configuration file (/etc/apache2/sites-available/100-nc.conf). What command do you execute to enable this file?",
        "answer": "Answer: a2ensite 100-nc.conf\n\nExplanation: To actually turn the site 'on,' you use the Apache2 Enable Site (a2ensite) command, which links it to the active system.\nReference: <<< ネットワーク応用04-2_www設定.pdf >>>"
    },
    q_2_5: {
        "question": "2. (5) In Web server settings, it is considered bad practice to show the file structure within the server to the public. From this perspective, which part of the apache2.conf description should be deleted? Answer only the exact word.",
        "answer": "Answer: Indexes\n\nExplanation: Deleting the 'Indexes' word secures your folder by returning a 'Forbidden' error instead of automatically displaying a list of all your secret backend files and folders.\nReference: <<< ネットワーク応用04-2_www設定.pdf >>>"
    },
    q_2_6: {
        "question": "2. (6) What kind of servers are the following packages used to build?\n(a) bind9\n(b) isc-dhcp-server\n(c) apache2",
        "answer": "Answer:\n(a) DNS Server\n(b) DHCP Server\n(c) Web Server\n\nExplanation: BIND9 translates domain names. isc-dhcp-server hands out IP addresses. apache2 handles HTTP requests.\nReference: <<< ネットワーク応用06_dns1.pdf >>>, <<< DHCP_server.pdf >>>, <<< ネットワーク応用04-1_www導入.pdf >>>"
    },
    q_3_1: {
        "question": "3. (1) You decided to install the isc-dhcp-server package and edit dhcpd.conf. Configure the IP address assignment with the following conditions. Write the contents that should be added to dhcpd.conf (starting with subnet).\n- Both server and client belong to the 10.0.120.0/20 network.\n- The number of IP addresses to be assigned is exactly 10.\n- The server's own IP address is manually set to 10.0.120.2.\n- Specify the router at 10.0.120.1 as the default gateway.\n- Use 8.8.8.8 as the DNS server.",
        "answer":"""Answer: 
```text
subnet 10.0.112.0 netmask 255.255.240.0 {
    option routers 10.0.120.1;
    option domain-name-servers 8.8.8.8;
    range 10.0.120.10 10.0.120.19;
}
```
Explanation: CIDR /20 converts to subnet mask 255.255.240.0, and the correct network address is 10.0.112.0. Pick any 10 IPs (like 10 to 19) avoiding the router and server IPs.\nReference: <<< DHCP_server.pdf >>>""",
         
    
    },
    q_3_2: {
        "question": "3. (2) Assume the Web server's IP address is 192.168.0.1, and the Apache configuration file has the DocumentRoot set to /var/www/html/website1/. When accessing http://192.168.0.1/index.html, where is the displayed web page stored on the server? Answer with the absolute path of the file.",
        "answer": "Answer: /var/www/html/website1/index.html\n\nExplanation: In Apache, DocumentRoot specifies where the base directory of the website is located on the hard disk. The server will look directly inside this directory.\nReference: <<< ネットワーク応用04-2_www設定.pdf >>>"
    },
    q_3_3: {
        "question": "3. (3) Answer the record names used to indicate the following information in DNS settings:\n(a) Information necessary for reverse lookup, which defines the domain name corresponding to an IP address.\n(b) Defines the mail server.\n(c) Defines the name server.",
        "answer": "Answer:\n(a) PTR (Pointer Record)\n(b) MX (Mail Exchange Record)\n(c) NS (Name Server Record)\n\nReference: <<<< out of FILE >>>, <<< ネットワーク応用06_dns1.pdf >>>"
    },
    q_3_4: {
        "question": "3. (4) In the authoritative DNS server, the zone information for nc2.example is set. When accessing the following URLs, answer the IP address obtained by name resolution. If it fails, write X.\n(a) http://www.nc2.example\n(b) http://www2.nc2.example\n(c) http://www.news.example\n(d) http://nc2.example",
        "answer": "Answer:\n(a) 10.13.64.105 (Resolves directly to the A record for www)\n(b) 10.13.64.105 (Resolves to www via CNAME alias)\n(c) x (news.example is in a completely different domain space, so resolution fails here)\n(d) 10.13.64.1 (Resolves to the origin @ record A 10.13.64.1 for the root domain)\n\nReference: <<< ネットワーク応用06_dns1.pdf >>>"
    },
    q_3_5: {
        "question": "3. (5) A terminal is equipped with 3 NICs connected to 192.168.100.0/24 (enp0s3), 192.168.110.0/24 (enp0s8), and 10.13.0.0/16 (enp0s9). Answer the 2 iptables commands to execute the following behavior:\n- Forward packets coming from 192.168.100.0/24 to the 10.13.0.0/16 destination.\n- Forward packets coming from 192.168.110.0/24 to the 192.168.100.0/24 destination.",
        "answer": "Answer:\n1. sudo iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o enp0s9 -j MASQUERADE\n2. sudo iptables -t nat -A POSTROUTING -s 192.168.110.0/24 -o enp0s3 -j MASQUERADE\n\nExplanation: NAPT (MASQUERADE) setup for routing. -s specifies the source network, and -o specifies the out-interface.\nReference: <<< ネットワーク応用05-1_GW.pdf >>>"
    }
}

thai_translations = {
    q_1_1: {
        "question": "1. (1) คุณได้กำหนดค่า IP Address บนอินเทอร์เฟซเครือข่าย (NIC) หากคุณไม่ได้รับข้อมูลเซิร์ฟเวอร์ DNS จาก ISP หรือหากคุณไม่ต้องการใช้งาน คุณสามารถระบุ IP Address ของเซิร์ฟเวอร์ DNS สาธารณะได้ ที่อยู่ IP ของเซิร์ฟเวอร์ DNS สาธารณะของ Google คืออะไร?",
        "answer": "คำตอบ: 8.8.8.8\n\nอ้างอิง: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_2: {
        "question": "1. (2) คำสั่งใด (โดยปกติจะเป็นตัวอักษร 4 ตัวที่เพิ่มไว้ที่จุดเริ่มต้นของคำสั่ง) ที่ใช้เมื่อเข้าสู่ระบบด้วยผู้ใช้ทั่วไปและต้องการประมวลผลบางอย่างชั่วคราวด้วยสิทธิ์ผู้ดูแลระบบ?",
        "answer": "คำตอบ: sudo\n\nอ้างอิง: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_3_a: {
        "question": "1. (3)(a) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: แสดงรายการไฟล์และไดเรกทอรีในไดเรกทอรีปัจจุบัน",
        "answer": "คำตอบ: ls\n\nอ้างอิง: <<<< out of FILE >>>"
    },
    q_1_3_b: {
        "question": "1. (3)(b) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: คัดลอกไฟล์ชื่อ test.txt ในไดเรกทอรีปัจจุบันเป็นไฟล์ชื่อ test2.txt",
        "answer": "คำตอบ: cp test.txt test2.txt\n\nอ้างอิง: <<<< out of FILE >>>"
    },
    q_1_3_c: {
        "question": "1. (3)(c) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: แก้ไขไฟล์ test.txt ในไดเรกทอรีปัจจุบันโดยใช้คำสั่ง vi",
        "answer": "คำตอบ: vi test.txt\n\nอ้างอิง: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_3_d: {
        "question": "1. (3)(d) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: ตรวจสอบว่าบริการที่ชื่อ smbd ทำงานตามปกติหรือไม่",
        "answer": "คำตอบ: systemctl status smbd\n\nอ้างอิง: <<<<< out of FILE >>>"
    },
    q_1_3_e: {
        "question": "1. (3)(e) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: รีสตาร์ทบริการที่ชื่อ isc-dhcp-server",
        "answer": "คำตอบ: systemctl restart isc-dhcp-server\n\nอ้างอิง: <<< DHCP_server.pdf >>>"
    },
    q_1_3_f: {
        "question": "1. (3)(f) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: ติดตั้งแพ็กเกจชื่อ apache2",
        "answer": "คำตอบ: apt install -y apache2\n\nอ้างอิง: <<< ネットワーク応用04-1_www導入.pdf >>>"
    },
    q_1_3_g: {
        "question": "1. (3)(g) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: แสดงข้อมูลเช่น IP Address ที่กำหนดให้กับอินเทอร์เฟซเครือข่าย (NIC)",
        "answer": "คำตอบ: ip a\n\nอ้างอิง: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_1_3_h: {
        "question": "1. (3)(h) จงเขียนคำสั่งเพื่อดำเนินการต่อไปนี้ใน Ubuntu: คุณได้สร้างไฟล์คอนฟิกูเรชันสำหรับ IP Address (99-nc2.yaml) ในไดเรกทอรี /etc/netplan และต้องการปรับใช้เนื้อหากับระบบ",
        "answer": "คำตอบ: netplan apply\n\nอ้างอิง: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_2_1: {
        "question": "2. (1) เทอร์มินัลจำเป็นต้องมี IP Address เพื่อเชื่อมต่อกับเครือข่าย โปรโตคอลที่ใช้ในการกำหนดข้อมูลการเชื่อมต่อเครือข่ายอัตโนมัติเช่น IP Address คืออะไร?",
        "answer": "คำตอบ: DHCP (Dynamic Host Configuration Protocol)\n\nคำอธิบาย: DHCP จะตั้งค่าอุปกรณ์บนเครือข่าย IP โดยอัตโนมัติ แทนที่จะพิมพ์ IP Address ด้วยตนเอง\nอ้างอิง: <<< DHCP_server.pdf >>>"
    },
    q_2_2: {
        "question": "2. (2) ในขณะที่เซิร์ฟเวอร์และไคลเอนต์ใน (1) กำลังแลกเปลี่ยนการกำหนด IP Address ไคลเอนต์ใช้ที่อยู่ IP ต้นทางเป็นอะไร?",
        "answer": "คำตอบ: 0.0.0.0\n\nคำอธิบาย: เมื่อคอมพิวเตอร์เชื่อมต่อเครือข่ายครั้งแรก มันยังไม่มี IP Address จึงใช้ 0.0.0.0 เป็นตัวยึดตำแหน่งชั่วคราวเพื่อค้นหา DHCP เซิร์ฟเวอร์\nอ้างอิง: <<<< out of FILE >>>"
    },
    q_2_3: {
        "question": "2. (3) คุณใช้คำสั่งใดในการส่งแพ็กเก็ตไปยังเทอร์มินัลที่มี IP Address 192.168.100.100 และตรวจสอบว่ามีการตอบสนองหรือไม่?",
        "answer": "คำตอบ: ping 192.168.100.100\n\nคำอธิบาย: คำสั่ง ping จะส่งแพ็กเก็ต ICMP Echo Request ไปยัง IP เป้าหมายเพื่อทดสอบเครือข่าย\nอ้างอิง: <<< ネットワーク応用02-2_serverのIPアドレス.pdf >>>"
    },
    q_2_4: {
        "question": "2. (4) คุณได้สร้างไฟล์คอนฟิกูเรชันของ Apache2 (/etc/apache2/sites-available/100-nc.conf) คุณต้องใช้คำสั่งใดเพื่อเปิดใช้งานไฟล์นี้?",
        "answer": "คำตอบ: a2ensite 100-nc.conf\n\nคำอธิบาย: ใช้คำสั่ง Apache2 Enable Site (a2ensite) เพื่อเปิดใช้งานไซต์ โดยจะเชื่อมโยงกับระบบที่ใช้งานอยู่\nอ้างอิง: <<< ネットワーク応用04-2_www設定.pdf >>>"
    },
    q_2_5: {
        "question": "2. (5) ในการตั้งค่าเว็บเซิร์ฟเวอร์ ถือเป็นแนวทางปฏิบัติที่ไม่ดีที่จะแสดงโครงสร้างไฟล์ภายในเซิร์ฟเวอร์ต่อสาธารณะ จากมุมมองนี้ ส่วนใดของคำอธิบาย apache2.conf ต่อไปนี้ควรถูกลบออก? (ตอบเฉพาะคำที่ต้องลบ)",
        "answer": "คำตอบ: Indexes\n\nคำอธิบาย: การลบคำว่า 'Indexes' ออกจะช่วยรักษาความปลอดภัยโฟลเดอร์ของคุณโดยการส่งกลับข้อผิดพลาด 'Forbidden' แทนการแสดงไฟล์และโฟลเดอร์แบ็กเอนด์ทั้งหมดอัตโนมัติ\nอ้างอิง: <<< ネットワーク応用04-2_www設定.pdf >>>"
    },
    q_2_6: {
        "question": "2. (6) แพ็กเกจต่อไปนี้ใช้สร้างเซิร์ฟเวอร์ประเภทใด?\n(a) bind9\n(b) isc-dhcp-server\n(c) apache2",
        "answer": "คำตอบ:\n(a) DNS Server (เซิร์ฟเวอร์ DNS)\n(b) DHCP Server (เซิร์ฟเวอร์ DHCP)\n(c) Web Server (เว็บเซิร์ฟเวอร์)\n\nคำอธิบาย: BIND9 ใช้แปลงชื่อโดเมน, isc-dhcp-server แจกจ่าย IP Address, apache2 จัดการ HTTP Requests\nอ้างอิง: <<< ネットワーク応用06_dns1.pdf >>>, <<< DHCP_server.pdf >>>, <<< ネットワーク応用04-1_www導入.pdf >>>"
    },
    q_3_1: {
        "question": "3. (1) คุณได้ติดตั้งแพ็กเกจ isc-dhcp-server และตั้งค่า dhcpd.conf กำหนดการจ่าย IP Address ตามเงื่อนไขต่อไปนี้ จงเขียนเนื้อหาที่ควรเพิ่มใน dhcpd.conf (เริ่มด้วย subnet)\n- เซิร์ฟเวอร์และไคลเอนต์อยู่ในเครือข่าย 10.0.120.0/20\n- จำนวน IP Address ที่จะแจกจ่ายคือ 10\n- IP Address ของเซิร์ฟเวอร์ถูกตั้งค่าเองเป็น 10.0.120.2\n- ระบุเราเตอร์ที่ 10.0.120.1 เป็นเกตเวย์เริ่มต้น\n- ใช้ 8.8.8.8 เป็นเซิร์ฟเวอร์ DNS",
        "answer":"""Answer: 
```text
subnet 10.0.112.0 netmask 255.255.240.0 {
    option routers 10.0.120.1;
    option domain-name-servers 8.8.8.8;
    range 10.0.120.10 10.0.120.19;
}
```
คำอธิบาย: CIDR /20 แปลงเป็นซับเน็ตมาสก์ 255.255.240.0 เครือข่ายที่ถูกต้องคือ 10.0.112.0 แจกจ่าย IP 10 หมายเลข โดยหลีกเลี่ยง IP ของเราเตอร์และเซิร์ฟเวอร์\nอ้างอิง: <<< DHCP_server.pdf >>>""",
    },
    q_3_2: {
        "question": "3. (2) สมมติว่า IP Address ของเว็บเซิร์ฟเวอร์คือ 192.168.0.1 และการตั้งค่า DocumentRoot ของ Apache ชี้ไปที่ /var/www/html/website1/ เมื่อเข้าถึง http://192.168.0.1/index.html หน้าเว็บที่แสดงถูกเก็บไว้ที่ไหนบนเซิร์ฟเวอร์? (ตอบด้วยพาธสัมบูรณ์ Absolute path)",
        "answer": "คำตอบ: /var/www/html/website1/index.html\n\nคำอธิบาย: ใน Apache, DocumentRoot จะระบุตำแหน่งพื้นฐานของเว็บไซต์ เซิร์ฟเวอร์จะเข้าไปค้นหาไฟล์ในไดเรกทอรีนี้โดยตรง\nอ้างอิง: <<< ネットワーク応用04-2_www設定.pdf >>>"
    },
    q_3_3: {
        "question": "3. (3) จงตอบชื่อเรคคอร์ด (Record names) ที่ใช้ระบุข้อมูลต่อไปนี้ในการตั้งค่า DNS:\n(a) ข้อมูลที่จำเป็นสำหรับการค้นหาแบบย้อนกลับ (Reverse lookup) ซึ่งกำหนดชื่อโดเมนที่สอดคล้องกับ IP Address\n(b) กำหนดเซิร์ฟเวอร์อีเมล\n(c) กำหนดเนมเซิร์ฟเวอร์ (Name server)",
        "answer": "คำตอบ:\n(a) PTR (Pointer Record)\n(b) MX (Mail Exchange Record)\n(c) NS (Name Server Record)\n\nอ้างอิง: <<<< out of FILE >>>, <<< ネットワーク応用06_dns1.pdf >>>"
    },
    q_3_4: {
        "question": "3. (4) ในเซิร์ฟเวอร์ DNS ที่มีอำนาจ (Authoritative DNS server) ได้ตั้งค่าข้อมูลโซนสำหรับ nc2.example เมื่อเข้าถึง URL ต่อไปนี้ จงตอบ IP Address ที่ได้จากการแปลงชื่อ (Name resolution) หากการแปลงชื่อล้มเหลวให้เขียน X\n(a) http://www.nc2.example\n(b) http://www2.nc2.example\n(c) http://www.news.example\n(d) http://nc2.example",
        "answer": "คำตอบ:\n(a) 10.13.64.105 (แปลงชื่อโดยตรงไปยังเรคคอร์ด A สำหรับ www)\n(b) 10.13.64.105 (แปลงชื่อเป็น www ผ่าน CNAME alias)\n(c) x (news.example อยู่ในโดเมนที่ต่างกันอย่างสิ้นเชิง การแปลงชื่อจึงล้มเหลว)\n(d) 10.13.64.1 (แปลงชื่อไปยัง origin @ เรคคอร์ด A 10.13.64.1 สำหรับโดเมนหลัก)\n\nอ้างอิง: <<< ネットワーク応用06_dns1.pdf >>>"
    },
    q_3_5: {
        "question": "3. (5) เทอร์มินัลมี 3 NIC ที่เชื่อมต่อกับเครือข่าย 192.168.100.0/24 (enp0s3), 192.168.110.0/24 (enp0s8) และ 10.13.0.0/16 (enp0s9) จงตอบคำสั่ง iptables 2 คำสั่งเพื่อดำเนินการตามพฤติกรรมต่อไปนี้:\n- ส่งต่อแพ็กเก็ต (Forward packets) ที่มาจาก 192.168.100.0/24 ไปยังปลายทาง 10.13.0.0/16\n- ส่งต่อแพ็กเก็ต (Forward packets) ที่มาจาก 192.168.110.0/24 ไปยังปลายทาง 192.168.100.0/24",
        "answer": "คำตอบ:\n1. sudo iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o enp0s9 -j MASQUERADE\n2. sudo iptables -t nat -A POSTROUTING -s 192.168.110.0/24 -o enp0s3 -j MASQUERADE\n\nคำอธิบาย: เป็นการตั้งค่า NAPT (MASQUERADE) สำหรับ routing โดย -s ใช้ระบุเครือข่ายต้นทาง และ -o ใช้ระบุอินเทอร์เฟซขาออก\nอ้างอิง: <<< ネットワーク応用05-1_GW.pdf >>>"
    }
}