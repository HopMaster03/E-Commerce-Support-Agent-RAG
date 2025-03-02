import chainlit as cl
import os
from dotenv import load_dotenv
from agent.support_agent import CustomerSupportAgent
load_dotenv()

support_agent = CustomerSupportAgent()

@cl.on_chat_start
async def start():
    """Initialize chat & load data when a new chat session starts"""
    loading_msg = cl.Message(content="Initializing the customer support agent...")
    await loading_msg.send()
    ids = support_agent.create_agent_knowledge()

    # Update loading message
    loading_msg.content= f"Data loaded and indexed: {len(ids)} chunks from organization details"
    await loading_msg.update()

    # Send welcome message
    welcome = support_agent.welcome_message()
    await cl.Message(content=welcome).send()
    

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming queries
    Args: 
        message (cl.Message) : Incoming message from Chainlit
    Returns:
        cl.Message : LLM generated Response
    """
    query = message.content
    response = support_agent.process_query(query)

    await cl.Message(content=response).send()


if __name__ == "__main__":
    # Ensure required directories exist
    os.makedirs("data/knowledge_base", exist_ok=True)






