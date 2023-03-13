import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Sua Conta Twilio aqui"
# Your Auth Token from twilio.com/console
auth_token  = "Seu token"

client = Client(account_sid, auth_token)

tabela_alunos=pd.read_excel("notas.xlsx")

tabela_alunos["media"] = tabela_alunos["Nota 1"] + tabela_alunos["Nota 2"] + tabela_alunos["Nota 3"] + tabela_alunos["Nota 4"]
tabela_alunos["media"] = tabela_alunos["media"]/4

if (tabela_alunos["media"] < 6).any():
        aluno = tabela_alunos.loc[tabela_alunos["media"] < 6, "Alunos"].values[0]
        nota = tabela_alunos.loc[tabela_alunos["media"] < 6, "media"].values[0]

message = client.messages.create(
    to="seu numero",
    from_="numero twilio",
    body=f"o aluno {aluno} reprovou com {nota}")

print(message.sid)