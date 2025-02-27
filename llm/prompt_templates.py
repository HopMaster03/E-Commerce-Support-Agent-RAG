class PromptTemplates:
    @staticmethod
    def rag_prompt(query, context_docs, conversation_history=""):
        """
        Create a prompt with retrieved context for RAG-based answers
        
        Args:
            query (str): Customer query
            context_docs (list): Retrieved documents
            conversation_history (str): Formatted conversation history
            
        Returns:
            str: Formatted prompt
        """
        context = "\n\n".join([doc["text"] for doc in context_docs])
        
        history_section = ""
        if conversation_history:
            history_section = f"""
CONVERSATION HISTORY:
{conversation_history}
"""
        
        return f"""
You are a helpful e-commerce customer support agent. Answer the customer's question based on the provided context information and conversation history.

CONTEXT INFORMATION:
{context}
{history_section}
CUSTOMER QUESTION:
{query}

Provide a helpful, accurate, and concise response based on the context provided and the conversation history. If the context doesn't contain enough information to answer the question, admit that you don't have enough information rather than making up an answer.
"""

    @staticmethod
    def product_prompt(query, product_data, conversation_history=""):
        """
        Create a prompt with product data
        
        Args:
            query (str): Customer query
            product_data (dict): Product information
            conversation_history (str): Formatted conversation history
            
        Returns:
            str: Formatted prompt
        """
        product_info = "\n".join([f"{k}: {v}" for k, v in product_data.items()])
        
        history_section = ""
        if conversation_history:
            history_section = f"""
CONVERSATION HISTORY:
{conversation_history}
"""
        
        return f"""
You are a helpful e-commerce customer support agent. Answer the customer's question about our product based on the provided product information and conversation history.

PRODUCT INFORMATION:
{product_info}
{history_section}
CUSTOMER QUESTION:
{query}

Provide a helpful, accurate, and concise response based on the product information provided and the conversation history. If the product information doesn't contain enough details to answer the question, acknowledge this and suggest what additional information might be needed.
"""

    @staticmethod
    def system_message():
        """
        Create a system message for the customer support agent
        
        Returns:
            str: System message
        """
        return """
You are an AI customer support agent for an e-commerce store. Your goal is to help customers with their questions about products, orders, shipping, returns, and other store policies.

Follow these guidelines:
1. Be helpful, professional, and concise
2. Only share information that you are confident about based on the provided context
3. If you don't know the answer, acknowledge this and offer to escalate to a human agent
4. Don't make up information about products, policies, or procedures
5. When discussing products, include key details like price, availability, and features
6. Remember previous parts of the conversation when answering follow-up questions
7. Be consistent with information you've provided earlier in the conversation
"""