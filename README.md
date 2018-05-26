# StackOverFlow

#简介
一个爬取StackOverFlow社区帖子的python爬虫工具（V1.0）

#功能
获取指定关键词和数目的帖子信息
1.	获取内容：帖子标题（title）+问题内容（question）+回复（answer）+该帖子的URL（url）
2.	生成格式为CSV，用Excel可以打开

#使用方法
1.	由于目前还没有转exe，所以需要在pycharm上运行。
2.	需要python3环境，在“File→Default setting→Project Interpreter”中添加requests、beautifulsoup4这两个支持库。
3.	打开本文件，右键点击文件名称，选择“Run‘StackOverFlow’”，根据提示输入关键词和爬取页数（默认每页50条）。
4.	生成的文件保存在StackOverFlow.py文件的同路径下。
