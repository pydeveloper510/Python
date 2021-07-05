# Python
Python scraping pattern

You can find very usful sample codes in this.
I am using this codes for working.
## Html select tag select method (au scraping)
## Main selenium structrure
## Scroll down selenium (completed have to add)
## String split, convert
## Ip rolling
## solve capcha (using extension)
## session and cookie compare
## CSP disabled
## extension crx add
## extensuib zip add
## login using scrapy
## login method 
## cookie or session expired time, relogin  sleep(5) must
## scrapy period time that send requests
## depends on network speed
## high speed method
## ai testing
## ai sample script
## repeated not find element problem
## AI
## add new tabs on selenium chrome and firefox
## run script on ubuntu
            
   # capcha solver site link
    
    axie import extenstion swap to extension
    extension is handler 0
    
    # username = os.getenv("USERNAME")
        # userProfile = "C:\\Users\\" + username + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    
    upload and download file to google driver
    
## logging
    import logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
    logging.warning('Total time the function({}) was executed: {} minutes {} seconds'.format(func.__name__, minutes, seconds))

## schedule
설치: 
pip install schedule


# 사용방법
import schedule
import time
 
def job():
    print("I'm working...")
 

### 10초에 한번씩 실행
schedule.every(10).second.do(job)
### 10분에 한번씩 실행
schedule.every(10).minutes.do(job)
### 매 시간 실행
schedule.every().hour.do(job)
### 매일 10:30 에 실행
schedule.every().day.at("10:30").do(job)
### 매주 월요일 실행
schedule.every().monday.do(job)
### 매주 수요일 13:15 에 실행
schedule.every().wednesday.at("13:15").do(job)
 

while True:
    schedule.run_pending()
    time.sleep(1)
    
__  @ 2021 06 18 __
