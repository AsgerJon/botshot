"""ShellKeeNum enumerates the possible states of each shell."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from worktoy.keenum import KeeNum, auto


class Shell(KeeNum):
  """ShellKeeNum enumerates the possible states of each shell."""

  EMPTY = auto()
  HIDDEN = auto()
  WAS_LIVE = auto()
  WAS_BLANK = auto()
  LIVE = auto()
  BLANK = auto()
