from commands.base_command import BaseCommand
import random
from settings import ranks

class Check(BaseCommand):

    def __init__(self):
        description = "Checks valorant stats"
        params = ["user"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            user = params[0].split("#")[0]; tag = params[0].split("#")[1]
        except:
            msg = "Please send the user in this format **HazAr#1639**"
            await message.channel.send(msg)
            return
        msg = "Please allow up to 5 seconds for us to look up the user"
        await message.channel.send(msg)

        web = f"https://tracker.gg/valorant/profile/riot/{user}%23{tag}/overview?playlist=competitive"

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.options import Options
        import os
        

        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver.get(web)

        rank_xpath = "/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[2]/div[2]/div/div[1]/div[1]/span[2]"

        # def Click(xpath):
        #     driver.find_element_by_xpath(xpath).click()

        # def SendKeys(xpath, input):
        #     driver.find_element_by_xpath(xpath).send_keys(input)

        def Wait(time, xpath):
            WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        try:
            Wait(5, rank_xpath)
        except:
            msg = f"{params[0]} has either never played ranked or is a private account"
            await message.channel.send(msg)
            return
            
        rank = driver.find_element_by_xpath(rank_xpath).text
        driver.quit()
        msg = f"{params[0]} is {rank} or {ranks[rank]}"
        print(msg)
        await message.channel.send(msg)
