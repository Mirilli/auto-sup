from g4f.client import Client as OpenAI
import testGmail as gmail

client = OpenAI()

completion = client.chat.completions.create(
  model="gemini",
  messages=[
    {"role": "system", "content": "Você é o assistente do João Mirilli e se chama Ailson. Seu papel é auxilia-lo respondendo seus emails. Você deve analisar a mensagem de email recebida e criar uma resposta coerente para esta mensagem. Deixe claro que você é um assistente virtual. no prompt enviarei o <nome> e a <mensagem> do email. Em sua resposta, não escreva nada além da resposta do email. Não inclua campos com variaveis ex:'[insira aqui...]' ou '&lt;insira aqui...&gt;' ou **insira aqui** ou **observação**. Se você não for capaz de responder a mensagem, responda 'Conteúdo não disponível'."},
    {"role": "user", "content": f'<nome>Julia</nome> <mensagem>TE AMO MEU AMOR JULIA ODONNELL 55 11 9 7544 1221 Em sáb., 23 de mar. de 2024 às 11:11, &lt;joao.mirilli@gmail.com&gt; escreveu: Te amo meu amor! ❤️ &lt;/br&gt; This is a test email sent via Gmail API.</mensagem>'}
  ]
)

# Tente acessar o conteúdo da mensagem assim
#message_content = completion.choices[0].message.content if hasattr(completion.choices[0].message, 'content') else "Conteúdo não disponível"
message_content = completion.choices[0].message.content

print(message_content)
