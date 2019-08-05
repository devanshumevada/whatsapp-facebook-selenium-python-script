from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

contact = input('Enter the name of Contact')
msg = input('Enter message')
number_of_times = int(input('Enter how many times do you want to send this message'))

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(contact))
user.click()

typing_area = driver.find_element_by_class_name('_3u328')

for i in range(number_of_times):
    typing_area.send_keys(msg)
    btn = driver.find_element_by_class_name('_3M-N-')
    btn.click()



   