from PyQt5.QtWidgets import QWidget, QDateEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
 
class ReservaUnitaria(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarReserva.ui',self)
        self.btnEditarReserva.clicked.connect(self)
 
# if __name__ == "__main__":
#     from PyQt5.QtWidgets import QApplication
#     app = QApplication([])
#     widget = ReservaUnitaria()
#     widget.show()
#     app.exec_()
 
   