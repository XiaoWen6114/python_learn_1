from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print('date:')
x1=input("month:")
x2=input('day:')


options=Options()
options.add_argument("--headless=new")
print('Start!')
url=r'https://flights.ctrip.com/online/list/oneway-csx-syx?depdate=2024-'+x1+'-'+x2+'&cabin=y_s_c_f&adult=1&child=0&infant=0'
driver = webdriver.Chrome(options=options) 
driver.set_window_size(500, 1500)

print('Getting url...')
driver.get(url)
time.sleep(3)
print(driver.current_url)

WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "plane-No"))
)
message=[]
js = "return document.body.scrollHeight"
new_height = driver.execute_script(js)
for i in range(0, new_height*2, 30):
    driver.execute_script('window.scrollTo(0, %s)' % i)
time.sleep(6)

#eps = driver.find_elements(by=By.XPATH,value='//a[@rel="noreferrer noopener"]')
flights = driver.find_elements(by=By.XPATH,value="//span[@class='plane-No']")
depTime = driver.find_elements(by=By.XPATH,value='//div[@class="depart-box"]/div[@class="time"]')
arrTime = driver.find_elements(by=By.XPATH,value='//div[@class="arrive-box"]/div[@class="time"]')
prices = driver.find_elements(by=By.XPATH,value='//span[@class="price"]')
def txt(a):
    b=[]
    for i in a:
        b.append(i.text)
    return b
f=txt(flights)
d=txt(depTime)
a=txt(arrTime)
p=txt(prices)
mess = list(zip(f,d,a,p))
time.sleep(1)
driver.quit()
message.extend(mess)
print(message)
def cpy(a):
    b=''
    for i in a:
        b=b+str(i)+'\n'
    import pyperclip as pc
    pc.copy(b)
cpy(message)
