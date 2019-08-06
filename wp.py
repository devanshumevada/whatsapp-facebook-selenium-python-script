from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

contact = input('Enter the name of Contact')


user = driver.find_element_by_xpath('//span[@title="{}"]'.format(contact))
user.click()

typing_area = driver.find_element_by_class_name('_3u328')

while True:
    msg = input('Please enter your message: ')
    if msg=='exit':
        break
    else:
        typing_area.send_keys(msg)
        btn = driver.find_element_by_class_name('_3M-N-')
        btn.click()



   
