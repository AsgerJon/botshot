"""ShellView provides a view of a shell indicating its state."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QSizeF, QRectF, QPointF, Qt, QLine, QLineF
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from ezside.basewidgets import BoxWidget
from ezside.tools import emptyPen, emptyBrush
from worktoy.desc import Field
from worktoy.text import typeMsg

from botshot.game import Shell


class ShellView(BoxWidget):
  """ShellView provides a view of a shell indicating its state."""

  __shell_state__ = None

  baseColor = Field()
  baseBrush = Field()
  barrelColor = Field()
  barrelBrush = Field()
  shellState = Field()
  pen = Field()

  @pen.GET
  def _getPen(self) -> QPen:
    """Getter-function for pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setColor(QColor(0, 0, 0, 255))
    pen.setWidth(2)
    return pen

  @baseColor.GET
  def _getBaseColor(self) -> QColor:
    """Return the base color of the widget. """
    return QColor(127, 127, 0, 255)

  @baseBrush.GET
  def _getBaseBrush(self) -> QBrush:
    """Getter-function for base brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    brush.setColor(self.baseColor)
    return brush

  @shellState.GET
  def _getShellState(self) -> Shell:
    if self.__shell_state__ is None:
      e = """Shell state not initialized!"""
      raise RuntimeError
    if isinstance(self.__shell_state__, Shell):
      return self.__shell_state__
    e = typeMsg('shellState', self.__shell_state__, Shell)
    raise TypeError(e)

  @shellState.SET
  def _setShellState(self, shellState: Shell) -> None:
    if not isinstance(shellState, Shell):
      e = typeMsg('shellState', shellState, Shell)
      raise TypeError(e)
    self.__shell_state__ = shellState

  @barrelColor.GET
  def _getBarrelColor(self) -> QColor:
    """Return the barrel color of the widget. """
    colorData = {
        Shell.EMPTY    : QColor(0, 0, 0, 0, ),
        Shell.HIDDEN   : QColor(207, 207, 207, 255),
        Shell.WAS_BLANK: QColor(0, 169, 255, 255),
        Shell.WAS_LIVE : QColor(255, 0, 0, 255),
        Shell.BLANK    : QColor(47, 207, 255, 255),
        Shell.LIVE     : QColor(255, 47, 47, 255),
    }
    return colorData[self.shellState]

  @barrelBrush.GET
  def _getBarrelBrush(self) -> QBrush:
    """Getter-function for barrel brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    brush.setColor(self.barrelColor)
    return brush

  def requiredRect(self) -> QRectF:
    """Return the required rectangle of the widget. """
    return QRectF(QPointF(0, 0), QSizeF(128, 48)) + self.allMargins

  def requireSize(self) -> QSizeF:
    """Return the required size of the widget. """
    return self.requiredRect().size()

  def paintMeLike(self, rect: QRectF, painter: QPainter) -> None:
    """Paint the widget. """
    edgeRect = QRectF(QPointF(0, 0), QSizeF(8, rect.height()))
    baseRect = QRectF(QPointF(8, 8), QSizeF(24, rect.height() - 16))
    barrelRect = QRectF(QPointF(32, 8), QSizeF(96, rect.height() - 16))
    ringLineA = QLineF(QPointF(28, 0), QPointF(28, rect.height()))
    ringLineB = QLineF(QPointF(24, 0), QPointF(24, rect.height()))
    painter.setPen(emptyPen())
    painter.setBrush(self.baseBrush)
    painter.drawRect(edgeRect)
    painter.drawRect(baseRect)
    painter.setBrush(self.barrelBrush)
    painter.drawRect(barrelRect)
    painter.setBrush(emptyBrush())
    painter.setPen(self.pen)
    painter.drawLine(ringLineA)
    painter.drawLine(ringLineB)

  def __init__(self, *args) -> None:
    BoxWidget.__init__(self)
    self.paddings = 4
    self.borders = 2
    self.margins = 2
