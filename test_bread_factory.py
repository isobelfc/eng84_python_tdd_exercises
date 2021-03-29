# Bread factory testing

# import the bread_factory code to test
from bread_factory import Bread

# Importing unittest to inherit TestCase to create our tests against the code
import unittest

class BreadFactory(unittest.TestCase):
    bread = Bread()

    def test_make_dough(self):
        self.assertEqual(self.bread.make_dough("water", "flour"), "dough")
        # checks that water and flour makes dough, if true test passes

    def test_bake_dough(self):
        self.assertEqual(self.bread.bake_dough("dough"), "naan")
        # checks that dough makes naan, if true test passes

    def test_run_factory(self):
        self.assertEqual(self.bread.run_factory("water", "flour"), "naan")
        # checks that water and flour makes naan, if true test passes
