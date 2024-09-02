import os
import sys

from PIL import Image
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFileDialog, QMessageBox

from ui_MainWin import Ui_MainWindow

class ImageProcessor(QWidget):
    def __init__(self, Ui_MainWindow):
        super().__init__()

        self.imageLabel = Ui_MainWindow.imageLabel
        self.exportButton = Ui_MainWindow.exportButton
        self.openButton = Ui_MainWindow.openButton
        self.photoWidthEdit = Ui_MainWindow.widthLineEdit
        self.photoHeightEdit = Ui_MainWindow.heightLineEdit
        self.resolutionEdit = Ui_MainWindow.resolutionLineEdit
        self.sizeLineEdit = Ui_MainWindow.sizeLineEdit

        self.img_path = 'resources/image/22.png'
        pixmap = QPixmap(self.img_path)
        pixmap = pixmap.scaled(500, 500)  # 适应显示区域
        self.imageLabel.setPixmap(pixmap)
        # self.bondFunction()

    def bondFunction(self):
        # 创建按钮
        self.openButton.clicked.connect(self.select_image)
        self.exportButton.clicked.connect(self.export_image)

    def select_image(self):
        options = QFileDialog.Option.ReadOnly
        self.img_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                       "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)

        if self.img_path:
            pixmap = QPixmap(self.img_path)
            pixmap = pixmap.scaled(500, 500)  # 适应显示区域
            self.imageLabel.setPixmap(pixmap)

    def export_image(self):
        if not self.img_path:
            QMessageBox.critical(self, "Error", "Please select an image first.")
            return

        try:
            # 打开原始图像
            img = Image.open(self.img_path)

            # 重新调整图片大小
            img = img.resize((int(self.photoWidthEdit.text()), int(self.photoHeightEdit.text())), Image.LANCZOS)

            # 选择保存路径
            options = QFileDialog.Option.ReadOnly
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "JPG Files (*.jpg);;All Files (*)",
                                                         options=options)
            if output_path:
                # 保存为JPG格式，设置分辨率350dpi
                img.save(output_path, format="JPEG", dpi=(int(self.resolutionEdit.text()), int(self.resolutionEdit.text())), quality=100)

                # 重新检查文件大小是否小于50KB
                if os.path.getsize(output_path) > int(self.sizeLineEdit.text()) * 1024:
                    # 压缩图片直到满足大小要求
                    quality = 100
                    while os.path.getsize(output_path) > int(self.sizeLineEdit.text()) * 1024 and quality > 10:
                        img.save(output_path, format="JPEG", dpi=(int(self.resolutionEdit.text()), int(self.resolutionEdit.text())), quality=quality)
                        quality -= 5

                QMessageBox.information(self, "Success", "Image exported successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    processor = ImageProcessor(ui)
    ui.openButton.clicked.connect(processor.select_image)
    ui.exportButton.clicked.connect(processor.export_image)

    MainWindow.show()
    sys.exit(app.exec())