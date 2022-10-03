from PyQt5.QtWidgets import QApplication, QMainWindow
import ui_main, sys, base64


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = ui_main.Ui_MainWindow()
        self.main.setupUi(self)
        self.main.encryptButton.clicked.connect(lambda: self.encryptText())
        self.main.decryptButton.clicked.connect(lambda: self.decryptText())
        
    def encryptText(self):
        txt_to_encode = self.main.encodeTxt.text()
        txt_to_encode_bytes = txt_to_encode.encode("utf-8")
        base64_bytes = base64.b64encode(txt_to_encode_bytes)
        encodedtxt = base64_bytes.decode("utf-8")
        self.main.encryptOutput.setText(encodedtxt)
    
    def decryptText(self):
        txt_to_decode = self.main.decodeTxt.text()
        base64_bytes = txt_to_decode.encode('utf-8')
        txt_to_decode_bytes = base64.b64decode(base64_bytes)
        decoded_txt = txt_to_decode_bytes.decode('utf-8')
        self.main.decryptOutput.setText(decoded_txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
