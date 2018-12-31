# ScrapySeleniumTest

Scrapy Selenium on Taobao Product

selenium和phantomjs已经和平分手了，取而代之的是传统豪强的两个千金，chrome--headless和firefox--headless，这个spider记录了如何在scrapy中对接selenium；在这里我们要分清两个中间件的区别,downloader.middleware和spider.middleware
#Downloader 
#Downloader的作用有两个：1.在Scheduler发送Request给Downloader之前修改Request。2。在Response发送给Spider之前对其进行修改。

Spider Middleware有以下3个作用：1.在Downloader发送Response给Spider之前对其进行处理。2.在Spider发送Request给Scheduler之前对其进行处理。3.在Spider发送Item给Item Pipeline之前对其进行处理。