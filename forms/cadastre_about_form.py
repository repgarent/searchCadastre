# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/cadastre_about_form.ui'
#
# Created: Tue Nov  5 16:39:48 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_cadastre_about_form(object):
    def setupUi(self, cadastre_about_form):
        cadastre_about_form.setObjectName(_fromUtf8("cadastre_about_form"))
        cadastre_about_form.resize(692, 652)
        self.verticalLayout = QtGui.QVBoxLayout(cadastre_about_form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(cadastre_about_form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 656, 709))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setOpenExternalLinks(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_19 = QtGui.QLabel(self.groupBox_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_6)
        self.label_20.setOpenExternalLinks(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_2.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setOpenExternalLinks(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_2.addWidget(self.label_18)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(cadastre_about_form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(cadastre_about_form)
        QtCore.QMetaObject.connectSlotsByName(cadastre_about_form)

    def retranslateUi(self, cadastre_about_form):
        cadastre_about_form.setWindowTitle(_translate("cadastre_about_form", "Cadastre - A propos", None))
        self.groupBox.setTitle(_translate("cadastre_about_form", "Financeurs", None))
        self.label_5.setText(_translate("cadastre_about_form", "La réalisation du plugin Cadastre a été financée par", None))
        self.label_8.setText(_translate("cadastre_about_form", "<html><head/><body><p><a href=\"http://europa.eu/index_fr.htm\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\"/><img src=\":/plugins/cadastre/images/logo_europe.png\"/></a></p></body></html>", None))
        self.label_9.setText(_translate("cadastre_about_form", "<html><head/><body><p><a href=\"http://www.picardie-europe.eu/\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\"/><img src=\":/plugins/cadastre/images/logo_feder.png\"/></a></p></body></html>", None))
        self.label_6.setText(_translate("cadastre_about_form", "<html><head/><body><p><a href=\"http://www.aduga.org/\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\"/><img src=\":/plugins/cadastre/images/logo_aduga.png\"/></a></p></body></html>", None))
        self.label.setText(_translate("cadastre_about_form", "<a href=\"http://www.aduga.org/\" style=\"color:#434343;text-decoration:none;\">L\'Agence de Développement et  d\'Urbanisme du Grand Amiénois</a>", None))
        self.label_4.setText(_translate("cadastre_about_form", "<a href=\"http://www.picardie-europe.eu/\" style=\"color:#434343;text-decoration:none;\">Le  Fonds Européen de Développement Régional de Picardie</a>", None))
        self.label_3.setText(_translate("cadastre_about_form", "<a href=\"http://europa.eu/index_fr.htm\" style=\"color:#434343;text-decoration:none;\">L\'Union Européenne</a>", None))
        self.label_7.setText(_translate("cadastre_about_form", "<html><head/><body><p><a href=\"http://www.picardie.fr/\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\"/><img src=\":/plugins/cadastre/images/logo_picardie.png\"/></a></p></body></html>", None))
        self.label_2.setText(_translate("cadastre_about_form", "<a href=\"http://www.picardie.fr/\" style=\"color:#434343;text-decoration:none;\">Le Conseil Régional de Picardie</a>", None))
        self.groupBox_2.setTitle(_translate("cadastre_about_form", "Conception", None))
        self.label_10.setText(_translate("cadastre_about_form", "Le plugin Cadastre a été conçu et développé par la Société 3liz", None))
        self.label_12.setText(_translate("cadastre_about_form", "<html><head/><body><p><a href=\"http://www.3liz.com/\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\"/><img src=\":/plugins/cadastre/images/logo_3liz.png\"/></a></p></body></html>", None))
        self.label_11.setText(_translate("cadastre_about_form", "<a href=\"http://www.3liz.com\" style=\"color:#7BA11A;text-decoration:none;\">Libérez vos SIG !</a>", None))
        self.groupBox_3.setTitle(_translate("cadastre_about_form", "Auteurs", None))
        self.label_13.setText(_translate("cadastre_about_form", "Michaël DOUCHIN", None))
        self.label_14.setText(_translate("cadastre_about_form", "<a href=\"mailto:mdouchin@3liz.com?subject=Plugin cadastre - A propos\" style=\"color:#7BA11A;text-decoration:none;\">mdouchin@3liz.com</a>", None))
        self.groupBox_6.setTitle(_translate("cadastre_about_form", "Sources", None))
        self.label_19.setText(_translate("cadastre_about_form", "Dépôt sur GitHub", None))
        self.label_20.setText(_translate("cadastre_about_form", "<a href=\"https://github.com/3liz/QgisCadastrePlugin\" style=\"color:#7BA11A;text-decoration:none;\">https://github.com/3liz/QgisCadastrePlugin</a>", None))
        self.groupBox_4.setTitle(_translate("cadastre_about_form", "Licence", None))
        self.label_15.setText(_translate("cadastre_about_form", "Licence GPL Version 3", None))
        self.label_16.setText(_translate("cadastre_about_form", "<html><head/><body><p><a href=\"http://www.gnu.org/licenses/gpl.html\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\"/><img src=\":/plugins/cadastre/images/logo_gnu3.png\"/></a></p></body></html>", None))
        self.groupBox_5.setTitle(_translate("cadastre_about_form", "Ressources", None))
        self.label_17.setText(_translate("cadastre_about_form", "Les scripts d\'import pour PostGreSQL proviennent de l\'outil OpenCadastre (licence GPL). Ils ont été adaptés et améliorés pour leur utilisation dans ce plugin. Nos remerciement aux contributeurs.", None))
        self.label_18.setText(_translate("cadastre_about_form", "<a href=\"https://adullact.net/scm/viewvc.php/trunk/data/pgsql/?root=opencadastre\"  style=\"color:#7BA11A;text-decoration:none;\">Dépôt OpenCadastre</a>", None))

import resource_rc