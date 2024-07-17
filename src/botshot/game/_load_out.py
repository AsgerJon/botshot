"""LoadOut encapsulates the state of the shotgun. The class treats the
shotgun and the actions as Markov states. An instance receives an action,
determines if the action is valid for the current state, and then updates
accordingly. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.desc import AttriBox
from worktoy.ezdata import EZData


class FLAG:
  """Replacement for bool in AttriBox"""

  __inner_state__ = None

  def __init__(self, state: bool = False):
    self.__inner_state__ = True if state else False

  def __bool__(self) -> bool:
    return True if self.__inner_state__ else False


class LoadOut(EZData):
  """LoadOut encapsulates the state of the shotgun. The class treats the
  shotgun and the actions as Markov states. An instance receives an action,
  determines if the action is valid for the current state, and then updates
  accordingly. """

  __invert_next__ = None

  live = AttriBox[int](0)
  blank = AttriBox[int](0)

  def shootLive(self) -> None:
    """Shoot the live shell. """
    if TYPE_CHECKING:
      assert isinstance(self.live, int)
    if not self.live ** 2:
      e = """Tried to shoot blank, but no blanks are left!"""
      raise RuntimeError(e)
    if self.__invert_next__:
      self.__invert_next__ = False
      return self.shootBlank()
    self.live -= 1

  def shootBlank(self) -> None:
    """Shoot the blank shell. """
    if TYPE_CHECKING:
      assert isinstance(self.blank, int)
    if not self.blank ** 2:
      e = """Tried to shoot blank, but no blanks are left!"""
      raise RuntimeError(e)
    if self.__invert_next__:
      self.__invert_next__ = False
      return self.shootLive()
    self.blank -= 1
