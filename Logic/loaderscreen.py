from Resources.all_imports import *


class splashscene(QSplashScreen):

    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("./UIFiles/SplashScreen_File.ui", self)
        self.makeWindowCenter()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def progress(self):
        for i in range(101):
            time.sleep(0.03)
            self.progressBar.setValue(i)

    def makeWindowCenter(self):
        """For launching windows in center."""
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
