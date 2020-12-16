# -*- coding: utf-8 -*-

# Scrapy settings for JDSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JDSpider'

SPIDER_MODULES = ['JDSpider.spiders']
NEWSPIDER_MODULE = 'JDSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JDSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#    'cookies': 'shshshfpa=a4905f2e-8106-08d3-4910-30d81a94af12-1538448025; shshshfpb=28245fb27c48342febacbadddc671efd85b2bc33e7707002e99b2da971; __jdu=1538448024682649296362; PCSYCityID=CN_350000_350500_350503; areaId=16; ipLoc-djd=16-1332-42931-59649; user-key=7d8fa408-43bf-470a-b84c-add520b0a324; cn=0; unpl=V2_ZzNtbUYAExJyC0RSKxEPV2IEEl1KVhMUJwxBVXtNXgNhUUZcclRCFnQUR1NnG10UZwQZXUJcQRNFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdXgxiBhtcQVJEHHYPQ1x4EVsHYAAibUVncyVxAEZVfhpsBFcCIh8WC0MScgxPUzYZWAduBhdUQ1RGEnwLQVFzGlQCZQQRbUNnQA%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5fa66237a9bc461190a0c5601e377ce0|1593504697840; __jdc=122270672; 3AB9D23F7A4B3C9B=FY3VSEBIHHA6OBY2634Z4IS2QYJ7GIIUQHHNH6JON3LKSUF34TVIG4WDWNXIOFYZV4IG2ZO5ZADVP6IPO4R3ZPFCXU; shshshfp=840db8a291fad3759e89c573d15a046c; __jda=122270672.1538448024682649296362.1538448025.1593504698.1593513001.46'
#    'Cookie':'log-uid=c602fc29f89d4bd2a628f14e44f28873; ASP.NET_SessionId=s22gagsw4lif5la3zcwvaas1; lsjgcxToken=6E50054E357C53F305D2DD93260D1BCAB074F2EF39141375EC80DE43C856B5E379D39FF1762E72D98BD1B63362C70815290C09AD6A8461A8ED32FEAD76F02CE5; Hm_lvt_85f48cee3e51cd48eaba80781b243db3=1592913949,1593417503,1593509421,1593516060; Hm_lvt_01a310dc95b71311522403c3237671ae=1592913949,1593417504,1593509421,1593516060; _ga=GA1.2.1917004152.1593516060; _gid=GA1.2.613211809.1593516060; Hm_lpvt_85f48cee3e51cd48eaba80781b243db3=1593523436; Hm_lpvt_01a310dc95b71311522403c3237671ae=1593523437; _gat_gtag_UA_145348783_1=1',
#}
IPPOOL= [
    {"ipaddr":"114.96.45.140:4516"}]

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JDSpider.middlewares.JdspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'JDSpider.middlewares.JdspiderDownloaderMiddleware': 543,
    'JDSpider.middlewares.MyproxiesSpiderMiddleware': 125,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'JDSpider.pipelines.JdspiderPipeline': 300,
    #'JDSpider.pipelines.JdspiderPipelineItemPrice': 400,
    #'JDSpider.pipelines.JdspiderPipelineItemVolume': 500,
    #'JDSpider.pipelines.JdspiderPipelineItemDatePrice':300

}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
