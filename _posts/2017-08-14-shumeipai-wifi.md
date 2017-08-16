## 树莓派配置WIFI上网

针对固件 `raspberry-lite`， 主要命令是 `wpa_cli`。

```shell
wpa_cli scan # 扫描可用WIFI
wpa_cli add_network # 增加一个网络配置，返回是一个id
wpa_cli set_network <id> ssid <ssid> # 配置网络ssid
wpa_cli set_network <id> psk <password> # 配置网络密码
wpa_cli save_config # 保存配置 
```