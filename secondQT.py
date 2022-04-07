import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class HelloWorld(QWidget):
    def __init__(self): #yukarıdaki class'ın kurucusu init'tir.
        #Ve self parametresi, bu nesnenin bir örneğini ifade eder.
        super().__init__() # üst sınıftaki metotlara erişebilmek için super() kullanılır.
        #QWidget'ın constructorlarına erişebilmek için __init__ kullanılır.
        textLabel = QLabel(self)
        textLabel.setText("Merhaba Bursa Teknik Üniversitesi!")
        textLabel.move(50, 85) #yazının yeri belirtilir.

        # resize() metodu ile pencereye boyutlar tanımlanır.
        self.resize(320, 240)
        self.setWindowTitle("Hello, BTU!")


class LoginForm(QWidget):
    def __init__(self):#yukarıdaki class'ın kurucusu init'tir.
        #Ve self parametresi, bu nesnenin bir örneğini ifade eder.
        super().__init__()# üst sınıftaki metotlara erişebilmek için super() kullanılır.
        #QWidget'ın constructorlarına erişebilmek için __init__ kullanılır.
        self.setWindowTitle('Kayit Formu')
        self.resize(500, 120)

        layout = QGridLayout() #QGridLayout'dan layout değişkeni oluşturulur.

        label_name = QLabel('<font size="4"> Kullanici Adi </font>') 
        #QLabel sınıfından label_Name değişkeni oluşturulur.
        self.lineEdit_username = QLineEdit() #QLineEdit sınıfından ilgili değişken oluşturuldu.
        self.lineEdit_username.setPlaceholderText('Kullanici adi giriniz...')
        layout.addWidget(label_name, 0, 0) #a0: QWidget, satır: int, sütun: int
        layout.addWidget(self.lineEdit_username, 0, 1) #a0: QWidget, satır: int, sütun: int

        label_password = QLabel('<font size="4"> Sifre </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Lütfen şifrenizi giriniz...')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Giriş')  #Buton sınıfından ilgili değişken oluşturuldu.
        button_login.clicked.connect(self.check_password) 
        #Butona tıklandığında check_password fonksiyonuna yönlendirildi.
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout) #pencerenin ana düzeni belirlendi.

    def check_password(self):
        msg = QMessageBox() #QMessageBox sınıfından nesne tanımlanır.

        if self.lineEdit_username.text() == 'sefa' and self.lineEdit_password.text() == 'sefa':
            msg.setText('Basarili Giris...') #setText metodu çalıştırılır ve ekrana string bastırılır.
            msg.exec_()
            app.quit()
        else:
            msg.setText('Bir yerlerde hata yaptiniz...')
            msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm() #LoginForm'dan yeni bir nesne oluşturulur.

    form.show() #Ekrana bastırılır.


if __name__ == '__main__':

    form2 = HelloWorld() #HelloWorld'den yeni bir nesne oluşturulur.

    form2.show() #Ekrana bastırılır.

sys.exit(app.exec_())  #uygulama çalıştırılır ve sonlandırılır.
