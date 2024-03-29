# -*- coding: utf-8 -*-

"""
/***************************************************************************
 MatchUsingTime
                                 A QGIS plugin
 Match the time and point sequence with location information with the file with time information to generate the point at the position of the file.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-14
        copyright            : (C) 2021 by Yoichi Kayama/Aero Asahi Corp
        email                : yoichi.kayama@gmail.com
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

__author__ = 'Yoichi Kayama/Aero Asahi Corp'
__date__ = '2021-07-14'
__copyright__ = '(C) 2021 by Yoichi Kayama/Aero Asahi Corp'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider
from .MatchUsingTime_algorithm import MatchUsingTimeAlgorithm
from .MatchUsingTime_MP4algorithm  import MatchMp4UsingTimeAlgorithm
from .createlogfromgpx_algorithm  import CreateLogFromGpxAlgorithm
import os
import inspect
from qgis.PyQt.QtGui import QIcon

class MatchUsingTimeProvider(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(MatchUsingTimeAlgorithm())
        self.addAlgorithm(MatchMp4UsingTimeAlgorithm())
        self.addAlgorithm(CreateLogFromGpxAlgorithm())       
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'Aero Asahi Corp'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('Aero Asahi Corp')

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]
        icon = QIcon(os.path.join(os.path.join(cmd_folder, 'providerIcon.svg')))
        return icon
        
        #return QgsProcessingProvider.icon(self)

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()
