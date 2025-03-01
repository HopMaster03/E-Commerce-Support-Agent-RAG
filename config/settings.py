import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Model Configuration
EMBEDDING_MODEL = "openai/text-embedding-ada-002"
LLM_MODEL = "gpt-3.5-turbo-16k"

# Retrieval Settings
TOP_K_RESULTS = 5
SIMILARITY_THRESHOLD = 0.75

# Agent Settings
MAX_TOKENS = 500
TEMPERATURE = 0.2