from g4f.client import Client as OpenAI
import testGmail as gmail



def get_completion_from_messages(mensagem, nome):
  print('get_completion_from_messages')
  client = OpenAI()

  completion = client.chat.completions.create(
    model="openchat_3.5",
    messages=[
      {"role": "system", "content": "Você é o assistente do João Mirilli e se chama Ailson. Seu papel é auxilia-lo respondendo seus emails. Você deve analisar a mensagem de email recebida e criar uma resposta coerente para esta mensagem. Deixe claro que você é um assistente virtual. no prompt enviarei o <nome> e a <mensagem> do email. Em sua resposta, não escreva nada além da resposta do email. Não inclua campos com variaveis ex:'[insira aqui...]' ou '&lt;insira aqui...&gt;' ou **insira aqui** ou **observação**. Se você não for capaz de responder a mensagem, responda 'Conteúdo não disponível'. Você deve responder somente o texto como uma resposta de email."},
      {"role": "user", "content": f'<nome>{nome}</nome> <mensagem>{mensagem}</mensagem>'}
    ]
  )
  message_content = completion.choices[0].message.content

  print(message_content)
  return message_content

#message_content = completion.choices[0].message.content if hasattr(completion.choices[0].message, 'content') else "Conteúdo não disponível"

get_completion_from_messages('olá, poderia me sugerir algo para fazer em são paulo em maio? estarei lá po ruma semana.', 'Zéira')