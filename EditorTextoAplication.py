import sys
from PyQt5.QtWidgets import QAction,QApplication,QFileDialog,QMainWindow
from Diagnosticos_new import EditortextoMainWindow

class EditorTextoApplication(QMainWindow):
    def __init__(self):
        super().__init__()
#crea instancia
        self.ui=EditortextoMainWindow()
        self.ui.setupUi(self)
#metodos para los botones 
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionSalir.triggered.connect(self.salir)

        self.show()
#funcion para abrir archivos
    def abrir(self):
        archivo =QFileDialog.getOpenFileName(self, "abrir archivo", "C:\\", "Tetx files (.txt)")
#lee el archivo
        if archivo [0]:
            with open(archivo[0], "rt") as f:
                datos=f.read()
                self.ui.text_editor.setText(datos)
#funcion para leer 
    def guardar(self):
        options= QFileDialog.options()
#con options hacemos que se use el dialogo de pyqt
        options |= QFileDialog.DontUseNtiveDialog
#guarda el archivo guardando lo importante en el objeto archivo
        archivo, _ = QFileDialog.getSaveFileName(self, "guardar archivo", "C:\\", "Text files (.txt)", options)
#para escribir en el archivo        
        with open(archivo, "wt") as f:
            f.write(self.ui.text_editor.toPlainText())

    def salir(self):
        sys.exit(0)        

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=EditorTextoApplication()
    ventana.show()
    sys.exit(app.exec_())
