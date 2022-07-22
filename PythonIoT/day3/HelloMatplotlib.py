import sys
from PySide2.QtWidgets import QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

if __name__ == "__main__":
    import numpy as np
    app = QApplication(sys.argv)

    x = np.linspace(0,1,50)

    y1 = np.cos(4*np.pi*x)
    y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

    canvasWidget = FigureCanvas(Figure(figsize=(6,4)))
    ax = canvasWidget.figure.add_subplot(2,1,1)
    ax.plot(x,y1,'r-*',lw=1)
    ax.grid(True)
    ax.set_ylabel(r'$sin(4 \pi x)$')
    ax.axis([0,1,-1.5,1.5])

    ax = canvasWidget.figure.add_subplot(2,1,2)
    ax.plot(x,y2,'b--o',lw=1)
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel(r'$ e^{-2x} sin(4\pi x) $')
    ax.axis([0,1,-1.5,1.5])     

    canvasWidget.figure.tight_layout()

    canvasWidget.show()
    app.exec_()