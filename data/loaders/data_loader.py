import json
from pathlib import Path


class DataLoader:
    def __init__(self, 
                 customer_file_path: str = "data/knowledge_base/customer_data.json", 
                 org_file_path: str="data/knowledge_base/organization_data.txt"):
        self.customer_file_path = customer_file_path
        self.org_file_path = org_file_path
        
    ### TODO: Update this function such that it extracts data from JSON of customer data to our own pydantic model 
    # def load_customer_data(self) -> CustomerData:
    #     """
    #     Load customer data from JSON file and convert to Pydantic model
        
    #     Returns:
    #         CustomerData: Parsed customer data
    #     """
    #     try:
    #         with open(self.customer_file_path, 'r', encoding='utf-8') as file:
    #             data = json.load(file)
    #             return CustomerData.parse_obj(data)
    #     except Exception as e:
    #         print(f"Error loading customer data: {e}")
    #         # Return minimal valid data
    #         return CustomerData(
    #             organization_details=OrganizationDetails(
    #                 name="Default Organization",
    #                 description="Default description"
    #             )
    #         )
    
    
    ### TODO: Done
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
    
    # def load_products(self) -> list[ProductData]:
    #     """Extract just the products from the customer data"""
    #     customer_data = self.load_customer_data()
    #     return customer_data.products or []
    
    # def load_faq(self) -> dict:
    #     """Extract just the FAQ from the customer data"""
    #     customer_data = self.load_customer_data()
    #     return customer_data.faq or {}
    
    # def load_knowledge_base(self) -> dict:
    #     """Extract just the knowledge base from the customer data"""
    #     customer_data = self.load_customer_data()
    #     return customer_data.knowledge_base or {}


