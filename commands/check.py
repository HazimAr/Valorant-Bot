from commands.base_command import BaseCommand
import random

class Check(BaseCommand):

    def __init__(self):
        description = "Checks valorant stats"
        params = ["user"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            user = params.split("#")[0]; tag = params.split("#")[1]
            url = "https://tracker.gg/valorant/profile/riot/{user}%23{tag}/overview"
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from time import sleep

            driver = webdriver.Chrome("D:/Code/Python/Webscraping/Drivers/chromedriver")
            web = "https://google.com"
            driver.get(web)

            signInX = "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/a"
            googleEmailX = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
            googleNextX = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
            googlePassX = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"

            def Click(xpath):
                driver.find_element_by_xpath(xpath).click()

            def SendKeys(xpath, input):
                driver.find_element_by_xpath(xpath).send_keys(input)

            def Wait(time, xpath):
                WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))

            Wait(10, signInX)
            Click(signInX)
            Wait(10, googleEmailX)
            SendKeys(googleEmailX, 'email@gmail.com')
            Click(googleNextX)
            Wait(10, googlePassX)
            SendKeys(googlePassX, '123')
            Click(googleNextX)
        except:
            msg = "Please send the user in this format**HazAr#1639**"

        await message.channel.send(msg)
