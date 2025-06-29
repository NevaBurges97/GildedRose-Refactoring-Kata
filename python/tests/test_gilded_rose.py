# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_name(self):
        items = [Item("Elixir of the Mongoose", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        
    def test_update_ordinary_item_before_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 19)
        
    def test_update_ordinary_item_1_day_before_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 0)
        self.assertEqual(gilded_rose.items[0].quality, 19)

    def test_update_ordinary_item_on_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -1)
        self.assertEqual(gilded_rose.items[0].quality, 18)

    def test_update_ordinary_item_after_sell_date(self):
        items = [Item("Elixir of the Mongoose", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 18)

if __name__ == '__main__':
    unittest.main()
