# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Cadastre - loading main methods
                                 A QGIS plugin
 This plugins helps users to import the french land registry ('cadastre')
 into a database. It is meant to ease the use of the data in QGIs
 by providing search tools and appropriate layer symbology.
                              -------------------
        begin                : 2013-06-11
        copyright            : (C) 2013 by 3liz
        email                : info@3liz.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import sys, os, glob
import re
import time
import tempfile
import shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from datetime import datetime

# db_manager scripts
from db_manager.db_plugins.plugin import DBPlugin, Schema, Table, BaseError
from db_manager.db_plugins import createDbPlugin
from db_manager.dlg_db_error import DlgDbError


class cadastreLoading(QObject):

    cadastreLoadingFinished = pyqtSignal()

    def __init__(self, dialog):
        QObject.__init__(self)
        self.dialog = dialog

        self.startTime = datetime.now()

        # common cadastre methods
        self.qc = self.dialog.qc
        self.defaultThemeDir = 'classique'
        self.themeDir = None

        # List of database layers to load inQGIS
        self.qgisCadastreLayerList = [
            {'label': u'Commune', 'name': 'geo_commune', 'table': 'geo_commune', 'geom': 'geom', 'sql': ''},
            {'label': u'Voies, routes et chemins', 'name': 'geo_zoncommuni', 'table': 'geo_zoncommuni', 'geom': 'geom', 'sql': ''},
            {'label': u'Noms de voies', 'name': 'geo_label_zoncommuni', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" IN ( \'ZONCOMMUNI_id\', \'TRONROUTE_ID\') '},
            {'label': u'Secteurs', 'name': 'geo_subdsect', 'table': 'geo_subdsect', 'geom': 'geom', 'sql': ''},
            {'label': u'Subdivisions fiscales', 'name': 'geo_subdfisc', 'table': 'geo_subdfisc', 'geom': 'geom', 'sql': ''},
            {'label': u'Subdivisions fiscales (étiquette)', 'name': 'geo_label_subdfisc', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'SUBDFISC_id\''},
            {'label': u'Bâti', 'name': 'geo_batiment', 'table': 'geo_batiment', 'geom': 'geom', 'sql': ''},
            {'label': u'Parcelles', 'name': 'geo_parcelle', 'table': 'geo_parcelle', 'geom': 'geom', 'sql': '', 'key': 'ogc_fid'},
            {'label': u'Parcelles (étiquettes)', 'name': 'geo_label_parcelle', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'PARCELLE_id\''},
            {'label': u'Lieux-dits', 'name': 'geo_lieudit', 'table': 'geo_lieudit', 'geom': 'geom', 'sql': ''},
            {'label': u'Lieux-dits  (étiquettes)', 'name': 'geo_label_lieudit', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'LIEUDIT_id\''},
            {'label': u'Sections', 'name': 'geo_section', 'table': 'geo_section', 'geom': 'geom', 'sql': ''},
            {'label': u'Sections (étiquettes)', 'name': 'geo_label_section', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'SECTION_id\''},
            {'label': u'Bornes', 'name': 'geo_borne', 'table': 'geo_borne', 'geom': 'geom', 'sql': ''},
            {'label': u'Croix', 'name': 'geo_croix', 'table': 'geo_croix', 'geom': 'geom', 'sql': ''},
            {'label': u'Repères géodésiques', 'name': 'geo_ptcanv', 'table': 'geo_ptcanv', 'geom': 'geom', 'sql': ''},
            {'label': u'Murs, fossés, clotûres', 'name': 'geo_symblim', 'table': 'geo_symblim', 'geom': 'geom', 'sql': ''},
            {'label': u'Cours d\'eau', 'name': 'geo_tronfluv', 'table': 'geo_tronfluv', 'geom': 'geom', 'sql': ''},
            {'label': u'Cours d\'eau (étiquettes)', 'name': 'geo_label_tronfluv', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'TRONFLUV_id\''},
            {'label': u'Surfaces', 'name': 'geo_tsurf', 'table': 'geo_tsurf', 'geom': 'geom', 'sql': ''},
            {'label': u'Surfaces (étiquettes)', 'name': 'geo_label_tsurf', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'TSURF_id\''},
            {'label': u'Objets ponctuels', 'name': 'geo_tpoint', 'table': 'geo_tpoint', 'geom': 'geom', 'sql': ''},
            {'label': u'Objets ponctuels (étiquettes)', 'name': 'geo_label_tpoint', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'TPOINT_id\''},
            {'label': u'Objets linéaires', 'name': 'geo_tline', 'table': 'geo_tline', 'geom': 'geom', 'sql': ''},
            {'label': u'Objets linéaires (étiquettes)', 'name': 'geo_label_tline', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'TLINE_id\''},
            {'label': u'Numéros de voie', 'name': 'geo_label_num_voie', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'NUMVOIE_id\''},
            {'label': u'Établissements publics', 'name': 'geo_label_voiep', 'table': 'geo_label', 'geom': 'geom', 'sql': '"ogr_obj_lnk_layer" = \'VOIEP_id\''},
            {'label': u'Unités foncières', 'name': 'geo_unite_fonciere', 'table': 'geo_unite_fonciere', 'geom':'geom', 'sql': '', 'dbType': 'postgis'}
        ]

    def updateTimer(self):
        b = datetime.now()
        diff = b - self.startTime
        self.qc.updateLog(u'%s s' % diff.seconds)

    def getGroupIndex(self, groupName):
        '''
        Get a legend group index by its name
        '''
        relationList = self.dialog.iface.legendInterface().groupLayerRelationship()
        i = 0
        for item in relationList:
            if item[0]:
                if item[0] == groupName:
                    return i
                i = i + 1
        return 0

    def processLoading(self):
        '''
        Load all the layers in QGIS
        and apply corresponding style
        '''
        self.startTime = datetime.now()
        QApplication.setOverrideCursor(Qt.WaitCursor)

        # default style to apply for Cadastre layers
        self.themeDir = unicode(self.dialog.liTheme.currentText())
        if not os.path.exists(os.path.join(
            self.qc.plugin_dir,
            "styles/%s" % self.themeDir
        )):
            self.themeDir = self.defaultThemeDir

        # set Cadastre SVG path if not set
        cadastreSvgPath = os.path.join(
            self.qc.plugin_dir,
            "styles/%s/svg" % self.themeDir
        )
        s = QSettings()
        qgisSvgPaths = s.value("svg/searchPathsForSVG", 10, type=str)
        if not cadastreSvgPath in qgisSvgPaths:
            if qgisSvgPaths:
                qgisSvgPaths = u"%s|%s" % (qgisSvgPaths, cadastreSvgPath)
            else:
                qgisSvgPaths = u"%s" % cadastreSvgPath
            s.setValue("svg/searchPathsForSVG", qgisSvgPaths)
            self.qc.updateLog(u"* Le chemin contenant les SVG du plugin Cadastre a été ajouté dans les options de QGIS")

        # Get selected options
        providerName = self.dialog.dbpluginclass.providerName()
        qgisCadastreLayers = []
        self.dialog.schema = unicode(self.dialog.liDbSchema.currentText())
        self.dialog.totalSteps = len(self.qgisCadastreLayerList)

        # Run the loading
        self.updateTimer()
        self.qc.updateLog(u'Chargement des tables :')

        # Get database list of tables
        layerUri = self.dialog.db.uri()
        if self.dialog.dbType == 'postgis':
            schemaSearch = [s for s in self.dialog.db.schemas() if s.name == self.dialog.schema]
            schemaInst = schemaSearch[0]
            dbTables = self.dialog.db.tables(schemaInst)
        if self.dialog.dbType == 'spatialite':
            dbTables = self.dialog.db.tables()

        # Loop throuhg qgisQastreLayerList and load each corresponding table
        for item in self.qgisCadastreLayerList:

            if item.has_key('dbType') and item['dbType'] != self.dialog.dbType:
                continue

            # Tables - Get db_manager table instance
            tableList = [a for a in dbTables if a.name == item['table']]
            if len(tableList) == 0 and not item.has_key('isView'):
                self.qc.updateLog(u'  - Aucune table trouvée pour %s' % item['label'])
                continue

            if tableList:
                table = tableList[0]
                source = table.name
                uniqueField = table.getValidQGisUniqueFields(True)
                if uniqueField:
                    uniqueCol = uniqueField.name
                else:
                    uniqueCol = 'ogc_fid'

            schema = self.dialog.schema

            # View
            if item.has_key('isView'):
                if self.dialog.dbType == 'spatialite':
                    schemaReplace = ''
                else:
                    schemaReplace = '"%s".' % self.dialog.schema
                source = item['table'].replace('schema.', schemaReplace)
                uniqueCol = item['key']
                schema = None

            sql = item['sql']
            geomCol = item['geom']

            # Create vector layer
            layerUri.setDataSource(
                schema,
                source,
                geomCol,
                sql,
                uniqueCol
            )
            vlayer = QgsVectorLayer(layerUri.uri(), item['label'], providerName)

            # apply style
            qmlPath = os.path.join(
                self.qc.plugin_dir,
                "styles/%s/%s.qml" % (self.themeDir, item['name'])
            )
            if os.path.exists(qmlPath):
                vlayer.loadNamedStyle(qmlPath)

            # append vector layer to the list
            qgisCadastreLayers.append(vlayer)

            # update progress bar
            self.qc.updateLog(u'* %s' % item['label'])
            self.dialog.step+=1
            self.qc.updateProgressBar()

        self.updateTimer()

        # Add all layers to QGIS registry
        self.qc.updateLog(u'Ajout des couches dans le registre de QGIS')
        QgsMapLayerRegistry.instance().addMapLayers(qgisCadastreLayers)
        self.updateTimer()

        # Create a group "Cadastre" and move all layers into it
        self.qc.updateLog(u'Ajout des couches dans le groupe Cadastre')
        li = self.dialog.iface.legendInterface()
        groups = []
        for group in li.groupLayerRelationship():
            if group[0]:
                groups.append(group[0])
        if u"Cadastre" in groups:
            g1 = self.getGroupIndex(u"Cadastre")
        else:
            g1 = li.addGroup("Cadastre")
        for layer in qgisCadastreLayers:
            li.moveLayer(layer, g1)
            li.setLayerExpanded(layer, False)
            #~ layer.updateExtents()
            if layer.name() == u'Unités foncières':
                li.setLayerVisible(layer, False)
        li.setGroupExpanded(g1, False) # broken ?
        self.updateTimer()




        # Zoom to full extent
        self.qc.updateLog(u'Zoom sur les couches')
        from qgis.utils import iface
        canvas = iface.mapCanvas()
        canvas.zoomToFullExtent()
        self.updateTimer()

        # progress bar
        self.dialog.step+=1
        self.qc.updateProgressBar()

        # Emit signal
        self.qc.updateLog(u'Mise à jour des outils cadastre')
        self.cadastreLoadingFinished.emit()
        self.updateTimer()

        # Final message
        QApplication.restoreOverrideCursor()
        QMessageBox.information(
            self.dialog,
            u"Cadastre",
            u"Les données ont bien été chargées dans QGIS"
        )
        self.dialog.pbProcess.setValue(0)


        QApplication.restoreOverrideCursor()
