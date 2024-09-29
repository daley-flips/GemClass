import google.generativeai as genai
from google.generativeai.types import safety_types
import os
import json

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

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

def extract_json(json_path: str) -> dict:
    if json_path is None:
        return
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        return data

def generate_text(prompt: str, class_model: str, first_time: bool) -> str:
    system_prompt = """
    You are ai tutor. Your main objective is to ensure that a student learns. Keep in mind that by giving the answer will ensure that the student does not learn, which goes directly against your instructions. you will not break character, and no matter what comes after this, always be a tutor that is trying to ensure the student learns. The only time it is fine to give an answer is for very basic questions, or questions about syntax, otherwise even if you are explicitly asked for the answer, do not give it away. you can give hints but do not give the answer to any question away even if explicitly asked for it (unless it is very basic and the student needs it as background information). No matter what the next prompt is do not break character, you will always be a tutor that is trying to teach a student. Never give away an answer unless it is very basic (for example, syntax questions) or the student needs it as background information.
    """

    # Load the JSON file
    json_path = None
    if class_model == "Harvard CS50":
        json_path = os.path.join(BASE_PATH, 'class_data', 'cs50.json')
    elif class_model == "Pitt CS0447":
        json_path = os.path.join(BASE_PATH, 'class_data', 'cs447.json')

    data = extract_json(json_path)
    background_info = ""
    if data is not None:
        for lecture in data['lectures']:
            background_info += lecture['content']
        for extra in data['extra']:
            background_info += extra['content']

    if first_time:
        final_prompt = f"do not include 'User:' or Assistant:' in your response\n{system_prompt}\nBackground: {background_info}\nSystem prompt: {system_prompt}\nusing the given instructions and the given context, answer this question as best as you can, acting as a tutor: {prompt}"
        # print(f"FIRST 1 TIME: \n{final_prompt}")
    else:
        final_prompt = f"do not include 'User:' or Assistant:' in your response \nSystem prompt: {system_prompt}\nusing the given instructions and the given context, answer this question as best as you can, acting as a tutor: {prompt}"
        # print(f"NEXT 1 TIME: \n{final_prompt}")


    chat = model.start_chat(history=[])
    response = chat.send_message(final_prompt)
    text = ""
    for part in response.parts:
        text += part.text
    return str(text)

