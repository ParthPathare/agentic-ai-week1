import requests
 
RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
def call_llm(prompt: str) -> str:
    print("[LLM] Calling LLM with prompt:", prompt)
 
    try:
        response = requests.post(
            RENDER_API_URL,
            json={"prompt": prompt},
            timeout=10
        )
 
        if response.status_code != 200:
            print("[LLM] Non-200 response:", response.status_code)
            return "LLM_FAILED"
 
        try:
            data = response.json()
        except Exception:
            print("[LLM] Response not JSON:", response.text)
            return "LLM_FAILED"
 
        if "response" not in data:
            print("[LLM] Missing 'response' key")
            return "LLM_FAILED"
 
        print("[LLM] Response received successfully")
        return data["response"]
 
    except Exception as e:
        print("[LLM] Exception:", str(e))
        return "LLM_FAILED"