from dao.StudentsDao import alunos


def removeStudent(id):
    for aluno in alunos:
        if ['id'] == id:
            aluno.remove(id)
           