from flask import Blueprint, render_template, request, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/otra')
def otra():
    return render_template('min-alabanza.html')

@main_bp.route('/otra2', methods=['POST'])
def otra2():
    """ lista = [1,5,7,"Hola", [1,2,3,4,5]] """
    if request.method == 'POST':
        return [
            request.form['clave'],
            request.form['correo']
        ]
    else:
        return jsonify({"mensaje": "Solo se aceptan solicitudes POST"}) 
    # return []
