"""LoadOut is a class that represents a load out for a player in the game."""
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from attribox import AttriBox
from vistutils.fields import EmptyField


class LoadOut:
  """LoadOut is a class that represents a load out for a player in the
  game."""

  __shell_order__ = None

  lives = AttriBox[int](0)
  blanks = AttriBox[int](0)
  shellOrder = EmptyField()

  def _createShellOrder(self) -> None:
    """Creator function for the shells in the loud out. """
    self.__shell_order__ = [None, ] * (self.lives + self.blanks)

  @shellOrder.GET
  def _getShellOrder(self, **kwargs) -> list[Optional[bool]]:
    """Get the shells in the load out. """
    if self.__shell_order__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createShellOrder()
      return self._getShellOrder(_recursion=True)
    if isinstance(self.__shell_order__, list):
      return self.__shell_order__

  def __init__(self, lives: int, blanks: int) -> None:
    self.lives = lives
    self.blanks = blanks

  def reveal(self, index: int, state: bool) -> None:
    """Reveal the state of a shell. """
    if TYPE_CHECKING:
      assert isinstance(self.shellOrder, list)
    if index < 0:
      e = """The index must be a non-negative integer!"""
      raise ValueError(e)
    if index >= len(self.shellOrder):
      e = f"""The index must be less than !"""
      raise ValueError(e)

    self.shellOrder[index] = state

  def liveShot(self, ) -> None:
    """Perform a live shot. """
    if TYPE_CHECKING:
      assert isinstance(self.shellOrder, list)
    shell = self.shellOrder.pop(0)
    if shell is None:
      if not self.lives:
        e = """There are no live shells left, but a live shot was 
        attempted!"""
        raise ValueError(e)
      self.lives -= 1
    elif shell:
      return
    e = """The upcoming shell was known to be blank, but a live shot was
    attempted!"""
    raise ValueError(e)

  def blankShot(self, ) -> None:
    """Perform a blank shot. """
    if TYPE_CHECKING:
      assert isinstance(self.shellOrder, list)
    shell = self.shellOrder.pop(0)
    if shell is None:
      if self.blanks:
        self.blanks -= 1
        return
      e = """There are no blank shells left, but a blank shot was
      attempted!"""
      raise ValueError(e)
    elif shell:
      e = """The upcoming shell was known to be live, but a blank shot was
      attempted!"""
      raise ValueError(e)

  def nextChance(self) -> float:
    """Returns the probability that the next shot is live"""
    if self.lives + self.blanks:
      return self.lives / (self.lives + self.blanks)
