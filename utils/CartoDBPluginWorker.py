"""
/***************************************************************************
CartoDB Plugin
A QGIS plugin

----------------------------------------------------------------------------
begin                : 2014-09-08
copyright            : (C) 2014 by Michael Salgado, Kudos Ltda.
email                : michaelsalgado@gkudos.com, info@gkudos.com
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
from PyQt4.QtCore import QThread, QMetaObject


class CartoDBPluginWorker(QThread):
    def __init__(self, object, method):
        QThread.__init__(self)
        self.object = object
        self.method = method

    def __del__(self):
        self.wait()

    def run(self):
        QMetaObject.invokeMethod(self.object, self.method)
        return
