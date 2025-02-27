import re
import html
from typing import List, Dict

class TextProcessor:
    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Decode HTML entities
        text = html.unescape(text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove URLs for cleaner text
        text = re.sub(r'https?://\S+', '', text)
        
        return text
    
    def chunk_text(self, text: str, metadata: Dict = None) -> List[Dict]:
        """
        Split text into overlapping chunks
        
        Args:
            text (str): Text to split into chunks
            metadata (dict, optional): Metadata to attach to each chunk
            
        Returns:
            list: List of dicts with text chunks and metadata
        """
        if not text:
            return []
            
        text = self.clean_text(text)
        
        # Split text by sentences to avoid cutting in the middle of sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current_chunk = []
        current_size = 0
        
        for sentence in sentences:
            sentence_size = len(sentence)
            
            if current_size + sentence_size > self.chunk_size and current_chunk:
                # Current chunk is full, save it
                chunk_text = ' '.join(current_chunk)
                chunks.append({
                    "text": chunk_text,
                    "metadata": metadata.copy() if metadata else {}
                })
                
                # Start new chunk with overlap
                overlap_size = 0
                overlap_chunk = []
                
                # Add sentences from the end of the previous chunk for overlap
                for prev_sentence in reversed(current_chunk):
                    if overlap_size + len(prev_sentence) <= self.chunk_overlap:
                        overlap_chunk.insert(0, prev_sentence)
                        overlap_size += len(prev_sentence) + 1  # +1 for space
                    else:
                        break
                
                current_chunk = overlap_chunk
                current_size = overlap_size
            
            # Add the current sentence to the chunk
            current_chunk.append(sentence)
            current_size += sentence_size + 1  # +1 for space
        
        # Add the last chunk if not empty
        if current_chunk:
            chunk_text = ' '.join(current_chunk)
            chunks.append({
                "text": chunk_text,
                "metadata": metadata.copy() if metadata else {}
            })
        
        return chunks