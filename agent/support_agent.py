# from rag.retriever import RAGRetriever
from llm.litellm_service import LiteLLMService
from data.loaders.data_loader import DataLoader
from data.processors.text_processor import TextProcessor
from embeddings.embedding_service import EmbeddingService
from embeddings.vector_store import ChromaVectorStore
from llm.prompt_templates import classifier_system_message
from agent.decision_engine import parse_llm_intent
from typing import List, Dict, Any


class CustomerSupportAgent:
    def __init__(self):
        self.llm_service = LiteLLMService()
        self.text_processor = TextProcessor() 
        self.embedding_service = EmbeddingService() 
        self.vector_store = ChromaVectorStore() 
        self.data_loader = DataLoader() 
    
    def create_agent_knowledge(self):

        org_details = self.data_loader.load_organization_details()
        
        # Chunking 
        org_chunks = self.text_processor.extract_org_chunks(org_details)
        faq_chunks = self.text_processor.extract_faq_chunks(org_details)
        embedding_text, document_text, metadata_text = self.text_processor.embedding_preparation(org_chunks,faq_chunks)

        embeddings = self.embedding_service.generate_embeddings(embedding_text)

        ids = self.vector_store.add_embeddings(
            embeddings=embeddings,
            texts=document_text,
            metadatas=metadata_text
        )
        return ids

    def process_query(self, query):
        #   TODO: - Update the response such that we get the product data to search too.
        response = self.llm_service.generate_response(prompt=query, system_message=classifier_system_message)
        classification = parse_llm_intent(response)
        if classification.needs_general_knowledge:
            embedded_query = self.embedding_service.get_query_embedding(query)
            context = self.vector_store.collection.query(query_embeddings=embedded_query, n_results=3)
            cleaned_context = self.text_processor.clean_context(context)

        if classification.needs_product_specific_knowledge:
            #   TODO: Perform retrieval of data from JSON
            print("Get customer Data")
        #   TODO: Use the retrieved context and generate another LLM response
        
    def welcome_message(self):
        """Generate a welcome message for the chatbot"""
        prompt = "Generate a brief welcome message for a customer contacting e-commerce support."
        system_message = "You are a friendly customer support agent for an e-commerce store."
        
        welcome_message = self.llm_service.generate_response(prompt, system_message)
        
        return welcome_message