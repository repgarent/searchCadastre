rem Paramétrage de l'environnement d'exécution
@echo off
Call "C:\Program Files\QGIS Brighton\bin\o4w_env.bat"
@echo on

rem Compilation des interfaces QtDesigner
Call "C:\Program Files\QGIS Brighton\bin\pyuic4.bat" -o forms/new_cadastre_search_form.py forms/new_cadastre_search_form.ui  

rem Compilation des ressources
Call "C:\Program Files\QGIS Brighton\bin\pyrcc4.exe" -o resources_rc.py resources.qrc

rem Déploiement du plugin
xcopy /S /Y D:\informatique\projetGithub\searchCadastre\*.* C:\Users\alexis\.qgis2\python\plugins\searchCadastre

