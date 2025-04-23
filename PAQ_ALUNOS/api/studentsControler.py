from flask import Flask, jsonify


from usecases import updateStudentUseCase, insertStudentUseCase, inactiveStudentUseCase,removeStudentUseCase,findStudentsUseCase,findAllStudentsUseCase
from dto import studentUpdateDto, studentInsertDto
from flask_pydantic import validate
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Student API",
        "version": "1.0"
    },
    "definitions": {
        "StudentDTO": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "example": "alice"
                },
                "apelido": {
                    "type": "string",
                    "example": "Alitche"
                }
            },
            "required": ["name", "apelido"]
        },
        "StudentInsertDTO": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "example": "João"
                },
                "apelido": {
                    "type": "string",
                    "example": "Juca"
                }
            },
            "required": ["name", "apelido"]
        }
    }
})

@app.route('/alunos', methods=['GET'])
def get_alunos():
    """
    Get all students
    ---
    responses:
      200:
        description: A list of all students
        schema:
          type: array
          items:
            type: object
    """
    return jsonify(findAllStudentsUseCase.findAllStudents())

@app.route('/alunos/<string:id>', methods=['GET'])
def get_aluno(id):
    """
    Get a student by ID
    ---
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The student ID
    responses:
      200:
        description: A student object
        schema:
          type: object
    """
    return jsonify(findStudentsUseCase.findStudent(id))

@app.route('/alunos/<string:id>', methods=['DELETE'])
def remove_aluno(id):
    """
    Remove a student by ID
    ---
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The student ID
    responses:
      200:
        description: Success message
    """
    removeStudentUseCase.removeStudent(id)
    return f"Aluno {id} removido com sucesso!"

@app.route('/alunos/<string:id>/inactive', methods=['PATCH'])
def inactive_aluno(id):
    """
    Inactivate a student
    ---
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The student ID
    responses:
      200:
        description: Success message
    """
    inactiveStudentUseCase.inactiveStudents(id)
    return f"Aluno {id} inativado com sucesso!"

@app.route('/alunos/<string:id>', methods=['PUT'])
@validate()
def update_aluno(id: str, body: studentUpdateDto.StudentDTO):
    """
    Update a student
    ---
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The student ID
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/StudentDTO'
    responses:
      200:
        description: Success message
    """
    updateStudentUseCase.updateStudent(id,body)
    return f"Aluno {id} atualizado com sucesso!"

@app.route('/alunos', methods=['POST'])
@validate()
def insert_aluno( body: studentInsertDto.StudentInsertDTO):
    """
    Insert a new student
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/StudentInsertDTO'
    responses:
      200:
        description: Success message
    """
    insertStudentUseCase.studentInsert(body)
    return f"Aluno inserido com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)


