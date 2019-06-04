from models.ToolsForCleaning import ToolsForCleaning
from models.InsectRemediesToxicity import InsectRemediesToxicity

class ShoeCareTools(ToolsForCleaning):

    def __init__(self, price, costs_per_month, producer, chemical_composition, point_of_using, insect_type, toxicity):
        super().__init__(price, costs_per_month, producer, chemical_composition, point_of_using)
        self.insect_type = insect_type
        self.toxicity = toxicity

    def __str__(self, price, costs_per_month, producer, chemical_composition, point_of_using, insect_type, toxicity):
        super().__str__(price, costs_per_month, producer, chemical_composition, point_of_using)\
               + " Shoe Care Tools { " \
               + str(self.insect_type) + \
               + str(self.toxicity) + " }"

    def __del__(self):
        print("Insect Remedies was deleted!")
