# RasPiとMac/ChromeをBLEでつないでLチカ

## インストール

### RasPi側

[pybleno](https://github.com/Adam-Langley/pybleno)をインストールする

```bash
# 必要なパッケージのインストール
# [bleno](https://github.com/noble/bleno#prerequisites)による
$ sudo apt-get install bluetooth bluez libbluetooth-dev libudev-dev

# bluetoothd の停止
$ sudo systemctl stop bluetooth       # とりあえず今回だけ
# $ sudo systemctl disable bluetooth    # 起動時にも停止

# hci0のマニュアル起動
$ sudo hciconfig hci0 up

# pybleno のインストール
$ pip install pybleno
```

### Mac側

[BlueJelly](https://github.com/electricbaka/bluejelly.git)をインストールする

```bash
$ git clone https://github.com/electricbaka/bluejelly.git
```

## 操作方法

### RasPi側

1. ペリフェラルを立ち上げる

  ```
  $ cd /home/pi/examples/ble_switch
  $ sudo ./peripheral.py
  ```

### Mac側

1. 「設定」でBluetoothを有効化
2. `Chrome` を立ち上げる
3. `file:///Users/dspace/source/bluejelly/src/notify.html`に接続
4. [Start Notify] ボタンを押して接続
5. スイッチのオンオフでLEDがオン・オフし、`read data`値が変更される
6. [Stop Notify] ボタンを押して切断
