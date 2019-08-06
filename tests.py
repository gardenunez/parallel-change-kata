import unittest
import service

class SuperHeroTests(unittest.TestCase):

    def test_get_name_by_id_1(self):
        super_hero = service.SuperHero()
        name = super_hero.get_name_by_id("1")
        self.assertEqual("Jane Hopper ( Eleven )", name)

    def test_get_name_by_id_3(self):
        super_hero = service.SuperHero()
        name = super_hero.get_name_by_id("3")
        self.assertEqual("Bruce Banner ( Hulk )", name)

    def test_get_name_by_id_when_does_not_exists(self):
        super_hero = service.SuperHero()
        name = super_hero.get_name_by_id("4")
        self.assertIsNone(name)

    def test_get_lenght(self):
        super_hero = service.SuperHero()
        lenght = super_hero.get_lenght()
        self.assertEqual(3, lenght)


if __name__ == "__main__":
    unittest.main()