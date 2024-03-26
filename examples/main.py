from jbtsdk import JabutiSDK

jsdk = JabutiSDK(api_url='https://api.tecban.jabuti.ai', api_key='wMlVr9oAKk4c5ShYShOGt9g1pOytpSSn8duYzz9A')
print(jsdk.invoke('Quem é o atual presidente Brasil ?'))