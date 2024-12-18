from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl, QPropertyAnimation, QRect
import sys

class PympStyleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("io.ico"))
        self.setWindowTitle("PYmediaPlayer")
        self.setGeometry(350,100, 700,500)

        # Apply pymp-like colors
        p = self.palette()
        p.setColor(QPalette.Window, QColor("#121212"))  # Dark background
        self.setPalette(p)

        # pymp font
        self.setFont(QFont("Arial", 10))

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;  /* Dark theme background */
                color: #FFFFFF;  /* Light font color */
                font-family: 'Arial', sans-serif;
            }

            QPushButton {
                background-color: #007BFF;  /* Blue color for buttons */
                color: #FFFFFF;
                border: none;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #0056b3;  /* Darker blue on hover */
            }

            QPushButton:disabled {
                background-color: #333333;  /* Gray for disabled state */
                color: #AAAAAA;
            }

            QSlider {
                background-color: #121212;
                height: 5px;
                border-radius: 2px;
            }

            QSlider::groove:horizontal {
                background: #333333;  /* Groove color */
                height: 5px;
                border-radius: 2px;
            }

            QSlider::handle:horizontal {
                background: #007BFF;
                width: 14px;
                height: 14px;
                margin: -5px 0;
                border-radius: 7px;
            }

            QSlider::handle:horizontal:hover {
                background: #0056b3;
            }

            QVideoWidget {
                background-color: #000000;
                border-radius: 10px;
            }
        """)

        self.create_player()

    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        self.openBtn = QPushButton('Open')
        self.openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton('Play')
        self.playBtn.setEnabled(True)
        self.playBtn.clicked.connect(self.play_video)

        self.playBtn = QPushButton('Pause')
        self.playBtn.setDisabled(False)
        self.playBtn.clicked.connect(self.pause_video)

        self.fullscreenBtn = QPushButton('Fullscreen')
        self.fullscreenBtn.clicked.connect(self.toggle_fullscreen)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(10, 10, 10, 10)
        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.fullscreenBtn)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(videowidget)

        self.setLayout(vbox)

        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.mediaStatusChanged.connect(self.pause_video)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def pause_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.fullscreenBtn.setText('Fullscreen')
        else:
            self.showFullScreen()
            self.fullscreenBtn.setText('Exit Fullscreen')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.showNormal()
            self.fullscreenBtn.setText('Fullscreen')

app = QApplication(sys.argv)
window = PympStyleWindow()
window.show()
sys.exit(app.exec_())
