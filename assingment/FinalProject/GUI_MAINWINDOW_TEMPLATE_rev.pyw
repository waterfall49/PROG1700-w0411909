import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import Qpixmap 

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_CountriesOfTheWorld
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_CountriesOfTheWorld.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.label_Countryname.hide()
        self.label_Population.hide()
        self.label_area_output.hide()
        self.label_density_output.hide()
        self.label_Flag.hide()
        self.label_percent.hide()
        self.label_percent_output.hide()
        self.pushButton_update.hide()
        self.label_Area.hide()
        self.textEdit_Population.hide()
        self.comboBox_squremeter.hide()
        self.groupBox.hide()
        self.radioButton_km.hide()
        self.radioButton_sm.hide()
        self.actionLoad_Countries.triggered.connect(self.countrybutton_clicked)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def countrybutton_clicked(self):
        # Call the SetMessage() function
        self.LoadCountriesFromFile()

#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)

    #     # Set Hello message in line edit box

    def LoadCountriesFromFile(self):

        objFile = open('countries.txt')
        for line in objFile : 
            line = line.replace("\n","")
            listLine = line.split(",")
            self.listWidget_countrylist.addItem(listLine[0]) 
        objFile.close()

    imagePixmap = Qpixmap("GUI/Flags/Albania.png")
    self.label_Countryname.setPixmap(imagePixmap)
        
#Example Helper Function
#    def Save(self):
#       Implement the save functionality here

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY