import DescManga
from PyQt4.QtGui import QMainWindow, QApplication
import requests, bs4
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal as Signal
                                #jalar interfaz
class VentanaMain(QMainWindow,DescManga.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaMain, self).__init__(parent)
        self.setupUi(self) #jalar interfaz



        #res = requests.get('http://mangachameleon.com/?c=545b812745b9efab4343f776&i=4e70ea03c092255ef70046f0')  # accedo a la web



        self.pushBoton_stop.clicked.connect(self.funcionStop)
        self.pushBoton_start.clicked.connect(self.funcionStart)

    def funcionStop(self):
        print ("I am button stop me :3")

    def funcionStart(self):
        miLink = self.lineEdit_link.text()
        miHilo = ClaseHilo(miLink, self) #paso valores que puedo obtener#CREAR INSTANCIA

        miHilo.datos_listos.connect(self.colocarDatos)

        miHilo.start() #lanzo mi hilo

    def colocarDatos(self, miTitulo, cadena_hola):

        self.label_titulo.setText(miTitulo[0].get_text())# titulo
        self.label_capitulo.setText(cadena_hola)




class ClaseHilo(QThread): #obetner to-do de la web operaciones que no depende de mi
    datos_listos = Signal(list, str)

    def __init__(self, miLink, parent=None):#INICIALIZO OBJETO
        QThread.__init__(self, parent)
        self.link = requests.get(miLink) #obtener link


    def run(self):#obtener datos de la paginaWeb
        #str(self.link) o unicode(self.link)
        noStarchSoup = bs4.BeautifulSoup(self.link.text, "lxml")  # accedo al codigo fuente
        elems = noStarchSoup.select('h2 > a')  # busco el elemto dando esta especificacion ('h2 > a')
        # elems[0].get_text()  # obetengo el texto <h2><a>Naruto</a></h2> ---> Naruto
       # miTitulo=elems[0].get_text()
        #print(miTitulo)
        self.datos_listos.emit(elems, 'HOla')







if __name__ == '__main__':
    # App Object
    app = QApplication([])
    # Window Object
    window = VentanaMain()
    # Show Window
    window.show()
    # Start App
    app.exec_()

    #si hay error = parser --> File-Setting-Proyect-install lxml