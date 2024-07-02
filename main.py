"""Main tester script"""
# *************************************************************************
#  AGPL-3.0 license                                                       *
#  Copyright (c) 2024 Asger Jon Vistisen                                  *
# *************************************************************************
from __future__ import annotations

import sys
import os
import time

from icecream import ic
from typing import Callable, Any, Never

from vistutils.text import stringList

from botshot.game import Shell, EventType


def tester00() -> int:
  """Hello World!"""
  stuff = [sys, os, 'hello world', ic, Any, Never]
  for item in stuff:
    print(item)
  return 0


def tester01() -> int:
  """Test of botshot game logic."""
  for cls in [Shell, EventType, ]:
    print(77 * '_')
    print('Beginning of %s' % cls.__name__)
    for item in cls:
      print(item)
    print('End of %s' % cls.__name__)
    print(77 * '¨')


def tester02() -> int:
  """Test of list multiplication."""
  lol = ['lmao', ]
  print(lol)
  print(lol * 3)
  return 0


def main(*args: Callable) -> None:
  """Main Tester Script"""
  tic = time.perf_counter_ns()
  print('Running python script located at: \n%s' % sys.argv[0])
  print('Started at: %s' % time.ctime())
  print(77 * '-')
  retCode = 0
  for callMeMaybe in args:
    print('\nRunning: %s\n' % callMeMaybe.__name__)
    try:
      retCode = callMeMaybe()
    except BaseException as exception:
      print('Exception: %s' % exception)
      retCode = -1
  retCode = 0 if retCode is None else retCode
  print(77 * '-')
  print('Return Code: %s' % retCode)
  toc = time.perf_counter_ns() - tic
  if toc < 1000:
    print('Runtime: %d nanoseconds' % (int(toc),))
  elif toc < 1000000:
    print('Runtime: %d microseconds' % (int(toc * 1e-03),))
  elif toc < 1000000000:
    print('Runtime: %d milliseconds' % (int(toc * 1e-06),))


if __name__ == '__main__':
  main(tester01)
