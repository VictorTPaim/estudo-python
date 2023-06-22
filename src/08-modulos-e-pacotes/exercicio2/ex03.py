import uteis

aluno1 = uteis.Aluno('SP0101', 'João da Silva', 'joao@email.com')
projeto1 = uteis.Projeto(1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')
participacao = uteis.Participacao(1, '05/06', '14/11', aluno1, projeto1)
participacao2 = uteis.Participacao(2, '20/06', '20/12', aluno1, projeto1)
print(participacao)
print(participacao2)
