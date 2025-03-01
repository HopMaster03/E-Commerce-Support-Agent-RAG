import chromadb
from chromadb.config import Settings
from embedding_service import EmbeddingService
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
        # Initialize ephemeral client (in-memory only)
        self.client = chromadb.Client(Settings(
            anonymized_telemetry=False
        ))
        
        # Create collection
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
        Add pre-generated embeddings to the collection if they haven't been added before.
        
        Args:
            embeddings: List of pre-generated embedding vectors.
            texts: List of text documents corresponding to the embeddings.
            metadatas: Optional metadata for each document.
            ids: Optional custom IDs for each document. Will generate UUIDs if not provided.
        """
        # Generate IDs if not provided
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in embeddings]
        
        # Check which IDs are not already in the collection
        existing_ids = set()
        try:
            existing = self.collection.get(ids=ids)
            existing_ids = set(existing['ids'])
        except:
            pass  # No existing IDs
        
        # Filter out already existing items
        new_indices = [i for i, id_val in enumerate(ids) if id_val not in existing_ids]
        
        if not new_indices:
            return  # Nothing new to add
        
        # Extract only the new items to add
        new_ids = [ids[i] for i in new_indices]
        new_embeddings = [embeddings[i] for i in new_indices]
        new_texts = [texts[i] for i in new_indices] if texts else None
        new_metadatas = [metadatas[i] for i in new_indices] if metadatas else None
        
        # Add new embeddings to the collection
        self.collection.add(
            embeddings=new_embeddings,
            documents=new_texts,
            metadatas=new_metadatas,
            ids=new_ids
        )
        return new_ids

    
    