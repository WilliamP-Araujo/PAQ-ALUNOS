from services import studentService
from dto import studentInsertDto

def insertStudent(studentDto: studentInsertDto.StudentInsertDTO):
    return studentService.insertStudent(studentDto)