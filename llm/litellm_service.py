import litellm
from config.settings import OPENAI_API_KEY, LLM_MODEL, MAX_TOKENS, TEMPERATURE

class LiteLLMService:
    def __init__(self):
        litellm.api_key = OPENAI_API_KEY
        
        self.model = LLM_MODEL
    
    def generate_response(self, prompt, system_message=None):
        """
        Generate a response from the LLM
        
        Args:
            prompt (str): User prompt
            system_message (str, optional): System message for context
            
        Returns:
            str: LLM response
        """
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
            
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = litellm.completion(
                model=self.model,
                messages=messages,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating LLM response: {e}")
            return "I'm sorry, I couldn't generate a response at this time."