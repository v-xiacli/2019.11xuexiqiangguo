# xuexiqiangguo
lovestudy!
这个可以来看学习强国 美中不足的是网页版的 最多一天刷25分


程序结构 
study_login.py 主脚本 第一次使用需要登陆（扫码的 可以说是违背了自动化标准了 谁叫他只能扫码登陆呢？？？！！！）
第二次会使用cookie登陆 就不需要扫码了 如果cookie失效则删除cookiedata.json即可（其实也可以通过判断网页元素来判断有没有登陆成功 但我懒得搞了）

article_urls.txt 用来存放所有的文章链接 大概有几千条 通过study_writeurls.py来爬取

video_urls.txt 用来存放视频链接 大概有几千条 通过study_writeurls.py来爬取

artical_haveread.txt 和 video_haveread.txt 用来存放已经看过的链接 避免重复观看 默认有几十条放在里面 防止有些内容比较新已经看过

study_writeurls.py 几千个链接的来源 链接到手，它也结束了它的使命。
