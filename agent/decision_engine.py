from models.schema import QueryClassification
import ast
import re
import json

def parse_llm_intent(response)-> QueryClassification:
    # Extract and parse the JSON from the response
    try:
        # Use ast.literal_eval to parse the Python string representation
        parsed_str = ast.literal_eval(response)
        classification = QueryClassification(**parsed_str)
        return classification
    except Exception as e:
        print(f"Error parsing classification: {e}")
    
    # Default to safer option if parsing fails
    return QueryClassification(needs_general_knowledge=True, needs_customer_data=True)