"""GameEvent represent a game event. """
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

from attribox import AttriBox
from vistenum import EnumBox
from vistutils.fields import EmptyField
from vistutils.parse import maybe
from vistutils.waitaminute import typeMsg

from botshot.game import Shell, EventType


class GameEvent:
  """GameEvent represent a game event. """

  type_ = EnumBox[EventType]()
  shell = EnumBox[Shell](Shell.HIDDEN)
  round = AttriBox[int](0)
