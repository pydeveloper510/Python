import logging

logging.basicConfig(
    filename='HISTORYlistener.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

####################################################################################################

import logging

class MyFormatter(logging.Formatter):
    def format(self, record):
        record.message2 = ""
        if(record.args):
            record.func_name = record.args.get("func_name", "Fallback Value")
        return super().format(record)

logger = logging.getLogger()
fh = logging.FileHandler(filename='log.txt', mode='a')
fh.setFormatter(MyFormatter('%(asctime)s --- %(func_name)s --- %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.basicConfig(level=logging.INFO, handlers=[fh])

def write_log(func_name, message):
    logger.info(message, {"func_name": func_name})
    

####################################################################################################
# log daily
current_dir = os.path.dirname(os.path.realpath(__file__))
current_file = os.path.basename(__file__)
current_file_name = current_file[:-3]  # xxxx.py

LOG_FILENAME = '{}.log'.format(datetime.now().strftime("%Y_%m_%d"))

log_dir = '{}/logs'.format(current_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# create logger
myLogger = logging.getLogger() # logger name: test
myLogger.setLevel(logging.DEBUG) # logger lvl: DEBUG

# create handler
file_handler = logging.handlers.TimedRotatingFileHandler(
  filename=log_dir + '/' + LOG_FILENAME, when='midnight', interval=1,  encoding='utf-8'
  ) # 자정마다 한 번씩 로테이션
# file_handler.suffix = 'log-%Y%m%d' # set suffix

myLogger.addHandler(file_handler) # add handler on logger
formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s')
file_handler.setFormatter(formatter) # set format on logger
# 2019-08-11 - INFO - [test.py:37] Hello! This is my script.

