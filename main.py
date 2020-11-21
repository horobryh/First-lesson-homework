import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connect = sqlite3.connect('coffee.db')
        variety = self.connect.cursor().execute(
            'SELECT title FROM Coffee').fetchall()
        self.cb_variety.addItems(map(lambda x: x[0], variety))
        self.titles = {0: 'Молотый', 1: 'В зёрнах'}
        self.cb_variety.currentTextChanged.connect(self.load_info)
        self.load_info()

    def load_info(self):
        results = self.connect.cursor().execute('''SELECT * FROM Coffee c 
            JOIN Degree_of_roasting dor ON c.degree_of_roasting = dor.id 
                WHERE c.title = ?''', (
            self.cb_variety.currentText(),)).fetchall()[0]
        self.le_id.setText(str(results[0]))
        self.le_degree.setText(results[-1])
        self.le_price.setText(str(results[5]))
        self.le_volume.setText(str(results[6]))
        self.le_taste.setText(results[4])
        self.le_type.setText(self.titles[int(results[3])])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
