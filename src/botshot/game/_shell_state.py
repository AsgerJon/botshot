"""ShellState encapsulates the state of a shell. """
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from vistenum import VistEnum, auto


class ShellState(VistEnum):
  """ShellState encapsulates the state of a shell. """
  #  States after ejection
  wasBlank = auto()
  wasLive = auto()
  #  States before ejection
  hidden = auto()
  live = auto()
  blank = auto()
  #  Empty means that no shell was ever present
  empty = auto()
