import google.generativeai as genai
from google.generativeai.types import safety_types
import os

key_path = "/Users/daleyfraser/Documents/cs/steelhacks/gemini/geminitracksteelhacks-b4ddf1bcc62d.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

safe = {
    'HARM_CATEGORY_HARASSMENT':'block_none',
    'HARM_CATEGORY_HATE_SPEECH':'block_none',
    'HARM_CATEGORY_SEXUALLY_EXPLICIT':'block_none',
    'HARM_CATEGORY_DANGEROUS_CONTENT':'block_none',
}

generation_config = genai.types.GenerationConfig(
    temperature=1.5,
)
# Initialize the GenerativeModel with these safety settings
model = genai.GenerativeModel(
    model_name='models/gemini-1.5-flash-latest',
    safety_settings=safe,
    generation_config=generation_config,
)

def generate_text(prompt: str) -> str:
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    text = ""
    for part in response.parts:
        text += part.text
    return str(text)

# generate_text('make a cookie')