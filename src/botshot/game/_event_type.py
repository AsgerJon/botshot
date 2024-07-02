"""EventType enumeration for game events. """
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from vistenum import VistEnum, auto


class EventType(VistEnum):
  """Event enumeration for game events. """

  BEER = auto()
  GLASS = auto()
  PHONE = auto()
  SHOT = auto()
  INVERT = auto()
