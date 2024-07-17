"""Inventory encapsulates the inventory of a player"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.text import typeMsg

from botshot.game import Item


class Inventory:
  """Inventory encapsulates the inventory of a player. """

  __inner_items__ = None

  def _createItems(self) -> None:
    """Creator-function for the items"""
    self.__inner_items__ = [Item.NULL for _ in range(8)]

  def _getItems(self, **kwargs) -> list[Item]:
    """Get the items in the inventory. """
    if self.__inner_items__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createItems()
      return self._getItems(_recursion=True)
    if isinstance(self.__inner_items__, list):
      for item in self.__inner_items__:
        if not isinstance(item, Item):
          e = typeMsg('item', item, Item)
          raise TypeError(e)
      return self.__inner_items__
    e = typeMsg('items', self.__inner_items__, list)
    raise TypeError(e)

  def append(self, item: Item) -> None:
    """Append an item to the inventory. """
    for (i, item) in self._getItems():
      if item is Item.NULL:
        self.__inner_items__[i] = item
        return
    e = """Out of space, how unfortunate!"""
    raise RuntimeError(e)

  def take(self, item: Item) -> None:
    """Take an item from the inventory. """
    for (i, item) in self._getItems():
      if item is item:
        self.__inner_items__[i] = Item.NULL
        return
    e = """Item not in inventory!"""
    raise RuntimeError(e)
