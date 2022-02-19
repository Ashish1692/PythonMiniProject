from all_imports import *

# Application root location ↓
if system() == "Windows":
    appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"
elif system() == "Linux":
    appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "//"


class App(QMainWindow):
    def __init__(self):
        """Constructor."""
        super(App, self).__init__()
        uic.loadUi(appFolder + "Main_Ui_File.ui", self)  # Load the UI(User Interface) file.

        self.makeWindowCenter()
        self.run_system()  # main operating function of this GUI FIle
        # Status Bar Message
        self.statusBar().showMessage("Convert your to files to PDF.")
        self.setWindowTitle("File Format Converter")

    def makeWindowCenter(self):
        """For launching windows in center."""
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def run_system(self):
        """Main load function"""
        self.pushButton.clicked.connect(self.add_folder_button_on_click)
        self.pushButton_add.clicked.connect(self.add_images_button_on_click)
        self.pushButton_remove.clicked.connect(self.remove_button_on_click)
        self.pushButton_up.clicked.connect(self.up_button_on_click)
        self.pushButton_down.clicked.connect(self.down_button_on_click)
        self.pushButton_make_pdf.clicked.connect(self.make_pdf_button_on_click)
        self.pushButton_clear.clicked.connect(self.clear_button_on_click)

    def add_folder_button_on_click(self):
        """Add a Folder button"""

        dir_path = QFileDialog.getExistingDirectory(self, 'Open File')

        if dir_path != "":
            dir_files = main.make_pdf_all(dir_path)
            for i in dir_files:
                next_row = self.listWidget.count()
                self.listWidget.insertItem(next_row, i)
        else:
            return

    def add_images_button_on_click(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File")
        next_row = self.listWidget.count()
        if file_name[0] != "":
            self.listWidget.insertItem(next_row, file_name[0])

    def remove_button_on_click(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        if item is None:
            pass

        else:
            get_reply = QMessageBox.question(self, "Remove An Image File", "Do you want to remove " + str(item.text())
                                             + " from the list?", QMessageBox.Yes | QMessageBox.No)
            if get_reply == QMessageBox.Yes:
                element = self.listWidget.takeItem(current_row)
                del element
            else:
                pass

    def up_button_on_click(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 1:
            item = self.listWidget.takeItem(current_row)
            self.listWidget.insertItem(current_row - 1, item)
            self.listWidget.setCurrentItem(item)

    def down_button_on_click(self):
        current_row = self.listWidget.currentRow()
        if current_row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(current_row)
            self.listWidget.insertItem(current_row + 1, item)
            self.listWidget.setCurrentItem(item)

    def clear_button_on_click(self):
        reply = QMessageBox.question(self, "Clear List Box", "Do you want to clear all the selections?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.listWidget.clear()

    def make_pdf_button_on_click(self):
        if self.listWidget.count() == 0:
            reply = QMessageBox.information(
                self, "Warning!", "List box is empty! Add files to list box first.", QMessageBox.Ok)

        else:
            items_list = []
            for i in range(self.listWidget.count()):
                items_list.append(str(self.listWidget.item(i).text()))

            pdf_name, ok = QInputDialog.getText(self, "PDF Name", "Give A Name To Your PDF File", QLineEdit.Normal)
            if pdf_name == "":
                QMessageBox.information(self, "Alert", "Please Give Your PDF a name.", QMessageBox.Ok)
                return
            if ok and pdf_name is not None:
                reply = QMessageBox.information(self, "PDF Location", "Let's Select A Destination "
                                                "To Save Your PDF File!", QMessageBox.Ok)

                if reply == QMessageBox.Ok:

                    pdf_location = QFileDialog.getExistingDirectory(self, 'Open File')
                    pdf_name += ".pdf"
                    if pdf_location == "":
                        return
                    main.make_pdf_only_selected(items_list, pdf_name, pdf_location)
                    last_reply = QMessageBox.information(self, "Done!", "Hurrah! Your PDF is ready! "
                                                                        "Go to your selected location to find "
                                                                        "the PDF.", QMessageBox.Ok)
                    if last_reply == QMessageBox.Ok:
                        pass
                else:
                    return


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        app.setStyle(QStyleFactory.create("Fusion"))

        darkPalette = QtGui.QPalette()
        darkColor = QColor(15,17,18)
        disabledColor = QColor(127, 127, 127)
        darkPalette.setColor(QPalette.Window, darkColor)
        darkPalette.setColor(QPalette.WindowText, Qt.white)
        darkPalette.setColor(QPalette.Base, QColor(0,8,5))
        darkPalette.setColor(QPalette.AlternateBase, darkColor)
        darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        darkPalette.setColor(QPalette.ToolTipText, Qt.white)
        darkPalette.setColor(QPalette.Text, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.Text, disabledColor)
        darkPalette.setColor(QPalette.Button, darkColor)
        darkPalette.setColor(QPalette.ButtonText, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, disabledColor)
        darkPalette.setColor(QPalette.BrightText, Qt.red)
        darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.HighlightedText, Qt.black)
        darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, disabledColor)

        app.setPalette(darkPalette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

        splash = splashscene() # init the splashscreen ui 
        splash.show()          # show splashscreen ui
        splash.progress()      # updating progressbar

        run_main = App()  # Instantiate The App() class
        run_main.show()

        splash.finish(run_main) # this will run main module when progress reaches to 100

        try:
            sys.exit(app.exec_())
        except Exception as t:
            raise t
        finally:
            print("Application Ran Successfully...")
            
    except Exception as e:
        print(f"Error:{e}")
    
