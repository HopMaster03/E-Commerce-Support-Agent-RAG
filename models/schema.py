from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any


class OrganizationDetails(BaseModel):
    """Organization information for the e-commerce store"""
    name: str
    description: str
    website: Optional[str] = None
    support_email: Optional[str] = None
    support_phone: Optional[str] = None
    business_hours: Optional[str] = None
    policies: Optional[Dict[str, str]] = None  # e.g., "return_policy", "shipping_policy"


class ProductData(BaseModel):
    """Product information"""
    id: str
    name: str
    description: str
    price: float
    category: str
    in_stock: bool = True
    variants: Optional[List[Dict[str, Any]]] = None
    specifications: Optional[Dict[str, Any]] = None
    

class CustomerData(BaseModel):
    """Main data model for storing all customer-specific data"""
    organization_details: OrganizationDetails
    products: Optional[List[ProductData]] = None
    faq: Optional[Dict[str, str]] = None  # Question -> Answer mapping
    knowledge_base: Optional[Dict[str, str]] = None  # Topic -> Content mapping
