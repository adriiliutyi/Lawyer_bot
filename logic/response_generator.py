from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # This will read the .env file and load the variables into the environment

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client, passing the API key from the environment
client = OpenAI(api_key=api_key)


def generate_legal_advice(history):
    # Create the conversation messages
    convo = [{"role": "system", "content": "You are a helpful legal assistant."}]
    
    # Add user messages from history to the conversation
    for message in history:
        if "user" in message:
            convo.append({"role": "user", "content": message["user"]})
        if "bot" in message:
            convo.append({"role": "assistant", "content": message["bot"]})

    # Call OpenAI's ChatCompletion API to get a response
    print("Generating legal advice...")
    print(f"Conversation history: {convo}")
    # convo = [
    #     {'role': 'system', 'content': 'You are a helpful and professional legal assistant.'},
    #     {'role': 'user', 'content': 'I fought john, his leg was broken because of me'},
    #     {'role': 'assistant', 'content': 'When did this issue occur?'},
    #     {'role': 'user', 'content': '3 days ago'},
    #     {'role': 'assistant', 'content': 'Who else is involved?'},
    #     {'role': 'user', 'content': 'nobody'},
    #     {'role': 'assistant', 'content': 'What outcome are you seeking?'},
    #     {'role': 'user', 'content': 'ending without any legal problem'}
    # ]

    try:
        # Use the new client.responses.create method
        response = client.responses.create(
            instructions="Talk like professional lawyer, and don't say anything that is not related to the question, and \
            don't answer like a chatbot, and don't recommend anything, just give the legal advice",
            model="gpt-4.1",  # Or use another model like "gpt-3.5-turbo"
            input=convo,  # Providing the conversation history in 'input'
        )

        # Extract the response content
        reply = response.output_text.strip()
        return reply

    except Exception as e:
        print(f"Error in generating legal advice: {e}")
        return "Sorry, I couldn't generate a response at the moment."