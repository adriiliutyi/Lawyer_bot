from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # This will read the .env file and load the variables into the environment

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client, passing the API key from the environment
client = OpenAI(api_key=api_key)


async def generate_legal_advice(history):
    convo = "\n".join([f"{'User' if 'user' in m else 'Bot'}: {list(m.values())[0]}" for m in history])
    prompt = convo + "\nBot: Based on all the above, here's my legal advice:"
    
    response = client.responses.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful legal assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
