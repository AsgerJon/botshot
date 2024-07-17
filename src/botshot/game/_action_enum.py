"""ActionEnum class for defining the actions that can be taken by both the
player and the dealer. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, auto


class Action(KeeNum):
  """ActionEnum class for defining the actions that can be taken by both the
  player and the dealer. """

  #  Shoot other or self
  SHOOT = auto()  # Shoot at other
  YOLO = auto()  # Shoot at self

  #  Use items
  BEER = auto()  # Drink beer
  SMOKE = auto()  # Smoke cigarette
  GLASS = auto()  # Use magnifying glass
  PILL = auto()  # Take pill
  PHONE = auto()  # Use phone
  CUFF = auto()  # Use handcuffs
  INVERT = auto()  # Changes live to blank and blank to live
  SAW = auto()  # Saw off shotgun barrel

  #  Steal items
  STEAL_BEER = auto()  # Steal beer
  STEAL_GLASS = auto()  # Steal magnifying glass
  STEAL_PILL = auto()  # Steal pill
  STEAL_PHONE = auto()  # Steal phone
  STEAL_CUFF = auto()  # Steal handcuffs
  STEAL_SAW = auto()  # Steal saw
  STEAL_INVERT = auto()  # Steal invert
  STEAL_SMOKE = auto()  # Steal cigarette
