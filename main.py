# THIS CODE TAKES 45 SECONDS TO FULLY LAUNCH AND SET THE INDICATORS,
# SO RUN IT WHEN THERE ARE 45-50 SECONDS REMAINING ON THE CANDLE



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())


import os
import time
import datetime
import smtplib

os.environ['PATH'] += r"C:/Users/REMOVED/chromedriver_win32"
now = datetime.date(2022, 5, 19)

Server = 'smtp.gmail.com'
PORT = 587
FROM = 'REMOVED'
TO = 'REMOVED'
TO1 = 'REMOVED'
PASS = 'REMOVED'

def generator():
    global driver                              # making driver global and not garbage so it doesn't close at the end
    driver = webdriver.Chrome()

    driver.get('https://in.tradingview.com/')
    time.sleep(2)

    # ops_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/button')
    ops_btn = driver.find_element(By.XPATH, '//*[@id="tv-main-page-promo"]/div[1]/div[2]/div[1]/div/div/div/a[1]/div')
    # driver.find_element(By.XPATH, "element_xpath")
    ops_btn.click()     # Selecting button to open chart
    time.sleep(0.5)

    chrt = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div[2]/span/div[1]/div/div/div/a/div[2]/div')
    chrt.click()        # Clicking chart button
    time.sleep(2)
    '''
    cookie = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/article/div[2]/div/button/span')
    cookie.click()      # Accepting cookies because the pop up is fkn annoying
    time.sleep(1)
    '''
    chart_name = driver.find_element(By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div')
    chart_name.click()  # Clicking chart name to change it to our choice
    time.sleep(1)

    driver.maximize_window()        # Why are you even reading this part?
    time.sleep(0.5)

    text_box = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input')
    text_box.send_keys("SOLBUSD")   # Searching for SOLBUSD chart
    time.sleep(1)

    chart_Load = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[4]/div/div/div[2]/div[1]')
    chart_Load.click()              # Clicking on the chart of our choice
    time.sleep(2)
    
    # TIMEFRAMECHANGETIMEFRAMECHANGETIMEFRAMECHANGETIMEFRAMECHANGETIMEFRAMECHANGETIMEFRAMECHANGETIMEFRAMECHANGE
    change_tf = driver.find_element(By.XPATH, '//*[@id="header-toolbar-intervals"]').click()
    time.sleep(0.4)
    change_tf_click = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]/div/div[1]/div').click()
    time.sleep(2)
    
    indicator_btn = driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]')
    indicator_btn.click()           # Clicking on 'Indicators' tab
    time.sleep(1)

    indicator1_search = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[2]/div/input')
    indicator1_search.send_keys("supertrend")
    time.sleep(3)                   # Indicator search
    sel_ind1 = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[2]/div[1]/span[2]/span[3]')
    sel_ind1.click()                 # Opening supertrend indicator
    time.sleep(3)

    close_ind1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]').click()
    time.sleep(1)

    open_ind2box = driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]/div').click()
    time.sleep(1)           # Opening indicator box to put EMA indicator
    
    indicator2_search = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[2]/div/input').send_keys('ema')
    time.sleep(1)           # Searching for EMA

    sel_ind2 = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[2]/div[1]/span[2]').click()
    time.sleep(1)           # Selecting moving average exponential

    close_ind2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]').click()
    time.sleep(1)           # Closing indiators box

    ind2_set = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]')
    ind2_set.click()        # Opening EMA settings by double clicking
    ind2_set.click()
    time.sleep(1)

    ema_time = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[3]/div/span/span[1]/input')
    ema_time.send_keys(Keys.BACKSPACE)
    ema_time.send_keys("200")   # Setting time as 200
    time.sleep(0.2)
    ema_close = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[4]/div/span/button').click()


    deselecting1 = driver.find_element(By.XPATH, '//*[@id="drawing-toolbar"]/div/div/div/div/div[1]/span[2]/div/div/div[1]/div')
    deselecting1.click()            # Clicking on line drawing tool to remove
    time.sleep(1)                   # selection from indicator box

    deselecting2 = driver.find_element(By.XPATH, '//*[@id="drawing-toolbar"]/div/div/div/div/div[1]/span[1]/div/div/div[1]/div')
    deselecting2.click()            # Clicking on pointer tool to select pointer
    time.sleep(2)

    
    buy_signal = 0                  # Setting buy
    sell_signal = 0                 #             and sell signals to 0

    # Start buy/sell signal search *FUNCTION* here

    while buy_signal == 0 and sell_signal == 0:         # Looking for a signal

        current_price = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]')
        a = current_price.text
        # print(a)

        EMA_val = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]')
        b = EMA_val.text
        # print(b)

        # Determining buy or sell signal *FUNCTION* (Thinking about not applying this function)

        if a > b:               # Current Price > EMA200
            supertrend_long_val = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div')
            #                                                   /html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div
            c = supertrend_long_val.text

            if c == 'n/a':
                # print("No buy signal right now")
                pass
                
            elif float(c) > 0:

                buy_signal = 1
                # pass

        elif b > a:             # EMA200 > Current Price
            supertrend_short_val = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[3]')
            #                                                   /html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[3]
            #                                                   /html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[3]/div
            # print("SELLLLLLL")
            d = supertrend_short_val.text
            # print("SUPERTREND SHORT VALUE = " + d)

            if d == 'n/a':
                # print("No sell signal right now")
                pass
                
            elif float(d) > 0:
                sell_signal = 1
                # pass
        
        # Check and send email *FUNCTION*

        if buy_signal == 1:
            # print("BUY SIGNAL IS HERE")
            buy_email()
            buy_emailm()
            # break                   # Remove this break when adding constantly checking loops

        elif sell_signal == 1:
            # print("SELL SIGNAL IS HERE")
            sell_email()
            sell_emailm()
            # break                   # Remove this break when adding constantly checking loops
       
        else:
            pass

        # Continue checking *FUNCTION*

        while buy_signal == 1 or sell_signal == 1:
            # This loop will keep repeating itself without checking for buy or sell signal again, change it
            # Wait, no it won't. I'm too smart lmao

            if buy_signal == 1:
                
                if c == 'n/a':
                    # print("Buy signal stopped")
                    # pass
                    break
                        
                elif float(c)>0:
                    print("Still buying")
                    time.sleep(300)
                    pass
            
            elif sell_signal == 1:
                if d == 'n/a':
                    print("Sell signal stopped")
                    break
                elif float(d) > 0:
                    print("Still selling")
                    # time.sleep(900)
                    pass                     

    print("CODE COMPLETED")

def buy_email():

    msg = MIMEMultipart()
    msg['SUBJECT'] = 'BUY SOLBUSD '  + str(now)
    msg["FROM"] = FROM
    msg["TO"] = TO
    msg.attach(MIMEText('Buy signal found for SOLBUSD'))

    print("Initialising Server")

    server = smtplib.SMTP(Server, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())

    print("**********\n"*5 + "****BUY MESSAGE SENT****\n" +"**********\n"*5)

    server.quit()


def sell_email():

    msg = MIMEMultipart()
    msg['SUBJECT'] = 'SELL SOLBUSD '  + str(now)
    msg["FROM"] = FROM
    msg["TO"] = TO
    msg.attach(MIMEText('Sell signal found for SOLBUSD'))

    print("Initialising Server")

    server = smtplib.SMTP(Server, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())

    print("**********\n"*5 + "****SELL MESSAGE SENT****\n" +"**********\n"*5)

    server.quit()

def buy_emailm():

    msg = MIMEMultipart()
    msg['SUBJECT'] = 'BUY SOLBUSD '  + str(now)
    msg["FROM"] = FROM
    msg["TO1"] = TO1
    msg.attach(MIMEText('Buy signal found for SOLBUSD'))

    print("Initialising Server")

    server = smtplib.SMTP(Server, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO1, msg.as_string())

    print("**********\n"*5 + "****BUY MESSAGE SENT****\n" +"**********\n"*5)

    server.quit()


def sell_emailm():

    msg = MIMEMultipart()
    msg['SUBJECT'] = 'SELL SOLBUSD '  + str(now)
    msg["FROM"] = FROM
    msg["TO1"] = TO1
    msg.attach(MIMEText('Sell signal found for SOLBUSD'))

    print("Initialising Server")

    server = smtplib.SMTP(Server, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO1, msg.as_string())

    print("**********\n"*5 + "****SELL MESSAGE SENT****\n" +"**********\n"*5)

    server.quit()

generator()
