from jbtsdk import JabutiSDK

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print("dotenv not found")
    
jsdk = JabutiSDK()

#Listar contextos existentes
print(jsdk.list_contexts())

# Criar ou atualizar contextos
# jsdk.create_update_context("teste3", "teste_data.pdf")

#Interagir com um contexto
# print(jsdk.fast_chat('Do que se trata o documento ?', 'teste3'))

# Deletar contexto
jsdk.delete_context("teste3")