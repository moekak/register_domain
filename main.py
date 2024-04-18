from domain_manager import main
main()

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.alert import Alert
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import NoSuchElementException


# # ChromeDriverManagerを使ってChrome Driverのインスタンスを作成
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


# # # chatGptを開く
# # chat_url = "https://chat.openai.com/"
# # driver.get(chat_url)

# # # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# # login_btn = WebDriverWait(driver, 10).until(
# #     EC.presence_of_element_located((By.CLASS_NAME, "btn-neutral"))
# # )
# # driver.execute_script("arguments[0].click();", login_btn)

# # urlを開く
# url = "https://www.value-domain.com/"
# driver.get(url)

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# btn_el = WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#hd_login"))
# )
# driver.execute_script("arguments[0].click();", btn_el)

# # ユーザー名を入力
# input_el = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#username"))
# )
# input_el.send_keys("waipotgangla")

# # パスワードを入力
# pass_el = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#password"))
# )
# pass_el.send_keys("happy3596")

# # ログインボタンをクリック
# login_btn = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#login_submit_btn"))
# )
# driver.execute_script("arguments[0].click();", login_btn)




# register_btn = driver.find_element(by=By.CSS_SELECTOR, value="#cpside_domain_all")
# driver.execute_script("arguments[0].click();", register_btn)

# link_element = driver.find_element(By.XPATH, '//a[text()="ドメインの一括空き検索"]')
# driver.execute_script("arguments[0].click();", link_element)

# domain_data = input("登録ドメインを入力してください スペースで区切ってください）:")

# print(domain_data)

# textarea = driver.find_element(by=By.CSS_SELECTOR, value="#searchArea")

# for data in domain_data.split():
#       input_el = driver.find_element(by=By.CSS_SELECTOR, value="#searchArea")
#       input_el.send_keys(data)
#       input_el.send_keys(Keys.ENTER)

# # ドメイン検索ボタンをクリックする
# result_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_list")))
# driver.execute_script("arguments[0].click();", result_btn)

# # CSSセレクターを使用してdata-tld属性を指定する方法
# tr_elements = driver.find_elements(by=By.CSS_SELECTOR, value='[data-tld_puny]')




# for element in tr_elements:
#       try:
#             price_element = element.find_element(By.CSS_SELECTOR, ".price")
#             price_text = price_element.text.replace("円", "")
#       except NoSuchElementException:
#             print("Price element not found in this row")
#             continue

#       if int(price_text) <= 550:
#             purchase_btn = WebDriverWait(driver, 10).until(
#                   EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_check02_entry"))
#             )
#             driver.execute_script("arguments[0].scrollIntoView(true);", purchase_btn)
#             driver.execute_script("arguments[0].click();", purchase_btn)

#             domain_data_list = domain_data.split()

#             for data in domain_data_list:
#                   textarea_el = driver.find_element(by=By.NAME, value="domains")
#                   textarea_el.send_keys(data)
#                   textarea_el.send_keys(Keys.ENTER)

                  

#             # 次の画面で価格表示・登録者情報を設定するボタンをクリックする
#             next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "modglobal3")))
#             print(next_btn)
#             driver.execute_script("arguments[0].click();", next_btn)

#             # 名義を代理公開する
#             open_el = driver.find_element(by=By.XPATH, value="//a[@href='#end']")

#             actions = ActionChains(driver)
#             # 要素までスクロール
#             actions.move_to_element(open_el).perform()
#             driver.execute_script("arguments[0].click();", open_el)

#             # アラートを取得
#             alert = Alert(driver)

#             # アラートのOKボタンをクリック
#             alert.accept()

#             # 次の画面で価格表示・登録者情報を設定するボタンをクリックする
#             register_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_list02_entry")))
#             driver.execute_script("arguments[0].click();", register_btn)

#             # アラートのOKボタンをクリック
#             alert.accept()



#             success_el = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, "domains_list_success")))
#             domain_data = success_el.text
#             domain_list = domain_data.split()

#             print(domain_list)
#             print(type(domain_list))

      

#             input("press btn to stop")


















