from services.lama_model import LamaModel 
from services.summary_creator import SummaryCreator

class DefaultController:
    def __init__(self):
        self.lama = LamaModel() 
        self.summary_creator = SummaryCreator()

    def generate_incident_description(self, input_text, response_length, additional_data=None, fields_to_extract=None):
        if additional_data:
            summary = self.summary_creator.create_abstract_summary_from_json(additional_data, fields_to_extract)
            combined_input = f"{input_text} {summary}"
            print(combined_input)
            input_text = combined_input
        else:
            combined_input = input_text
            input_text = combined_input

        return self.lama.generate_text(input_text, response_length)

    