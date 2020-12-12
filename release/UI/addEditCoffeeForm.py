# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 260)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_title = QtWidgets.QLineEdit(Form)
        self.le_title.setObjectName("le_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_title)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cb_degree = QtWidgets.QComboBox(Form)
        self.cb_degree.setObjectName("cb_degree")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_degree)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cb_type = QtWidgets.QComboBox(Form)
        self.cb_type.setObjectName("cb_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_type)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.le_taste = QtWidgets.QLineEdit(Form)
        self.le_taste.setObjectName("le_taste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_taste)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.sb_price = QtWidgets.QSpinBox(Form)
        self.sb_price.setMinimum(1)
        self.sb_price.setMaximum(999999999)
        self.sb_price.setObjectName("sb_price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sb_price)
        self.sb_volume = QtWidgets.QSpinBox(Form)
        self.sb_volume.setMinimum(1)
        self.sb_volume.setMaximum(999999999)
        self.sb_volume.setProperty("value", 1)
        self.sb_volume.setObjectName("sb_volume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sb_volume)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_save = QtWidgets.QPushButton(Form)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout.addWidget(self.pb_save)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Сорт кофе"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Вид кофе"))
        self.label_4.setText(_translate("Form", "Вкус"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))
        self.pb_save.setText(_translate("Form", "Сохранить"))
