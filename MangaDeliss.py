import DescManga
from PyQt4.QtGui import QMainWindow, QApplication
                                #jalar interfaz
class VentanaMain(QMainWindow,DescManga.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaMain, self).__init__(parent)
        self.setupUi(self) #jalar interfaz
        self.pushBoton_stop.clicked.connect(self.funcionStop)

    def funcionStop(self):
        print ("I am button stop me :3")



if __name__ == '__main__':
    # App Object
    app = QApplication([])
    # Window Object
    window = VentanaMain()
    # Show Window
    window.show()
    # Start App
    app.exec_()