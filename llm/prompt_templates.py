#Update required(update to instruct model to output the customer_data)
classifier_system_message = """
        Analyze the following customer support query and determine:
        1. needs_general_knowledge is True when the query's intent is to get the following details:
        - Organization Details
        - General Product details
        - Any FAQ
        - Company's background history
        2. needs_product_specific_knowledge is True when the query's intent is to get the following details:
        - Their Order details and Order status
        - Shipment Updates
        - Their Shipping address and Delivery Address
        - Order Tracking Number
        3.
        
        Respond with a JSON object in this exact format:
        {{
            "needs_general_knowledge": True/False,
            "needs_customer_data": True/False,
            "customer_identifiers": ["id1", "id2", ...] // List any order numbers, customer IDs, etc.
        }}
        """