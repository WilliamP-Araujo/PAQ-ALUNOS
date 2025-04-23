from dto import studentInsertDto
from dao.StudentsDao import alunos
import uuid


def studentInsert(studentInsertDTO :studentInsertDto.StudentInsertDTO): 
    new_aluno = {"id": uuid.uuid4(), "name": studentInsertDTO.name, "apelido": studentInsertDTO.apelido,"active": True}
    alunos.append(new_aluno)
    