from selenium import webdriver
import time

recipient = input("Enter the recipient's email address: ")
subject = input('Enter the subject: ')
message_text = input('Enter the message text: ')

# Open the browser
browser = webdriver.Firefox()
browser.get('https://mx.sdf.org/sm/src/login.php')

# Log in with one's email address and password
email_elem = browser.find_element_by_name('login_username')
email_elem.send_keys('username')        # insert username here
password_elem = browser.find_element_by_name("secretkey")
password_elem.send_keys("password") # insert password here
password_elem.submit()

# Find the compose button.
time.sleep(3)
browser.switch_to.frame('right')
compose_button_elem = browser.find_element_by_link_text("Compose")
compose_button_elem.click()

# Enter the desired email into the To: field
time.sleep(2)
to_elem = browser.find_element_by_name('send_to')
to_elem.send_keys(recipient)

# Enter the subject
subject_elem = browser.find_element_by_name('subject')
subject_elem.send_keys(subject)

# Enter the message text
message_elem = browser.find_element_by_name('body')
message_elem.send_keys(message_text)

# Send the email
send_elem_button = browser.find_element_by_name('send')
send_elem_button.click()
print('Sending email...')
print('Email sent!')
print('Closing browser window...')
browser.quit()
