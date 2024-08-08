"""MainWindow provides the main window for the botshot application."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from botshot.widgets import LayoutWindow


class MainWindow(LayoutWindow):
  """MainWindow provides the main window for the botshot application."""

  def show(self) -> None:
    """Reimplementing show method"""
    self.initUi()
    self.initSignalSlot()
    LayoutWindow.show(self)
