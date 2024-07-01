"""ShellState encapsulates the state of a shell. """
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from vistenum import VistEnum, auto
from vistutils.fields import EmptyField


class ShellState(VistEnum):
  """ShellState encapsulates the state of a shell. """
  #  States after ejection
  ejected = EmptyField()
  wasBlank = auto()
  wasLive = auto()
  #  States before ejection
  hidden = auto()
  live = auto()
  blank = auto()
  #  Empty means that no shell was ever present
  empty = auto()

  def _getEjectedMembers(self) -> list:
    """Get a list of the ejected states. """
    return [self.wasBlank, self.wasLive]

  def _getNotEjectedMembers(self) -> list:
    """Get a list of the non-ejected states. """
    return [self.hidden, self.live, self.blank, ]

  @ejected.GET
  def _getEjected(self) -> bool:
    """Getter function for ejected flag. """
    if self in self._getEjectedMembers():
      return True
    if self in self._getNotEjectedMembers():
      return False
    if self is self.empty:
      e = """The empty state is neither ejected nor not ejected!"""
      raise AttributeError(e)
