import uteis

aluno1 = uteis.Aluno('SP0101', 'João da Silva', 'joao@email.com')
aluno2 = uteis.Aluno('SP0102', 'Maria da Silva', 'maria@email.com')
projeto1 = uteis.Projeto(1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')
projeto2 = uteis.Projeto(2, 'Laboratório de Desenvolvimento de Software', 'João Augusto')
participacao = uteis.Participacao(1, '05/06', '14/11', aluno1, projeto2)
participacao2 = uteis.Participacao(2, '20/06', '20/12', aluno2, projeto2)
projeto1.add_participacao(participacao)
projeto1.add_participacao(participacao2)
print(projeto1)
projeto1.print_participacao()
