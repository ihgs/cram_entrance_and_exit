# -*- coding: utf-8 -*-
import datetime
import time
from PyQt4 import QtGui
from PyQt4.QtCore import QTimer, Qt


MESSAGE_INIT = u"カードをタッチしてください"
MESSAGE_GREET = u"こんにちは"
MESSAGE_CALL_TEACHER = u"先生に連絡してください"
TITLE = u"入室管理"

def now():
    d = datetime.datetime.today()
    return d.strftime("%Y-%m-%d %H:%M")

def font():
    return QtGui.QFont("Times", 30)


class Display(QtGui.QMainWindow):
    def __init__(self):
        super(Display, self).__init__()
        self.initUI()

    def initUI(self):
        self.timeLabel = QtGui.QLabel(now())
        self.timeLabel.setFont(font())
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.messageLabel = QtGui.QLabel(MESSAGE_INIT)
        self.messageLabel.setFont(font())

        self.nameLabel = QtGui.QLabel("")
        self.nameLabel.setFont(font())

        self.errorLabel = QtGui.QLabel("")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, Qt.red)
        self.errorLabel.setPalette(palette)

        grid = QtGui.QVBoxLayout()

        grid.addWidget(self.timeLabel)
        grid.addWidget(self.messageLabel)
        grid.addWidget(self.nameLabel)
        grid.addWidget(self.errorLabel)

        timer = QTimer(self)
        timer.timeout.connect(self.time_draw)
        timer.start(5000)

        window = QtGui.QWidget()
        window.setLayout(grid)
        self.setCentralWidget(window)
        self.setGeometry(0,0, 480, 320)
        self.setWindowTitle(TITLE)
        self.show()

    def show_name(self, name):
        self.messageLabel.setText(MESSAGE_GREET)
        self.nameLabel.setText(name)
        time.sleep(3)
        self.messageLabel.setText(MESSAGE_GREET)
        self.nameLabel.setText("")

    def show_error(self, error):
        self.errorLabel.setText(error)
        self.messageLabel.setText(MESSAGE_CALL_TEACHER)
        self.nameLabel.setText("")

    def callback(self, opt):
        if opt.has_key("name"):
            self.show_name(opt["name"])
        elif opt.has_key("error"):
            self.show_error("check log by 'journalctl -u eaecm'")


    def time_draw(self):
        self.timeLabel.setText(now())
