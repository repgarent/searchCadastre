# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/cadastre_search_form.ui'
#
# Created: Mon Jan 27 10:07:04 2014
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

class Ui_cadastre_search_form(object):
    def setupUi(self, cadastre_search_form):
        cadastre_search_form.setObjectName(_fromUtf8("cadastre_search_form"))
        cadastre_search_form.resize(339, 625)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea_3 = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 319, 580))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.grpLieu = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.grpLieu.setObjectName(_fromUtf8("grpLieu"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.grpLieu)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_12 = QtGui.QLabel(self.grpLieu)
        self.label_12.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.grpLieu)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.grpLieu)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.liCommune = QtGui.QComboBox(self.grpLieu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liCommune.sizePolicy().hasHeightForWidth())
        self.liCommune.setSizePolicy(sizePolicy)
        self.liCommune.setObjectName(_fromUtf8("liCommune"))
        self.gridLayout.addWidget(self.liCommune, 0, 1, 1, 1)
        self.liSection = QtGui.QComboBox(self.grpLieu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liSection.sizePolicy().hasHeightForWidth())
        self.liSection.setSizePolicy(sizePolicy)
        self.liSection.setObjectName(_fromUtf8("liSection"))
        self.gridLayout.addWidget(self.liSection, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.liParcelle = QtGui.QComboBox(self.grpLieu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liParcelle.sizePolicy().hasHeightForWidth())
        self.liParcelle.setSizePolicy(sizePolicy)
        self.liParcelle.setEditable(True)
        self.liParcelle.setObjectName(_fromUtf8("liParcelle"))
        self.horizontalLayout_4.addWidget(self.liParcelle)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.btResetCommune = QtGui.QToolButton(self.grpLieu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btResetCommune.setIcon(icon)
        self.btResetCommune.setObjectName(_fromUtf8("btResetCommune"))
        self.gridLayout.addWidget(self.btResetCommune, 0, 2, 1, 1)
        self.btResetSection = QtGui.QToolButton(self.grpLieu)
        self.btResetSection.setIcon(icon)
        self.btResetSection.setObjectName(_fromUtf8("btResetSection"))
        self.gridLayout.addWidget(self.btResetSection, 1, 2, 1, 1)
        self.btResetParcelle = QtGui.QToolButton(self.grpLieu)
        self.btResetParcelle.setIcon(icon)
        self.btResetParcelle.setObjectName(_fromUtf8("btResetParcelle"))
        self.gridLayout.addWidget(self.btResetParcelle, 2, 2, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btCentrerLieu = QtGui.QPushButton(self.grpLieu)
        self.btCentrerLieu.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/centrer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btCentrerLieu.setIcon(icon1)
        self.btCentrerLieu.setObjectName(_fromUtf8("btCentrerLieu"))
        self.horizontalLayout_2.addWidget(self.btCentrerLieu)
        self.btZoomerLieu = QtGui.QPushButton(self.grpLieu)
        self.btZoomerLieu.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/zoom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btZoomerLieu.setIcon(icon2)
        self.btZoomerLieu.setObjectName(_fromUtf8("btZoomerLieu"))
        self.horizontalLayout_2.addWidget(self.btZoomerLieu)
        self.btSelectionnerLieu = QtGui.QPushButton(self.grpLieu)
        self.btSelectionnerLieu.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSelectionnerLieu.setIcon(icon3)
        self.btSelectionnerLieu.setObjectName(_fromUtf8("btSelectionnerLieu"))
        self.horizontalLayout_2.addWidget(self.btSelectionnerLieu)
        self.btExportParcelle = QtGui.QPushButton(self.grpLieu)
        self.btExportParcelle.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/releve.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btExportParcelle.setIcon(icon4)
        self.btExportParcelle.setObjectName(_fromUtf8("btExportParcelle"))
        self.horizontalLayout_2.addWidget(self.btExportParcelle)
        self.verticalLayout_14.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addWidget(self.grpLieu)
        self.grpAdresse = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.grpAdresse.setObjectName(_fromUtf8("grpAdresse"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.grpAdresse)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.liAdresse = QtGui.QComboBox(self.grpAdresse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liAdresse.sizePolicy().hasHeightForWidth())
        self.liAdresse.setSizePolicy(sizePolicy)
        self.liAdresse.setEditable(True)
        self.liAdresse.setObjectName(_fromUtf8("liAdresse"))
        self.gridLayout_3.addWidget(self.liAdresse, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.grpAdresse)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.grpAdresse)
        self.label_6.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.liParcelleAdresse = QtGui.QComboBox(self.grpAdresse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liParcelleAdresse.sizePolicy().hasHeightForWidth())
        self.liParcelleAdresse.setSizePolicy(sizePolicy)
        self.liParcelleAdresse.setEditable(True)
        self.liParcelleAdresse.setObjectName(_fromUtf8("liParcelleAdresse"))
        self.gridLayout_3.addWidget(self.liParcelleAdresse, 1, 1, 1, 1)
        self.btResetParcelleAdresse = QtGui.QToolButton(self.grpAdresse)
        self.btResetParcelleAdresse.setIcon(icon)
        self.btResetParcelleAdresse.setObjectName(_fromUtf8("btResetParcelleAdresse"))
        self.gridLayout_3.addWidget(self.btResetParcelleAdresse, 1, 2, 1, 1)
        self.btSearchAdresse = QtGui.QToolButton(self.grpAdresse)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSearchAdresse.setIcon(icon5)
        self.btSearchAdresse.setObjectName(_fromUtf8("btSearchAdresse"))
        self.gridLayout_3.addWidget(self.btSearchAdresse, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btCentrerAdresse = QtGui.QPushButton(self.grpAdresse)
        self.btCentrerAdresse.setText(_fromUtf8(""))
        self.btCentrerAdresse.setIcon(icon1)
        self.btCentrerAdresse.setObjectName(_fromUtf8("btCentrerAdresse"))
        self.horizontalLayout.addWidget(self.btCentrerAdresse)
        self.btZoomerAdresse = QtGui.QPushButton(self.grpAdresse)
        self.btZoomerAdresse.setText(_fromUtf8(""))
        self.btZoomerAdresse.setIcon(icon2)
        self.btZoomerAdresse.setObjectName(_fromUtf8("btZoomerAdresse"))
        self.horizontalLayout.addWidget(self.btZoomerAdresse)
        self.btSelectionnerAdresse = QtGui.QPushButton(self.grpAdresse)
        self.btSelectionnerAdresse.setText(_fromUtf8(""))
        self.btSelectionnerAdresse.setIcon(icon3)
        self.btSelectionnerAdresse.setObjectName(_fromUtf8("btSelectionnerAdresse"))
        self.horizontalLayout.addWidget(self.btSelectionnerAdresse)
        self.btExportParcelleAdresse = QtGui.QPushButton(self.grpAdresse)
        self.btExportParcelleAdresse.setText(_fromUtf8(""))
        self.btExportParcelleAdresse.setIcon(icon4)
        self.btExportParcelleAdresse.setObjectName(_fromUtf8("btExportParcelleAdresse"))
        self.horizontalLayout.addWidget(self.btExportParcelleAdresse)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_13.addWidget(self.grpAdresse)
        self.grpProprietaire = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.grpProprietaire.setObjectName(_fromUtf8("grpProprietaire"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.grpProprietaire)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.liProprietaire = QtGui.QComboBox(self.grpProprietaire)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liProprietaire.sizePolicy().hasHeightForWidth())
        self.liProprietaire.setSizePolicy(sizePolicy)
        self.liProprietaire.setEditable(True)
        self.liProprietaire.setObjectName(_fromUtf8("liProprietaire"))
        self.gridLayout_2.addWidget(self.liProprietaire, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.grpProprietaire)
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.liParcelleProprietaire = QtGui.QComboBox(self.grpProprietaire)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liParcelleProprietaire.sizePolicy().hasHeightForWidth())
        self.liParcelleProprietaire.setSizePolicy(sizePolicy)
        self.liParcelleProprietaire.setEditable(True)
        self.liParcelleProprietaire.setObjectName(_fromUtf8("liParcelleProprietaire"))
        self.gridLayout_2.addWidget(self.liParcelleProprietaire, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.grpProprietaire)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.btSearchProprietaire = QtGui.QToolButton(self.grpProprietaire)
        self.btSearchProprietaire.setIcon(icon5)
        self.btSearchProprietaire.setObjectName(_fromUtf8("btSearchProprietaire"))
        self.gridLayout_2.addWidget(self.btSearchProprietaire, 0, 2, 1, 1)
        self.btResetParcelleProprietaire = QtGui.QToolButton(self.grpProprietaire)
        self.btResetParcelleProprietaire.setIcon(icon)
        self.btResetParcelleProprietaire.setObjectName(_fromUtf8("btResetParcelleProprietaire"))
        self.gridLayout_2.addWidget(self.btResetParcelleProprietaire, 1, 2, 1, 1)
        self.btExportParcelleProprietaire = QtGui.QToolButton(self.grpProprietaire)
        self.btExportParcelleProprietaire.setIcon(icon4)
        self.btExportParcelleProprietaire.setObjectName(_fromUtf8("btExportParcelleProprietaire"))
        self.gridLayout_2.addWidget(self.btExportParcelleProprietaire, 1, 3, 1, 1)
        self.btExportProprietaire = QtGui.QToolButton(self.grpProprietaire)
        self.btExportProprietaire.setIcon(icon4)
        self.btExportProprietaire.setObjectName(_fromUtf8("btExportProprietaire"))
        self.gridLayout_2.addWidget(self.btExportProprietaire, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btCentrerProprietaire = QtGui.QPushButton(self.grpProprietaire)
        self.btCentrerProprietaire.setText(_fromUtf8(""))
        self.btCentrerProprietaire.setIcon(icon1)
        self.btCentrerProprietaire.setObjectName(_fromUtf8("btCentrerProprietaire"))
        self.horizontalLayout_3.addWidget(self.btCentrerProprietaire)
        self.btZoomerProprietaire = QtGui.QPushButton(self.grpProprietaire)
        self.btZoomerProprietaire.setText(_fromUtf8(""))
        self.btZoomerProprietaire.setIcon(icon2)
        self.btZoomerProprietaire.setObjectName(_fromUtf8("btZoomerProprietaire"))
        self.horizontalLayout_3.addWidget(self.btZoomerProprietaire)
        self.btSelectionnerProprietaire = QtGui.QPushButton(self.grpProprietaire)
        self.btSelectionnerProprietaire.setText(_fromUtf8(""))
        self.btSelectionnerProprietaire.setIcon(icon3)
        self.btSelectionnerProprietaire.setObjectName(_fromUtf8("btSelectionnerProprietaire"))
        self.horizontalLayout_3.addWidget(self.btSelectionnerProprietaire)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addWidget(self.grpProprietaire)
        self.txtLog = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.txtLog.setObjectName(_fromUtf8("txtLog"))
        self.verticalLayout_13.addWidget(self.txtLog)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_3)
        cadastre_search_form.setWidget(self.dockWidgetContents)

        self.retranslateUi(cadastre_search_form)
        QtCore.QMetaObject.connectSlotsByName(cadastre_search_form)
        cadastre_search_form.setTabOrder(self.scrollArea_3, self.liAdresse)
        cadastre_search_form.setTabOrder(self.liAdresse, self.btSearchAdresse)
        cadastre_search_form.setTabOrder(self.btSearchAdresse, self.liParcelleAdresse)
        cadastre_search_form.setTabOrder(self.liParcelleAdresse, self.btResetParcelleAdresse)
        cadastre_search_form.setTabOrder(self.btResetParcelleAdresse, self.btCentrerAdresse)
        cadastre_search_form.setTabOrder(self.btCentrerAdresse, self.btZoomerAdresse)
        cadastre_search_form.setTabOrder(self.btZoomerAdresse, self.btSelectionnerAdresse)
        cadastre_search_form.setTabOrder(self.btSelectionnerAdresse, self.btExportParcelleAdresse)
        cadastre_search_form.setTabOrder(self.btExportParcelleAdresse, self.liCommune)
        cadastre_search_form.setTabOrder(self.liCommune, self.btResetCommune)
        cadastre_search_form.setTabOrder(self.btResetCommune, self.liSection)
        cadastre_search_form.setTabOrder(self.liSection, self.btResetSection)
        cadastre_search_form.setTabOrder(self.btResetSection, self.liParcelle)
        cadastre_search_form.setTabOrder(self.liParcelle, self.btResetParcelle)
        cadastre_search_form.setTabOrder(self.btResetParcelle, self.btCentrerLieu)
        cadastre_search_form.setTabOrder(self.btCentrerLieu, self.btZoomerLieu)
        cadastre_search_form.setTabOrder(self.btZoomerLieu, self.btSelectionnerLieu)
        cadastre_search_form.setTabOrder(self.btSelectionnerLieu, self.btExportParcelle)
        cadastre_search_form.setTabOrder(self.btExportParcelle, self.liProprietaire)
        cadastre_search_form.setTabOrder(self.liProprietaire, self.btSearchProprietaire)
        cadastre_search_form.setTabOrder(self.btSearchProprietaire, self.btExportProprietaire)
        cadastre_search_form.setTabOrder(self.btExportProprietaire, self.liParcelleProprietaire)
        cadastre_search_form.setTabOrder(self.liParcelleProprietaire, self.btResetParcelleProprietaire)
        cadastre_search_form.setTabOrder(self.btResetParcelleProprietaire, self.btExportParcelleProprietaire)
        cadastre_search_form.setTabOrder(self.btExportParcelleProprietaire, self.btCentrerProprietaire)
        cadastre_search_form.setTabOrder(self.btCentrerProprietaire, self.btZoomerProprietaire)
        cadastre_search_form.setTabOrder(self.btZoomerProprietaire, self.btSelectionnerProprietaire)
        cadastre_search_form.setTabOrder(self.btSelectionnerProprietaire, self.txtLog)

    def retranslateUi(self, cadastre_search_form):
        cadastre_search_form.setWindowTitle(_translate("cadastre_search_form", "Cadastre - Outils de recherche", None))
        self.grpLieu.setTitle(_translate("cadastre_search_form", "Recherche de lieux", None))
        self.label_12.setText(_translate("cadastre_search_form", "Commune", None))
        self.label_2.setText(_translate("cadastre_search_form", "Parcelle", None))
        self.label.setText(_translate("cadastre_search_form", "Section", None))
        self.btResetCommune.setToolTip(_translate("cadastre_search_form", "Retour à l\'ensemble des communes", None))
        self.btResetCommune.setText(_translate("cadastre_search_form", "...", None))
        self.btResetSection.setToolTip(_translate("cadastre_search_form", "Retour à l\'ensemble des sections", None))
        self.btResetSection.setText(_translate("cadastre_search_form", "...", None))
        self.btResetParcelle.setToolTip(_translate("cadastre_search_form", "Retour à l\'ensemble des parcelles", None))
        self.btResetParcelle.setText(_translate("cadastre_search_form", "...", None))
        self.btCentrerLieu.setToolTip(_translate("cadastre_search_form", "Centrer sur l\'objet", None))
        self.btZoomerLieu.setToolTip(_translate("cadastre_search_form", "Zoomer sur l\'objet", None))
        self.btSelectionnerLieu.setToolTip(_translate("cadastre_search_form", "Sélectionner l\'objet", None))
        self.btExportParcelle.setToolTip(_translate("cadastre_search_form", "Exporter le relevé parcellaire", None))
        self.grpAdresse.setTitle(_translate("cadastre_search_form", "Recherche d\'adresse", None))
        self.label_5.setText(_translate("cadastre_search_form", "Adresse", None))
        self.label_6.setText(_translate("cadastre_search_form", "Parcelle", None))
        self.btResetParcelleAdresse.setToolTip(_translate("cadastre_search_form", "Retour à l\'ensemble des parcelles", None))
        self.btResetParcelleAdresse.setText(_translate("cadastre_search_form", "...", None))
        self.btSearchAdresse.setToolTip(_translate("cadastre_search_form", "Lancer la recherche", None))
        self.btSearchAdresse.setText(_translate("cadastre_search_form", "...", None))
        self.btCentrerAdresse.setToolTip(_translate("cadastre_search_form", "Centrer sur la/les parcelle(s)", None))
        self.btZoomerAdresse.setToolTip(_translate("cadastre_search_form", "Zoomer sur la/les parcelle(s)", None))
        self.btSelectionnerAdresse.setToolTip(_translate("cadastre_search_form", "Sélectionner la/les parcelle(s)", None))
        self.btExportParcelleAdresse.setToolTip(_translate("cadastre_search_form", "Exporter le relevé parcellaire", None))
        self.grpProprietaire.setTitle(_translate("cadastre_search_form", "Recherche de propriétaire", None))
        self.label_3.setText(_translate("cadastre_search_form", "Parcelle", None))
        self.label_4.setText(_translate("cadastre_search_form", "Nom", None))
        self.btSearchProprietaire.setToolTip(_translate("cadastre_search_form", "Lancer la recherche", None))
        self.btSearchProprietaire.setText(_translate("cadastre_search_form", "...", None))
        self.btResetParcelleProprietaire.setToolTip(_translate("cadastre_search_form", "Retour à l\'ensemble des parcelles", None))
        self.btResetParcelleProprietaire.setText(_translate("cadastre_search_form", "...", None))
        self.btExportParcelleProprietaire.setToolTip(_translate("cadastre_search_form", "Exporter le relevé parcellaire", None))
        self.btExportParcelleProprietaire.setText(_translate("cadastre_search_form", "...", None))
        self.btExportProprietaire.setToolTip(_translate("cadastre_search_form", "Exporter le relevé de propriété", None))
        self.btExportProprietaire.setText(_translate("cadastre_search_form", "...", None))
        self.btCentrerProprietaire.setToolTip(_translate("cadastre_search_form", "Centrer sur la/les parcelle(s)", None))
        self.btZoomerProprietaire.setToolTip(_translate("cadastre_search_form", "Zoomer sur la/les parcelle(s)", None))
        self.btSelectionnerProprietaire.setToolTip(_translate("cadastre_search_form", "Sélectionner la/les parcelle(s)", None))
        self.txtLog.setHtml(_translate("cadastre_search_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

import resource_rc
