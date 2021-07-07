from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

def clickButton(xpath, time):
    global driver
    driver.find_element_by_xpath(xpath).click()
    sleep(time)

def logIn(username, password):
    global driver
    clickButton("/html/body/div[3]/div/div/button[1]", 2)
    clickButton("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[1]/a", 2)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
    clickButton("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button", 4)
    clickButton("/html/body/div[1]/div/div/section/main/div/div/div/div/button", 2)
    clickButton("/html/body/div[4]/div/div/div/div[3]/button[2]", 2)


driver = webdriver.Firefox(executable_path= r"C:\Users\daniel\PycharmProjects\SystemMonitor\geckodriver.exe")
driver.get(('https://www.instagram.com/instagram'))
logIn("insert username here", "insert password here")
sleep(2)
