import chromadb
from chromadb.config import Settings
import uuid
from config.settings import CHROMA_PERSIST_DIRECTORY

class ChromaVectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=CHROMA_PERSIST_DIRECTORY,
            settings=Settings(allow_reset=True)
        )
        # Create collections if they don't exist
        self.product_collection = self._get_or_create_collection("product_data")
        self.kb_collection = self._get_or_create_collection("knowledge_base")
    
    def _get_or_create_collection(self, name):
        try:
            return self.client.get_collection(name=name)
        except:
            return self.client.create_collection(name=name)
    
    def add_texts(self, collection_name, texts, embeddings, metadatas=None):
        """
        Add texts and their embeddings to the specified collection
        
        Args:
            collection_name (str): Name of the collection
            texts (list): List of text strings
            embeddings (list): List of embedding vectors
            metadatas (list, optional): List of metadata dicts
        """
        collection = self._get_or_create_collection(collection_name)
        
        # Generate IDs if not provided
        ids = [str(uuid.uuid4()) for _ in range(len(texts))]
        
        # Add data to collection
        collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas if metadatas else None,
            ids=ids
        )
        
        return ids
    
    def query(self, collection_name, query_embedding, top_k=5):
        """
        Query the vector store with an embedding
        
        Args:
            collection_name (str): Name of the collection to query
            query_embedding (list): Query embedding vector
            top_k (int): Number of results to return
            
        Returns:
            dict: Query results with documents, ids, and metadatas
        """
        collection = self._get_or_create_collection(collection_name)
        
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        return {
            "documents": results["documents"][0],
            "ids": results["ids"][0],
            "metadatas": results["metadatas"][0] if results["metadatas"] else None,
            "distances": results["distances"][0]
        }