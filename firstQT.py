import sys #python standart kütüphane modülü
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# Her pyqt uygulaması, bir application nesnesi oluşturmalıdır.
# Application nesnesi, QTWidgets modülünde yer alır.
app = QApplication(sys.argv)





#  QWidget widget, pyqt5'deki tüm kullanıcı arabirimi nesnelerinin temel sınıfıdır.

root = QWidget()

textLabel = QLabel(root)
textLabel.setText("Merhaba Bursa Teknik Üniversitesi!")
textLabel.move(50,85) # 

root.resize(320, 240)  # resize() metodu ile pencereye boyutlar tanımlanır.
root.setWindowTitle("Hello, World!")  
root.show()  # show() metodu ile yaptığımız işlemi ekranda görürürüz.

sys.exit(app.exec_())  # Uygulamamızı çalıştırma aşaması...