from dto import studentUpdateDto
from dao.StudentsDao import alunos

def updateStudent(id,studentDto:studentUpdateDto.StudentDTO):
    for aluno in alunos:
        if aluno['id'] == id:
            aluno["name"] = studentDto.name
            aluno["apelido"] = studentDto.apelido
            break