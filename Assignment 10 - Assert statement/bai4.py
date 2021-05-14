from selenium import webdriver

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
print(driver.title)
assert "Automation Practice Site" in driver.title
driver.close()
