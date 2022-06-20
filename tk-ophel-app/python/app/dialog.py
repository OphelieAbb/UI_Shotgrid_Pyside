# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("Starter Template App...", app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()

        # logging happens via a standard toolkit logger
        logger.info("Launching Starter Application...")

        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk

        # lastly, set up our very basic UI
        # self.ui.context.setText("Current Context: %s" % self._app.context)
        print(self._app.get_setting('var_1'))
        print(self._app.engine)

        layout = QtGui.QVBoxLayout()

        layout_top = QtGui.QHBoxLayout()

        self.button_box = QtGui.QPushButton("Bouton 1", self)
        layout_top.addWidget(self.button_box)

        self.button_box = QtGui.QPushButton("Bouton 2", self)
        layout_top.addWidget(self.button_box)

        self.button_box = QtGui.QPushButton("Bouton 3", self)
        layout_top.addWidget(self.button_box)

        layout.addLayout(layout_top)

        #layout_vertical = QtGui.QHBoxLayout()
        gridLayout = QtGui.QGridLayout()

        self.label = QtGui.QLabel("Line 1:")
        gridLayout.addWidget(self.label, 0, 0)
        self.line = QtGui.QLineEdit()
        gridLayout.addWidget(self.line, 0, 1)

        self.label = QtGui.QLabel("Line 2:")
        gridLayout.addWidget(self.label, 1, 0)
        self.line = QtGui.QLineEdit()
        gridLayout.addWidget(self.line, 1, 1)

        self.label = QtGui.QLabel("Line 2:")
        gridLayout.addWidget(self.label, 2, 0)
        self.line = QtGui.QLineEdit()
        gridLayout.addWidget(self.line, 2, 1)

        self.zone_text = QtGui.QTextEdit()
        gridLayout.addWidget(self.zone_text, 0, 2, 4, 1)

        layout.addLayout(gridLayout)

        fromLayout = QtGui.QFormLayout()
        fromLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.nameLineEdit = QtGui.QLineEdit()
        fromLayout.addRow("Line 1", self.nameLineEdit)
        self.comboBox = QtGui.QComboBox()
        fromLayout.addRow("Line 2", self.comboBox)
        self.spinebBox = QtGui.QSpinBox()
        fromLayout.addRow("Line 3", self.spinebBox)

        layout.addLayout(fromLayout)

        data = [
            ["File Cache", "filecach1", "render1", 20],
            ["Arnold", "dgdgg", "render2", 30],
            ["File", "filesdlfjlsdcach1", "render3", 20],
        ]

        self.treeWidget = QtGui.QTreeWidget(self)
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setGeometry(QtCore.QRect(390, 170, 331, 391))

        # self.item = QtGui.QTreeWidgetItem(self.treewidget)
        # self.label_1 = QtGui.QLabel('icon 1')
        # self.treeWidget.setItemWidget(self.item, 1,self.label_1)

        # Create header
        # self.treeWidget.headerItem().setText(0, "TYPE")
        header_list = ["TYPE", "NODE", "JOB NAME", "PRIORITY"]
        for index, header_name in enumerate(header_list):
            self.treeWidget.headerItem().setText(index, header_name)

        # Create item
        # item1 = QtGui.QTreeWidgetItem(self.treeWidget)
        # self.treeWidget.addTopLevelItem(item1)
        # #self.item.setObjectName("TYPE")
        # item1.setText(0, "File Cache")
        # item1.setText(1, "Arnold")
        # item1.setText(2, "Mantra")
        # self.item1.header().setVisible(True)

        # Create Item from data
        for element in data:
            item = QtGui.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.addTopLevelItem(item)
            #self.item.setObjectName("TYPE")
            item.setText(0, element[0])
            item.setText(1, element[1])
            item.setText(2, element[2])

            # add spinbox in the 4th
            in_spinbox = QtGui.QSpinBox()
            in_spinbox.setValue(element[3])
            self.treeWidget.setItemWidget(item, 3, in_spinbox)



        layout.addWidget(self.treeWidget)



        # layout_vertical.addStretch()
        # layout_edit = QtGui.QVBoxLayout()

        # self.line_edit = QtGui.QLineEdit("Ophelie")

        # self.setLayout(layout_edit)
        self.setLayout(layout)
