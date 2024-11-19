
## how to solve
zipを解答するとファイルが一つ出現する。

fileコマンドで確認すると、windowsのメモリダンプファイルだった。

```bash
root@d44910630b5b:~/lib/1337uplive2024/HoardedFlag# file memory_dump.raw 
memory_dump.raw: MS Windows 64bit crash dump, full dump, 524045 pages
```
 
pachi — 2024/11/16 21:39
https://blog.hamayanhamayan.com/entry/2022/12/14/231806  
これを参考にしながら、この問題を解いている。  
はじめてメモリダンプ系をとくので、備忘録代わりに手順も記入する。

```shell
python3 /opt/volatility3/vol.py -f {memory_dump.raw} windows.filescan
```

下記コマンド履歴を見ると7zをたたいていたので、それで解凍できた。
 7z a -pScaredToDeathScaredToLook1312 -mhe flag.7z flag.zip

```
python3 /opt/volatility3/vol.py -f memory_dump.raw windows.cmdscan.CmdScan
```

