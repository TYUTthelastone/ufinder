import logging
import logging.handlers;
import sys
import os
import time
def init():
    log_file = f"log/log_{time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())}.log"
    if not os.path.exists("log"):
        os.mkdir("log")
    handler_test = logging.handlers.RotatingFileHandler(filename=log_file,maxBytes=10*1024*1024,backupCount=30) # stdout to file
    handler_control = logging.StreamHandler()    # stdout to console
    handler_test.setLevel(logging.DEBUG)               # 设置ERROR级别
    handler_control.setLevel(logging.DEBUG)             # 设置INFO级别
    
    fmt = "[%(thread)d] %(asctime)s [%(levelname)s] %(message)s"
    formatter = logging.Formatter(fmt)
    handler_test.setFormatter(formatter)
    handler_control.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)           #设置了这个才会把debug以上的输出到控制台
    
    logger.addHandler(handler_test)    #添加handler
    logger.addHandler(handler_control)
    
def debug(message):
    file = sys._getframe(1).f_code.co_filename
    file = os.path.basename(file)
    line = sys._getframe(1).f_lineno
    logging.debug(f"{file}-{line}: {message}")

def info(message):
    file = sys._getframe(1).f_code.co_filename
    file = os.path.basename(file)
    line = sys._getframe(1).f_lineno
    logging.info(f"{file}-{line}: {message}")
    
def warn(message):
    file = sys._getframe(1).f_code.co_filename
    file = os.path.basename(file)
    line = sys._getframe(1).f_lineno
    logging.warning(f"{file}-{line}: {message}")
    
def error(message):
    file = sys._getframe(1).f_code.co_filename
    file = os.path.basename(file)
    line = sys._getframe(1).f_lineno
    logging.error(f"{file}-{line}: {message}")
    
def fatal(message):
    file = sys._getframe(1).f_code.co_filename
    file = os.path.basename(file)
    line = sys._getframe(1).f_lineno
    logging.critical(f"{file}-{line}: {message}")
    
if __name__ == "__main__":
    init()
    info("Welcome")