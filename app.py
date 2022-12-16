# Cria um arquivo pronto para escrita

nome_arquivo = 'agenda.txt'
minha_agenda = open(nome_arquivo, 'w')
print(f'Arquivo {nome_arquivo} criado com sucesso!')
minha_agenda.close()

#