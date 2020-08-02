# Recipe

ingredients = ["2 avocados", "1 lime", "2 tsp salt"]
instructions = ["chop avocados", "chop onion",
                "squeeze lime", "add salt", "mix well"]


class Recipe:
    def __init__(self):
        self.name = "recipe1"
        self.preparation_time =10 

    def print_ingredients(self):
        for ingredient in ingredients:
            print(f"\t *To make {ingredients} you need to do the following:")
             
        

    def print_instructions(self):
        for instruction in instructions:
            print(f"\t +To make {instructions} you need to do the following:")
       

    def add_ingredient(self, ingredient):
        ingredient.append("4 bread")
        print(ingredients)
        
    def add_instruction(self, instruction):
        instruction.append("eat hummas")
        print(instructions)

obj = Recipe()

obj.print_ingredients()
obj.print_instructions()
obj.add_ingredient(ingredients)
obj.add_instruction(instructions)