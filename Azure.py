import os
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "https://guilh-m28xpur1-australiaeast.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4-32k")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_KEY")

# Inicializar o cliente OpenAI do Azure com autenticação baseada em chave
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

# Gerar a conclusão
completion = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": "Principais serviços do Azure para desenvolvedores de softwares"}],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())