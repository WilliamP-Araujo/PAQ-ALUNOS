from flask import Flask, jsonify

from usecases import findAllStudentsUseCase


app =Flask(__name__)


@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(findAllStudentsUseCase.findAllStudents())

if __name__ == '__main__':
    app.run(debug=True)