from datetime import datetime
import logging.handlers
import logging
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
current_file = os.path.basename(__file__)
current_file_name = current_file[:-3]  # (filename).py

LOG_FILENAME = '{}.log'.format(datetime.now().strftime("%Y_%m_%d"))
SEND_LOG_FILENAME = '{}send.log'.format(datetime.now().strftime("%Y_%m_%d"))

log_dir = '{}/logs'.format(current_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# create logger
myLogger = logging.getLogger('dev')  # logger name: test
sendLogger = logging.getLogger('pub')
myLogger.setLevel(logging.DEBUG)  # logger lvl: DEBUG
sendLogger.setLevel(logging.DEBUG)  # logger lvl: DEBUG

# create file handler
file_handler = logging.handlers.TimedRotatingFileHandler(
  filename=log_dir + '/' + LOG_FILENAME, when='midnight', interval=1,  encoding='utf-8'
  )  # rotation logger name daily
send_file_handler = logging.handlers.TimedRotatingFileHandler(
  filename=log_dir + '/' + SEND_LOG_FILENAME, when='midnight', interval=1,  encoding='utf-8'
  )  # rotation logger name daily
# file_handler.suffix = 'log-%Y%m%d' # set suffix on filename

# create stream handler
stream_handler = logging.StreamHandler()

myLogger.addHandler(file_handler)  # add file handler on logger
sendLogger.addHandler(send_file_handler)
myLogger.addHandler(stream_handler)  # add stream handler on logeer
sendLogger.addHandler(stream_handler)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s')
file_handler.setFormatter(formatter)  # set format on logger
send_file_handler.setFormatter(formatter)
# 2019-08-11 - INFO - [test.py:37] Hello! This is my script.
