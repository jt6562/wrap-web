# wrap-web
Using iframe tag wrap a web page to hide original URL
You would use this to open a web page by special browser, for example: Weixin

简单的使用iframe标签打开一个网页，目的是隐藏原网页的URL地址。
主要用于某些特定的浏览器，比如微信内置的浏览器禁止打开淘宝页面，恶心的竞争手段。

配合Firefox浏览器扩展[share2qr]("https://github.com/jt6562/share2QR")使用，可以方便的在浏览淘宝页面时，使用微信“扫一扫”功能将某个淘宝页面分享给其他好友。

##开发调试环境(Develop&Debug)
1. run 'virtualenv .venv'
2. run 'pip -r requirement.txt'
3. run 'gunicorn --reload app:app'
