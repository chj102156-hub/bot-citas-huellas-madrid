
import os
import json
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = json.dumps({
        "chat_id": CHAT_ID,
        "text": mensaje
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=datos,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as respuesta:
        print(respuesta.read().decode("utf-8"))

if __name__ == "__main__":
    enviar_mensaje("🤖 ¡Bot de Citas Huellas Madrid conectado!")
