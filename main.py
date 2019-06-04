from managers.CleaningToolsManager import CleaningToolsManager
from models import ShoeCareToolsColor
from models.ChemicalSubstances import ChemicalSubstances
from models import AirFresheners
from models import InsectRemedies
from models import InsectRemediesToxicity
from models import LaundryDetergents
from models import ShoeCareTools
from models.ToolsForCleaning import ToolsForCleaning
from models.ToolsPointOfUsing import ToolsPointOfUsing


cleaning_tools_manager = CleaningToolsManager()

antiMosquito = ToolsForCleaning(12.5, 3.5, 'Uganda', ChemicalSubstances.SALTS, ToolsPointOfUsing.OUTDOOR)
jungleFlavourX100 = ToolsForCleaning(15.5, 1.0, 'Yugoslavia', ChemicalSubstances.OXIDES, ToolsPointOfUsing.INDOOR)
leathureCare = ToolsForCleaning(30, 12, 'Ukraine', ChemicalSubstances.OXIDES, ToolsPointOfUsing.INDOOR)

cleaning_tools_manager.add_element_to_list(antiMosquito)
cleaning_tools_manager.add_element_to_list(jungleFlavourX100)
cleaning_tools_manager.add_element_to_list(leathureCare)

cleaning_tools_manager.sort_by_price(True)
cleaning_tools_manager.show_list_elements()

cleaning_tools_manager.sort_by_costs_per_month(True)
cleaning_tools_manager.show_list_elements()

cleaning_tools_manager.find_by_producer("Ukraine")

