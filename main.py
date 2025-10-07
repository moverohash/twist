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
    form = await request.form()
    
    sender = form.get("sender")
    recipient = form.get("recipient")
    subject = form.get("subject")
    body_plain = form.get("body-plain")

    print(f"📬 E-mail recebido de: {sender}")
    print(f"📨 Enviado para: {recipient}")
    print(f"📛 Assunto: {subject}")
    print("💬 Corpo:", body_plain)

    # Procurar código de 6 dígitos (ex: código do Instagram)
    code = None
    if body_plain:
        match = re.search(r"\b\d{6}\b", body_plain)
        if match:
            code = match.group(0)
            print(f"✅ Código detectado: {code}")

    return JSONResponse({
        "status": "ok",
        "sender": sender,
        "recipient": recipient,
        "code": code
    })
