import os
import requests
import json

class JabutiSDK():
    def __init__(self, api_url='', api_key=''):
        self.api_url = api_url if api_url else os.getenv("JBT_SDK_API_URL")
        self.api_key = api_key if api_key else os.getenv("JBT_SDK_API_KEY")
        
    def invoke(self, input, context, callbacks=[]):
        try:
            headers = {'x-api-key': self.api_key}
            response = requests.post(self.api_url, data=json.dumps({"input": f"{str(input)}", "context": f"{str(context)}"}), headers=headers)
            if callbacks:
                for cb in callbacks:
                    cb.on_llm_new_token(token=response.text)
            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return None