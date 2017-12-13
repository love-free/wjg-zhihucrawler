# zhihucrawler
python爬取知乎用户基本信息  
程序用到了python3.5，mysql数据库，自行准备好环境  
**注:**  
1. 做了两个很小改动的版本，一个普通版，一个协程版  
2. 在windows上测试通过  
3. 使用前请先修改数据库信息，导入sql文件  
4. 由于知乎页面随时可能改版，所以解析html获取信息可能会获取不到信息，请自行解析修改。不会解析，请参照[https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html# "BeautifulSoup")  
5. 手机登陆有点问题，请使用邮箱登陆
