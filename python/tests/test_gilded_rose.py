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

    def test_update_ordinary_item_after_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 18)

    def test_update_ordinary_item_zero_quality_before_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 0)

    def test_update_ordinary_item_zero_quality_after_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 0)

    def test_update_ordinary_item_low_quality_before_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", 10, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 0)

    def test_update_ordinary_item_low_quality_after_sell_by_date(self):
        items = [Item("Elixir of the Mongoose", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 0)

    def test_update_aged_brie(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 21)

    def test_update_aged_brie_on_sell_by_date(self):
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -1)
        self.assertEqual(gilded_rose.items[0].quality, 22)

    def test_update_aged_brie_after_sell_by_date(self):
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 22)

    def test_update_aged_brie_highest_quality_before_sell_by_date(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[0].quality, 50)

    def test_update_aged_brie_highest_quality_after_sell_by_date(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 50)

    def test_update_aged_brie_high_quality_after_sell_by_date(self):
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, -2)
        self.assertEqual(gilded_rose.items[0].quality, 50)
    
    def test_update_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 0)
        self.assertEqual(gilded_rose.items[0].quality, 80)

if __name__ == '__main__':
    unittest.main()
