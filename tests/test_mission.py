# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get(
            "http://localhost:8069/web#cids=1&menu_id=147&action=196&model=mission.delegation&view_type=form")
        self.driver.implicitly_wait(150)
        time.sleep(3)
        self.driver.find_element(By.NAME, "chef").click()
        self.driver.find_element(By.ID, "ui-id-9").click()
        self.driver.find_element(By.NAME, "type_mission_id").click()
        self.driver.find_element(By.ID, "ui-id-16").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "trajet").click()
        self.driver.find_element(By.NAME, "trajet").send_keys("Dakar-Fatick-Dakar")
        time.sleep(2)
        self.driver.find_element(By.NAME, "motif").click()
        self.driver.find_element(By.NAME, "motif").send_keys("Test automation")
        time.sleep(2)
        moyen = Select(self.driver.find_element(By.NAME, "moyen_transport"))
        moyen.select_by_index(3)
        # self.driver.find_element(By.NAME, "moyen_transport").send_keys("Voiture")
        time.sleep(5)
        self.driver.find_element(By.NAME, "date_depart").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .day:nth-child(5)").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "date_retour").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > .day:nth-child(7)").click()
        time.sleep(4)
        self.driver.find_element(By.NAME, "lieu_depart").click()
        self.driver.find_element(By.ID, "ui-id-22").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "lieu_arrive").click()
        self.driver.find_element(By.ID, "ui-id-32").click()
        time.sleep(2)
        # self.driver.find_element(By.NAME, "o_datepicker_button").click()
        # self.driver.find_element(By.NAME, "date_depart").get_attribute('')
        self.driver.find_element(By.LINK_TEXT, "EQUIPE DE LA MISSION").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".o_data_cell:nth-child(3) .o_input").click()
        # self.driver.find_element(By.ID, "ui-id-17").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Ajouter une ligne").click()
        # self.driver.find_element(By.NAME, "employee_id").click()
        # self.driver.find_element(By.ID, "ui-id-10").click()
        self.driver.find_element(By.CSS_SELECTOR, ".o_data_cell:nth-child(3) .o_input").click()
        self.driver.find_element(By.ID, "ui-id-18").click()  # ui-id-17 , ui-id-18, ui-id-19
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "VEHICULES DE LA MISSION").click()
        self.driver.find_element(By.LINK_TEXT, "Ajouter une ligne").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Carburant").click()
        self.driver.find_element(By.LINK_TEXT, "Ajouter une ligne").click()
        # self.driver.find_element(By.NAME, "employee_id").click()
        time.sleep(5)
