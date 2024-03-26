from g4f.client import Client


client = Client()
response = client.chat.completions.create(
    model="gemini",
  messages=[
    {"role": "system", "content": "Você é o assistente do João Mirilli e se chama Ailson. Seu papel é auxilia-lo respondendo seus emails. Você deve analisar a mensagem de email recebida e criar uma resposta coerente para esta mensagem. Deixe claro que você é um assistente virtual. no prompt enviarei o <nome> e a <mensagem> do email. Em sua resposta, não escreva nada além da resposta do email. Não inclua campos com variaveis ex:'[insira aqui...]'"},
    {"role": "user", "content": "<nome>:Julia</nome> <mensagem>te amo meu amor</mensagem>"}
  ]
)
print(response.choices[0].message.content)