import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator_ui import Ui_MainWindow  # Import the generated class from the .ui file

class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Connect buttons to their respective methods
        self.pushButton_0.clicked.connect(lambda: self.append_number("0"))
        self.pushButton_1.clicked.connect(lambda: self.append_number("1"))
        self.pushButton_2.clicked.connect(lambda: self.append_number("2"))
        self.pushButton_3.clicked.connect(lambda: self.append_number("3"))
        self.pushButton_4.clicked.connect(lambda: self.append_number("4"))
        self.pushButton_5.clicked.connect(lambda: self.append_number("5"))
        self.pushButton_6.clicked.connect(lambda: self.append_number("6"))
        self.pushButton_7.clicked.connect(lambda: self.append_number("7"))
        self.pushButton_8.clicked.connect(lambda: self.append_number("8"))
        self.pushButton_9.clicked.connect(lambda: self.append_number("9"))

        self.pushButton_add.clicked.connect(lambda: self.operation("+"))
        self.pushButton_subtract.clicked.connect(lambda: self.operation("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.operation("*"))
        self.pushButton_divide.clicked.connect(lambda: self.operation("/"))
        self.pushButton_equals.clicked.connect(self.calculate_result)
        self.pushButton_clear.clicked.connect(self.clear_display)

        self.current_operation = None
        self.first_number = None

    def append_number(self, number):
        current_text = self.lineEdit.text()
        new_text = current_text + number
        self.lineEdit.setText(new_text)

    def operation(self, op):
        self.first_number = float(self.lineEdit.text())
        self.current_operation = op
        self.lineEdit.clear()

    def calculate_result(self):
        second_number = float(self.lineEdit.text())
        if self.current_operation == "+":
            result = self.first_number + second_number
        elif self.current_operation == "-":
            result = self.first_number - second_number
        elif self.current_operation == "*":
            result = self.first_number * second_number
        elif self.current_operation == "/":
            result = self.first_number / second_number
        self.lineEdit.setText(str(result))

    def clear_display(self):
        self.lineEdit.clear()
        self.current_operation = None
        self.first_number = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
