import json
from pathlib import Path
from agent.utils import parse_json_to_pydantic
from models.schema import QueryResponse

class DataLoader:
    def __init__(self, 
                 customer_file_path: str = "data/knowledge_base/customer_data.json", 
                 org_file_path: str="data/knowledge_base/organization_data.txt"):
        
        self.customer_file_path = customer_file_path
        self.org_file_path = org_file_path
        
    def load_customer_details(self, query_details : QueryResponse) -> str:
        """Parse customer data to Pydantic,
            Extracts requested customer data from JSON dataset,
            Formats output to a readable string"""
        customer_data = parse_json_to_pydantic(self.customer_file_path)
        customer_order_details = customer_data.customer_orders

        matched_details = {}
        matched_order = None
        
        # Find the matching order first
        for orders in customer_order_details:
            if orders.order_id == query_details.order_id:
                matched_order = orders
                break 
        
        # If order found, extract requested details
        if matched_order:
            for detail in query_details.requested_detail:
                match detail:
                    case "order_id":
                        matched_details["Order ID"] = matched_order.order_id
                    case "order_date":
                        matched_details["Order date"] = matched_order.order_date
                    case "expected_delivery_date":
                        matched_details["Expected delivery date"] = matched_order.expected_delivery_date
                    case "customer_name":
                        matched_details["Customer"] = matched_order.customer_name
                    case "customer_email":
                        matched_details["Email"] = matched_order.customer_email
                    case "customer_phone":
                        matched_details["Phone"] = matched_order.customer_phone
                    case "shipping_address":
                        matched_details["Shipping address"] = matched_order.shipping_address
                    case "billing_address":
                        matched_details["Billing address"] = matched_order.billing_address
                    case "payment_method":
                        matched_details["Payment method"] = matched_order.payment_method
                    case "order_status":
                        matched_details["Order status"] = matched_order.order_status
                    case "tracking_number":
                        matched_details["Tracking number"] = matched_order.tracking_number 
        
        # Format the output
        if matched_details:
            formatted_output = f"Order Information for {query_details.order_id}:\n"
            for key, value in matched_details.items():
                formatted_output += f"- {key}: {value}\n"
            return formatted_output
        else:
            return "No matching order information found."

    def load_organization_details(self) -> str:
        """
        Load Organization Data from knowledge base (organization_data.txt)

        Returns: (str) Text Data from knowledge base
        """
        try:
            with open(self.org_file_path,"r") as file:
                return file.read()
        except Exception as e:
            print(f"Error loading organization data: {e}")
    



