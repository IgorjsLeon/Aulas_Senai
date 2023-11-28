from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Abrindo o navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
navegador = webdriver.Chrome(options=options)

#Abrindo o site pelo navegador
navegador.get('https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&ifkv=ASKXGp2Y4j60IfToLFj2XOeVSjQF2eDDSgTOoTc7EVlWfuURlS4QhS3FdcL6XUUdpCxmoeGiGFUpaw&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(1)

#seleciona o campo email
try:
    elemento = navegador.find_element(By.ID, 'identifierId')

    #Digite no campo email
    elemento.send_keys("joaquin@gmail.com")
    time.sleep(1)

    #Da enter
    elemento.send_keys(Keys.RETURN)
    time.sleep(3)

finally:
    navegador.close()
