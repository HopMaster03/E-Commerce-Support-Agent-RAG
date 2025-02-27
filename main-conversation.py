import chainlit as cl
import os
from dotenv import load_dotenv

from agent.support_agent import CustomerSupportAgent
from data.loaders.data_loader import DataLoader, prepare_organization_texts
from data.processors.text_processor import TextProcessor
from embeddings.embedding_service import EmbeddingService
from embeddings.vector_store import ChromaVectorStore

# Load environment variables
load_dotenv()

# Initialize components
text_processor = TextProcessor()
embedding_service = EmbeddingService()
vector_store = ChromaVectorStore()
data_loader = DataLoader()

@cl.on_chat_start
async def start():
    """Initialize chat and load data when a new chat session starts"""
    # Send initial loading message
    loading_msg = cl.Message(content="Initializing the customer support agent...")
    await loading_msg.send()
    
    # Create a new instance of the support agent for this session
    support_agent = CustomerSupportAgent()
    
    # Load organization details
    org_details = data_loader.load_organization_details()
    
    # Prepare texts for embedding
    org_texts = prepare_organization_texts(org_details)
    
    # Process and chunk the texts
    all_chunks = []
    all_metadatas = []
    
    for item in org_texts:
        chunks = text_processor.chunk_text(item["text"], item["metadata"])
        for chunk in chunks:
            all_chunks.append(chunk["text"])
            all_metadatas.append(chunk["metadata"])
    
    # Generate embeddings
    if all_chunks:
        embeddings = embedding_service.generate_embeddings(all_chunks)
        
        # Store in vector database
        vector_store.add_texts("knowledge_base", all_chunks, embeddings, all_metadatas)
        
        # Update loading message
        await loading_msg.update(content=f"Data loaded and indexed: {len(all_chunks)} chunks from organization details")
    else:
        await loading_msg.update(content="No organization data found to index")
    
    # Send welcome message
    welcome = support_agent.welcome_message()
    await cl.Message(content=welcome).send()
    
    # Store agent in session for later use
    cl.user_session.set("agent", support_agent)

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages"""
    # Get query from the message
    query = message.content
    
    # Get the agent from the session
    agent = cl.user_session.get("agent")
    
    # Process the query and get a response
    response = agent.process_query(query)
    
    # Send the response
    await cl.Message(
        content=response["answer"],
        elements=[
            cl.Text(name="Source", content=f"Source: {response['source']}", display="inline")
        ]
    ).send()


# Enable chat history persistence with Chainlit
@cl.on_chat_resume
async def on_chat_resume(state):
    """Restore the agent instance when a chat is resumed"""
    # Create a new agent instance with cleared history
    support_agent = CustomerSupportAgent()
    
    # Reconstruct conversation history from Chainlit messages
    for message in state.get("messages", []):
        if message["role"] == "user":
            support_agent.conversation_history.add_message("user", message["content"])
        elif message["role"] == "assistant":
            support_agent.conversation_history.add_message("assistant", message["content"])
    
    # Store the agent in the session
    cl.user_session.set("agent", support_agent)


if __name__ == "__main__":
    # Ensure required directories exist
    os.makedirs("data/knowledge_base", exist_ok=True)
    
    # Chainlit will handle the web server
    # The app will be run with: chainlit run app.py





