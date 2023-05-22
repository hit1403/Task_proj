import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPixmap
from window2_ui import Ui_MainWindow
from PIL import Image
from PIL.ImageQt import ImageQt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.canvas = QGraphicsView(self)
        self.canvas.setGeometry(150, 30, 1200, 650)
        self.canvas.setStyleSheet("background-color: white")

        self.scene = QGraphicsScene(self)
        self.canvas.setScene(self.scene)

        self.ui.pushButton_1.clicked.connect(self.render_image)

    def render_image(self):
        folder_path = r"C:\Users\l\PycharmProjects\pythonProject\images"
        image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not image_files:
            print("No image files found in the folder.")
            return
        random_image_file = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image_file)

        image = Image.open(image_path)

        pixmap = QPixmap.fromImage(ImageQt(image))
        pixmap_item = self.scene.addPixmap(pixmap)
        pixmap_item.setPos(
            random.randint(0, self.canvas.width()),
            random.randint(0, self.canvas.height()),
        )
        print(image_path)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
