from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Getting email-id
your_email= input('Enter your email')
#Getting password
password= input('Enter your password')
#Getting friend name
friend_name= input("Enter your friend's full name")

#Firefox
driver= webdriver.Firefox()
driver.implicitly_wait(30)
#Getting Facebook
driver.get('http://www.facebook.com')
e_mail= driver.find_element_by_id('email')
#Entering Email-id
e_mail.send_keys(your_email)
#Entering Password
passwdd= driver.find_element_by_id('pass')
passwdd.send_keys(password)
#Logging IN
passwdd.send_keys(Keys.ENTER)
#Wait till page loads completely
driver.implicitly_wait(30)
#Entering Friend's name
friend= driver.find_element_by_id('u_0_8')
friend.send_keys(friend_name)
friend.send_keys(Keys.ENTER)
#Finding friend amongst all (See ALL)
see_all= driver.find_element_by_class_name('_5dw8')
see_all.click()
#Clicking on friend's name
name= driver.find_element_by_class_name('_32mo')
name.click()
#Getting info
birthday= driver.find_element_by_id('intro_container_id')
print(birthday.text)
