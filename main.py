from fastapi import FastAPI
from sentimentanalysis import sent_analysis

emotions = ["positive", "negative", "neutral"]

app = FastAPI(debug=True)

@app.get("/classify_emotions")
async def classify_emotions(prompt: str):
    response = sent_analysis(prompt_user=prompt, emotions=emotions )
    return response
    

#uvicorn main:app --reload #To run fastApi service
