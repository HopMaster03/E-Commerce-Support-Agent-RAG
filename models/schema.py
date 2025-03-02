from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Literal

class Product(BaseModel):
    product_name: Optional[str] = Field(None, description="Optional product name")
    product_type: Optional[str] = Field(None, description="Optional product type")
    unit_price: Optional[float] = Field(None, description="Optional unit price")
    ordered_quantity: Optional[int] = Field(None, description="Optional ordered quantity")
    discount: Optional[float] = Field(None, description="Optional discount")

class OrderDetails(BaseModel):
    order_id: Optional[str] = Field(None, description="Optional order ID")
    order_date: Optional[str] = Field(None, description="Optional order date")
    expected_delivery_date: Optional[str] = Field(None, description="Optional expected delivery date")
    customer_name: Optional[str] = Field(None, description="Optional customer name")
    customer_email: Optional[str] = Field(None, description="Optional customer email")
    customer_phone: Optional[str] = Field(None, description="Optional customer phone")
    shipping_address: Optional[str] = Field(None, description="Optional shipping address")
    billing_address: Optional[str] = Field(None, description="Optional billing address")
    payment_method: Optional[str] = Field(None, description="Optional payment method")
    order_status: Optional[str] = Field(None, description="Optional order status")
    tracking_number: Optional[str] = Field(None, description="Optional tracking number")
    products: Optional[List[Product]] = Field(None, description="Optional product")

class CustomerDetails(BaseModel):
    customer_name: str 
    customer_email: str 
    customer_phone: str 
    shipping_address: str 
    billing_address: str 

class CustomerOrdersData(BaseModel):
    customer_orders: List[OrderDetails] 
    customer_details: CustomerDetails 

class QueryResponse(BaseModel):
    needs_general_knowledge: bool 
    needs_customer_data: bool 
    order_id: str = None
    requested_detail: List[str] = None
    order_details: OrderDetails = None