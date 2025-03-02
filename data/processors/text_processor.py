import re
import html
from typing import List, Dict

class TextProcessor:
    def __init__(self):
        pass
    
    def extract_org_chunks(self, content : str):
        """Extracts all Organization Details
        Args:
            content: str: contains the entire Organization text
        Returns:
            returns header wise split organization chunks
        """
        org_chunks = []
        org_section_match = re.search(r"## 1\. Organization Details([\s\S]*?)(?=---|\Z)", content, re.DOTALL)
        if org_section_match:
            org_section = org_section_match.group(1).strip()
            org_pattern = re.compile(r"### (.*?)\n([\s\S]*?)(?=### |\Z)", re.DOTALL)
            for title, content in org_pattern.findall(org_section):
                org_chunks.append({
                    "type": "OrgDetails",
                    "title": title.strip(),
                    "content": content.strip()
                })
        return org_chunks
    
    def extract_faq_chunks(self, content : str):
        """Extracts all FAQ Details
        Args:
            content: str: contains the entire Organization text
        Returns:
            returns Question and Answer wise split chunks
        """
        faq_section_match = re.search(r"## FAQ_START ##\s*([\s\S]*?)\s*## FAQ_END ##", content, re.DOTALL)
        faq_chunks = []
        if faq_section_match:
            faq_section = faq_section_match.group(1).strip()
            faq_pattern = re.compile(r"FAQ_QUESTION: (.*?)\nFAQ_ANSWER: (.*?)(?=\n\nFAQ_QUESTION:|\n\n## FAQ_END ##|\Z)", re.DOTALL)
            
            for question, answer in faq_pattern.findall(faq_section):
                faq_chunks.append({
                    "type": "FAQ",
                    "question": question.strip(),
                    "content": answer.strip()
                })
        return faq_chunks
    
    def embedding_preparation(self, 
                              org_chunks : list,
                              faq_chunks : list):
        """Generate Documents, raw_texts and Metadata for embedding
        Args:
            org_chunks: str
            faq_chunks: str
        Returns:
            texts: Used to create embeddings
            documents_for_embeddings: Used as reference for documents
            metadata_for_embeddings: Used as metadata
            
        """
        texts = []
        documents_for_embedding = []
        metadata_for_embedding = []

        for item in org_chunks:
            combined_text = f"{item['title']} {item['content']}"
            texts.append(combined_text)
            documents_for_embedding.append(combined_text)
            metadata = {
                "title": item['title'],
                "source": "organization",
                "doc_type": "policy"
            }
            metadata_for_embedding.append(metadata)

        for item in faq_chunks:
            combined_text = f"{item['question']} {item['content']}"
            texts.append(combined_text)
            documents_for_embedding.append(combined_text)
            metadata = {
                "title": item['question'],
                "source": "faq",
                "doc_type": "question"
            }
            metadata_for_embedding.append(metadata)
        return texts, documents_for_embedding, metadata_for_embedding

    def clean_context(self,results):
        """Structures the context to improve readability
        Args:
            results: contain results from a query search
        Returns:
            returns clean context"""
        context = ""
        for item in range(0,len(results['documents'][0]),1):
                context += f"{item+1}. "+ results['documents'][0][item]+ "\n" 
        return context


    
    
    