# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/simple_cadastre_search_form.ui'
#
# Created: Tue Dec 23 14:26:34 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_simple_cadastre_search_form(object):
    def setupUi(self, simple_cadastre_search_form):
        simple_cadastre_search_form.setObjectName(_fromUtf8("simple_cadastre_search_form"))
        simple_cadastre_search_form.resize(545, 852)
        simple_cadastre_search_form.setMinimumSize(QtCore.QSize(545, 310))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setMaximumSize(QtCore.QSize(944, 16777215))
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(17, 542, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.grpLieu = QtGui.QGroupBox(self.dockWidgetContents)
        self.grpLieu.setObjectName(_fromUtf8("grpLieu"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.grpLieu)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_13 = QtGui.QLabel(self.grpLieu)
        self.label_13.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.liCommune = QtGui.QComboBox(self.grpLieu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liCommune.sizePolicy().hasHeightForWidth())
        self.liCommune.setSizePolicy(sizePolicy)
        self.liCommune.setObjectName(_fromUtf8("liCommune"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.liCommune)
        self.label_4 = QtGui.QLabel(self.grpLieu)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.liSection = QtGui.QComboBox(self.grpLieu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liSection.sizePolicy().hasHeightForWidth())
        self.liSection.setSizePolicy(sizePolicy)
        self.liSection.setObjectName(_fromUtf8("liSection"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.liSection)
        self.label_10 = QtGui.QLabel(self.grpLieu)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.liAdresse = QtGui.QLineEdit(self.grpLieu)
        self.liAdresse.setObjectName(_fromUtf8("liAdresse"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.liAdresse)
        self.label_9 = QtGui.QLabel(self.grpLieu)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        #self.liProprietaire = QtGui.QLineEdit(self.grpLieu)
        #self.liProprietaire.setObjectName(_fromUtf8("liProprietaire"))
        #self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.liProprietaire)
        self.label_3 = QtGui.QLabel(self.grpLieu)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.liParcelle = QtGui.QComboBox(self.grpLieu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liParcelle.sizePolicy().hasHeightForWidth())
        self.liParcelle.setSizePolicy(sizePolicy)
        self.liParcelle.setEditable(True)
        self.liParcelle.setObjectName(_fromUtf8("liParcelle"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.liParcelle)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btCentrerLieu = QtGui.QPushButton(self.grpLieu)
        self.btCentrerLieu.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/centrer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btCentrerLieu.setIcon(icon)
        self.btCentrerLieu.setObjectName(_fromUtf8("btCentrerLieu"))
        self.horizontalLayout_3.addWidget(self.btCentrerLieu)
        self.btZoomerLieu = QtGui.QPushButton(self.grpLieu)
        self.btZoomerLieu.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/zoom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btZoomerLieu.setIcon(icon1)
        self.btZoomerLieu.setObjectName(_fromUtf8("btZoomerLieu"))
        self.horizontalLayout_3.addWidget(self.btZoomerLieu)
        self.btSelectionnerLieu = QtGui.QPushButton(self.grpLieu)
        self.btSelectionnerLieu.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSelectionnerLieu.setIcon(icon2)
        self.btSelectionnerLieu.setObjectName(_fromUtf8("btSelectionnerLieu"))
        self.horizontalLayout_3.addWidget(self.btSelectionnerLieu)
        self.btExportParcelle = QtGui.QPushButton(self.grpLieu)
        self.btExportParcelle.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/releve.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btExportParcelle.setIcon(icon3)
        self.btExportParcelle.setObjectName(_fromUtf8("btExportParcelle"))
        self.horizontalLayout_3.addWidget(self.btExportParcelle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_2.addWidget(self.grpLieu, 0, 1, 1, 1)
        self.txtLog = QtGui.QLabel(self.dockWidgetContents)
        self.txtLog.setText(_fromUtf8(""))
        self.txtLog.setObjectName(_fromUtf8("txtLog"))
        self.gridLayout_2.addWidget(self.txtLog, 1, 1, 1, 1)
        simple_cadastre_search_form.setWidget(self.dockWidgetContents)

        self.retranslateUi(simple_cadastre_search_form)
        QtCore.QMetaObject.connectSlotsByName(simple_cadastre_search_form)

    def retranslateUi(self, simple_cadastre_search_form):
        simple_cadastre_search_form.setWindowTitle(_translate("simple_cadastre_search_form", "Cadastre - Outils de recherche", None))
        self.grpLieu.setTitle(_translate("simple_cadastre_search_form", "Recherche", None))
        self.label_13.setText(_translate("simple_cadastre_search_form", "Commune", None))
        self.label_4.setText(_translate("simple_cadastre_search_form", "Section", None))
        self.label_10.setText(_translate("simple_cadastre_search_form", "Adresse", None))
        self.label_9.setText(_translate("simple_cadastre_search_form", "Propriétaire", None))
        self.label_3.setText(_translate("simple_cadastre_search_form", "Parcelle", None))
        self.btCentrerLieu.setToolTip(_translate("simple_cadastre_search_form", "Centrer sur l\'objet", None))
        self.btZoomerLieu.setToolTip(_translate("simple_cadastre_search_form", "Zoomer sur l\'objet", None))
        self.btSelectionnerLieu.setToolTip(_translate("simple_cadastre_search_form", "Sélectionner l\'objet", None))
        self.btExportParcelle.setToolTip(_translate("simple_cadastre_search_form", "Exporter le relevé parcellaire", None))

import resource_rc
