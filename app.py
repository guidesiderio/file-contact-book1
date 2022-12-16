# Cria um arquivo pronto para escrita

nome_arquivo = 'agenda.txt'
minha_agenda = open(nome_arquivo, 'w')
print(f'Arquivo {nome_arquivo} criado com sucesso!')
minha_agenda.close()

# Cria 3 contatos com a estrutura (id_contato, nome_contato)
contato1 = ('1', 'Maria Joaquina de Amaral Pereira Goes')
contato2 = ('2', 'Carlos de Andrade')
contato3 = ('3', 'Antônio da Silva')

