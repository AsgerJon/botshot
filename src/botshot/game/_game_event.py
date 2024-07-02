"""GameEvent represent a game event. """
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from attribox import AttriBox
from vistutils.fields import EmptyField
from vistutils.parse import maybe
from vistutils.waitaminute import typeMsg

from botshot.game import Shell, EventType


class GameEvent:
  """GameEvent represent a game event. """

  __round_num__ = None
  __shell_state__ = None
  __event_type__ = None

  state = EmptyField()
  type_ = EmptyField()
  index = AttriBox[int](0)

  @state.GET
  def _getState(self, **kwargs) -> Shell:
    """Get the state of the shell. """
    if self.__shell_state__ is None:
      e = """The shell state has not been set!"""
      raise ValueError(e)
    if isinstance(self.__shell_state__, Shell):
      return self.__shell_state__
    e = typeMsg('__shell_state__', self.__shell_state__, Shell)
    raise TypeError(e)

  @state.SET
  def _setState(self, value: Shell, **kwargs) -> None:
    """Set the state of the shell. """
    if self.__shell_state__ is not None:
      e = """The shell state has already been set!"""
      raise ValueError(e)
    if not isinstance(value, Shell):
      e = typeMsg('value', value, Shell)
      raise TypeError(e)
    self.__shell_state__ = value

  @type_.GET
  def _getType(self, **kwargs) -> EventType:
    """Get the type of the event. """
    if self.__event_type__ is None:
      e = """The event type has not been set!"""
      raise ValueError(e)
    if isinstance(self.__event_type__, EventType):
      return self.__event_type__
    e = typeMsg('__event_type__', self.__event_type__, EventType)
    raise TypeError(e)

  @type_.SET
  def _setType(self, value: EventType, **kwargs) -> None:
    """Set the type of the event. """
    if self.__event_type__ is not None:
      e = """The event type has already been set!"""
      raise ValueError(e)
    if not isinstance(value, EventType):
      e = typeMsg('value', value, EventType)
      raise TypeError(e)
    self.__event_type__ = value

  def __init__(self, *args) -> None:
    round_, state, type_ = None, None, None
    for arg in args:
      if isinstance(arg, int) and round is None:
        round = arg
      elif isinstance(arg, Shell) and state is None:
        state = arg
      elif isinstance(arg, EventType) and type_ is None:
        type_ = arg
    if round_ and type_ is not EventType.PHONE:
      e = """Only phone events may have non-zero round numbers!"""
      raise ValueError(e)
    self.index = maybe(round_, 0)
    self.state = state
    self.type_ = type_
