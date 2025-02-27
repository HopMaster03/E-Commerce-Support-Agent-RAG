import litellm
from config.settings import OPENAI_API_KEY, EMBEDDING_MODEL

class EmbeddingService:
    def __init__(self):
        litellm.api_key = OPENAI_API_KEY
        self.model = EMBEDDING_MODEL
    
    def generate_embeddings(self, texts):
        """
        Generate embeddings for a list of texts
        
        Args:
            texts (list): List of text strings
            
        Returns:
            list: List of embedding vectors
        """
        if not texts:
            return []
            
        # Handle batching for efficiency
        embeddings = []
        batch_size = 20  # Adjust based on API limits
        
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
                # Add appropriate error handling
        
        return embeddings
    
    def get_single_embedding(self, text):
        """Generate embedding for a single text"""
        if not text:
            return None
            
        try:
            response = litellm.embedding(
                model=self.model,
                input=[text]
            )
            return response["data"][0]["embedding"]
        except Exception as e:
            print(f"Error generating single embedding: {e}")
            return None