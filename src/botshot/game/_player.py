"""Player encapsulates the player."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.desc import AttriBox

from botshot.game import Inventory


class Player:
  """Player encapsulates the player."""
  inventory = AttriBox[Inventory]()
