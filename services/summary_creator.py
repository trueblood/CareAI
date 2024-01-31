
class SummaryCreator:
    def create_summary_from_json(self, json_data, fields):
        # Assuming json_data is a list of dictionaries
        summaries = []

        for item in json_data:
            extracted_info = {field: item.get(field, 'N/A') for field in fields}
            summary = ', '.join([f'{key}: {value}' for key, value in extracted_info.items()])
            summaries.append(summary)

        return ' | '.join(summaries)
    
    def create_abstract_summary_from_json(self, json_data, fields):
        summaries = []

        for item in json_data:
            # Extract information based on the specified fields
            extracted_info = {field: item.get(field, 'N/A') for field in fields}
            
            # Construct a narrative-like summary from the extracted information
            summary_parts = ["An incident occurred"]
            if 'CommunityName' in extracted_info and extracted_info['CommunityName'] != 'N/A':
                summary_parts.append(f"at {extracted_info['CommunityName']}")
            if 'FirstName' in extracted_info and extracted_info['FirstName'] != 'N/A':
                resident_name = f"involving a resident named {extracted_info['FirstName']}"
                if 'LastName' in extracted_info and extracted_info['LastName'] != 'N/A':
                    resident_name += f" {extracted_info['LastName']}"
                summary_parts.append(resident_name)
            if 'State' in extracted_info and extracted_info['State'] != 'N/A':
                summary_parts.append(f"in {extracted_info['State']}")
            if 'Description' in extracted_info and extracted_info['Description'] != 'N/A':
                summary_parts.append(f". Here is info about the event, {extracted_info['Description']}")

            # Combine the parts to form a single sentence for this item
            summary = ' '.join(summary_parts) + "."
            summaries.append(summary)

        return ' | '.join(summaries)