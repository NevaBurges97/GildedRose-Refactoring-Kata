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
        super().__init__(item.name, item.sell_in, item.quality)

    @abstractmethod
    def update_quality():
        pass
    
    def decrease_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality += 1


class OrdinaryItem(BaseItem):
    def update_quality(self):
        self.sell_in -= 1
        self.decrease_quality()
        if self.sell_in < 0:
            self.decrease_quality()


class BackstagePasses(BaseItem):
    def update_quality(self):
        self.sell_in -= 1
        self.increase_quality()
        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 5:
            self.increase_quality()
        if self.sell_in < 0:
            self.quality = 0


class AgedBrie(BaseItem):
    def update_quality(self):
        self.sell_in -= 1
        self.increase_quality()
        if self.sell_in < 0:
            self.increase_quality()


class Sulfuras(BaseItem):
    def update_quality(self):
        pass


class GildedRose(object):
    ITEM_CLASSES = {
        "Aged Brie": AgedBrie,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
        "Sulfuras, Hand of Ragnaros": Sulfuras
    }

    def __init__(self, items: list[Item]):
        self.items: list[BaseItem] = [self.create_item(item) for item in items]

    def create_item(self, item: Item):
        item_class = self.ITEM_CLASSES.get(item.name, OrdinaryItem)
        return item_class(item)
    
    def update_quality(self):
        for item in self.items:
            item.update_quality()
