from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://pythonscraping.com/pages/javascript/draggableDemo.html")

print(driver.find_element_by_id("message").text)

element = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("div2")
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()
driver.get_screenshot_as_file('pythonscraping.png')  # 截屏
print(driver.find_element_by_id("message").text)
driver.close()
