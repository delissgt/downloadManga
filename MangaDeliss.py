import DescManga
from PyQt4.QtGui import QMainWindow, QApplication
import requests, bs4
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal as Signal
import re

                                #jalar interfaz
class VentanaMain(QMainWindow,DescManga.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaMain, self).__init__(parent)
        self.setupUi(self) #jalar interfaz

        self.pushBoton_stop.clicked.connect(self.funcionStop)
        self.pushBoton_start.clicked.connect(self.funcionStart)

    def funcionStop(self):
        print ("I am button stop me :3")

    def funcionStart(self):
        miLink = self.lineEdit_link.text()
        miHilo = ClaseHilo(miLink, self) #paso valores que puedo obtener#CREAR INSTANCIA

        miHilo.datos_listos.connect(self.colocarDatos)
        miHilo.start() #lanzo mi hilo

    def colocarDatos(self, miTitulo, micapitulo):

        self.label_titulo.setText(miTitulo[0].get_text())# titulo
        self.label_capitulo.setText(micapitulo)




class ClaseHilo(QThread): #obetner to-do de la web operaciones que no depende de mi
    datos_listos = Signal(list, str)

    def __init__(self, miLink, parent=None):#INICIALIZO OBJETO
        QThread.__init__(self, parent)
        self.link = requests.get(miLink) #obtener link


    def run(self):#obtener datos de la paginaWeb
        #str(self.link) o unicode(self.link)
        noStarchSoup = bs4.BeautifulSoup(self.link.text, "lxml")  # accedo al codigo fuente

        obtener_titulo = noStarchSoup.select('h2 > a')  # busco el elemto dando esta especificacion ('h2 > a')


        get_texto_cap = noStarchSoup.select('option[selected="selected"]')  # obtener numero captitulo
        texto = get_texto_cap[0].get_text()
        expresion_regular = re.compile(r'(\d)?(\d)?\d(\.)?(\d)?(\d)?(\d)?')
        cap = expresion_regular.search(texto)
        capitulo = cap.group()



        self.datos_listos.emit(obtener_titulo, capitulo)







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