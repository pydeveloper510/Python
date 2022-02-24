# Python
Python scraping pattern

You can find very usful sample codes in here.
I am using this codes for working.
## Html select tag select method (au scraping)
## Main selenium structrure
## Scroll down selenium (completed have to add)
## String split, convert

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
            
    axie import extenstion swap to extension
    extension is handler 0
    
    get user name
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
    
# get tempfile location
# python send payload with requests
# python chunked response decoding(br)
# python 16 to 10
    10_str = int(16_str, 16)
    print(10_str)
# 10 to any
    any_str = "{0:o}".format(10_str) // o -> 8  b-> 2 x -> 16
    print(any_str)
# requests test url
    IP: https://api.myip.com
    all info : https://httpbin.org/
# rpc request 'code': -32602, 'message': 'invalid argument 0: json: cannot unmarshal invalid hex string into Go struct field CallArgs.data of type hexutil.Bytes' ERR
    delete space \n
# version
    일반적으로 앱 버전은 1.0.0 식의 구조를 가지고 있으며 점(.)으로 구분된다.
    <Major Version> . <Minor Version> . <Build or Maintenance Version>
    Major Version: 1부터 시작. 앱 전체 디자인 또는 기능 등이 매우 크게 바뀌는 경우 올림
    Miner Version: 0부터 시작. 기능 추가 기능 변경 등의 경우 올림
    Build or Maintenance Version: 1부터 시작. 자잘한 버그 수정, 코드 보완 등 미미한 변화가 발생한 경우 올림. 패치 버전이라고도 함
# delete space 
    def my_handle(self):
    sentence = ' hello  apple  '
    sentence.strip()
# web3 
send money axie complete
get private key from seed

# pyautogui

get image position
move to image 
click image

get image postion that we want to screenshot on screen
screenshot image
click that image

# action chain
# pyinstaller err
pynput 1.6.8 python 3.8.6
pyinstaller --hidden-import="pynput.keyboard._win32" --hidden-import="pynput.mouse._win32" app.py

pyinstaller --noconfirm --onefile --windowed --icon "H:/Workspace/pythonProject/odin_res/kaka.ico"  "H:/Workspace/pythonProject/odin_res/installer_test.py"

    pyinstaller  --hidden-import="pynput.keyboard._win32" --hidden-import="pynput.mouse._win32" --onefile --windowed --icon "H:/Workspace/pythonProject/odin_res/kaka.ico" main.py

# pynput
mouse controller listener
keyboard controller listener

mouse = m_controller()
mouse.position = (1, 100)
mouse.move(10, 10)
mouse.click(Button.left, 2)
sleep(2)

keyboard = k_controller()
keyboard.press(Key.tab)
sleep(2)
keyboard.press(Key.tab)
sleep(2)
keyboard.press(Key.enter)

# connect mysql db
# send data to db
# write data to db

# pyqt5
fixedsize (rogi project)
QMessagebox
realtime update label text
realtime update table widget (rogi project)
progress bar

# c++ + python
C++ install python native developement
version???
winhttp
add resource file to project

# python remove file
os.remove("./test.txt")


# python listener keyboard click event

def listenKeyboardFunc(self):
    while True:
        if keyboard.read_key() == 'a':
            self.pos = {}
            self.num = 0
            self.clickFlag = 1
            print(self.clickFlag)

        if keyboard.read_key() == 's':
            self.clickFlag = 0
            print(self.clickFlag)

        if keyboard.read_key() == 'd':
            self.clickFlag = -1
            print(self.clickFlag)
            break
                
# websocket

## websocket server (python file)
```
import asyncio;
# 웹 소켓 모듈을 선언한다.
import websockets;
# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
while True:
# 클라이언트로부터 메시지를 대기한다.
data = await websocket.recv();
print("receive : " + data);
# 클라인언트로 echo를 붙여서 재 전송한다.
await websocket.send("echo : " + data);
# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다.
start_server = websockets.serve(accept, "localhost", 9998);
# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();
```
                
 ## websocket client (html file)
 ```
 <!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<form>
<!-- 서버로 메시지를 보낼 텍스트 박스 -->
<input id="textMessage" type="text">
<!-- 전송 버튼 -->
<input onclick="sendMessage()" value="Send" type="button">
<!-- 접속 종료 버튼 -->
<input onclick="disconnect()" value="Disconnect" type="button">
</form>
<br />
<!-- 출력 area -->
<textarea id="messageTextArea" rows="10" cols="50"></textarea>
<script type="text/javascript">
// 웹 서버를 접속한다.
var webSocket = new WebSocket("ws://localhost:9998");
// 웹 서버와의 통신을 주고 받은 결과를 출력할 오브젝트를 가져옵니다.
var messageTextArea = document.getElementById("messageTextArea");
// 소켓 접속이 되면 호출되는 함수
webSocket.onopen = function(message){
messageTextArea.value += "Server connect...\n";
};
// 소켓 접속이 끝나면 호출되는 함수
webSocket.onclose = function(message){
messageTextArea.value += "Server Disconnect...\n";
};
// 소켓 통신 중에 에러가 발생되면 호출되는 함수
webSocket.onerror = function(message){
messageTextArea.value += "error...\n";
};
// 소켓 서버로 부터 메시지가 오면 호출되는 함수.
webSocket.onmessage = function(message){
// 출력 area에 메시지를 표시한다.
messageTextArea.value += "Recieve From Server => "+message.data+"\n";
};
// 서버로 메시지를 전송하는 함수
function sendMessage(){
var message = document.getElementById("textMessage");
messageTextArea.value += "Send to Server => "+message.value+"\n";
//웹소켓으로 textMessage객체의 값을 보낸다.
webSocket.send(message.value);
//textMessage객체의 값 초기화
message.value = "";
}
function disconnect(){
webSocket.close();
}
</script>
</body>
</html>
```
#scrapy response get herf

```
item_urls = response.xpath('//*[@id="component_2"]/div/div/span/div[1]/div[2]/div[1]/div/span/a/@href').getall()
```

__ @ 2021 06 18 __
