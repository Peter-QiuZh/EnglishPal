# -*- coding: utf-8 -*-
# Run the docker image using the following command:
# docker run -d -p 4444:4444 selenium/standalone-chrome
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import random, string

#driver = webdriver.Remote('http://localhost:4444/wd/hub', DesiredCapabilities.FIREFOX)
#driver.implicitly_wait(10)

@pytest.mark.usefixtures
def test_login_security_fix():
    try:
        driver.get(URL)
        
        elem = driver.find_element_by_link_text('登录')
        elem.click()
        
        uname = 'lanhui'
        elem = driver.find_element_by_name('username')
        elem.send_keys(uname)
        
        elem = driver.find_element_by_name('password')
        # 使用原有漏洞密码登录
        elem.send_keys("' or 'a'='a'or'a'='a")
        
        elem = driver.find_element_by_xpath('//form[1]/p[3]/input[1]') # 找到登录按钮
        elem.click()
        
        driver.save_screenshot('./app/test/test_login_security_fix0.png')
        assert '无法通过验证。' in driver.page_source
    finally:
        driver.quit()
