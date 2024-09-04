import sys
import os 

from src.ui_interface import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomQToolTip import QCustomQToolTip

from src.functions import GuiFunctions

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # loadJsonStyle(self, self.ui, jsonfiles = {
        #     "json-styles/style.json"
        # })

        self.show()

        QAppSettings.updateAppSettings(self)

        self.app_functions = GuiFunctions(self)
    
    def sassCompilationProgress(self, n):
        self.ui.activityProgress.setValue(n)

#Executa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())