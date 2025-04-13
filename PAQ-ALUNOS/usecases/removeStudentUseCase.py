from dao.StudentsDao import alunos


def removeStudent(nome):
    for aluno in alunos:
        if ['name'].lower() == nome.lower():
            aluno.remove(aluno)
            return f"Aluno '{nome}' removido com sucesso!"