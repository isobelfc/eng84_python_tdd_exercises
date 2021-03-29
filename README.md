# Exercises

## Bread factory
**Setup**
- I created a test file `test_bread_factory.py` and a file `bread_factory.py`
- Within `bread_factory.py`, I created an empty class `Bread` with the `pass` keyword
- Imported `Bread` into `test_bread_factory.py` with `from bread_factory import bread`
- Also imported `unittest`
- Created a class in the test file called `BreadFactory`
```python
class BreadFactory(unittest.TestCase):
    bread = Bread()
```

**Writing the tests**
- Defined three methods within `BreadFactory`, each one named `test_*`
- Used `assertEqual` to give intended values of running each function
```python
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
```
- When run at this stage, all 3 tests fail

**Write the code to pass the tests**
- Defined 3 functions in `Bread` class: `make_dough`, `bake_dough` and `run_factory`
- Each one took one or two ingredients as arguments, and then returned the food produced, or `unknown recipe`, using an `if` statement
- I ran the code after defining each function to check there were no syntax errors
- I then ran the tests again before moving on to defining the next function
- In this way, I could see the test results go from 3 failures, to 2 failures and 1 pass, to 1 failure and 2 passes, to all three passing
- The final defined functions were as follows:
```python
class Bread():
    def make_dough(self, ingredient1, ingredient2):
        if ingredient1 == "water" and ingredient2 == "flour":
            return "dough"
        else:
            return "recipe unknown"

    def bake_dough(self, ingredient):
        if ingredient == "dough":
            return "naan"
        else:
            return "recipe unknown"

    def run_factory(self, ingredient1, ingredient2):
        if ingredient1 == "water" and ingredient2 == "flour":
            return "naan"
        else:
            return "recipe unknown"
```