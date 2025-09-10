from flask import Flask, render_template, redirect, url_for

from zona_fit_app.cliente import Cliente
from zona_fit_app.cliente_dao import ClienteDAO
from zona_fit_app.cliente_form import ClienteForm

app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

app.config['SECRET_KEY'] = 'llave_secreta' # Llave CSRF (req para usar wtf)
# Sirve para evitar ataques cuando enviamos informacion de nuestro formulario a nuestro servidor web

@app.route('/') # http://localhost:5000/
@app.route('/index.html') # http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio/')
    # Recuperamos los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()

    # Creamos un objeto de cliente vacio
    cliente = Cliente()
    cliente_forma = ClienteForm(obj = cliente)

    return render_template('index.html', titulo = titulo_app, clientes = clientes_db, forma = cliente_forma) # Inyectamos datos a la plantilla

@app.route('/guardar', methods=['POST'])
def guardar():
    # Creamos los objetos varios de cliente
    cliente = Cliente()
    cliente_form = ClienteForm(obj = cliente)
    # Validamos el formulario
    if cliente_form.validate_on_submit():
        # Llenamos el objeto cliente con los valores del formulario
        cliente_form.populate_obj(cliente)
        # Validar existencia del id
        if not cliente.id: # Si el id es cadena vacia regresa V
            # Insertar el nuevo cliente en la bd
            ClienteDAO.insertar(cliente)
        else:
            # Modificamos el cliente en la bd
            ClienteDAO.actualizar(cliente)
    # Redireccionar al inicio
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>') # localhost:5000/editar/1
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj = cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo = titulo_app, clientes = clientes_db, forma = cliente_forma)

@app.route('/eliminar/<int:id>') # localhost:5000/eliminar/1
def eliminar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug = True)