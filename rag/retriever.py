from embeddings.embedding_service import EmbeddingService
from embeddings.vector_store import ChromaVectorStore
from config.settings import TOP_K_RESULTS, SIMILARITY_THRESHOLD

class RAGRetriever:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaVectorStore()
    
    def needs_rag(self, query: str) -> bool:
        """
        Determine if a query needs RAG-based knowledge retrieval
        
        Args:
            query (str): Customer query
            
        Returns:
            bool: True if RAG is needed, False otherwise
        """
        # Simple keyword-based detection (can be enhanced with ML classification)
        product_keywords = ['product', 'item', 'buy', 'purchase', 'price', 'cost', 'how much']
        policy_keywords = ['policy', 'return', 'shipping', 'delivery', 'warranty', 'refund']
        
        query_lower = query.lower()
        
        # Check if query is primarily about products
        if any(keyword in query_lower for keyword in product_keywords):
            return False
        
        # Check if query is about policies or other knowledge
        if any(keyword in query_lower for keyword in policy_keywords):
            return True
            
        # Default to using RAG when uncertain
        return True
    
    def retrieve(self, query: str, use_product_data=False) -> list:
        """
        Retrieve relevant context for a query
        
        Args:
            query (str): Customer query
            use_product_data (bool): Whether to search product data
            
        Returns:
            list: Retrieved documents
        """
        # Generate embedding for query
        query_embedding = self.embedding_service.get_single_embedding(query)
        if not query_embedding:
            return []
        
        # Determine which collection to search
        collection = "product_data" if use_product_data else "knowledge_base"
        
        # Retrieve similar documents
        results = self.vector_store.query(
            collection_name=collection,
            query_embedding=query_embedding,
            top_k=TOP_K_RESULTS
        )
        
        # Filter by similarity threshold
        filtered_results = []
        for i, distance in enumerate(results["distances"]):
            # Convert distance to similarity score (1 - distance for cosine distance)
            similarity = 1 - distance
            if similarity >= SIMILARITY_THRESHOLD:
                doc = {
                    "text": results["documents"][i],
                    "similarity": similarity
                }
                if results["metadatas"] and results["metadatas"][i]:
                    doc["metadata"] = results["metadatas"][i]
                filtered_results.append(doc)
        
        return filtered_results