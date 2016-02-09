import binascii
import nfc


class MyCardReader(object):

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

if __name__ == '__main__':
    cr = MyCardReader()
    while True:
        print "touch card:"
        cr.waiting_read_id()
        print "released"
        print cr.idm
