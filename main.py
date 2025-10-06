from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import re

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return open("templates/index.html").read()

@app.post("/incoming")
async def incoming_email(request: Request):
    data = await request.json()
    body = data.get("body", "")
    match = re.search(r"\b\d{6}\b", body)
    if match:
        code = match.group(0)
        print("Instagram code:", code)
    return {"status": "ok"}
