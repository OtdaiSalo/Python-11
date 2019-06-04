def find_by_producer():
    print("Found by producer:")


class CleaningToolsManager:
    cleaning_tools = []


    def add_element_to_list(self, cleaning_tool):
        self.cleaning_tools.append(cleaning_tool)


    def show_list_elements(self):
        print("\nAll elements in list:")
        for element in self.cleaning_tools:
            print(element)
        print("\n")

    def sort_by_price (self, reverse):
        self.cleaning_tools.sort(key=lambda cleaning_tools: cleaning_tools.price,
                  reverse=reverse)


    def sort_by_costs_per_month (self, reverse):
        self.cleaning_tools.sort(key=lambda cleaning_tools: cleaning_tools.costs_per_month, reverse=reverse)


    def find_by_producer(self, producer):
        temp_list = []
        for cleaning_tools in self.cleaning_tools:
            if cleaning_tools.producer ==  producer:
                temp_list.append(cleaning_tools)

        print("\nFind by name result:")
        for cleaning_tools in temp_list:
            print(cleaning_tools)
        return temp_list
        print("")


    def __del__(self):
        print("\nCleaning tools manager is deleted!")


