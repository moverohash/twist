from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import re

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>FastAPI Email Receiver</title>
      <link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.0/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100 flex flex-col items-center justify-center h-screen">
      <h1 class="text-3xl font-bold mb-4">📩 Instagram Code Receiver</h1>
      <div class="bg-white shadow p-4 rounded w-96 text-center">
        Your FastAPI app is working on Render 🚀
      </div>
    </body>
    </html>
    """

@app.post("/incoming")
async def incoming_email(request: Request):
    data = await request.json()
    body = data.get("body", "")
    match = re.search(r"\b\d{6}\b", body)
    if match:
        code = match.group(0)
        print("📨 Instagram code:", code)
    return {"status": "ok"}
