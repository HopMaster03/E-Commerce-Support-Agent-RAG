import json
from pathlib import Path
from models.schema import CustomerData, OrganizationDetails, ProductData


class DataLoader:
    def __init__(self, data_file_path: str = "data/knowledge_base/customer_data.json"):
        self.data_file_path = data_file_path
        
    def load_customer_data(self) -> CustomerData:
        """
        Load customer data from JSON file and convert to Pydantic model
        
        Returns:
            CustomerData: Parsed customer data
        """
        try:
            with open(self.data_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return CustomerData.parse_obj(data)
        except Exception as e:
            print(f"Error loading customer data: {e}")
            # Return minimal valid data
            return CustomerData(
                organization_details=OrganizationDetails(
                    name="Default Organization",
                    description="Default description"
                )
            )
    
    def load_organization_details(self) -> OrganizationDetails:
        """Extract just the organization details from the customer data"""
        customer_data = self.load_customer_data()
        return customer_data.organization_details
    
    def load_products(self) -> list[ProductData]:
        """Extract just the products from the customer data"""
        customer_data = self.load_customer_data()
        return customer_data.products or []
    
    def load_faq(self) -> dict:
        """Extract just the FAQ from the customer data"""
        customer_data = self.load_customer_data()
        return customer_data.faq or {}
    
    def load_knowledge_base(self) -> dict:
        """Extract just the knowledge base from the customer data"""
        customer_data = self.load_customer_data()
        return customer_data.knowledge_base or {}


def prepare_organization_texts(org_details: OrganizationDetails) -> list[dict]:
    """
    Convert organization details into chunks for embedding
    
    Args:
        org_details: OrganizationDetails object
        
    Returns:
        list: List of dicts with text and metadata
    """
    texts = []
    
    # Add basic info
    basic_info = f"Organization Name: {org_details.name}\nDescription: {org_details.description}"
    if org_details.website:
        basic_info += f"\nWebsite: {org_details.website}"
    if org_details.support_email:
        basic_info += f"\nSupport Email: {org_details.support_email}"
    if org_details.support_phone:
        basic_info += f"\nSupport Phone: {org_details.support_phone}"
    if org_details.business_hours:
        basic_info += f"\nBusiness Hours: {org_details.business_hours}"
    
    texts.append({
        "text": basic_info,
        "metadata": {
            "source": "organization_details",
            "type": "basic_info"
        }
    })
    
    # Add policies if available
    if org_details.policies:
        for policy_name, policy_text in org_details.policies.items():
            texts.append({
                "text": f"Policy: {policy_name}\n\n{policy_text}",
                "metadata": {
                    "source": "organization_details",
                    "type": "policy",
                    "policy_name": policy_name
                }
            })
    
    return texts