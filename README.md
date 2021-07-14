# Python
Python scraping pattern

You can find very usful sample codes in here.
I am using this codes for working.
## Html select tag select method (au scraping)
## Main selenium structrure
## Scroll down selenium (completed have to add)
## String split, convert
## solve captcha (using extension)
    https://2captcha.com/2captcha-api#solving_hcaptcha
    http://www.hyocr.com/index.php
## session and cookie compare
## CSP disabled
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
    driver.window_handles[0]
    driver.switch_to_window(window_after)
    driver.execute_script('window.open("about:blank", "_blank");')
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
   
# option
    chrome_options.add_argument("--disable-popup-blocking")
# open browser with on your local chrome.exe
    try:
      shutil.rmtree(r"c:\chrometemp")  # delete cache file
    except FileNotFoundError:
      pass

    subprocess.Popen(
    r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    r' --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')  # debuger

     option = Options()
    # option.add_extension(r'assets\extension\1.1.6_0.crx')
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    try:
      self.main_driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    except:
    chromedriver_autoinstaller.install(True)
    self.main_driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    self.main_driver.implicitly_wait(10)

# multi thread (Qthread) pyqt5 
            from PyQt5.QtCore import QObject, QThread, pyqtSignal
            # Snip...

            # Step 1: Create a worker class
            class Worker(QObject):
                finished = pyqtSignal()
                progress = pyqtSignal(int)

                def run(self):
                    """Long-running task."""
                    for i in range(5):
                        sleep(1)
                        self.progress.emit(i + 1)
                    self.finished.emit()

            class Window(QMainWindow):
                # Snip...
                def runLongTask(self):
                    # Step 2: Create a QThread object
                    self.thread = QThread()
                    # Step 3: Create a worker object
                    self.worker = Worker()
                    # Step 4: Move worker to the thread
                    self.worker.moveToThread(self.thread)
                    # Step 5: Connect signals and slots
                    self.thread.started.connect(self.worker.run)
                    self.worker.finished.connect(self.thread.quit)
                    self.worker.finished.connect(self.worker.deleteLater)
                    self.thread.finished.connect(self.thread.deleteLater)
                    self.worker.progress.connect(self.reportProgress)
                    # Step 6: Start the thread
                    self.thread.start()

                    # Final resets
                    self.longRunningBtn.setEnabled(False)
                    self.thread.finished.connect(
                        lambda: self.longRunningBtn.setEnabled(True)
                    )
                    self.thread.finished.connect(
                        lambda: self.stepLabel.setText("Long-Running Step: 0")
                    )
# pyqt5 item disabled Qthread usage
# 2captcha API
# cloudflare captcha
    javascript callback funtion they encript token in callback function ???
    
# get tempfile location
# python send payload with requests


__ @ 2021 06 18 __
