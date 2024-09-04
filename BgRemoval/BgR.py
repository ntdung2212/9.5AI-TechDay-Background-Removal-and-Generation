import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import CallAPI

# Ensure path is relative to the script location
currentdir = os.path.dirname(os.path.abspath(__file__))
form_ui_path = os.path.join(currentdir, 'form.ui')

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(form_ui_path, self)
        self.setWindowTitle('9.5 AI | Background Removal |')

        self.InputView = self.findChild(QLabel, "InputView")
        self.OutputView = self.findChild(QLabel, "OutputView")
        self.GetFilePathButton = self.findChild(QPushButton, "GetFilePath")
        self.RunButton = self.findChild(QPushButton, "RunBgR")
        self.SavePNGButton = self.findChild(QPushButton, "SavePNG")
        
        self.GetFilePathButton.clicked.connect(self.GetFile)
        self.RunButton.clicked.connect(self.Run)
        self.SavePNGButton.clicked.connect(self.Save)
        
        self.imagePath = None
        self.resultImage = None

    def GetFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose an image...", "", "Images (*.png *.jpg *.jpeg)")
        if filename:
            self.imagePath = filename
            pixmap = QPixmap(self.imagePath)
            self.InputView.setPixmap(pixmap)

    def Run(self):
        if not self.imagePath:
            print("No file selected.")
            return

        result = CallAPI.CallAPI(self.imagePath)
        if isinstance(result, str):
        # Assuming result is a path to the image file
            self.resultImage = result
            pixmap = QPixmap(self.resultImage)
            self.OutputView.setPixmap(pixmap)
        else:
            print("Unexpected result format:", result)

    def Save(self):
        if not self.resultImage:
            print("No processed image to save.")
            return
        
        savePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png)")
        if savePath:
            if isinstance(self.resultImage, str):
                pixmap = QPixmap(self.resultImage)
                pixmap.save(savePath)
            else:
                with open(savePath, 'wb') as f:
                    f.write(self.resultImage)

app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()