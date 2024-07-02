"""Shell provides enumeration for shells covering live, blank and hidden
shells. """
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from vistenum import VistEnum, auto


class Shell(VistEnum):
  """Shell provides enumeration for shells covering live, blank and hidden
  shells. """
  LIVE = auto()
  BLANK = auto()
  HIDDEN = auto()
