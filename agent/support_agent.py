from rag.retriever import RAGRetriever
from llm.litellm_service import LiteLLMService
from llm.prompt_templates import PromptTemplates
from data.processors.text_processor import TextProcessor
from typing import List, Dict, Any

class ConversationHistory:
    def __init__(self, max_history: int = 10):
        self.messages: List[Dict[str, Any]] = []
        self.max_history = max_history
    
    def add_message(self, role: str, content: str):
        """Add a message to the conversation history"""
        self.messages.append({
            "role": role,
            "content": content
        })
        
        # Trim history if it exceeds max length
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]
    
    def get_history(self) -> List[Dict[str, Any]]:
        """Get the conversation history"""
        return self.messages
    
    def get_formatted_history(self) -> str:
        """Get the conversation history as a formatted string"""
        formatted = ""
        for msg in self.messages:
            role = "Customer" if msg["role"] == "user" else "Agent"
            formatted += f"{role}: {msg['content']}\n\n"
        return formatted
    
    def clear(self):
        """Clear the conversation history"""
        self.messages = []


class CustomerSupportAgent:
    def __init__(self):
        self.retriever = RAGRetriever()
        self.llm_service = LiteLLMService()
        self.prompt_templates = PromptTemplates()
        self.text_processor = TextProcessor()
        self.conversation_history = ConversationHistory()
    
    def process_query(self, query, product_data=None):
        """
        Process a customer query and generate a response
        
        Args:
            query (str): Customer query
            product_data (dict, optional): Product data for product-specific queries
            
        Returns:
            dict: Response with answer and metadata
        """
        # Clean the query
        query = self.text_processor.clean_text(query)
        
        # Add user query to conversation history
        self.conversation_history.add_message("user", query)
        
        # Check if RAG is needed
        needs_rag = self.retriever.needs_rag(query)
        
        if needs_rag:
            # Retrieve relevant documents
            context_docs = self.retriever.retrieve(query)
            
            if not context_docs:
                # Fallback to product data if available
                if product_data:
                    prompt = self.prompt_templates.product_prompt(query, product_data, self.conversation_history.get_formatted_history())
                    source = "product_data"
                else:
                    # No context found, use general response with conversation history
                    chat_history = self.conversation_history.get_formatted_history()
                    prompt = f"""
As a customer support agent, please answer this question based on the conversation history:

CONVERSATION HISTORY:
{chat_history}

CUSTOMER'S LATEST QUESTION:
{query}
"""
                    source = "general_knowledge"
            else:
                # Use RAG prompt with retrieved context and conversation history
                prompt = self.prompt_templates.rag_prompt(query, context_docs, self.conversation_history.get_formatted_history())
                source = "knowledge_base"
        else:
            # Use product data if available
            if product_data:
                prompt = self.prompt_templates.product_prompt(query, product_data, self.conversation_history.get_formatted_history())
                source = "product_data"
            else:
                # Fallback to RAG if no product data
                context_docs = self.retriever.retrieve(query)
                prompt = self.prompt_templates.rag_prompt(query, context_docs, self.conversation_history.get_formatted_history())
                source = "knowledge_base"
        
        # Generate response
        system_message = self.prompt_templates.system_message()
        answer = self.llm_service.generate_response(prompt, system_message)
        
        # Add agent response to conversation history
        self.conversation_history.add_message("assistant", answer)
        
        return {
            "answer": answer,
            "source": source,
            "rag_used": needs_rag
        }
    
    def welcome_message(self):
        """Generate a welcome message for the chatbot"""
        prompt = "Generate a brief welcome message for a customer contacting e-commerce support."
        system_message = "You are a friendly customer support agent for an e-commerce store."
        
        welcome_message = self.llm_service.generate_response(prompt, system_message)
        
        # Add welcome message to conversation history
        self.conversation_history.add_message("assistant", welcome_message)
        
        return welcome_message