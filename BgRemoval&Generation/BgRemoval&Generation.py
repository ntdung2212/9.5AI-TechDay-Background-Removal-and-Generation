import sys
import os
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit, QTextEdit
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import CallAPI  # Assume this is your API handler module

# Ensure path is relative to the script location
currentdir = os.path.dirname(os.path.abspath(__file__))
form_ui_path = os.path.join(currentdir, 'form.ui')


# Worker class for handling API calls in a separate thread
class ApiWorker(QObject):
    finished = pyqtSignal(object)  # Signal for completion of API call (can emit a string or list)
    error = pyqtSignal(str)        # Signal for errors during the API call

    def __init__(self, image_url=None, image_path=None, prompt=None):
        super().__init__()
        self.image_url = image_url
        self.image_path = image_path
        self.prompt = prompt

    def run(self):
        try:
            if self.prompt:
                # Background generation
                result = CallAPI.generate_background(self.image_path, self.prompt)
                if result:
                    self.finished.emit(result)  # Emit the result as a string (image path)
                else:
                    self.error.emit("Background generation failed.")
            elif self.image_url:
                # Background removal with URL
                result = CallAPI.BgRWithUrl(self.image_url)
                if isinstance(result, list):
                    self.finished.emit(result)  # Emit the result as a list [new image path, original image path]
                else:
                    self.error.emit("Unexpected result format from URL input.")
            elif self.image_path:
                # Background removal with file path
                result = CallAPI.BgR(self.image_path)
                if result:
                    self.finished.emit(result)  # Emit the result as a string (image path)
                else:
                    self.error.emit("Background removal failed.")
            else:
                self.error.emit("No file or URL selected.")
        except Exception as e:
            self.error.emit(str(e))


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(form_ui_path, self)
        self.setWindowTitle('AI Background Removal & Generation')

        # UI elements
        self.InputView = self.findChild(QLabel, "InputView")
        self.OutputView = self.findChild(QLabel, "OutputView")
        self.GetFilePathButton = self.findChild(QPushButton, "GetFilePath")
        self.RunButton = self.findChild(QPushButton, "RunBgR")
        self.SavePNGButton = self.findChild(QPushButton, "SavePNG")
        self.UrlInput = self.findChild(QLineEdit, "UrlInput")  # Input for URL
        self.GenerateBgButton = self.findChild(QPushButton, "GenerateBg")
        self.PromptInput = self.findChild(QTextEdit, "PromptInput")
        
        # Connect buttons to functions
        self.GetFilePathButton.clicked.connect(self.GetFile)
        self.RunButton.clicked.connect(self.RunBgRemoval)
        self.SavePNGButton.clicked.connect(self.Save)
        self.GenerateBgButton.clicked.connect(self.GenerateBackground)
        
        # Internal state variables
        self.imagePath = None
        self.resultImage = None
        self.originalImage = None

        # Make sure QLabel doesn't automatically scale contents
        self.InputView.setScaledContents(False)
        self.OutputView.setScaledContents(False)

        # Pixmap placeholders
        self.pixmap_input = None
        self.pixmap_output = None
        self.api_thread = None  # Thread to run API calls in background

    def GetFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose an image...", "", "Images (*.png *.jpg *.jpeg)")
        if filename:
            self.imagePath = filename
            self.UrlInput.clear()  # Clear URL input if file is selected
            self.pixmap_input = QPixmap(self.imagePath)
            
            # Display the input image in InputView
            self.update_image(self.InputView, self.pixmap_input)

    def RunBgRemoval(self):
        image_url = self.UrlInput.text().strip()
        if image_url or self.imagePath:
            # Disable the Run button during processing
            self.RunButton.setEnabled(False)

            # Create and start the worker thread for background removal
            self.api_thread = QThread()
            self.api_worker = ApiWorker(image_url=image_url, image_path=self.imagePath)
            self.api_worker.moveToThread(self.api_thread)

            # Connect signals to handle completion or error
            self.api_worker.finished.connect(self.on_api_finished)
            self.api_worker.error.connect(self.on_api_error)

            # Start the worker in the background
            self.api_thread.started.connect(self.api_worker.run)
            self.api_thread.start()
        else:
            print("No file or URL selected.")
    
    def GenerateBackground(self):
        prompt = self.PromptInput.toPlainText().strip()
        if not prompt:
            print("Please enter a prompt.")
            return

        if not self.resultImage:
            print("No background-removed image to generate a background for.")
            return

        # Disable the button during processing
        self.GenerateBgButton.setEnabled(False)

        # Create and start the worker thread for background generation
        self.bg_thread = QThread()
        self.bg_worker = ApiWorker(image_path=self.resultImage, prompt=prompt)
        self.bg_worker.moveToThread(self.bg_thread)

        # Connect signals to handle completion or error
        self.bg_worker.finished.connect(self.on_bg_generated)
        self.bg_worker.error.connect(self.on_api_error)

        # Start the worker
        self.bg_thread.started.connect(self.bg_worker.run)
        self.bg_thread.start()

    def on_api_finished(self, result):
        # Handle the result from the API call
        if isinstance(result, str):
            # Filepath to the new image
            self.resultImage = result
            self.originalImage = None  # No original image available
        elif isinstance(result, list) and len(result) >= 2:
            # Filepath to the new image and original image
            self.resultImage = result[0]
            self.originalImage = result[1]
        else:
            print("Unexpected result format from background removal API.")
            return

        # Display the original image in InputView (if available)
        if self.originalImage:
            self.pixmap_input = QPixmap(self.originalImage)
            self.update_image(self.InputView, self.pixmap_input)

        # Display the result image (background removed) in OutputView
        if self.resultImage:
            self.pixmap_output = QPixmap(self.resultImage)
            self.update_image(self.OutputView, self.pixmap_output)
        else:
            print("No result image to display.")

        # Re-enable the Run button
        self.RunButton.setEnabled(True)
        self.api_thread.quit()

    def on_bg_generated(self, result):
        # Display the generated background image
        if isinstance(result, str):
            self.pixmap_output = QPixmap(result)
        else:
            print("Unexpected result format from background generation API.")
            return

        # Check if the QPixmap is valid and display it
        if not self.pixmap_output.isNull():
            self.update_image(self.OutputView, self.pixmap_output)
        else:
            print("Failed to load generated background image.")
        
        self.GenerateBgButton.setEnabled(True)
        self.bg_thread.quit()

    def on_api_error(self, error_message):
        print("Error:", error_message)
        self.RunButton.setEnabled(True)
        self.GenerateBgButton.setEnabled(True)
        self.api_thread.quit()

    def update_image(self, label, pixmap):
        """
        Resize the image to fit within the QLabel while keeping its aspect ratio.
        """
        if pixmap is not None:
            scaled_pixmap = pixmap.scaled(
                label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            label.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        """
        This method is called whenever the window is resized.
        It will resize the displayed images while keeping their aspect ratios.
        """
        if self.pixmap_input:
            self.update_image(self.InputView, self.pixmap_input)
        if self.pixmap_output:
            self.update_image(self.OutputView, self.pixmap_output)
        super().resizeEvent(event)

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
