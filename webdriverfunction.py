from selenium import webdriver

#1.声明浏览器对象
browser = webdriver.Chrome()

#2.访问页面
browser.get() #get方法
#可惜的是browser不支持post方法

def get_system_cookies(url,account,password):
    '''通过request 登陆系统，获取cookie'''
    cookiesList = []
    data = {"username":account,"passwd":password}
    roomSession  = requests.Session()
    roomSession.post(url,data=data)
    loadCookies = requests.utils.dict_from_cookiejar(roomSession.cookies)
    for cookieName,cookieValue in loadCookies.items():
        cookies = {}
        cookies['name'] = cookieName
        cookies['value'] = cookieValue
        cookiesList.append(cookies)
    return cookiesList

#3.获取节点
browser.find_element_by_css_selector() = browser.find_element(By.id, 'q')

#4.获取多个节点
browser.find_elements_by_css_selector()

#5.节点交互
send_keys()
clear()
click()

#6.动作链（鼠标拖拽，键盘按键）
from selenium.webdriver import ActionChains
source = browser.find_elements
target = browser.find_elements
#选中要拖拽的节点和拖拽后的目标节点
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
#下拉页面
browser.execute_script("window.scrollBy(0,250)")
browser.execute_script('alert("to bottom")')

#7.获取节点属性，文本值
logo = browser.find_element_by_id('')
print(logo.get_attribute('class'))
print(logo.text)

#8.切换iframe
find_element_by_id()
browser.switch_to.frame()
browser.switch_to.parent_frame()

#9延时等待（分为显示和隐示两种）

#10 前进和后退
browser = webdriver.Chrome('/users/wangkaixi/desktop/chromedriver')
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

#11.cookies
browser.get_cookies()
browser.add_cookie()

#12 选项卡管理
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.taobao.com")
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get("https://python.org")





