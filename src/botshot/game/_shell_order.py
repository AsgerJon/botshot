"""The ShellOrder class encapsulates the shell order."""
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

import sys

from attribox import AttriBox
from vistutils.text import stringList, monoSpace
from vistutils.waitaminute import typeMsg

from botshot.game import ShellState

if sys.version_info.minor < 11:
  from typing_extensions import Self
else:
  from typing import Self


class ShellOrder:
  """The ShellOrder class encapsulates the shell order."""

  _shells = None
  __iter_contents__ = None

  initLiveCount = AttriBox[int](-1)
  initBlankCount = AttriBox[int](-1)
  liveCount = AttriBox[int](-1)
  blankCount = AttriBox[int](-1)
  invertNextFlag = AttriBox[bool](False)

  @staticmethod
  def _parseArgs(*args, **kwargs) -> dict[str, int]:
    """Parses positional and keyword arguments."""
    liveKeys = stringList("""live, liveShell, l, L""")
    blankKeys = stringList("""blank, blankShell, b, B""")
    names = stringList("""live, blank""")
    types = [int, int]
    values = {}
    KEYS = [liveKeys, blankKeys]
    unusedArgs = [a for a in args]
    for (keys, name, type_) in zip(KEYS, names, types):
      for key in keys:
        if key in kwargs:
          val = kwargs[key]
          if isinstance(val, type_):
            values[name] = val
            break
          e = typeMsg(name, val, type_)
          raise TypeError(e)
      else:
        frozenArgs = [a for a in unusedArgs]
        unusedArgs = []
        for arg in frozenArgs:
          if isinstance(arg, type_) and name not in values:
            values[name] = arg
          else:
            unusedArgs.append(arg)
        if name not in values:
          e = """Unable to parse argument: '%s' of type: '%s'! """
          raise TypeError(monoSpace(e % (name, type_)))
    for (key, val) in values.items():
      if not isinstance(val, int):
        e = typeMsg(key, val, int)
        raise TypeError(e)
      if val < 0:
        e = """The '%s' argument must be a positive integer! """
        raise ValueError(e % key)
    return values

  @staticmethod
  def _parseShells(*args) -> list:
    """Parse the shells from the arguments."""
    out = []
    for arg in args:
      try:
        if isinstance(arg, ShellState):
          out.append(arg)
      except Exception as exception:
        raise exception
    return out

  def __init__(self, *args, **kwargs) -> None:
    shellStates = self._parseShells(*args)
    if shellStates:
      self._shells = shellStates
    else:
      values = self._parseArgs(*args, **kwargs)
      self.initBlankCount = values.get('blank', 0)
      self.initLiveCount = values.get('live', 0)
      self.blankCount = values.get('blank', 0)
      self.liveCount = values.get('live', 0)
      liveCount = values.get('live', 0)
      blankCount = values.get('blank', 0)
      self._shells = [ShellState.hidden, ] * len(self)

  def __len__(self) -> int:
    return self.initLiveCount + self.initBlankCount

  def __iter__(self) -> Self:
    """Prepares the private variable __iter_contents__ for iteration
    protocol. """
    self.__iter_contents__ = [*self._shells, ]
    return self

  def __next__(self, ) -> ShellState:
    """Returns the next shell state."""
    try:
      return self.__iter_contents__.pop(0)
    except IndexError:
      raise StopIteration

  def _validateIndex(self, index: int) -> int:
    """Validates the index."""
    if not isinstance(index, int):
      e = typeMsg('index', index, int)
      raise TypeError(e)
    while index < 0:
      index += len(self)
    if index >= len(self):
      e = """The index: '%d' is out of range! """
      raise IndexError(e % index)
    return index

  def currentShellIndex(self) -> int:
    """Returns the index of the current shell."""
    for (i, shell) in enumerate(self):
      pass

  def __getitem__(self, index: int) -> ShellState:
    """Returns the shell state at the specified index."""
    return self._shells[self._validateIndex(index)]

  def __setitem__(self, index: int, value: bool) -> None:
    """True for live shell and False for blank shell. """
    key = self._validateIndex(index)
    self._shells[key] = ShellState.live if value else ShellState.blank

  def invertNext(self, ) -> None:
    """Inverts the next shell state."""
    self.invertNextFlag = not self.invertNextFlag

  def liveShot(self) -> None:
    """Shoots a live shell."""
    self.liveCount -= 1
    self._shells[self._shells.index(ShellState.live)] = ShellState.wasLive
