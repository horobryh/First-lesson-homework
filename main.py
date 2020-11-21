import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connect = sqlite3.connect('coffee.db')
        self.titles = {0: 'Молотый', 1: 'В зёрнах'}
        self.cb_variety.currentTextChanged.connect(self.load_info)
        self.update_all()
        self.need_update = True
        self.load_info()
        self.pb_add.clicked.connect(self.add_item)
        self.pb_edit.clicked.connect(self.edit_item)

    def load_info(self):
        if not self.need_update:
            return
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

    def add_item(self):
        self.form = AddEditCoffee(self.update_all)
        self.form.show()

    def edit_item(self):
        self.form = AddEditCoffee(self.update_all,
                                  self.cb_variety.currentText(),
                                  self.le_id.text())
        self.form.coffee_id = self.le_id.text()
        self.form.show()

    def update_all(self):
        variety = self.connect.cursor().execute(
            'SELECT title FROM Coffee').fetchall()
        self.need_update = False
        self.cb_variety.clear()
        self.cb_variety.addItems(map(lambda x: x[0], variety))
        self.need_update = True
        self.load_info()


class AddEditCoffee(QWidget):
    def __init__(self, func_update, title=None, coffee_id=None):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.connect = sqlite3.connect('coffee.db')
        self.func_update = func_update
        variety = self.connect.cursor().execute(
            'SELECT title FROM Degree_of_roasting').fetchall()
        self.cb_degree.addItems(map(lambda x: x[0], variety))
        self.titles = {0: 'Молотый', 1: 'В зёрнах'}
        self.cb_type.addItems(self.titles.values())
        self.pb_save.clicked.connect(self.save_item)
        self.coffee_id = coffee_id

        if title is not None:
            self.le_title.setText(str(title))
            self.le_title.setEnabled(False)
            self.cb_degree.setCurrentText(self.connect.cursor().execute(
                '''SELECT dor.title FROM Coffee c JOIN Degree_of_roasting dor 
                    ON c.degree_of_roasting = dor.id WHERE c.id = ?''',
                (self.coffee_id,)).fetchone()[0])
            info = self.connect.cursor().execute('''SELECT * FROM Coffee 
                WHERE id = ?''', (self.coffee_id,)).fetchone()
            self.cb_type.setCurrentText(self.titles[info[3]])
            self.le_taste.setText(info[4])
            self.sb_price.setValue(info[5])
            self.sb_volume.setValue(info[6])

    def save_item(self):
        title = self.le_title.text()
        degree = self.connect.cursor().execute('''SELECT id FROM 
            Degree_of_roasting WHERE title = ?''',
                                               (self.cb_degree.currentText(),
                                                )).fetchone()[0]
        type = {j: i for i, j in self.titles.items()}[self.cb_type.currentText()]
        taste = self.le_taste.text()
        price = self.sb_price.value()
        volume = self.sb_volume.value()
        if title == '' or taste == '':
            QMessageBox.critical(self, 'Ошибка заполнения',
                                 'Вы заполнили не все поля.', QMessageBox.Ok)
            return
        if not self.le_title.isEnabled():
            self.connect.cursor().execute('''UPDATE Coffee 
                SET title = ?, degree_of_roasting = ?, 
                    is_grounds_or_in_grains = ?, taste = ?, price = ?, 
                        volume = ? WHERE id = ?''', (title, degree, type,
                                                     taste, price, volume,
                                                     self.coffee_id))
        else:
            if self.connect.cursor().execute('''SELECT * FROM Coffee 
                    WHERE title = ?''', (title,)).fetchone() is not None:
                QMessageBox.critical(self, 'Ошибка названия',
                                     'Позиция с таким названием уже '
                                     'существует', QMessageBox.Ok)
                return
            self.connect.cursor().execute('''INSERT INTO Coffee(title, 
                degree_of_roasting, is_grounds_or_in_grains, taste, price, 
                    volume) VALUES(?, ?, ?, ?, ?, ?)''', (title, degree,
                                                          type, taste, price,
                                                          volume))
        self.connect.commit()
        self.func_update()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
