# -*- coding: utf-8 -*-
from abc import abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class BaseItem(Item):
    def __init__(self, item: Item):
        self.item = item

    @abstractmethod
    def update_quality():
        pass

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1


class OrdinaryItem(BaseItem):
    def update_quality(self):
        self.item.sell_in -= 1
        self.decrease_quality()
        if self.item.sell_in < 0:
            self.decrease_quality()


class BackstagePasses(BaseItem):
    def update_quality(self):
        self.item.sell_in -= 1
        self.increase_quality()
        if self.item.sell_in < 10:
            self.increase_quality()
        if self.item.sell_in < 5:
            self.increase_quality()
        if self.item.sell_in < 0:
            self.item.quality = 0


class AgedBrie(BaseItem):
    def update_quality(self):
        self.item.sell_in -= 1
        self.increase_quality()
        if self.item.sell_in < 0:
            self.increase_quality()


class Sulfuras(BaseItem):
    def update_quality(self):
        pass


class GildedRose(object):
    def __init__(self, items: list[Item]):
        self.items = items

    def get_item_class(self, item: Item):
        if item.name == "Aged Brie":
            return AgedBrie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
        else:
            return OrdinaryItem(item)
    
    def update_quality(self):
        for item in self.items:
            item_class = self.get_item_class(item)
            item_class.update_quality()
