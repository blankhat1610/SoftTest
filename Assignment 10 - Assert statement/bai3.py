from selenium import webdriver

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.set_window_size(1500, 1000)
a = 'width' + ':' + '1500' + ',' + 'height' + ':' + '1000'
assert a in driver.get_window_size()
driver.close()
