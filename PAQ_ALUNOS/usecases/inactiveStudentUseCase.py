from dao.StudentsDao import alunos

def inactiveStudents(id):
    for index, aluno in enumerate(alunos):
        if aluno['id'] == id:
            aluno['active'] = False
            break