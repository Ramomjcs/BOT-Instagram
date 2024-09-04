from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()  # Sem o parâmetro executable_path

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        
        try:
            login_button = driver.find_element(By.XPATH, "//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except Exception as e:
            print(f"Exceção capturada: {e}. Já estamos na página de login ou algo deu errado.")
        
        user_element = driver.find_element(By.NAME, "username")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)

        password_element = driver.find_element(By.NAME, "password")
        password_element.clear()
        time.sleep(random.randint(4, 6))
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        self.curtir_fotos_com_a_hastag("atualidades")

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print("Iniciando digitação na área de texto...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(5)
        
        for i in range(1, 3):  # Alterar o range conforme necessário
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        hrefs = driver.find_elements(By.TAG_NAME, "a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs if "/p/" in elem.get_attribute("href")]
        print(f"{hashtag} fotos encontradas: {len(pic_hrefs)}")

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(3)
            try:
                like_button = driver.find_element(By.XPATH, "//span[@aria-label='Curtir']")
                like_button.click()
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(f"Erro ao curtir a foto: {e}")
                time.sleep(5)


# Substitua pelas suas credenciais
Bot = InstagramBot("login", "senha")
Bot.login()
