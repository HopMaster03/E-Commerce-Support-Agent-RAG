import chainlit as cl
import os
from dotenv import load_dotenv
from agent.support_agent import CustomerSupportAgent
load_dotenv()

support_agent = CustomerSupportAgent()

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="What's my order status?",
            message="I cannot find where my order is right now, can you provide the status of the order for the Order ID A123456791?",
            icon="images/tim-cook.jpg",
            ),

        cl.Starter(
            label="Product Return Policy",
            message="What is Apple's return policy?",
            icon="images/apple-14.svg",
            ),
        cl.Starter(
            label="Reach out to Apple",
            message="Does apple have an email so that I can get in touch with the support team?",
            icon="images/apple-14.svg",
            ),
        cl.Starter(
            label="Payment Clarification",
            message="I'm not sure if made the payment through credit card or debit card for my order ID A123456789. could you check and confirm it for me?",
            icon="images/apple-14.svg",
            ),
        cl.Starter(
            label="Shipping Details",
            message="I need to know the shipping and delivery address for my order ID A123456789. can you help me?",
            icon="images/apple-14.svg",
            )
        ]
@cl.on_chat_start
async def start():
    support_agent.create_agent_knowledge()
    

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






