
class ToolsForCleaning:
    def __init__(self, price, costs_per_month, producer, chemical_composition, point_of_using):
        self.price = price
        self.costs_per_month = costs_per_month
        self.producer = producer
        self.chemical_composition = chemical_composition
        self.point_of_using = point_of_using

    def __str__(self):
        return "Tools for cleaning { " \
               + str(self.price) + ", " \
               + str(self.costs_per_month) + ", " \
               + self.producer + ", " \
               + str(self.chemical_composition) + ", " \
               + str(self.point_of_using) + " } "

    def __del__(self):
        print("Tools For Cleaning Deleted!")