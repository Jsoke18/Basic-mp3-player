import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QColor, QPalette, QPolygonF
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtSvg import QGraphicsSvgItem

class MP3Player(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize pygame mixer
        pygame.mixer.init()

        # Set up UI components
        self.init_ui()

    def init_ui(self):
        # Set background color
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(128, 0, 128))
        self.setPalette(palette)

        # Create buttons
        load_button = QPushButton('Load', self)
        load_button.clicked.connect(self.load_file)

        play_button = QPushButton('Play', self)
        play_button.clicked.connect(self.play)

        pause_button = QPushButton('Pause', self)
        pause_button.clicked.connect(self.pause)

        stop_button = QPushButton('Stop', self)
        stop_button.clicked.connect(self.stop)

        # Create label for file info
        self.file_label = QLabel('No file loaded', self)
        self.file_label.setAlignment(Qt.AlignCenter)
        self.file_label.setStyleSheet('color: white')

        # Create vector design
        vector_design = QGraphicsView(self)
        scene = QGraphicsScene(self)

        # Example: a simple triangle
        triangle = QPolygonF([QPointF(50, 0), QPointF(0, 100), QPointF(100, 100)])
        scene.addPolygon(triangle, Qt.white)
        vector_design.setScene(scene)

        # Create and set layout
        layout = QVBoxLayout()
        layout.addWidget(load_button)
        layout.addWidget(play_button)
        layout.addWidget(pause_button)
        layout.addWidget(stop_button)
        layout.addWidget(self.file_label)
        layout.addWidget(vector_design)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set window properties
        self.setWindowTitle('MP3 Player')
        self.setGeometry(100, 100, 300, 400)

    def load_file(self):
        mp3_file, _ = QFileDialog.getOpenFileName(self, "Open MP3 File", "", "MP3 Files (*.mp3)")
        if mp3_file:
            pygame.mixer.music.load(mp3_file)
            self.file_label.setText(os.path.basename(mp3_file))

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

app = QApplication(sys.argv)
player = MP3Player()
player.show()
sys.exit(app.exec_())
