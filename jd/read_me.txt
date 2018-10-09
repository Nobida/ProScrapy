Scrapy实战【3】爬取京东商城商品信息

训练点：动态页面抓取， 网站页面结构变化（观察数据提取），splash基本操作

通常在前端的动态网页中，数据被硬编码在javascript中，亦有javascript通过http请求跟网站动态交互获取数据（ajax），然后使用数据更新html页面，爬取此类动态网站需要先执行页面的javascript代码渲染页面
Splash支持执行用户自定义的渲染脚本，功能类似于phantomjs

1.如何编写lua脚本，以【滑动】为例
在开发者工具的console中进行实验，用document.getElementsByXXX方法随意选中页面下方的某元素，比如“下一页”按钮所在的<div>元素，然后在该元素对象上调用scrollIntoView(true)完成拖曳动作，
e = document.getElementsByClassName('pn-next')[0]
$('ul.gl-warp > li').length
len(response.css(‘ul.gl-warp > li’))

2.yield SplashRequest(url, callback = self.parse_info, endpoint = ‘execute’#服务器服务端点
			args = {‘lua_source’: lua_script},#传递给Splash的参数(除url以外)，如wait、timeout、images、js_source等
			cache_args = [‘lua_source’])#如果args中的某些参数每次调用都重复传递并且数据量较大(例如一段JavaScript代码)，此时可以把该参数名填入cache_args列表中，让Splash服务器缓存该参 数，如SplashRequest(url, args = {'js_source': js, 'wait': 0.5}, cache_args = ['js_source'])。


下一章 使用splash进行模拟点击