'''
@author: soterocra
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

import telepot

class DetranMG:

    DETRAN_URL = "https://www.detran.mg.gov.br/habilitacao/cnh-e-permissao-para-dirigir/acompanhar-entrega-cnh"
    
    DETRAN_CPF_ID = "ConsultarSituacaoCnhCpf"
    DETRAN_BIRTH_DATE_ID = "ConsultarSituacaoCnhDataNascimento"
    DETRAN_BTN_XPATH = "/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[2]/form/div[2]/div[3]/button"
    
    CPF_TEXT = "12345678910"
    BIRTH_DATE_TEXT = "01/01/1991"
    
    DRIVER_PATH = "drivers/chromedriver.exe"
    SCREENSHOT_PATH = "screenshots/last-status-detran.png"  
    
    def __init__(self, headless=False):    
        self.options = Options()
        if headless == True: self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(self.DRIVER_PATH, options=self.options)
        self.driver.implicitly_wait(30)
        
    def get_file_status(self):    
        self.driver.get(self.DETRAN_URL)        
        sleep(3)
        
        self.driver.execute_script("document.getElementById('{id}').value = '{cpf}'".format(id=self.DETRAN_CPF_ID, cpf=self.CPF_TEXT))
        self.driver.execute_script("document.getElementById('{id}').value = '{date}'".format(id=self.DETRAN_BIRTH_DATE_ID, date=self.BIRTH_DATE_TEXT))                           
        self.driver.find_element_by_xpath(self.DETRAN_BTN_XPATH).click()                                
        
        sleep(3)                
    
        self.driver.set_window_size(800, 1080)        
        self.driver.save_screenshot(self.SCREENSHOT_PATH)
        
        self.driver.close()
        
        return open(self.SCREENSHOT_PATH, 'rb')          
        
class TelegramBOT:
    
    TOKEN_BOT = 'SEU_TOKEN_AQUI'
    
    def __init__(self):
        self.bot = telepot.Bot(self.TOKEN_BOT)

    def get_updates(self):
        return self.bot.getUpdates()
    
    def send_photo(self, chat_id, file):        
        self.bot.sendPhoto(chat_id, file)

class App():
        
    WAIT_FOR_NEW_STATUS_IN_SECONDS = 3600
    
    @staticmethod
    def run():                
        bot = TelegramBOT()
        
        chat_id_list = set(map(lambda u: u['message']['chat']['id'], bot.get_updates()))

        while True:
            detran_service = DetranMG(True)
            for chat_id in chat_id_list:                
                bot.send_photo(chat_id, detran_service.get_file_status())                
            sleep(App.WAIT_FOR_NEW_STATUS_IN_SECONDS)

App.run()