from services.lama_model import LamaModel 

class DefaultController:
    def __init__(self):
        self.lama = LamaModel() 

    def generate_incident_description(self, input_text, response_length):
        return self.lama.generate_text(input_text, response_length) 

    