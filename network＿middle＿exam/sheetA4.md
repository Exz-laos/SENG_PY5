A4用紙の両面に手書きでまとめるための、「超圧縮・高効率カンペ（チートシート）」の構成案を作成しました。
過去問の傾向とこれまでの予想問題から、「コマンド」「設定の意味」「記述するコード」の3点を極限まで絞り込んでいます。このレイアウトのままA4用紙の【表面】と【裏面】に書き写すことで、試験中の検索スピードが最大化されます。

---

### 【表面】 コマンド・ネットワーク・DHCP・Webサーバ

**1. 必須Linuxコマンド＆基礎知識**
* **一時的な管理者権限**: `sudo`
* **隠しファイル含む詳細一覧**: `ls -la`
* **IPアドレスとNIC名(enp0sX)の確認**: `ip a` (または `ip link`)
* **通信テスト (4回で終了)**: `ping [IPアドレス] -c 4`
* **安全な即時シャットダウン**: `sudo shutdown now`
* **権限変更**: `sudo chmod 600 [ファイル]` (4:読 + 2:書 = 6。所有者のみ読み書き可能にする)
* **viの保存＆終了**: `[ESC]` を押した後 `[:][w][q][Enter]`
* **サービスの管理**: `sudo systemctl status / restart / reload [サービス名]` (状態確認 / 再起動 / 設定の無停止再読込)

**2. Netplan (IPアドレス設定)**
* **ファイルの場所**: `/etc/netplan/` 内の `.yaml`
* **階層ルール**: 一番上に `network:` 、その下に `ethernets:` 、その下に各NIC名
* **設定項目の意味**:
  * `version: 2`: Netplan設定フォーマットのバージョン2を使用
  * `/24`: サブネットマスクが24ビット (255.255.255.0) を意味する
* **静的IPの設定構文 (インデント必須)**:

```yaml
enp0s9:
  dhcp4: false
  dhcp6: false
  addresses: [192.168.200.2/24]
  optional: true  # IP設定完了を待たずにシステム起動を進める設定
```

* **反映コマンド**: `sudo netplan apply`

**3. DHCPサーバ (`isc-dhcp-server`)**

* **使用ポート**: サーバ `67` 番 / クライアント `68` 番
* **DHCP要求時の送信元IP**: `0.0.0.0` (まだIPを持っていないため)
* **権威(公式)サーバ化**: `dhcpd.conf` 内の `#authoritative;` の `#` を消す
* **DHCP配布設定 (192.168.100.101~150を配る場合)**:

```text
subnet 192.168.100.0 netmask 255.255.255.0 {
  option routers 192.168.100.1;  # デフォルトゲートウェイ(ルータ)のIP
  option domain-name-servers 8.8.8.8;  # キャッシュDNS完成時は192.168.100.1等に修正
  range 192.168.100.101 192.168.100.150;
}
```

**4. Webサーバ (`apache2`)**

* **ディレクトリ構造**: `sites-available` (設定の置き場) / `sites-enabled` (有効化済みの設定)
* **有効化 / 無効化コマンド**: `sudo a2ensite [ファイル]` / `sudo a2dissite [ファイル]`
* **ディレクトリ作成**: `sudo mkdir /var/www/website1`
* **設定項目の意味**:
  * `DocumentRoot`: Webブラウザアクセス時に表示するファイルを置く場所 (`/var/www/html` など)
  * `ServerAdmin student@kct.ac.jp`: エラー時に表示されるサーバ管理者の連絡先メアド
  * `ErrorLog`: エラーに関する記録(ログ)を保存するファイルの場所
  * `Require all granted`: 全てのアクセス(ユーザー/IP)を許可する

* **セキュリティ対策**: `apache2.conf` の `<Directory>` 内にある **`Indexes`** を削除（ファイル一覧表示を防ぐ）
* **HTMLタグ**: `<h1>` (一番大きな見出し)、`<title>` (ブラウザのタブに表示される名前)

---

### 【裏面】 ルータ(GW)・DNSサーバ

**5. ルータ / ゲートウェイ構築 (`iptables`)**

* **フォワーディング(パケット転送)の有効化**: `/etc/sysctl.conf` 内の `#net.ipv4.ip_forward=1` の `#` を消す
* **カーネルへの即時反映**: `sudo sysctl -p`
* **ファイアウォール確認**: `sudo ufw status` (転送がブロックされていないか確認)
* **NAPT (IPマスカレード) コマンド**:

```text
sudo iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o enp0s9 -j MASQUERADE
```

* `-s`: 送信元ネットワークを指定
* `-o`: パケットが出ていくインターフェース(出口NIC)を指定
* `-j MASQUERADE`: 送信元のIPアドレスを、出口NICのIPに自動で書き換える指示

**6. 権威DNSサーバ (`bind9` / `bind9-utils`)**

* **構文チェックコマンド**:
  * 全体設定: `named-checkconf`
  * ゾーン設定: `named-checkzone oreore.test /etc/bind/db.oreore`

* **名前解決のテスト**: `nslookup [ドメイン/IP]` または `dig [ドメイン]`
* **FQDNの掟**: ゾーンファイル内のドメイン名末尾には必ず **`.` (ドット)** をつける (例: `ns1.oreore.test.`)。忘れると自動でドメイン名が重複補完されエラーになる
* **レコードの種類**:
  * `type master;`: このサーバが大元のファイル(マスターデータ)を持っている宣言
  * `CNAME` レコード: `www2 IN CNAME www` (別名/エイリアスを定義する)
  * `PTR` レコード: IPアドレスからホスト名へ変換する「逆引き」の役割

* **逆引きゾーン名のルール**: ネットワークアドレス(例:`192.168.200.0/24`)の数字を逆順にし、`.in-addr.arpa` をつける
* **ゾーン宣言 (`named.conf.local`)**:

```text
zone "200.168.192.in-addr.arpa" {
    type master;
    file "/etc/bind/db.200.168.192.rev";
};
```

* **逆引きレコード (`db.200.168.192.rev`)**:

```text
1 IN PTR ns1.oreore.test.  # ネットワーク部はゾーン名で宣言済みのため、ホスト部「1」のみ記述
```

**7. キャッシュDNSサーバ**

* **特徴**: 自身でドメインを管理しないため、ゾーンファイルの作成(`db.oreore`等)は **不要**
* **設定の意味 (`named.conf.options`)**:
  * `acl "netc2" { 192.168.200.0/24; };`: ネットワーク範囲に変数のような名前(グループ)をつける
  * `listen-on { 192.168.100.1; };`: 指定したIPのインターフェースだけで問い合わせを待ち受ける
  * `allow-query { localhost; netc2; };`: 名前解決の質問を送れるネットワークを制限する
  * `recursion yes;`: 答えがわからない時に別のDNSへ再度問い合わせる(再帰)設定
  * `allow-recursion { netc1; localhost; };`: 攻撃防止のため、再帰問い合わせを許可する範囲を絞る
  * `forwarders { 192.168.200.1; };`: 知らないドメインの問い合わせを転送して代わりに調べてもらう外部サーバを指定

* **成功の証拠**: `nslookup` 実行時に **`Non-authoritative answer` (非権威の回答)** と表示されること。これは「キャッシュDNSサーバが代理で回答した」事実を示す