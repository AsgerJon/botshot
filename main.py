"""Main tester script"""
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

import sys
import os
from typing import Any, Never

from icecream import ic
from worktoy.yolo import yolo


def tester00() -> int:
  """Hello World!"""
  stuff = [sys, os, 'hello world', ic, Any, Never]
  for item in stuff:
    print(item)
  return 0


if __name__ == '__main__':
  yolo(tester00)
