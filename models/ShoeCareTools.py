from models.ToolsForCleaning import ToolsForCleaning
from models.ShoeCareToolsColor import ShoeCareToolsColor

class ShoeCareTools(ToolsForCleaning):

    def __init__(self, price, costs_per_month, producer, chemical_composition, point_of_using, material_type, color):
        super().__init__(price, costs_per_month, producer, chemical_composition, point_of_using)
        self.material_type = material_type
        self.color = color

    def __str__(self, price, costs_per_month, producer, chemical_composition, point_of_using, material_type, color):
        super().__str__(price, costs_per_month, producer, chemical_composition, point_of_using)\
               + " Shoe Care Tools { " \
               + str(self.material_type) + \
               + str(self.color) + " }"

    def __del__(self):
        print("Shoe Care Tools was deleted!")



