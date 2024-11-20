
config.jsonをみると
```"token": "Replace me with token when in use! Security Risk!",```
と書いてあった。

git管理フォルダがあったので、五日のタイミングで直接トークンを書いていたのではないか？と思い過去の変更点をみると、tokenが直接書かれていた。
その値をbase64でデコードすると、フラグがみつかった。

```
oot@568cfbfbdf97:~/solve/hackthebox/forensic/Illumination/Illumination.JS# git diff edc5aabf933f6bb161ceca6cf7d0d2160ce333ec 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a config.json 
diff --git a/config.json b/config.json
index 6735aa6..316dc21 100644
--- a/config.json
+++ b/config.json
@@ -1,6 +1,6 @@
 {
 
-       "token": "Replace me with token when in use! Security Risk!",
+       "token": "SFRCe3YzcnNpMG5fYzBudHIwbF9hbV9JX3JpZ2h0P30=",
        "prefix": "~",
        "lightNum": "1337",
        "username": "UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==",
root@568cfbfbdf97:~/solve/hackthebox/forensic/Illumination/Illumination.JS# 
```