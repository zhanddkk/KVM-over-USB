# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(400, 320)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_client_version_key = QLabel(AboutDialog)
        self.label_client_version_key.setObjectName(u"label_client_version_key")

        self.gridLayout.addWidget(self.label_client_version_key, 3, 0, 1, 1)

        self.label_project_name_key = QLabel(AboutDialog)
        self.label_project_name_key.setObjectName(u"label_project_name_key")

        self.gridLayout.addWidget(self.label_project_name_key, 0, 0, 1, 1)

        self.label_project_description_value = QLabel(AboutDialog)
        self.label_project_description_value.setObjectName(u"label_project_description_value")

        self.gridLayout.addWidget(self.label_project_description_value, 1, 0, 1, 1)

        self.label_project_fork_from_key = QLabel(AboutDialog)
        self.label_project_fork_from_key.setObjectName(u"label_project_fork_from_key")

        self.gridLayout.addWidget(self.label_project_fork_from_key, 2, 0, 1, 1)

        self.label_python_version_key = QLabel(AboutDialog)
        self.label_python_version_key.setObjectName(u"label_python_version_key")

        self.gridLayout.addWidget(self.label_python_version_key, 4, 0, 1, 1)

        self.label_python_version_value = QLabel(AboutDialog)
        self.label_python_version_value.setObjectName(u"label_python_version_value")
        self.label_python_version_value.setText(u"3.12.0")

        self.gridLayout.addWidget(self.label_python_version_value, 4, 1, 1, 1)

        self.label_client_version_value = QLabel(AboutDialog)
        self.label_client_version_value.setObjectName(u"label_client_version_value")
        self.label_client_version_value.setText(u"v2024.10.10")

        self.gridLayout.addWidget(self.label_client_version_value, 3, 1, 1, 1)

        self.label_project_fork_from_value = QLabel(AboutDialog)
        self.label_project_fork_from_value.setObjectName(u"label_project_fork_from_value")
        self.label_project_fork_from_value.setText(u"<a href=\"https://github.com/ElluIFX/KVM-Card-Mini-PySide6\">ElluIFX: KVM-Card-Mini-PySide6</a>")
        self.label_project_fork_from_value.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_project_fork_from_value, 2, 1, 1, 1)

        self.label_project_description_key = QLabel(AboutDialog)
        self.label_project_description_key.setObjectName(u"label_project_description_key")

        self.gridLayout.addWidget(self.label_project_description_key, 1, 1, 1, 1)

        self.label_project_name_value = QLabel(AboutDialog)
        self.label_project_name_value.setObjectName(u"label_project_name_value")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_project_name_value.sizePolicy().hasHeightForWidth())
        self.label_project_name_value.setSizePolicy(sizePolicy)
        self.label_project_name_value.setText(u"<a href=\"https://github.com/wevsty/KVM-over-USB\">KVM-over-USB</a>")
        self.label_project_name_value.setWordWrap(False)
        self.label_project_name_value.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_project_name_value, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_dependencies = QLabel(AboutDialog)
        self.label_dependencies.setObjectName(u"label_dependencies")

        self.verticalLayout.addWidget(self.label_dependencies)

        self.text_edit_info = QTextEdit(AboutDialog)
        self.text_edit_info.setObjectName(u"text_edit_info")
        self.text_edit_info.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_edit_info)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.label_client_version_key.setText(QCoreApplication.translate("AboutDialog", u"Client version:", None))
        self.label_project_name_key.setText(QCoreApplication.translate("AboutDialog", u"Project name:", None))
        self.label_project_description_value.setText(QCoreApplication.translate("AboutDialog", u"Project description:", None))
        self.label_project_fork_from_key.setText(QCoreApplication.translate("AboutDialog", u"Project fork from:", None))
        self.label_python_version_key.setText(QCoreApplication.translate("AboutDialog", u"Python version:", None))
        self.label_project_description_key.setText(QCoreApplication.translate("AboutDialog", u"A simple USB KVM solution", None))
        self.label_dependencies.setText(QCoreApplication.translate("AboutDialog", u"Dependencies:", None))
    # retranslateUi

