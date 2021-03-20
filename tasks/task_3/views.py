from flask import jsonify, Flask, request, Response

from services import appearance

app = Flask(__name__)


class ValidationError(Exception): pass


def serializer(data):
    print(data)
    for i in 'lesson', 'pupil', 'tutor':
        try:
            if len(data[i])%2 != 0:
                raise ValidationError()
        except KeyError:
            raise ValidationError
    
    return data
        
@app.route("/appearance", methods=['POST'])
def appearance_view():
    try:
        data = serializer(request.json)
    except ValidationError:
        return Response('Validation error', status=400)
    else:
        return jsonify(appearance(data))


if __name__ == '__main__':
    app.run(port=8000)
