import chainlit as cl
import os
from dotenv import load_dotenv

from agent.support_agent import CustomerSupportAgent


# Load environment variables
load_dotenv()

# Initialize components

support_agent = CustomerSupportAgent()

@cl.on_chat_start
async def start():
    """Initialize chat and load data when a new chat session starts"""
    # Send initial loading message
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
    """Handle incoming messages"""
    # Get query from the message
    query = message.content

    ###======================
    ### TODO: Process the query and generate a response
    ###======================
    response = support_agent.process_query(query)
    
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






