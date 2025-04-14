from flask import Flask, jsonify

from usecases import findAllStudentsUseCase
from usecases import findStudentsUseCase
from usecases import removeStudentUseCase
from usecases import inactiveStudentUseCase
from usecases import updateStudentUseCase
from dto import studentUpdateDto


app = Flask(__name__)


@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(findAllStudentsUseCase.findAllStudents())

@app.route('/alunos/<string:id>', methods=['GET'])
def get_aluno(id):
    return jsonify(findStudentsUseCase.findStudent(id))

@app.route('/alunos/<string:id>', methods='DELETE')
def remove_aluno(id):
    removeStudentUseCase.removeStudent(id)
    return f"Aluno {id} removido com sucesso!"

@app.route('/alunos/<string:id>/inactive', methods='PATCH')
def inactive_aluno(id):
    inactiveStudentUseCase.inactiveStudent(id)
    return f"Aluno {id} inativado com sucesso!"

@app.route('/alunos/<string:id>', methods='PUT')
def update_aluno(id,studentDto:studentUpdateDto.StudentDTO):
    updateStudentUseCase.updateStudent(id,studentDto)
    return f"Aluno {id} atualizado com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)


