if __name__ == "__main__":
    from PySide2.QtCore import QCoreApplication
    QCoreApplication.setLibraryPaths(['C:/DEV/Langs/Python/Python310/Lib/site-packages/PySide2/plugins'])

import sys
from PySide2.QtWidgets import QWidget, QApplication,QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams


class MatplotlibWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.canvas = FigureCanvas(Figure())
        vertLayout = QVBoxLayout()
        vertLayout.addWidget(self.canvas)
        self.setLayout(vertLayout)
        self.axes = self.canvas.figure.add_subplot(111)

if __name__ == "__main__":
    import numpy as np
    app = QApplication(sys.argv)
    window = MatplotlibWidget()
    window.show()

    x = np.linspace(0, 10. ,50)
    window.axes.plot(x, np.sin(x))
    window.axes.plot(x, np.sin(x),'*')

    app.exec_()