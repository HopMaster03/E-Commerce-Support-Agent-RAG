import litellm
from config.settings import OPENAI_API_KEY, EMBEDDING_MODEL,BATCH_SIZE

class EmbeddingService:
    def __init__(self):
        litellm.api_key = OPENAI_API_KEY
        self.model = EMBEDDING_MODEL
    
    def generate_embeddings(self, texts: list):
        """
        Generate embeddings for a list of texts
        Args:
            texts (list): List of text strings   
        Returns:
            list: List of embedding vectors
        """
        if not texts:
            return []

        embeddings = []
        batch_size = BATCH_SIZE 
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            try:
                responses = litellm.embedding(
                    model=self.model,
                    input=batch
                )
                batch_embeddings = [resp["embedding"] for resp in responses["data"]]
                embeddings.extend(batch_embeddings)
            except Exception as e:
                print(f"Error generating embeddings: {e}")
                
        return embeddings
    
    def get_query_embedding(self, query : str):
        """Generate embedding for a single text
        Args:
            query: str: User query
        Returns:
            returns query Embeddings
        """
        if not query:
            return None
            
        try:
            response = litellm.embedding(
                model=self.model,
                input=query
            )
            return response["data"][0]["embedding"]
        except Exception as e:
            print(f"Error generating single embedding: {e}")
            return None
    
    