import binascii
import nfc
import requests
import time
import datetime
import traceback
from logging import getLogger
logger = getLogger("eaecm")

class MyCardReader(object):


    def __init__(self, hostname, port, token):
        self.url = "https://%s:%s/api/stamp" % (hostname, port)
        self.token = token

    def setCallback(self, callback):
        self.callback = callback

    def on_connect(self, tag):
        logger.info("touched")
        self.idm = binascii.hexlify(tag.idm)
        logger.info("id:%s" % self.idm)
        try:
            name = self.send_id(self.idm)
            self.callback({"name": name})
            logger.info("name:%s" % name)
        except:
            self.callback({"error": True, "idm": self.idm })
            logger.error("error:%s" % self.idm)
            logger.error(traceback.format_exc())

        return True

    def waiting_read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        except:
            logger.error(traceback.format_exc())
        finally:
            clf.close()

    def send_id(self, id, reader="raspbrry"):
        now = datetime.datetime.now()
        unix_time = int(time.mktime(now.timetuple()))
        params = {
            "time": unix_time,
            "card_id": id,
            "device_name": reader
        }
        headers = {
            "ACCESS_TOKEN": self.token
        }
        response = requests.post(
            self.url, data=params, headers=headers
        )
        if response.status_code < 300:
            body = response.json()
            if body["status"] == "success":
                name = body["name"]
                return name
            else:
                logger.error(body["message"])
        return None
