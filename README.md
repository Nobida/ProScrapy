
## 试题爬虫项目
项目名|网站/app|入口|说明
---|---|---|---
scrapy_91taoke|[91淘课网](http://www.91taoke.com/)|[entrypoint.py](scrapy_91taoke/entrypoint.py)|本项目从91taoke.com爬取所有题目，在进行项目之前，先执行[91taoke_mapping.py](scrapy_91taoke/scrapy_91taoke/spiders/91taoke_mapping.py)爬取url的相关信息，之后直接可使用```python entrypoint.py```执行项目<br>[解析代码](scrapy_91taoke/scrapy_91taoke/parse/scrapy_91taoke_parse.py)<br>[爬取代码](scrapy_91taoke/scrapy_91taoke/spiders/91taoke_spider.py)
jiajiao1010|[精英家教网](http://www.1010jiajiao.com/gzyy/shiti_page_98)|[entrypoint.py](jiajiao1010/entrypoint.py)|本项目从[精英家教网](http://www.1010jiajiao.com/gzyy/shiti_page_98)爬取试题的题目信息(不含书本中的题目)，爬取的子url以及科目id映射存于[common.py](jiajiao1010/jiajiao1010/spiders/common.py)<br>[爬取代码](jiajiao1010/jiajiao1010/spiders/jj1010.py)
spider_jtyhjy|[好教育云平台试题系统](http://www.jtyhjy.com/sts/?disciplineCode=02&disciplineId=21&disciplineType=2&knowledgeId=2440932)|[jtyhjy.py](spider_jtyhjy/jtyhjy.py)|本项目从[好教育云平台试题系统](http://www.1010jiajiao.com/gzyy/shiti_page_98)爬取试题的题目信息，采取脚本的形式，先爬取所有科目及其对应知识点的json信息，存入文件，之后通过知识点和科目凑url，按照一定题目数量分页请求爬取，json信息[在此](spider_jtyhjy/working/knowledges/)<br>[爬取代码](spider_jtyhjy/jtyhjy.py)
spider_quyixian|[曲一线科学备考](http://4s.quyixian.com/SEC/)|[quyixian_spider.py](spider_quyixian/quyixian_spider.py)|本项目从[曲一线科学备考](http://4s.quyixian.com/SEC/)爬取书籍中的题目信息，添加错题采取脚本的形式，获取每本书的cid，通过cid获取每本书每个栏目的bid，通过bid获取栏目的页码信息，之后通过page和bid凑url，获取栏目所有试题id，分析js代码找到添加错题的接口，添加错题，[添加错题入口](spider_quyixian/quyixian.py)<br>爬取思路：从个人主页中的我的错题本中找出所有添加的书籍信息，通过bid请求返回数据为json形式的接口，该接口返回本书所有题目信息和qid，再根据qid请求答案解析接口，爬取答案。<br>[爬取代码](spider_quyixian/quyixian_spider.py)
anoah_scrapy|[优学派](http://www.anoah.com/api_cache/?q=json/Qti/get&info={%22param%22:{%22qid%22:%22question:173980%22,%22dataType%22:1}})|[entrypoint.py](anoah_scrapy/entrypoint.py)|本项目从anoah.com爬取所有题目，直接根据anoah的API进行循环遍历抓取，，之后直接可使用```python entrypoint.py```执行项目<br>[爬取代码](anoah_scrapy/anoah/spiders/ANOAH.py)
scrapy_xiangpi|[橡皮网](http://www.xiangpi.com/zujuan/1)|[entrypoint.py](scrapy_xiangpi/entrypoint.py)|本项目从橡皮网爬取所有题目，思路如下，在组卷首页使用脚本爬取目录，知识点结构，以学科id命名存入不同的文件，通过年级id,学科id,和读取出来的对应的章节id凑成完整的url，请求题目信息，在题目信息的中，含有试题id，之后通过试题id，进一步请求该试题的答案json，这里请求答案也需要带上年级和学科id，否则返回错误。<br>[爬取代码](scrapy_xiangpi/scrapy_xiangpi/spiders/xiangpi_spider.py)
wln|[未来脑](https://www.wln100.com/Test/1103710.html)|[entrypoint.py](wln/entrypoint.py)|本项目从未来脑网爬取所有题目，思路如下，以学科为划分作为start_urls，先爬取每个学科下的页数，遍历循环每一页题目，抓取test链接，再通过test页面抓取每道题的id。该爬虫设置了多重logger报警机制，当因抓取／相应！=200时会重新回到parse函数中进行抓取，直到符合一个条件后退出<br>[爬取代码](wln/wln/spiders/weilai.py)


----------

## 爬虫解析用到的服务：
### 图片下载
```
import requests
import hashlib

def download_img(spider_source, spider_url, image_url, image_url_md5, using_proxy=True, headers=""):
    url = "http://172.16.0.100:9000/apis/v1/image/collection/"
    data = dict(
        spider_source = spider_source,
        image_url = image_url,
        image_url_md5 = image_url_md5,
        spider_url = spider_url,
        headers = headers,
        proxy = True if using_proxy else None,
    )
    print(data)

    r = requests.post(url, data=data)
    if r.status_code==200:
        print(r.json())
        return True
    else:
        return False

if __name__=="__main__":
    spider_url = "http://www.mofangge.com/html/qDetail/02/x6/201003/g2kux6021294.html"
    image_url = 'http://pic19.nipic.com/20120210/7827303_221233267358_2.jpg'
    image_url_md5 = hashlib.md5(image_url.encode('utf8')).hexdigest()

    ret = download_img(8, spider_url, image_url, image_url_md5)
    if not ret:
        print("download error")

```
#### latex题目渲染

```
import requests
import json
def render_latex(html):
    url = "http://172.16.0.100:30001/render_latex/"
    data = {"html": html}
    r = requests.post(url, data=data)
    if r.status_code != 200:
        return ""

    content = json.loads(r.content)
    if content["meta"]["status"] != 0:
        return ""
    
    return content["data"]
    
html = "something $$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$ something $\frac{1}{2}$"
latex_html = render_latex(html)
print(latex_html)
```


----------

## 搜狗素材作文spider
pp作文和sucai作文是爬两个站的素材作文数据
```
python sucai_spider.py
python ppzuowen_spider.py
```

parser.py文件主要是从爬下的数据中提取需要的部分
```
python parser.py
python ppzuowen_parser.py
```
解析完发现字数字段需要添加，因此写了个add_wordage文件
```
python add_wordage.py
```
生成xml的程序和搜狗其他xml程序一样，需要调用xml_lib库，其实和搜狗其他几个xml程序中调用的库完全一样
```
python zuowensucai_xml.py
```
xml生成后需要将xml和链接txt上传到hanyu服务器，运行bash文件即可
```
bash upload.sh
```
