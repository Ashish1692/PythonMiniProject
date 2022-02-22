import os
import sys
import time
from platform import system

from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPalette, QPixmap
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QFileDialog,
                            QInputDialog, QLineEdit, QMainWindow, QMessageBox,
                            QSplashScreen, QStyleFactory)
from PyQt5.uic import loadUi, loadUiType

from Logic import Logic_App
from Logic.loaderscreen import splashscene
