from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("PYmediaPlayer")
        self.setGeometry(350,100, 700,500)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.GlobalColor.red)
        self.setPalette(p)



    def create_player(self):

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        Videowidget = QVideoWidget()


        self.openBtn = QPushButten() # type: ignore
        self.openBtn.setEnabled(False)




app = QApplication(sys.argv) # type: ignore
window = Window()
window.show()
sys.exit(app.exec_())