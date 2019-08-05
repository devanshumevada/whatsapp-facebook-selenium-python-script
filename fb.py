from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://facebook.com/')

email = 'type in your email here'
password = 'type in your password here'

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_xpath('//input[@value="Log In"]').click()