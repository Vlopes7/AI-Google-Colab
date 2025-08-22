import requests

OLLAMA_URL = "https://669e3e2459b3.ngrok-free.app/"

def chat_with_ollama(prompt, model='mistral'):
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                'model': model,
                'prompt': prompt,
                'stream': False  
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data['response']
    except Exception as e:
        return f"[ERRO] Falha ao conectar: {e}"

if __name__ == "__main__":
    prompt = input("Digite sua pergunta: ")
    resposta = chat_with_ollama(prompt)
    print("Resposta do modelo:", resposta)
