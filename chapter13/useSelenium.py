from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://en.wikipedia.org/wiki/Monty_Python")
assert "Monty Python " in driver.title
driver.close()


# usernameField = driver.find_element_by_name('username')
# myElement.click()
# myElement.click_and_hold()
# myElement.release()
# myElement.double_click()
# myElement.send_keys_to_element("content to enter")
