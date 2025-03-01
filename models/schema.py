from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Literal

# Update needed(re-check the schema for CustomerOrders)
class Product(BaseModel):
    product_name: str
    
class Order(BaseModel):
    order_id: str
    expected_delivery_date: str
    products: List[Product]

class CustomerOrders(BaseModel):
    customer_orders: List[Order]

class QueryClassification(BaseModel):
    needs_general_knowledge: bool = True
    needs_product_specific_knowledge: bool = False
    customer_product_data: CustomerOrders 