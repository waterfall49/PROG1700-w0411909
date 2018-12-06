import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import Ui_CountriesOfTheWorld

class MyForm(QMainWindow, Ui_CountriesOfTheWorld.Ui_MainWindow):
    # DON'T TOUCH!
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DON'T TOUCH

        # EVENT HOOKS HERE
        self.label_Population.hide()
        self.label_percent.hide()
        self.pushButton_update.hide()
        self.label_Area.hide()
        self.textEdit_Population.hide()
        self.comboBox_squremeter.hide()
        self.groupBox.hide()
        self.radioButton_km.hide()
        self.radioButton_sm.hide()
        self.actionLoad_Countries.triggered.connect(self.LoadCountries)
        self.listWidget_countrylist.itemClicked.connect(self.CountrySelected)
        self.comboBox_squremeter.currentIndexChanged.connect(self.ConvertSqUnits)

    # RESPONSES HERE    
    def CountrySelected(self,selectedCountryIndex):
        QMessageBox.information(self,"country changed",selectedCountryIndex.text())
        strCountryName = selectedCountryIndex.text()
        imagePixmap = QPixmap(f"assignment/FinalProject/Flags/{strCountryName}")
        self.label_CountryName.setText(strCountryName)
        self.label_CountryFlag.setPixmap(imagePixmap)
        self.label_CountryFlag.resize(imagePixmap.width(),imagePixmap.height())
        
    def LoadCountries(self):
        objFile = open("assingment/FinalProject/countries.txt")
        for line in objFile:
            lineList = line.split(",")
            self.listWidget_countrylist.addItem(lineList[0])
        objFile.close()

    def ConvertSqUnits(self):
        QMessageBox.information(self,"Event Received","Please convert between different units.")

# DON'T TOUCH
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
