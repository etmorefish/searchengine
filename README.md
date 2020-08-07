## searchengine
## 元搜索引擎  
### 项目描述
根据元数据（引擎名称、关键词、页码、等元数据）去调用引擎接口，达到数据实时返回的结果，基于这些搜索引擎，提供了一种多类别、轻量、高效、廉价的搜索引擎。主要通过信号控制，将爬虫搜索实时返回终端或通过其它方式捕获返回前端

#### 1 python3
#### 2 scrapy + MongoDB
```bash
pip install scrapy
pip install pymongo
```
#### 3 使用方法
```bash
git clone https://github.com/zhu733756/searchengine.git
cd searchengine [search.py的父目录]
python3 search.py [site] [keywords] [page] [sorttype]
eg: python search.py weixin 百事可乐 2 4
```
#####	site: 目前支持 bing/weibo/weixin/baidu/baidunews/ss_360/ss_360_zx/chinaso/chinaso_news 之一
#####	keywords: 关键词，多个用+连接
#####	page: 页码
#####	sorttype: baidunews支持 1-按照焦点排序，4-按时间排序
#####	输出结果以打印成json数据输出在终端
