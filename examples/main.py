from jbtsdk import JabutiSDK

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print("dotenv not found")
    
jsdk = JabutiSDK()

# print(jsdk.fast_chat('Do que se trata o documento ?', 'context_name'))

print(jsdk.list_contexts())