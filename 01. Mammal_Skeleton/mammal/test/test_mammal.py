from project.mammal import Mammal
import unittest
from unittest import TestCase, main



class TestMammal(TestCase):

    def test_attributes(self):
        mammal_1 = Mammal('Toshko', 'pig','hruphrup' )
        self.assertEqual('Toshko', mammal_1.name)
        self.assertEqual('pig', mammal_1.type)
        self.assertEqual('hruphrup', mammal_1.sound)
    def test_make_sound(self):
        mammal_1 = Mammal('Toshko', 'pig', 'hruphrup')
        self.assertEqual("Toshko makes hruphrup",  mammal_1.make_sound())

    def test_get_kingdom(self):
        mammal_1 = Mammal('Toshko', 'pig', 'hruphrup')
        self.assertEqual("animals", mammal_1.get_kingdom())

    def test_get_info(self):
        mammal_1 = Mammal('Toshko', 'pig', 'hruphrup')
        self.assertEqual("Toshko is of type pig", mammal_1.info())











if __name__ == '__main__':
    main()
