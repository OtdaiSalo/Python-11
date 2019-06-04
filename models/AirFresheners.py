from models.ToolsForCleaning import ToolsForCleaning

class ShoeCareTools(ToolsForCleaning):

    def __init__(self, price, costs_per_month, producer, point_of_using, chemical_composition, flavour, volume):
        super().__init__(price, costs_per_month, producer, point_of_using, chemical_composition)
        self.flavour = flavour
        self.volume = volume

    def __str__(self, price, costs_per_month, producer, chemical_composition, point_of_using, flavour, volume):
        super().__str__(price, costs_per_month, producer, chemical_composition, point_of_using)\
               + " Shoe Care Tools { " \
               + str(self.flavour) + \
               + str(self.volume) + " }"

    def __del__(self):
        print("Air Fresheners was deleted!")