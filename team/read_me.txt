Scrapy实战【1】：爬取虎扑球员及球队信息

训练技巧：链接爬取，层级爬取，正则，双子元素爬取，父元素->子元素爬取

一.链接爬取

在获取要爬取的下一页链接时通常有两种方法，第一种是使用CSS选择器选中某一元素的href属性，然后调用调用response.urljoin方法计算出绝对url地址，最后构造Request对象并提交；还有一种方法是直接导入scrapy.linkextractors中的LinkExtractor对象，构造提取规则，而后调用extract_links方法传入一个Response对象，最终将返回一个列表，其中每一个元素都是一个link对象。

二.层级爬取

当要爬取的数据分布在多个页面时，可以传入scrapy.Request方法中的meta参数，把之前收集到的信息传递到新请求里

三.正则（过滤不要的内容）
pattern = [^+(不要的内容)].*?

四.双子元素爬取

当要爬取的对象分布在一个父元素下的两个子元素下时，css提取时可用,隔开

五.父元素->子元素爬取

例子：想要抓取div标签下的第2个a元素
xpath: .xpath(‘//div/a[2]’)
css : css(div>a:nth-child(2))
