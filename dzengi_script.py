import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dzengi.com")

wait = WebDriverWait(driver, 20)

# Dzengi.com:Checklist_Main_Page
## Main Banner #1
### 1 Display button [Start Trading Now] on Banner #1
#### Click Paginator_00 on banner
try:
    paginator_00 = wait.until(EC.element_to_be_clickable((By.ID, 'slick-slide-control00')))
    paginator_00.click()
    print("Paginator_00 is clicked")
except:
    print("Paginator not displayed")

# Display check and click "Start trading" button
try:
    MB_1_StartTrading_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-type="hp_banner_platform"]')))
    MB_1_StartTrading_Btn.click()
    time.sleep(1)
    print("Main Banner 'Start Trading' is displayed and clicked")
except:
    print("Main Banner 'Start Trading' button is not displayed")

#Close Sign up modal window
try:
    Close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.s_cancel')))
    Close_btn.click()
    time.sleep(1)
    print("Close button of'Sign up' modal window is clicked")
except:
    print("Close button of'Sign up' modal window is NOT found")

##################################################################

### 1 Display and click button [DEMO] on Banner #1
#### Click Paginator_01 on banner
try:
    paginator_00 = wait.until(EC.element_to_be_clickable((By.ID, 'slick-slide-control00')))
    paginator_00.click()
    print("Paginator_00 is clicked")
except:
    print("Paginator not displayed")

# Display check and click "Start trading" button
try:
    MB_1_DEMO_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-type="hp_banner_platform_demo"]')))
    MB_1_DEMO_Btn.click()
    time.sleep(1)
    print("Main Banner 'DEMO' button is displayed and clicked")
except:
    print("Main Banner 'DEMO' button is not displayed")

#Close Sign up modal window
try:
    Close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.s_cancel')))
    Close_btn.click()
    time.sleep(1)
    print("Close button of'Sign up' modal window is clicked")
except:
    print("Close button of'Sign up' modal window is NOT found")

##################################################################

### 1 Display and click Trustpilot button on Banner #1
#### 
try:
    paginator_00 = wait.until(EC.element_to_be_clickable((By.ID, 'slick-slide-control00')))
    paginator_00.click()
    print("Paginator_00 is clicked")
except:
    print("Paginator not displayed")

# Display check and click "Trustpilot" button
try:
    MB_1_Trustpilot_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#slick-slide00 div.trustpilot.js-trustpilot_banner')))
    MB_1_Trustpilot_Btn.click()
    time.sleep(1)
    print("Main Banner 'Trustpilot' button is displayed and clicked")
except:
    print("Main Banner 'Trustpilot' button is not displayed")

#Check that page is scrolled to comments
# Replace 'your_element_locator' with a method to locate your element (e.g., By.ID, By.XPATH, By.CSS_SELECTOR)
try:
    carousel_1 = driver.find_element(By.CSS_SELECTOR, '.visualMarketBlock')
    wait.until(EC.visibility_of(carousel_1))
    carousel_1.is_displayed()
    print('Carousel_1 is displayed')
    time.sleep(1)
except:
    print('carousel_1 is not visible')