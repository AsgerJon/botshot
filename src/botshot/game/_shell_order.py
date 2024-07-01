"""The ShellOrder class encapsulates the shell order."""
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

import sys

from attribox import AttriBox
from vistutils.fields import EmptyField
from vistutils.text import stringList, monoSpace
from vistutils.waitaminute import typeMsg

from botshot.game import ShellState

if sys.version_info.minor < 11:
  from typing_extensions import Self
else:
  from typing import Self


class ShellOrder:
  """The ShellOrder class encapsulates the shell order."""

  __inner_shells__ = None
  __iter_contents__ = None

  initLiveCount = AttriBox[int](-1)
  initBlankCount = AttriBox[int](-1)
  currentLiveCount = AttriBox[int](-1)
  currentBlankCount = AttriBox[int](-1)
  hiddenLiveCount = EmptyField()
  hiddenBlankCount = EmptyField()
  initFullCount = EmptyField()
  currentFullCount = EmptyField()

  invertNextFlag = AttriBox[bool](False)

  @initFullCount.GET
  def initFullCount(self) -> int:
    """Get the initial full count."""
    return self.initLiveCount + self.initBlankCount

  @currentFullCount.GET
  def currentFullCount(self) -> int:
    """Get the current full count."""
    return self.currentLiveCount + self.currentBlankCount

  def __init__(self, liveCount: int, blankCount: int) -> None:
    self.initLiveCount = liveCount
    self.currentLiveCount = liveCount
    self.initBlankCount = blankCount
    self.currentBlankCount = blankCount

  def _getInnerShells(self, **kwargs) -> list:
    """Get the inner shells"""
    if self.__inner_shells__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self.__inner_shells__ = [ShellState.hidden]
      return self._getInnerShells(_recursion=True)
    if isinstance(self.__inner_shells__, list):
      return self.__inner_shells__
    e = typeMsg('self.__inner_shells__', self.__inner_shells__, list)
    raise TypeError(e)

  def _updateShells(self) -> None:
    """Updates the shells"""
