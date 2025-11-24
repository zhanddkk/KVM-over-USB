import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPainter, QPainterPath, QImage, QColor, QLinearGradient, QFont, QFontMetrics, QIcon
from main import AppMainWindow


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__(flags=Qt.WindowType.Window)
        pass

    @staticmethod
    def create_icon():
        _img = QImage(256, 256, QImage.Format.Format_ARGB32)
        _img.fill(QColor(0, 0, 0, 0))
        _lg = QLinearGradient()
        _lg.setColorAt(0, QColor(200, 200, 210))
        _lg.setColorAt(1, QColor(255, 16, 0))
        _lg.setStart(0, 0)
        _lg.setFinalStop(255, 255)
        _path = QPainterPath()
        _painter = QPainter(_img)
        _painter.setRenderHints(QPainter.RenderHint.Antialiasing, True)
        _path.addRoundedRect(0, 0, 256, 256, 64, 64)
        _painter.fillPath(_path, _lg)
        _path.clear()
        _font = QFont()
        _font.setFamily('Consolas')
        _font.setPixelSize(64)
        _str = 'KVM'
        _width = QFontMetrics(_font).horizontalAdvance(_str)
        _height = QFontMetrics(_font).height()

        _icon = AppMainWindow.change_icon_color('icons/main.ico', QColor(255, 255, 255))
        _painter.drawImage(3, 3, _icon.pixmap(250).toImage())

        _path.addText((256 - _width) // 2, (256 - _height) // 2 + _height // 2, _font, _str)
        _painter.setRenderHints(QPainter.RenderHint.Antialiasing, True)
        _lg.setColorAt(0, QColor(196, 196, 196))
        _lg.setColorAt(1, QColor(255, 255, 255))
        _lg.setStart((256 - _width) // 2, 128)
        _lg.setFinalStop((256 - _width) // 2 + _width, 128)
        _painter.fillPath(_path, _lg)
        _painter.end()
        return _img
    pass


def main():
    _app = QApplication(sys.argv)
    _win = MainWin()
    _img = _win.create_icon()
    _img.save('./icons/app.ico')
    _img.save('./icons/app.png')
    _win.show()
    _app.exec()
    pass


if __name__ == '__main__':
    main()
    pass
