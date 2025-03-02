import chromadb
from chromadb.config import Settings
from rag.embedding_service import EmbeddingService
import uuid
from typing import List, Dict, Any, Optional

class ChromaVectorStore:
    """
    A wrapper class for ChromaDB to store pre-generated embeddings
    using an ephemeral client.
    """
    
    def __init__(
        self,
        collection_name: str = "kb_collection"
    ):
        """
        Initialize the ChromaVectorStore with an ephemeral client.
        Args:
            collection_name: Name of the collection to use/create.
        """
        
        self.client = chromadb.Client(Settings(
            anonymized_telemetry=False
        ))
        
        self.collection = self.client.create_collection(name=collection_name)
        self.embedding_service = EmbeddingService()
    
    def add_embeddings(
        self,
        embeddings: List[List[float]],
        texts: List[str] = None,
        metadatas: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None
    ) -> List[str]:
        """
        Add embeddings to the collection.
        
        Args:
            embeddings: List of pre-generated embedding vectors.
            texts: List of text documents corresponding to the embeddings.
            metadatas: Optional metadata for each document.
            ids: Optional custom IDs for each document. Will generate UUIDs if not provided.
        Returns
            new_ids: return to successfully show Embedding and Indexing
        """
        # Generate IDs if not provided
        if ids is None:
            new_ids = [str(uuid.uuid4()) for _ in embeddings]
         
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=new_ids
        )
        return new_ids

    
    