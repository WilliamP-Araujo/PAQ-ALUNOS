from dao.StudentsDao import alunos

def findStudent(id):
   return list(filter(lambda c: c["id"] == id, alunos))
   