from dao.StudentsDao import alunos

def removeStudent(id):
    for index, aluno in enumerate(alunos):
        if aluno['id'] == id:
            del alunos[index]
            break
           