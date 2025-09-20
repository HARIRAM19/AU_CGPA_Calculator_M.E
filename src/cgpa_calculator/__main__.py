from PyQt5 import QtWidgets
import sys
from .cgpa_app import CGPACalculator

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CGPACalculator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
