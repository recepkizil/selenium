BASE_URL="https://www.saucedemo.com/"

username_id="user-name"
password_id="password"
login_button_id="login-button"

errorMessage_xpath = "//*[@id='login_button_container']/div/form/div[3]/h3"
errorMessage_text = "Epic sadface: Username and password do not match any user in this service"

blank_error_text_xpath = "//*[@id='login_button_container']/div/form/div[3]/h3"
blank_error_text = "Epic sadface: Username is required"

blank_password_text_xpath = "//*[@id='login_button_container']/div/form/div[3]/h3"
blank_password_text = "Epic sadface: Password is required" 


locked_user_text_xpath = "//*[@id='login_button_container']/div/form/div[3]/h3"
locked_user_text = "Epic sadface: Sorry, this user has been locked out."

order_confirm_xpath = "//h2[@class='complete-header']"
order_confirm_message_text= "Thank you for your order!"
