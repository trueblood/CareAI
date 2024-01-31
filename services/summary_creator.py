
class SummaryCreator:
    def create_summary_from_json(self, json_data, fields):
        # Assuming json_data is a list of dictionaries
        summaries = []

        for item in json_data:
            extracted_info = {field: item.get(field, 'N/A') for field in fields}
            summary = ', '.join([f'{key}: {value}' for key, value in extracted_info.items()])
            summaries.append(summary)

        return ' | '.join(summaries)