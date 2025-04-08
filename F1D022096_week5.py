import sys
import re
from PyQt5 import QtCore, QtWidgets

class UI_mainWindow(QtWidgets.QWidget):
    def Ui(self, mainWindow):
        mainWindow.setObjectName("Main Window")
        mainWindow.setFixedSize(650, 700)
        self.form_app = QtWidgets.QWidget(mainWindow)
        self.form_app.setObjectName("Form Application")

        # label dan input
        self.nameLabel = QtWidgets.QLabel("Name:", self.form_app)
        self.nameLabel.setGeometry(QtCore.QRect(50, 50, 120, 40))
        self.nameInput = QtWidgets.QLineEdit(self.form_app)
        self.nameInput.setGeometry(QtCore.QRect(180, 50, 400, 40))

        self.emailLabel = QtWidgets.QLabel("Email:", self.form_app)
        self.emailLabel.setGeometry(QtCore.QRect(50, 110, 120, 40))
        self.emailInput = QtWidgets.QLineEdit(self.form_app)
        self.emailInput.setGeometry(QtCore.QRect(180, 110, 400, 40))

        self.ageLabel = QtWidgets.QLabel("Age:", self.form_app)
        self.ageLabel.setGeometry(QtCore.QRect(50, 170, 120, 40))
        self.ageInput = QtWidgets.QLineEdit(self.form_app)
        self.ageInput.setGeometry(QtCore.QRect(180, 170, 400, 40))

        self.phoneLabel = QtWidgets.QLabel("Phone Number:", self.form_app)
        self.phoneLabel.setGeometry(QtCore.QRect(50, 230, 120, 40))
        self.phoneInput = QtWidgets.QLineEdit(self.form_app)
        self.phoneInput.setGeometry(QtCore.QRect(180, 230, 400, 40))
        self.phoneInput.setInputMask("+62 999 9999 9999")

        self.addressLabel = QtWidgets.QLabel("Address:", self.form_app)
        self.addressLabel.setGeometry(QtCore.QRect(50, 290, 120, 40))
        self.addressInput = QtWidgets.QTextEdit(self.form_app)
        self.addressInput.setGeometry(QtCore.QRect(180, 290, 400, 120))

        self.genderLabel = QtWidgets.QLabel("Gender:", self.form_app)
        self.genderLabel.setGeometry(QtCore.QRect(50, 430, 400, 40))
        self.genderCombo = QtWidgets.QComboBox(self.form_app)
        self.genderCombo.setGeometry(QtCore.QRect(180, 430, 400, 40))
        self.genderCombo.addItems(["", "Male", "Female"])

        self.educationLabel = QtWidgets.QLabel("Education:", self.form_app)
        self.educationLabel.setGeometry(QtCore.QRect(50, 490, 120, 40))
        self.educationCombo = QtWidgets.QComboBox(self.form_app)
        self.educationCombo.setGeometry(QtCore.QRect(180, 490, 400, 40))
        self.educationCombo.addItems(["", "Elementary School", "Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])

        self.saveButton = QtWidgets.QPushButton("Save", self.form_app)
        self.saveButton.setGeometry(QtCore.QRect(200, 550, 150, 50))
        self.clearButton = QtWidgets.QPushButton("Clear", self.form_app)
        self.clearButton.setGeometry(QtCore.QRect(400, 550, 150, 50))

        self.nimLabel = QtWidgets.QLabel("F1D022096", self.form_app)
        self.nimLabel.setGeometry(QtCore.QRect(480, 620, 400, 100))
        self.nimLabel.setStyleSheet("color: gray;")

        mainWindow.setCentralWidget(self.form_app)

        # event handlers
        self.saveButton.clicked.connect(self.validate_form)
        self.clearButton.clicked.connect(self.clear_form)

        # menginstall event filter untuk kunci 'Q'
        app.installEventFilter(self)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Form Validation"))

    def validate_form(self):
        name = self.nameInput.text().strip()
        email = self.emailInput.text().strip()
        age = self.ageInput.text().strip()
        phone = self.phoneInput.text().replace(" ", "").strip()
        address = self.addressInput.toPlainText().strip()
        gender = self.genderCombo.currentText()
        education = self.educationCombo.currentText()

        # aturan validasi
        if not all([name]):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "All fields are required.")
            return
        if not all([email]):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "All fields are required.")
            return

        if not re.match(r'^[\w\.-]+@gmail\.com$', email):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "Please enter a valid email address.")
            return

        if not all([age]):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "All fields are required.")
            return

        if not re.fullmatch(r'\d+', age):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "Please enter a valid age (integer value).")
            return

        age_value = int(age)
        if age_value < 1 or age_value > 100:
            QtWidgets.QMessageBox.warning(None, "Validation Error", "Age must be between 1 to 100.")
            return

        if len(phone) != 13:
            QtWidgets.QMessageBox.warning(None, "Validation Error", "Please enter a valid 13 digit phone number.")
            return

        if not all([address]):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "All fields are required.")
            return

        if not all([gender]):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "All fields are required.")
            return

        if not all([education]):
            QtWidgets.QMessageBox.warning(None, "Validation Error", "All fields are required.")
            return

        QtWidgets.QMessageBox.information(None, "Success", "Profile saved successfully!")
        self.clear_form()

    def clear_form(self):
        self.nameInput.clear()
        self.emailInput.clear()
        self.ageInput.clear()
        self.phoneInput.clear()
        self.addressInput.clear()
        self.genderCombo.setCurrentIndex(0)
        self.educationCombo.setCurrentIndex(0)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Q:
                QtWidgets.QApplication.quit()
                return True
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UI_mainWindow()
    ui.Ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())