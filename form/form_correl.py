# Form implementation generated from reading ui file 'form_correl.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 300)
        Dialog.setStyleSheet("QDialog{\n"
"background-color: #373737;\n"
"}\n"
"QLabel{\n"
"font-size: 10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_correl = QtWidgets.QTableWidget(Dialog)
        self.table_correl.setObjectName("table_correl")
        self.table_correl.setColumnCount(0)
        self.table_correl.setRowCount(0)
        self.horizontalLayout.addWidget(self.table_correl)
        self.graphic_correl = QtWidgets.QWidget(Dialog)
        self.graphic_correl.setObjectName("graphic_correl")
        self.horizontalLayout.addWidget(self.graphic_correl)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.znam_correl_label = QtWidgets.QLabel(Dialog)
        self.znam_correl_label.setObjectName("znam_correl_label")
        self.gridLayout.addWidget(self.znam_correl_label, 1, 1, 1, 1)
        self.coef_correl_label = QtWidgets.QLabel(Dialog)
        self.coef_correl_label.setObjectName("coef_correl_label")
        self.gridLayout.addWidget(self.coef_correl_label, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:10px;\">Коэффициент корреляции</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:10px;\">Значимость коэффциента корреляции</span></p></body></html>"))
        self.znam_correl_label.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:10px;\"></span></p></body></html>"))
        self.coef_correl_label.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:10px;\"></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())