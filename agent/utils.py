from models.schema import QueryResponse
from models.schema import CustomerOrdersData
import ast
import re
import json

def parse_llm_intent(response : str)-> QueryResponse:
    """Extracts JSON and parses in Pydantic
    Args:
        response: str : LLM response to parse
    Returns:
        classification: QueryResponse : parsed data
    """
    try:
        parsed_str = ast.literal_eval(response)
        classification = QueryResponse(**parsed_str)
        return classification
    except Exception as e:
        print(f"Error parsing classification: {e}")
    
    return QueryResponse(needs_general_knowledge=True, needs_customer_data=False)

def parse_json_to_pydantic(file_path: str) -> CustomerOrdersData:
    """
    Parse a JSON file and convert it to a Pydantic model instance.
    
    Args:
        file_path: str : Path to the JSON file
        
    Returns:
        returns CustomerOrderData Pydantic model instance
    """
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return CustomerOrdersData(**json_data)
