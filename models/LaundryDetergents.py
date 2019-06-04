from models.ToolsForCleaning import ToolsForCleaning

class ShoeCareTools(ToolsForCleaning):

    def __init__(self, price, costs_per_month, producer, chemical_composition, point_of_using, type_of_wasing, one_time_spending):
        super().__init__(price, costs_per_month, producer, chemical_composition, point_of_using)
        self.type_of_wasing = type_of_wasing
        self.one_time_spending = one_time_spending

    def __str__(self, price, costs_per_month, producer, chemical_composition, point_of_using, type_of_wasing, one_time_spending):
        super().__str__(price, costs_per_month, producer, chemical_composition, point_of_using)\
               + " Shoe Care Tools { " \
               + str(self.type_of_wasing) + \
               + str(self.one_time_spending) + " }"

    def __del__(self):
        print("Laundry Detergents was deleted!")
