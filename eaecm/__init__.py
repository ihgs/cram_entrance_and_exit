import binascii
import nfc
import requests
import time
import datetime

class MyCardReader(object):


    def __init__(self, hostname, port):
        self.url = "http://%s:%s/api/stamp" % (hostname, port)

    def on_connect(self, tag):
        print "touched"
        self.idm = binascii.hexlify(tag.idm)
        return True

    def waiting_read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

    def send_id(self, id, reader="raspberry"):
        now = datetime.datetime.now()
        unix_time = int(time.mktime(now.timetuple()))
        params = {
            "time": unix_time,
            "card_id": id,
            "device_name": reader
        }
        response = requests.post(
            self.url, params
        )
        if response.status_code == 200:
            body = response.json()
            if body["status"] == "success":
                name = body["name"]
                return name
            else:
                pass #TODO error
        return None

if __name__ == '__main__':
    cr = MyCardReader("localhost", "3000")
    print cr.send_id("aaaaa")
    # while True:
    #     print "touch card:"
    #     cr.waiting_read_id()
    #     print "released"
    #     print cr.idm
