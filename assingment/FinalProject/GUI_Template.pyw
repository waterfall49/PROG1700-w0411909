import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QButtonGroup
from PyQt5.QtGui import QPixmap
import Ui_CountriesOfTheWorld

class MyForm(QMainWindow, Ui_CountriesOfTheWorld.Ui_MainWindow):
    # DON'T TOUCH!
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        self.countries = []
    # END DON'T TOUCH

        # EVENT HOOKS HERE
        self.actionSave.setDisabled(True) # make "save" buttom inactive
        self.label_Population.hide()  # to hide everything on right side
        self.label_percent.hide()
        self.pushButton_update.hide()
        self.label_Area.hide()
        self.textEdit_Population.hide()
        self.comboBox_squremeter.hide()
        self.groupBox.hide()
        self.radioButton_km.hide()
        self.radioButton_sm.hide()
        self.btn_grp = QButtonGroup()  # make a group for radio buttons
        self.btn_grp.setExclusive(True)  # make a button group exclusive each other to be able to choose only one
        self.btn_grp.addButton(self.radioButton_km)  # add buttons in button group
        self.btn_grp.addButton(self.radioButton_sm)
        self.actionLoad_Countries.triggered.connect(self.LoadCountries)  # When click load countries button, load countries file
        self.listWidget_countrylist.itemClicked.connect(self.CountrySelected) # When choose one country in the list, show everything
        self.actionExit.triggered.connect(self.closeit)

    def LoadCountries(self):   # Open file and load name of countries
        objFile = open("assingment/FinalProject/countries.txt")
        for country in objFile:
            countryList = country.split(",")
            self.listWidget_countrylist.addItem(countryList[0])
            self.countries.append(countryList)
        objFile.close()

    def CountrySelected(self, selectCountryIndex): # When one country selected, show name, flag, population, area etc
        strCountry = selectCountryIndex.text()
        self.label_CountryName.setText(strCountry)
        strPath = "assingment/FinalProject/Flags/" + strCountry.replace(" ", "_") + ".png"
        #print(strPath)
        imagePixmap = QPixmap(strPath)
        self.label_CountryFlag.setPixmap(imagePixmap)   # show flag
        self.label_CountryFlag.resize(imagePixmap.width(), imagePixmap.height())

        for data in self.countries:
            if strCountry == data[0]:
                self.label_Population.show()  # show every button and box on right side
                self.pushButton_update.show()
                self.label_Area.show()
                self.comboBox_squremeter.show()
                self.groupBox.show()
                self.radioButton_km.show()
                self.radioButton_sm.show()
                self.radioButton_sm.setChecked(True)  # radiobutton_mile is default
                self.label_percent.show()
                self.textEdit_Population.show()
                number = format(int(data[1]),',')
                self.textEdit_Population.setText(number)  # show population
                self.label_area_output.setNum(int(data[2]))  # show area
                density = int(data[1])/int(data[2])  # calculate density
                self.label_density_output.setText(f"{density:.2f}")  # show density
                percent_population = self.CalculatePercentPopulation()  # calculate percentage of population in the world
                self.label_percent_output.setText(f"{percent_population:.4f}%")  # show percentage of population in the world
                self.comboBox_squremeter.setCurrentIndex(0) # make sq. Miles default 
                self.comboBox_squremeter.currentIndexChanged.connect(self.ConvertSqArea) # when choose sq.km in combobox, convert area
                self.radioButton_km.clicked.connect(self.ConvertSqDensity) # when choose sq.km in radio box, convert density
                self.radioButton_sm.clicked.connect(self.ShowSqMilesDensity) # when choose sq.miles in radio box, convert density

    def CalculatePercentPopulation(self):  # Calculate percent population 
        objFile = open("assingment/FinalProject/countries.txt")
        total = 0
        for a in objFile :
            a_list = a.split(",")
            total += int(a_list[1])
        num_population = self.textEdit_Population.toPlainText().replace(',','')
        per_population = int(num_population) / total * 100
        objFile.close()
        return(per_population)

    def ConvertSqArea(self):  # Convert area miles and Km
        if self.comboBox_squremeter.currentText() == "Sq. KM":
            Area_mi = float(self.label_area_output.text())
            Area_km = Area_mi / 0.3861
            self.label_area_output.setText(f"{Area_km:.2f}")
        else :
            Area_km = float(self.label_area_output.text())
            Area_mi = Area_km * 0.3861
            self.label_area_output.setText(f"{Area_mi:.1f}")

    def ConvertSqDensity(self):  # Convert population density of miles to km 
        Population = self.textEdit_Population.toPlainText().replace(',','')
        if self.comboBox_squremeter.currentText() == "Sq. KM":
            Area_km = float(self.label_area_output.text())
        else : 
            Area_km = float(self.label_area_output.text()) / 0.3861
        Population = int(Population)
        Density = Population / Area_km
        self.label_density_output.setText(f"{Density:.2f}")

    def ShowSqMilesDensity(self):   # Convert population density of km to miles 
        Population = self.textEdit_Population.toPlainText().replace(',','')
        if self.comboBox_squremeter.currentText() == "Sq. Miles":
            Area_mi = float(self.label_area_output.text())
            print(Area_mi)
        else : 
            Area_mi = float(self.label_area_output.text()) * 0.3861
            print(Area_mi)
        Population = int(Population)
        Density = Population / Area_mi
        self.label_density_output.setText(f"{Density:.2f}")

    def closeit(self):
        app.quit()

# DON'T TOUCH
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
