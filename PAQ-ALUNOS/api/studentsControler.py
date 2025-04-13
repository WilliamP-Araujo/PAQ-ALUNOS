from flask import Flask, jsonify

from usecases import findAllStudentsUseCase
from usecases import findStudentsUseCase
from usecases import removeStudentUseCase


app = Flask(__name__)


@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(findAllStudentsUseCase.findAllStudents())

@app.route('/aluno', methods=['GET'])
def get_aluno():
    return jsonify(findStudentsUseCase.findStudent())

@app.route('/removerAluno', methods='DELETE')
def remove_aluno():
    return jsonify(removeStudentUseCase.removeStudent())

if __name__ == '__main__':
    app.run(debug=True)


