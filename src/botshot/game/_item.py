"""Item encapsulates the items in the game."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, auto


class Item(KeeNum):
  """Item encapsulates the items in the game."""
  NULL = auto()  # No item
  BEER = auto()
  GLASS = auto()
  PHONE = auto()
  CIGARETTE = auto()
  INVERTER = auto()
  ADRENALINE = auto()
  PILL = auto()
  CUFFS = auto()
  SAW = auto()
