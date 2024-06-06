from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QStyle
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("PYmediaPlayer")
        self.setGeometry(350,100, 700,500)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.darkGreen)
        self.setPalette(p)

        self.create_player()

    def create_player(self):

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        Videowidget = QVideoWidget()


        self.openBtn = QPushButton('Open Video') # type: ignore




        self.playBtn = QPushButton() # type: ignore
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_M))

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)

        
        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)



        vbox = QVBoxLayout()

        vbox.addLayout(hbox)


        self.setLayout(vbox)










app = QApplication(sys.argv) # type: ignore
window = Window()
window.show()
sys.exit(app.exec_())