from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
key_token = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=key_token)

def sent_analysis(prompt_user:str, emotions: list):
    #Promoting for sentiment analysis
    prompt_system = f'''
    Your task is to analyse and report the overall sentiment
        of ONLY one out of the following emotions: {emotions}. Please RESPOND WITH THE EMOTION ONLY.
    '''
    #prompt_user =  "Hi how are you ?"
    #prompt_user ="They are so understanding, explain everything, never speak fast so you don't understand! Wish everyone was like them."
    #prompt_user ="This company is a scam. They stole my money during the return process"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        #response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content":  prompt_system},
            {"role": "user", "content": prompt_user}
        ],
        temperature=0,
        max_tokens=100,
    )
    return response.choices[0].message.content
