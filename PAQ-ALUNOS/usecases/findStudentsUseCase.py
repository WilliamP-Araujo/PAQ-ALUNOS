from dao.StudentsDao import alunos


def findStudent(nome):
    for aluno in alunos:
        if aluno["name"].lower() == nome.lower():
            return aluno
    return None