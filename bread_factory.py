# Bread factory exercise

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
