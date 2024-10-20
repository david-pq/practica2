from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curso', methods=['GET', 'POST'])
def curso():
    if request.method == 'POST':
        # Aquí procesaríamos los datos recibidos
        return redirect(url_for('success'))
    return render_template('curso.html')

@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        # Procesar registro de usuario
        return redirect(url_for('success'))
    return render_template('usuario.html')

@app.route('/producto', methods=['GET', 'POST'])
def producto():
    if request.method == 'POST':
        # Procesar registro de producto
        return redirect(url_for('success'))
    return render_template('producto.html')

@app.route('/libro', methods=['GET', 'POST'])
def libro():
    if request.method == 'POST':
        # Procesar registro de libro
        return redirect(url_for('success'))
    return render_template('libro.html')

@app.route('/inscripcion_completa', methods=['POST'])
def inscripcion_completa():
    # Aquí podrías procesar los datos del formulario si es necesario
    return render_template('inscripcion_completa.html')

@app.route('/usuario_completo', methods=['POST'])
def usuario_completo():
    return render_template('usuario_completo.html')

@app.route('/producto_completo', methods=['POST'])
def producto_completo():
    return render_template('producto_completo.html')

@app.route('/libro_completo', methods=['POST'])
def libro_completo():
    return render_template('libro_completo.html')


@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
