from flask import Flask, jsonify


from usecases import updateStudentUseCase, insertStudentUseCase, inactiveStudentUseCase,removeStudentUseCase,findStudentsUseCase,findAllStudentsUseCase
from dto import studentUpdateDto, studentInsertDto
from flask_pydantic import validate


app = Flask(__name__)


@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(findAllStudentsUseCase.findAllStudents())

@app.route('/alunos/<string:id>', methods=['GET'])
def get_aluno(id):
    return jsonify(findStudentsUseCase.findStudent(id))

@app.route('/alunos/<string:id>', methods=['DELETE'])
def remove_aluno(id):
    removeStudentUseCase.removeStudent(id)
    return f"Aluno {id} removido com sucesso!"

@app.route('/alunos/<string:id>/inactive', methods=['PATCH'])
def inactive_aluno(id):
    inactiveStudentUseCase.inactiveStudents(id)
    return f"Aluno {id} inativado com sucesso!"

@app.route('/alunos/<string:id>', methods=['PUT'])
@validate()
def update_aluno(id: str, body: studentUpdateDto.StudentDTO):
    updateStudentUseCase.updateStudent(id,body)
    return f"Aluno {id} atualizado com sucesso!"

@app.route('/alunos', methods=['POST'])
@validate()
def insert_aluno( body: studentInsertDto.StudentInsertDTO):
    insertStudentUseCase.studentInsert(body)
    return f"Aluno inserido com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)


