from flask import Flask, jsonify
from flasgger import Swagger


api = Flask(__name__)
Swagger(api)


@api.route('/calc/<string:op>/<int:number>/<int:other>')
def calc(op, number, other):
    """
    Calculation API
    This API endpoint is a calculator
    ---
    tags:
      - calculator
    parameters:
      - in: path
        name: op
        type: string
        required: true
        enum:
          - sum
          - mul
          - sub
          - div
      - in: path
        name: number
        type: integer
        required: true
      - in: path
        name: other
        type: integer
        required: true
    responses:
      200:
        description: The result
        schema:
          id: result
          properties:
            result:
              type: number
              format: float
              description: the calc result
              default: 1
    """

    operations = {
        "sum": lambda a, b: a + b,
        "mul": lambda a, b: a * b,
        "sub": lambda a, b: a - b,
        "div": lambda a, b: a / b,
    }
    result = operations[op](number, other)
    return jsonify({"result": result})

if __name__ == '__main__':
    api.run(debug=True)
