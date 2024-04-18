from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
# 環境変数を使うための準備
from dotenv import load_dotenv
import os
load_dotenv()



# グローバル変数の初期化(ユーザーがドメインを入力したとき用)
user_input_data = None
success_domain = None



# ChromeDriverManagerを使ってChrome Driverのインスタンスを作成
def create_webdriver_instance():
      from webdriver_manager.chrome import ChromeDriverManager
      from selenium.webdriver.chrome.service import Service
      service = Service(ChromeDriverManager().install())
      driver = webdriver.Chrome(service=service)
      return driver


# valueドメインにログインする処理
def login_to_site(driver, login_url, username, password):
      # URLにアクセスする
      driver.get(login_url)
      # ログインボタンを押す
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
      login_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#hd_login"))
      )
      driver.execute_script("arguments[0].click();", login_btn)

      # ユーザーネームを入力する
      WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#username"))
      ).send_keys(username)

      # パスワードを入力する
      WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#password"))
      ).send_keys(password)

      #ログインする  
      login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#login_submit_btn"))
      )
      driver.execute_script("arguments[0].click();", login_button)


# 登録したいドメインを入力する処理
def enter_domain_name(driver):
      # ドメイン一括登録ボタンを押す
      register_btn = WebDriverWait(driver, 20).until(
                  EC.presence_of_element_located((By.CSS_SELECTOR, "#cpside_domain_all"))
            )
      driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
      driver.execute_script("arguments[0].click();", register_btn)

      link_element = WebDriverWait(driver, 10).until(
                  EC.presence_of_element_located((By.XPATH, '//a[text()="ドメインの一括空き検索"]'))
            )

      driver.execute_script("arguments[0].click();", link_element)

      #コマンドターミナルから入力されたドメインを返す  
      user_input_data = input("登録ドメインを入力してください スペースで区切ってください）:")  
      return user_input_data

# 登録したいドメインの価格を表示させるための処理
def display_domain_price(driver, user_input_data):
      print(user_input_data)
      for data in user_input_data.split():
            textarea  = driver.find_element(by=By.CSS_SELECTOR, value="#searchArea")
            textarea.send_keys(data)
            textarea.send_keys(Keys.ENTER)

      # ドメイン検索ボタンをクリックする
      result_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_list")))
      driver.execute_script("arguments[0].click();", result_btn)

      # 各ドメインの情報が載ってるtrタグを返す
      return driver.find_elements(by=By.CSS_SELECTOR, value='[data-tld_puny]')


# ドメインの価格が範囲内かチェックする(boolean)
def check_domain_price(driver, user_input_data):
      tr_elements = display_domain_price(driver, user_input_data)
      for element in tr_elements:
            try:
                  price_element = element.find_element(By.CSS_SELECTOR, ".price")
                  price_text = price_element.text.replace("円", "")
            except NoSuchElementException:
                  print("Price element not found in this row")
                  continue

            if int(price_text) <= 550:
                 return True
            else:
                  return False
            
def purchase_domain(driver, user_input_data):
      if(check_domain_price(driver, user_input_data)):
            # 購入ボタンをクリックする」
            purchase_btn = WebDriverWait(driver, 10).until(
                  EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_check02_entry"))
            )
            # ボタンが画面上に表示されてないからその要素までスクロールさせる
            driver.execute_script("arguments[0].scrollIntoView(true);", purchase_btn)
            driver.execute_script("arguments[0].click();", purchase_btn)

            #登録させるドメイン
            domain_data_list = user_input_data.split()

            # ドメインをtextareaに自動で入力させる
            for data in domain_data_list:
                  textarea_el = driver.find_element(by=By.NAME, value="domains")
                  textarea_el.send_keys(data)
                  textarea_el.send_keys(Keys.ENTER)

            # 次の画面で価格表示・登録者情報を設定するボタンをクリックする
            next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "modglobal3")))
            driver.execute_script("arguments[0].click();", next_btn)

            # 名義を代理公開する
            open_el = driver.find_element(by=By.XPATH, value="//a[@href='#end']")
            driver.execute_script("arguments[0].scrollIntoView(true);", open_el)
            driver.execute_script("arguments[0].click();", open_el)

            # アラートを取得
            alert = Alert(driver)
            # アラートのOKボタンをクリック
            alert.accept()

            # 次の画面で価格表示・登録者情報を設定するボタンをクリックする
            register_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_list02_entry")))
            driver.execute_script("arguments[0].click();", register_btn)

            # アラートのOKボタンをクリック
            alert.accept()
      else:
            # ちゃんとした処理を入れる
            print("ドメインが高すぎます。やり直してください")

def process_purchase(driver):
      # ドメイン登録処理に時間かかることがあるから、最大で1分待機させる
      success_el = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, "domains_list_success")))
      # ドメイン処理に成功したドメインを取得
      domain_data = success_el.text
      # 文字列をリストにへんぁん
      domain_list = domain_data.split()

      success_domain = domain_list

      return success_domain


def main():
      driver = create_webdriver_instance()
      login_url = os.getenv("SITE_URL")
      username = os.getenv("LOGIN_ID")
      password = os.getenv("LOGIN_PASSWORD")

      login_to_site(driver, login_url, username, password)
      user_input_data = enter_domain_name(driver)  # 入力を取得
      purchase_domain(driver, user_input_data)
      # # 成功したドメイン
      success_domain = process_purchase(driver)
      input("wwwww")
      # # DNS設定

      dns_data = ""
      
      driver.get(login_url)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
      login_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#hd_login"))
      )
      driver.execute_script("arguments[0].click();", login_btn)


      # ドメインの設定操作
      setting_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cpside_domain_config")))
      driver.execute_script("arguments[0].click();", setting_btn)

      for domain in success_domain:
            # ユーザーネームを入力する
            domain_input_field = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located((By.CSS_SELECTOR, ".w43per"))
            )


            domain_input_field.send_keys(domain)

            search_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btnSubmitBlack")))
            driver.execute_script("arguments[0].click();", search_btn)


            open_btn = WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located((By.XPATH, f"//a[@href='moddns.php?action=moddns2&domainname={domain}']"))
            )
            driver.execute_script("arguments[0].click();", open_btn)
            if(success_domain[0] == domain):
                  dns_data = input("DNS情報を入力してください")
                  print(dns_data)
            
            # DNS情報を入力する
            WebDriverWait(driver, 20).until(
                  EC.visibility_of_element_located((By.CSS_SELECTOR, "#records"))
            ).send_keys(dns_data)


            send_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inputSend")))
            driver.execute_script("arguments[0].scrollIntoView(true);", send_btn)
            driver.execute_script("arguments[0].click();", send_btn)

            if(success_domain[-1] != domain):
                  return_button = WebDriverWait(driver, 60).until(
                        EC.visibility_of_element_located((By.XPATH, f"//a[@href='modall.php']"))
                  )
                  driver.execute_script("arguments[0].click();", return_button)
            else:
                driver.quit() 
            
            


            

      



            





