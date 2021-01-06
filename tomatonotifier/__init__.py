import sys
import PyQt5.QtWidgets as widgets
import PyQt5.QtCore as qtcore


def main():
    app = widgets.QApplication(sys.argv)
    win = widgets.QWidget()
    win.setWindowTitle("Tomato Timer")
    win.setFixedSize(200, 100)

    label = widgets.QLabel()
    label.setText('Hello from tomato timer')
    label.setAlignment(qtcore.Qt.AlignCenter)

    continue_btn = widgets.QPushButton()
    continue_btn.setText("Work")
    continue_btn.clicked.connect(lambda: app.exit(0))

    relax_btn = widgets.QPushButton()
    relax_btn.setText("Relax")
    relax_btn.clicked.connect(lambda: app.exit(0))

    hlayout = widgets.QHBoxLayout()
    hlayout.setSpacing(5)
    hlayout.addWidget(continue_btn)
    hlayout.addWidget(relax_btn)

    vlayout = widgets.QVBoxLayout()
    vlayout.setSpacing(5)
    vlayout.addWidget(label)
    vlayout.addLayout(hlayout)

    win.setLayout(vlayout)
    win.show()
    sys.exit(app.exec_())
