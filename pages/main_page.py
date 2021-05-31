import random
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import datetime

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_number = '0123456789'
name = '@mir.ru'
email = ''.join([random.choice(ascii_lowercase) for e in range(4)])
number_phone = ''.join([random.choice(ascii_number) for n in range(10)])
inn = ''.join([random.choice(ascii_number) for i in range(12)])
kpp = ''.join([random.choice(ascii_number) for k in range(9)])
bik = ''.join([random.choice(ascii_number) for b in range(9)])
account = ''.join([random.choice(ascii_number) for a in range(20)])
cor_bank = ''.join([random.choice(ascii_number) for c in range(20)])


class MainPage(BasePage):

    def should_be_register_legal(self):
        private_cab = self.browser.find_element(By.CSS_SELECTOR, 'a[class="logo"]')
        time.sleep(2)
        private_cab.click()

        button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/button')
        button.click()

        link = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/form/div[6]/a')
        link.click()

        select = Select(self.browser.find_element(By.TAG_NAME, 'select'))
        select.select_by_value('legal')

        input_company_name = self.browser.find_element(By.ID, 'company-name')
        input_company_name.send_keys('Очень серьезная компания')

        select_company = Select(self.browser.find_element(By.ID, 'company_type'))
        select_company.select_by_value('2')

        select_position = Select(self.browser.find_element(By.ID, 'company-signature_position_id'))
        select_position.select_by_value('2')

        input_fio = self.browser.find_element(By.ID, 'company-signatory_name')
        input_fio.send_keys('Роман Ко Михайлович')

        input_contact_face = self.browser.find_element(By.ID, 'company-contact_person')
        input_contact_face.send_keys('Роман Ко Михайлович')

        input_email = self.browser.find_element(By.ID, 'user-email')
        input_email.send_keys(f'{email}@mir.ru')

        input_phone = self.browser.find_element(By.ID, 'userprofile-phone')
        time.sleep(5)
        input_phone.send_keys(f'{number_phone}')

        input_leg_address = self.browser.find_element(By.ID, 'company-legal_address')
        input_leg_address.send_keys('г. Краснодар, ул. Ставропольская, д. 315')

        input_fact_address = self.browser.find_element(By.ID, 'actual_address')
        input_fact_address.send_keys('г. Краснодар, ул. Ставропольская, д. 315')

        input_inn = self.browser.find_element(By.ID, 'company-inn')
        input_inn.send_keys(f'{inn}')

        input_kpp = self.browser.find_element(By.ID, 'company-kpp')
        input_kpp.send_keys(f'{kpp}')

        input_name_bank = self.browser.find_element(By.ID, 'company-bank_name')
        input_name_bank.send_keys('ПАО СБЕРБАНК')

        input_bik_bank = self.browser.find_element(By.ID, 'company-bik')
        input_bik_bank.send_keys(f'{bik}')

        input_account_bank = self.browser.find_element(By.ID, 'company-bank_account')
        input_account_bank.send_keys(f'{account}')

        input_cor_bank = self.browser.find_element(By.ID, 'company-correspondent_account')
        input_cor_bank.send_keys(f'{cor_bank}')

        input_password = self.browser.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div[4]/div[2]/form/div[11]/div[1]/div/input')
        input_password.send_keys('CORoo90909')

        input_password_repeat = self.browser.find_element(By.XPATH,
                                                          '/html/body/div[1]/div[2]/div/div[4]/div[2]/form/div[11]/div[2]/div/input')
        input_password_repeat.send_keys('CORoo90909')

        button_reg = self.browser.find_element(By.CSS_SELECTOR, '#signup-button .button__text')
        time.sleep(2)
        button_reg.click()

        message = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]').text
        print(message)
        mess = 'Вы успешно'
        assert mess in message

    def should_be_approval_of_the_application(self):
        input_log = self.browser.find_element(By.ID, 'loginform-username')
        input_log.send_keys('webmaster')

        input_pass = self.browser.find_element(By.ID, 'loginform-password')
        input_pass.send_keys('X2e66Ep4r')

        button_enter = self.browser.find_element(By.CSS_SELECTOR, '[name="login-button"]')
        time.sleep(2)
        button_enter.click()

        button_personal_company = self.browser.find_element(By.CSS_SELECTOR, '[href="/company/index/"]')
        button_personal_company.click()

        # input_id_company = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div/div/div/div/table/thead/tr[2]/td[2]/input')
        # input_id_company.send_keys(308)
        # input_enter = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div/div/div/div/table/thead/tr[2]/td[2]/input')
        # input_enter.send_keys(u'\ue007')

        button_edit = self.browser.find_element(By.CLASS_NAME, 'glyphicon.glyphicon-pencil')
        button_edit.click()

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_edit_2 = self.browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
        button_edit_2.click()

        button_conf = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div/div/div/p[2]/a')
        button_conf.click()

        button_sign = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div/div/div/p[2]/a')
        button_sign.click()

        contract = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div/div/div/table/tbody/tr[5]/td').text
        answer = 'Да'

        assert contract == answer

    def should_be_authorization(self):
        private_cab = self.browser.find_element(By.CSS_SELECTOR, 'a[class="logo"]')
        time.sleep(2)
        private_cab.click()

        button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/button')
        button.click()

        input_email = self.browser.find_element(By.ID, 'loginform-email')
        input_email.send_keys(f'{email}@mir.ru')

        input_password = self.browser.find_element(By.ID, 'loginform-password')
        input_password.send_keys('CORoo90909')

        button_auth = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/form/div[5]/button/span')
        time.sleep(2)
        button_auth.click()

        button_setting = self.browser.find_element(By.XPATH, '/html/body/header/div[2]/div/div[2]/ul/li[1]/a').text
        button_set = 'Настройки'
        assert button_setting == button_set

        button_add = self.browser.find_element(By.XPATH, '/html/body/header/div[2]/div/div[2]/ul/li[2]/a').text
        button_add_comp = 'Добавить кампанию'
        assert button_add == button_add_comp

    def should_be_add_campaign(self):
        private_cab = self.browser.find_element(By.CSS_SELECTOR, 'a[class="logo"]')
        time.sleep(2)
        private_cab.click()

        button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/button')
        button.click()

        input_email = self.browser.find_element(By.ID, 'loginform-email')
        input_email.send_keys(f'{email}@mir.ru')

        input_password = self.browser.find_element(By.ID, 'loginform-password')
        input_password.send_keys('CORoo90909')

        button_auth = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/form/div[5]/button/span')
        time.sleep(2)
        button_auth.click()

        button_personal_area = self.browser.find_element(By.CLASS_NAME, 'header-user__name')
        button_personal_area.click()

        option_personal_area = self.browser.find_element(By.XPATH, '/html/body/header/div[1]/div[2]/div[2]/div/a[1]/span[1]')
        option_personal_area.click()

        button_add_campaign = self.browser.find_element(By.XPATH, '/html/body/header/div[2]/div/div[2]/ul/li[2]/a')
        button_add_campaign.click()

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        input_name_campaign = self.browser.find_element(By.ID, 'advert-name')
        input_name_campaign.send_keys('Плюшки')

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_type_ad = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div/div/div[1]')
        button_type_ad.click()

        button_banner = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div/div/div[2]/ul/li[4]')
        button_banner.click()
        time.sleep(2)

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        input_file = self.browser.find_element(By.ID, 'advertFileInput-123')
        input_file.send_keys(r'C:\Users\123\Desktop\Work\octa_add\plushki.jpg')

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        input_show = self.browser.find_element(By.ID, 'advert-impressions_count')
        input_show.send_keys('10')

        today = datetime.datetime.today()
        self.browser.execute_script(f"$('#advert-start_date').val('{today.day+1}.{today.month}.2021')")

        self.browser.execute_script(f"$('#advert-end_date').val('01.{today.month+1}.2021')")

        input_show_personal = self.browser.find_element(By.ID, 'advert-views_per_user_count')
        input_show_personal.send_keys('2')

        select_show_personal = Select(self.browser.find_element(By.ID, 'advert-sex_id'))
        select_show_personal.select_by_value("null")

        input_min_old = self.browser.find_element(By.ID, 'advert-min_age')
        input_min_old.send_keys('18')

        input_max_old = self.browser.find_element(By.ID, 'advert-max_age')
        input_max_old.send_keys('50')

        input_region = self.browser.find_element(By.ID, 'advert-regionids')
        input_region.click()
        # self.browser.execute_script("$('form-checkbox__title').val('Адыгея')")
        # time.sleep(2)

        input_region_cl = self.browser.find_element(By.CSS_SELECTOR, '.form-input.js-suggestSearch')
        input_region_cl.send_keys('Адыгея')

        self.browser.find_element(By.CSS_SELECTOR, '.form-suggest__body ul li:nth-child(1)').click()

        select_food = Select(self.browser.find_element(By.ID, 'advert-advert_category_id'))
        select_food.select_by_visible_text("Еда и напитки")

        button_send = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/form/div[6]/div[6]/button')
        button_send.click()

        success_add = self.browser.find_element(By.CSS_SELECTOR, '.page-info__title').text
        add_exp = 'Модерация рекламной кампании'
        assert success_add == add_exp

