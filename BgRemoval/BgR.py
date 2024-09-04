import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import CallAPI  # Import CallAPI module

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
        self.UrlInput = self.findChild(QLineEdit, "UrlInput")  # Add a QLineEdit for URL input
        
        self.GetFilePathButton.clicked.connect(self.GetFile)
        self.RunButton.clicked.connect(self.Run)
        self.SavePNGButton.clicked.connect(self.Save)
        
        self.imagePath = None
        self.resultImage = None
        self.originalImage = None

    def GetFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose an image...", "", "Images (*.png *.jpg *.jpeg)")
        if filename:
            self.imagePath = filename
            self.UrlInput.clear()  # Clear URL input if file is selected
            pixmap = QPixmap(self.imagePath)
            self.InputView.setPixmap(pixmap)

    def Run(self):
        image_url = self.UrlInput.text().strip()
        if image_url:
            # Call API using the image URL
            result = CallAPI.CallAPIWithUrl(image_url)
            if isinstance(result, list) and len(result) >= 2:
                self.resultImage = result[0]  # New image (background removed)
                self.originalImage = result[1]  # Original image
            else:
                print("Unexpected result format for URL input.")
                return
        elif self.imagePath:
            # Call API using the local file
            result = CallAPI.CallAPI(self.imagePath)
            self.resultImage = result  # Since result is a single image path

        else:
            print("No file or URL selected.")
            return
        
        # Display the result image
        if self.resultImage:
            pixmap = QPixmap(self.resultImage)
            self.OutputView.setPixmap(pixmap)
        else:
            print("No result image to display.")

    def Save(self):
        if not self.resultImage:
            print("No processed image to save.")
            return
        
        savePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "WebP Files (*.webp);;PNG Files (*.png)")
        if savePath:
            pixmap = QPixmap(self.resultImage)
            pixmap.save(savePath)

app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()