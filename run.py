from core.browser import Browser
from controller.login import Login
from controller.purchase import Purchase
from controller.email import Email
from controller.dingding import Dingding
from helpers.helpers import *
from retry import retry
import logging, os, traceback, sys

logging.basicConfig(
    filename=os.getcwd() + '/log/error.log',
    level=logging.ERROR,
    format="time:%(asctime)s \t levelname:%(levelname)s \n msg:%(message)s"
)
@retry(tries=3,delay=5,max_delay=20)
def scrapy_product():
        try:
            Login().login()
            Purchase().index().export().send_message()

        except Exception:
            msg = traceback.format_exception(*sys.exc_info())
            logging.error(
                ''.join(msg)
            )
            raise Exception(''.join(msg))
        finally:
            Browser().quit()
            print('do again!!!!')


if __name__ == '__main__':
    try:
        scrapy_product()
    except Exception as e:
        print(str(e))
        Email().send("".join(str(e)))