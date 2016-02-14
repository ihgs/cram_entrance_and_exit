import binascii
import nfc
import requests
import time
import datetime

class MyCardReader(object):


    def __init__(self, hostname, port, token):
        self.url = "http://%s:%s/api/stamp" % (hostname, port)
        self.token = token

    def on_connect(self, tag):
        print "touched"
        self.idm = binascii.hexlify(tag.idm)
        try:
            print self.send_id(self.idm)
        except requests.exceptions.RequestException as e:
            print e

        return True

    def waiting_read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
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
        if response.status_code == 200:
            body = response.json()
            if body["status"] == "success":
                name = body["name"]
                return name
            else:
                pass #TODO error
        return None
