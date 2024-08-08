"""LayoutWindow organizes widgets for the application window."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ezside.app import BaseWindow
from ezside.layouts import AbstractLayout
from worktoy.desc import AttriBox, THIS

from botshot.game import Shell
from botshot.widgets import ShellView


class LayoutWindow(BaseWindow):
  """LayoutWindow organizes widgets for the application window."""

  shellCount = AttriBox[int]()
  baseLayout = AttriBox[AbstractLayout](THIS)

  shellView0 = AttriBox[ShellView](THIS)
  shellView1 = AttriBox[ShellView](THIS)
  shellView2 = AttriBox[ShellView](THIS)
  shellView3 = AttriBox[ShellView](THIS)
  shellView4 = AttriBox[ShellView](THIS)
  shellView5 = AttriBox[ShellView](THIS)
  shellView6 = AttriBox[ShellView](THIS)
  shellView7 = AttriBox[ShellView](THIS)

  def getShells(self) -> list[ShellView]:
    """Return a list of all shell views."""
    return [getattr(self, 'shellView%d' % i) for i in range(8)]

  def resetShells(self) -> None:
    """Reset all shell views."""
    cls = type(self)
    for i in range(8):
      box = getattr(cls, 'shellView%d' % i)
      try:
        AttriBox.__instance_reset__(box, self)
      except AttributeError:
        pass
    box = getattr(cls, 'baseLayout')
    try:
      AttriBox.__instance_reset__(box, self)
    except AttributeError:
      pass

  def initUi(self) -> None:
    """Initialize the user interface."""
    for (i, view) in enumerate(self.getShells()):
      view.shellState = Shell.HIDDEN if i < self.shellCount else Shell.EMPTY
      self.baseLayout.addWidget(view, i, 0)
