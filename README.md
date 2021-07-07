# Python
Python scraping pattern

You can find very usful sample codes in this.
I am using this codes for working.
## Html select tag select method (au scraping)
## Main selenium structrure
## Scroll down selenium (completed have to add)
## String split, convert
## Ip rolling
## solve captcha (using extension)
            https://2captcha.com/2captcha-api#solving_hcaptcha
## session and cookie compare
## CSP disabled
## extension crx add
            options.add_extension(r'assets\extension\1.1.6_0.crx')
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
    
## schedule
Install: 
pip install schedule


# Usage
import schedule
import time
 
def job():
    print("I'm working...")
 

### Running per 10 seconds
schedule.every(10).second.do(job)
### Running per 10 minutes
schedule.every(10).minutes.do(job)
### Running per hour
schedule.every().hour.do(job)
### Running at 10:30 oclock everyday
schedule.every().day.at("10:30").do(job)
### Running every on monday
schedule.every().monday.do(job)
### Running on wednesday 13:15
schedule.every().wednesday.at("13:15").do(job)
 

while True:
    schedule.run_pending()
    time.sleep(1)
    
__  @ 2021 06 18 __
