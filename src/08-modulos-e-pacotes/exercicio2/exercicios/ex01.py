import uteis

aluno1 = uteis.Aluno.from_string('SP0101,João da Silva,joao@email.com')
aluno2 = uteis.Aluno('SP0102', 'João da Silva', 'joao@email.com')
print(aluno1)
print(aluno2)
