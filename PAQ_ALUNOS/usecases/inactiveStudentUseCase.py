from dao.StudentsDao import alunos

def inactiveStudents(id):
    for aluno in alunos:
        if ['id'] == id:
            aluno["active"] = False