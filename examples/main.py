from jbtsdk import JabutiSDK

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print("dotenv not found")
    
jsdk = JabutiSDK()

print(jsdk.invoke('Quais os valores da tecban ?', 'codigo_conduta_tecban'))