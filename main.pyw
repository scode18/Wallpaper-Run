from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 181)
        MainWindow.setStyleSheet("background-color: rgb(36, 36, 36)")
        MainWindow.setWindowIcon(QtGui.QIcon('code\\images\\logo.ico'))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.video_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.video_input.setGeometry(QtCore.QRect(0, 0, 661, 20))
        self.video_input.setStyleSheet("color: rgb(255, 255, 255)")
        self.video_input.setObjectName("video_input")

        self.ok_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(10, 30, 31, 24))
        self.ok_button.setStyleSheet("background-color: rgb(117, 250, 97)")
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.ok_button_clicked)

        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(50, 30, 141, 24))
        self.exit_button.setStyleSheet("background-color: rgb(255, 85, 118)")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.exit_button_clicked)

        self.text = QtWidgets.QLabel(parent=self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 160, 641, 16))
        self.text.setStyleSheet("color: rgb(255, 255, 255)")
        self.text.setObjectName("text")

        self.ver_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.ver_1.setGeometry(QtCore.QRect(520, 30, 141, 21))
        self.ver_1.setObjectName("ver_1")

        self.ver_0 = QtWidgets.QLabel(parent=self.centralwidget)
        self.ver_0.setGeometry(QtCore.QRect(200, 30, 101, 21))
        self.ver_0.setStyleSheet("background-color: rgb(36, 36, 36)")
        self.ver_0.setObjectName("ver_0")

        self.test_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.test_button.setGeometry(QtCore.QRect(10, 130, 121, 24))
        self.test_button.setStyleSheet("background-color: rgb(255, 194, 81)")
        self.test_button.setObjectName("test_button")
        self.test_button.clicked.connect(lambda: self.video_button_clicked('videos\\test.wmv'))

        self.test_img = QtWidgets.QLabel(parent=self.centralwidget)
        self.test_img.setGeometry(QtCore.QRect(10, 60, 121, 61))
        self.test_img.setObjectName("test_img")

        self.ah_img = QtWidgets.QLabel(parent=self.centralwidget)
        self.ah_img.setGeometry(QtCore.QRect(140, 60, 121, 61))
        self.ah_img.setObjectName("ah_img")

        self.car_2_img = QtWidgets.QLabel(parent=self.centralwidget)
        self.car_2_img.setGeometry(QtCore.QRect(400, 60, 121, 61))
        self.car_2_img.setObjectName("car_2_img")

        self.car_1_img = QtWidgets.QLabel(parent=self.centralwidget)
        self.car_1_img.setGeometry(QtCore.QRect(270, 60, 121, 61))
        self.car_1_img.setObjectName("car_1_img")

        self.car_3_img = QtWidgets.QLabel(parent=self.centralwidget)
        self.car_3_img.setGeometry(QtCore.QRect(530, 60, 121, 61))
        self.car_3_img.setObjectName("car_3_img")

        self.ah_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ah_button.setGeometry(QtCore.QRect(140, 130, 121, 24))
        self.ah_button.setStyleSheet("background-color: rgb(255, 194, 81)")
        self.ah_button.setObjectName("ah_button")
        self.ah_button.clicked.connect(lambda: self.video_button_clicked('videos\\Atomic-Heart-4K.mp4'))

        self.car_1_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.car_1_button.setGeometry(QtCore.QRect(270, 130, 121, 24))
        self.car_1_button.setStyleSheet("background-color: rgb(255, 194, 81)")
        self.car_1_button.setObjectName("car_1_button")
        self.car_1_button.clicked.connect(lambda: self.video_button_clicked('videos\\Sunset_Cruise_4k.mp4'))

        self.car_2_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.car_2_button.setGeometry(QtCore.QRect(400, 130, 121, 24))
        self.car_2_button.setStyleSheet("background-color: rgb(255, 194, 81)")
        self.car_2_button.setObjectName("car_2_button")
        self.car_2_button.clicked.connect(lambda: self.video_button_clicked('videos\\The_Drive_-_by_visualdon_4k.mp4'))

        self.car_3_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.car_3_button.setGeometry(QtCore.QRect(530, 130, 121, 24))
        self.car_3_button.setStyleSheet("background-color: rgb(255, 194, 81)")
        self.car_3_button.setObjectName("car_3_button")
        self.car_3_button.clicked.connect(lambda: self.video_button_clicked('videos\\The-Drive-remastered.mp4'))
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wallpaper Run"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.exit_button.setText(_translate("MainWindow", "Выключи свой мотор!"))
        self.text.setText(_translate("MainWindow", "Введи путь или имя видео. Например [\"videos\\test.wmv\"] или [\"C:\\video.mp4\"] Далее нажмите Enter или OK"))
        self.ver_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Solomon code 2020-2023</span></p></body></html>"))
        self.ver_0.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ver 0.3 - 23.04.2023</span></p></body></html>"))
        self.test_button.setText(_translate("MainWindow", "Test"))
        self.test_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/test.png\"/></p></body></html>"))
        self.ah_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/ah.png\"/></p></body></html>"))
        self.car_2_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/car_2.png\"/></p></body></html>"))
        self.car_1_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/car_1.png\"/></p></body></html>"))
        self.car_3_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/car_3.png\"/></p></body></html>"))
        self.ah_button.setText(_translate("MainWindow", "Atomic Heart"))
        self.car_1_button.setText(_translate("MainWindow", "Sunset Cruis"))
        self.car_2_button.setText(_translate("MainWindow", "The Drive"))
        self.car_3_button.setText(_translate("MainWindow", "The Drive Remastered"))

    def ok_button_clicked(self):
        name_or_path_video = self.video_input.text()
        subprocess.call('taskkill /im mpv.exe /f', shell=True)
        subprocess.call(f'wrc -v {name_or_path_video}', shell=True)

    def exit_button_clicked(self):
        subprocess.call('taskkill /im mpv.exe /f', shell=True)

    def video_button_clicked(self, video_name):
        subprocess.call('taskkill /im mpv.exe /f', shell=True)
        subprocess.call(f'wrc -v {video_name}', shell=True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
