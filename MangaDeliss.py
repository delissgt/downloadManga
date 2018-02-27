import DescManga
from PyQt4.QtGui import QMainWindow, QApplication
import requests, bs4
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal as Signal
import re
from PyQt4.QtCore import QDir
import tempfile
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

        miCarpetaTemp = QDir.tempPath()
        print (miCarpetaTemp)

        nameDirTemp = tempfile.mkdtemp(prefix='deliss', dir=str(miCarpetaTemp))


    def run(self):#obtener datos de la paginaWeb
        #str(self.link) o unicode(self.link)
        noStarchSoup = bs4.BeautifulSoup(self.link.text, "lxml")  # accedo al codigo fuente

        #Obtengo datos de la pagina
        obtener_titulo = noStarchSoup.select('h2 > a')  # busco el elemto dando esta especificacion ('h2 > a')
        #print (str(obtener_titulo[0]))


        elementoC = noStarchSoup.select('form > input[name=c]')
        c = elementoC[1].get('value')
        print (c)
        elementoI = noStarchSoup.select('form > input[name=i]')
        i = elementoI[1].get('value')
        print (i)
        elementoCP = noStarchSoup.select('form > input[name=cp]')
        cp = elementoCP[2].get('value')
        #numero inicial capitulo
        print (cp)

        numCapiF = noStarchSoup.select('form > select[name=cp]')
        num = numCapiF[0].select('option')[0].get_text()
        #numero final del capitulo
        print (num)



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


    #obtener contenido de la pagina
#TODO res = requests.get('www.link.com')

    #verificar que la pagina existe
#TODO res.raise_for_status

    #  filtrar acceder al contenido html de la pagina

#TODO noStarchSoup = bs4.BeautifulSoup(res.text , "lxml")

    # res.text --> regresa contenido
    #bs4.BeautifilSoup --> prepara para el filtrado
#NOTA add "lxml" y type (noStartSoup)<-- tipo soup
#import requests, bs4
#TODO contPag = requests.get('http://mangachameleon.com/?c=4e71db4bc09225616d11d05a&i=4e70ea03c092255ef70046f0')
#try:
#       contPag.raise_for_status()
#except Exception as exc:
#    print('No existe pagina: %s' % (exc))

#TODO pagSoup = bs4.BeautifulSoup(contPag.text, "lxml")
#type(pagSoup) --> tipo bs4.BeautifulSoup
#TODO elemtC = pagSoup.select('form > input[name="c"]')
#TODO type(elemtC) --> tipo list
#TODO str(elemtC[1])
#   '<input name="c" type="hidden" value="4e71db4bc09225616d11d05a"/>'
# TODO elemtC[1].get('value')
#e71db4bc09225616d11d05a' --> resultado OK




