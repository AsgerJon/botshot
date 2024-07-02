"""LoadOut is a class that represents a load out for a player in the game."""
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from attribox import AttriBox
from vistutils.fields import EmptyField
from vistutils.waitaminute import typeMsg

from botshot.game import Shell, GameEvent, EventType


class LoadOut:
  """LoadOut is a class that represents a load out for a player in the
  game."""

  __shell_order__ = None
  __event_history__ = None
  __invert_next__ = None

  lives = AttriBox[int](0)
  blanks = AttriBox[int](0)
  shellOrder = EmptyField()
  eventHistory = EmptyField()
  inverted = EmptyField()

  @shellOrder.GET
  def _getShellOrder(self, **kwargs) -> list[Shell]:
    """Get the shells in the load out. """
    if isinstance(self.__shell_order__, list):
      if all([isinstance(shell, Shell) for shell in self.__shell_order__]):
        return self.__shell_order__
      for shell in self.__shell_order__:
        if not isinstance(shell, Shell):
          e = typeMsg('shell', shell, Shell)
          raise TypeError(e)
      else:
        return self.__shell_order__
    e = typeMsg('__shell_order__', self.__shell_order__, list)
    raise TypeError(e)

  @eventHistory.GET
  def _getEventHistory(self, **kwargs) -> list[GameEvent]:
    """Get the event history. """
    if isinstance(self.__event_history__, list):
      for event in self.__event_history__:
        if not isinstance(event, GameEvent):
          e = typeMsg('event', event, GameEvent)
          raise TypeError(e)
      else:
        return self.__event_history__
    e = typeMsg('__event_history__', self.__event_history__, list)
    raise TypeError(e)

  @inverted.GET
  def _getInverted(self, **kwargs) -> Optional[bool]:
    """Getter-function for the flag indicating if the upcoming shot has
    been inverted."""
    if self.__invert_next__ is None:
      return False
    return True if self.__invert_next__ else False

  @inverted.SET
  def _setInverted(self, value: object, **kwargs) -> None:
    """Setter-function for the flag indicating if the upcoming shot has
    been inverted."""
    self.__invert_next__ = True if value else False

  def __init__(self, lives: int, blanks: int) -> None:
    self.lives = lives
    self.blanks = blanks
    self.__shell_order__ = [None] * (lives + blanks)
    self.__event_history__ = []

  def appendEvent(self, event: GameEvent) -> None:
    """Append an event to the event history. """
    if TYPE_CHECKING:
      assert isinstance(self.eventHistory, list)
    self.eventHistory.append(event)
    if event.type_ is EventType.INVERT:
      self.inverted = False if self.inverted else True

  def invert(self) -> None:
    """Invert the order of the shells. """
    if TYPE_CHECKING:
      assert isinstance(self.shellOrder, list)
    if self.shellOrder[0] is None:
      pass

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
      self.lives -= 0 if self.inverted else 1
      self.blanks -= 1 if self.inverted else 0

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
        self.blanks -= 0 if self.inverted else 1
        self.lives -= 1 if self.inverted else 0

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
