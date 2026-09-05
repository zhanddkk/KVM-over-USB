from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QImage
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QVideoSink, QVideoFrame, QVideoFrameFormat


class SmoothVideoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sink = QVideoSink()
        self.sink.videoFrameChanged.connect(self.on_frame)
        self._image = QImage()
        self._ratio_mode = Qt.KeepAspectRatio
        pass

    def videoSink(self) -> QVideoSink:
        return self.sink

    def setAspectRatioMode(self, ratio_mode):
        self._ratio_mode = ratio_mode
        pass

    def on_frame(self, frame: QVideoFrame):
        self._image = frame.toImage()
        self.update()  # 触发重绘
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        painter.begin(self)
        if not self._image.isNull():
            target_size = self.size()
            scaled = self._image.scaled(target_size, self._ratio_mode, Qt.SmoothTransformation)
            x = (self.width() - scaled.width()) // 2
            y = (self.height() - scaled.height()) // 2
            painter.drawImage(x, y, scaled)
            pass
        painter.end()
        pass
    pass
