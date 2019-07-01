# RasPiとMac/ChromeをBLEでつないでLチカ

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
