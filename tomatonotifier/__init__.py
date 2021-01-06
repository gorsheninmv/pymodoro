import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Show message!")
    b.move(50, 50)
    b.clicked.connect(lambda: app.exit(0))
    w.setWindowTitle("Tomato Timer")
    w.show()
    sys.exit(app.exec_())
