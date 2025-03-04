from llm.litellm_service import LiteLLMService
from data.loaders.data_loader import DataLoader
from data.processors.text_processor import TextProcessor
from rag.embedding_service import EmbeddingService
from rag.vector_store import ChromaVectorStore
from config.settings import TOP_K_RESULTS
from llm.prompt_templates import classifier_system_message, query_system_prompt, welcome_system_message, welcome_prompt
from agent.utils import parse_llm_intent

from typing import List, Dict, Any


class CustomerSupportAgent:
    def __init__(self):
        self.llm_service = LiteLLMService()
        self.text_processor = TextProcessor() 
        self.embedding_service = EmbeddingService() 
        self.vector_store = ChromaVectorStore() 
        self.data_loader = DataLoader() 
    
    def create_agent_knowledge(self):
        """Extract, Chunk, generate Embeddings & add to knowledge base
        Args:
            None
        Returns:
            ids: indexed chunks
        """

        org_details = self.data_loader.load_organization_details()
        
        org_chunks = self.text_processor.extract_org_chunks(org_details)
        faq_chunks = self.text_processor.extract_faq_chunks(org_details)
        embedding_text, document_text, metadata_text = self.text_processor.embedding_preparation(org_chunks,faq_chunks)

        embeddings = self.embedding_service.generate_embeddings(embedding_text)
        
        self.vector_store.add_embeddings(
            embeddings=embeddings,
            texts=document_text,
            metadatas=metadata_text
        )
       

    def process_query(self, query: str):
        """Classify query to adopt Adaptive RAG technique,
            Generates Contexts if RAG applies,
            Generates Customer Data if Order details apply
            
            Args:
                query: str : query received from user 
            Returns:
                query_response: str : Contains the LLM generated response
        """
        response = self.llm_service.generate_response(
            prompt=query, 
            system_message=classifier_system_message)
        
        classification = parse_llm_intent(response)
        cleaned_context = ""
        customer_data = ""
        if classification.needs_general_knowledge:
            embedded_query = self.embedding_service.get_query_embedding(query)
            context = self.vector_store.collection.query(query_embeddings=embedded_query, 
                                                         n_results=TOP_K_RESULTS)
            cleaned_context = self.text_processor.clean_context(context)

        if classification.needs_customer_data:
            customer_data = self.data_loader.load_customer_details(classification)

        formatted_system_message = query_system_prompt.format(
            context=cleaned_context,
            data=customer_data)
        
        query_response = self.llm_service.generate_response(prompt=query, 
                                                            system_message=formatted_system_message)
        return query_response


    def welcome_message(self):
        """Generate a welcome message for the chatbot"""
        welcome_message = self.llm_service.generate_response(welcome_prompt, welcome_system_message)
        
        return welcome_message
