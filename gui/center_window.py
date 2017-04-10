import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()   # get geometry of main window
        cp = QDesktopWidget().availableGeometry().center()  #  get center of desktop
        qr.moveCenter(cp)   # move center of rectangle (with main window geometry) to center of desktop
        self.move(qr.topLeft())  # move window's top left corner to rectangle's top left corner

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())