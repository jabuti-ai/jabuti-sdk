import os
import requests
import json

class JabutiSDK():
    def __init__(self, api_url='', api_key=''):
        self.api_url = api_url if api_url else os.getenv("JBT_SDK_API_URL")
        self.api_key = api_key if api_key else os.getenv("JBT_SDK_API_KEY")
    
    def list_contexts(self):
        try:
            headers = {'x-api-key': self.api_key}
            response = requests.get(f"{self.api_url}/contexts", headers=headers, timeout=15)
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def create_update_context(self, context_name, filename):
        try:
            headers = {'x-api-key': self.api_key}
            payload = {'context_name': context_name}
            files=[
                ('file',(filename, open('teste_data.pdf','rb'), 'application/pdf'))
            ]
            response = requests.post(f"{self.api_url}/contexts", headers=headers, data=payload, files=files, timeout=60)
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def delete_context(self, context_name):
        try:
            headers = {'x-api-key': self.api_key}
            payload = {'context_name': context_name}
            response = requests.delete(f"{self.api_url}/contexts", headers=headers, data=payload, timeout=15)
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def fast_chat(self, input, callbacks=[]):
        try:
            headers = {'x-api-key': self.api_key}
            response = requests.post(self.api_url, data=json.dumps({"input": f"{str(input)}"}), headers=headers, timeout=60)
            if callbacks:
                for cb in callbacks:
                    cb.on_llm_new_token(token=response.text)
            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return None