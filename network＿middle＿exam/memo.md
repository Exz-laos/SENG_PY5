A4両面1枚という限られたスペースに手書きでまとめるための、「超高効率・超圧縮カンペ（チートシート）」の構成案を作成しました。

過去問の傾向と、これまでに作成した予想問題から「ほぼ確実に出る」設定構文とコマンドだけを極限まで削ぎ落としてまとめました。A4用紙の「表面」と「裏面」に分けて、以下のようにブロックごとに書き写すのがおすすめです！

---

### 【表面】 基本コマンド・ネットワーク・DHCP・Web

#### 1. 必須 Linuxコマンド (よく問われるもの)

* **権限付与**: `sudo` (管理者権限)
* **IP確認**: `ip a` (または `ip address`)
* **通信テスト**: `ping 192.168.X.X -c 4` (-c 4 = 4回で終了)
* **権限変更**: `chmod 600 [ファイル名]` (600 = 4:読 + 2:書)
* **サービス状態**: `systemctl status [サービス名]`
* **サービス再起動**: `systemctl restart [サービス名]`
* **設定再読込(無停止)**: `systemctl reload [サービス名]`
* **シャットダウン**: `sudo shutdown now`
* **vi操作**: `[:][w][q][Enter]` (保存して終了)

#### 2. Netplan (IPアドレス設定)

* **ファイル場所**: `/etc/netplan/` (拡張子 `.yaml`)
* **反映コマンド**: `netplan apply`
* **親階層**: `network:` の下に `ethernets:`
* **固定IP構文** (※インデントの空白スペース超重要！):
```yaml
enp0sX:
  dhcp4: false
  addresses: [192.168.100.1/24]
  optional: true  ←(起動時の待機スキップ)

```



#### 3. DHCPサーバ (`isc-dhcp-server`)

* **ファイル**: `/etc/dhcp/dhcpd.conf`
* **有効化**: `#authoritative;` の `#` を消す
* **配布構文**:
```text
subnet 192.168.100.0 netmask 255.255.255.0 {
  option routers 192.168.100.1;
  option domain-name-servers 8.8.8.8;
  range 192.168.100.101 192.168.100.150;
}

```


* **ポート番号**: サーバ `67` / クライアント `68`
* **要求時の送信元IP**: `0.0.0.0` (IP未所持のため)

#### 4. Webサーバ (`apache2`)

* **ドキュメントルート**: `/var/www/html`
* **サイト有効化**: `a2ensite [ファイル名]`
* **サイト無効化**: `a2dissite [ファイル名]`
* **セキュリティ**: `<Directory>` 内の **`Indexes`** を削除 (ファイル一覧表示を防ぐ)
* **アクセス許可**: `Require all granted`
* **エラーログ場所**: `ErrorLog`
* **管理者アドレス**: `ServerAdmin`

---

### 【裏面】 ルータ(GW)・DNSサーバ・暗記事項

#### 5. ゲートウェイ / ルータ設定 (パケット転送)

* **機能有効化ファイル**: `/etc/sysctl.conf`
* **有効化する行**: `#net.ipv4.ip_forward=1` の `#` を消す
* **即時反映コマンド**: `sysctl -p`
* **NAPT (IPマスカレード) 呪文**:
`iptables -t nat -A POSTROUTING -s [送信元NW] -o [出口NIC] -j MASQUERADE`
*(※ -s は「ここから来た」、-o は「ここから出す」、-j MASQUERADE は「IPを書き換える」)*
* **FW確認**: `ufw status`

#### 6. DNSサーバ (`bind9`)

* **構文チェックコマンド**:
* 全体: `named-checkconf`
* ゾーン: `named-checkzone [ドメイン] [ファイルパス]`


* **名前解決テスト**: `dig www.oreore.test`
* **全体設定 (`named.conf.options`)**:
* `acl "netc" { 192.168.100.0/24; };` (NWに名前をつける)
* `allow-query { localhost; netc; };` (問い合わせ許可)
* `forwarders { 8.8.8.8; };` (知らない宛先をGoogleに丸投げ)


* **ゾーン宣言 (`named.conf.local`)**:
```text
zone "oreore.test" {
    type master;
    file "/etc/bind/db.oreore";
};

```


* **ゾーンファイル (`db.oreore`) の掟**:
* `@` = 基準となるドメイン自身 (オリジン)
* **FQDNの末尾には必ず `.` (ドット) をつける** (例: `ns1.oreore.test.`)
* `A` レコード = IPアドレスを指定
* `CNAME` レコード = 別名 (エイリアス) を指定
* `NS` レコード = ネームサーバを指定



#### 7. おまけの暗記事項

* **Google Public DNS**: `8.8.8.8` (または `8.8.4.4`)
* **クライアント用メモリ**: `2048 MB`
* **クライアントOS名**: `Xubuntu`
* **仮想ネットワーク**: 内部ネットワーク / Emulated VLAN

---

### 💡 カンペ作成のアドバイス

手書きで作る際は、英語のスペルミス（`authoritative` や `MASQUERADE`、`sysctl` など）に気をつけてください。文字の色を「コマンド」「設定ファイル名」「ファイルの中身」で3色ボールペンで書き分けると、試験中に一瞬で探せるようになります！