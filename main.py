from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ChromeDriverManagerを使ってChrome Driverのインスタンスを作成
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# # chatGptを開く
# chat_url = "https://chat.openai.com/"
# driver.get(chat_url)

# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# login_btn = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "btn-neutral"))
# )
# driver.execute_script("arguments[0].click();", login_btn)

# urlを開く
url = "https://www.value-domain.com/"
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

btn_el = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#hd_login"))
)
driver.execute_script("arguments[0].click();", btn_el)

# ユーザー名を入力
input_el = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#username"))
)
input_el.send_keys("waipotgangla")

# パスワードを入力
pass_el = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#password"))
)
pass_el.send_keys("happy3596")

# ログインボタンをクリック
login_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#login_submit_btn"))
)
driver.execute_script("arguments[0].click();", login_btn)

register_btn = driver.find_element(by=By.CSS_SELECTOR, value="#cpside_domain_all")
driver.execute_script("arguments[0].click();", register_btn)

link_element = driver.find_element(By.XPATH, '//a[text()="ドメインの一括空き検索"]')
driver.execute_script("arguments[0].click();", link_element)

domain_data = input("登録ドメインを入力してください スペースで区切ってください）:")

print(domain_data)

textarea = driver.find_element(by=By.CSS_SELECTOR, value="#searchArea")

for data in domain_data.split():
      input_el = driver.find_element(by=By.CSS_SELECTOR, value="#searchArea")
      input_el.send_keys(data)
      input_el.send_keys(Keys.ENTER)

# ドメイン検索ボタンをクリックする
result_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchdom_list")))
driver.execute_script("arguments[0].click();", result_btn)

input("press btn to stop")
