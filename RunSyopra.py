#importacion del framework
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='SyopraBD'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)


#declaracion de ruta / http://localhost:5000 - tipo insert 

@app.route('/')
def logicap():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM materiales')
    conmateriales = CC.fetchall() 
    print (conmateriales)
    return render_template('index.html', Listamateriales=conmateriales)

    
def __init__(self) -> None:
    pass
                       
@app.route('/guardarMaterial', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Nombre = request.form['txtnombre']
        Categoria = request.form['txtcategoria']
        Cantidad = request.form['txtcantidad']
        Max = request.form['txtmax']
        Min = request.form['txtmin']
        print(Nombre, Categoria, Cantidad, Max, Min)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO material (nombre, categoria, cantidad, max, min) VALUES (%s, %s, %s, %s, %s)', (Nombre, Categoria,Cantidad,Max,Min))
        mysql.connection.commit()

    flash('El Material fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM materiales WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Se eliminó el registro')
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM materiales WHERE id = %s', (id,))
    consultaID = cursorID.fetchone()

    return render_template('editarRegistro.html', materiales=consultaID)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varNombre = request.form['txtnombre']
        varCategoria = request.form['txtcategoria']
        varCantidad = request.form['txtcantidad']
        varMax = request.form['txtmax']
        varMin = request.form['txtmin']

        cursorAct = mysql.connection.cursor()
        cursorAct.execute('UPDATE materiales SET Nombre = %s, Categoria = %s, Cantidad = %s, Max = %s, Min = %s WHERE id = %s', (varNombre, varCategoria, varCantidad, varMax, varMin, id))
        mysql.connection.commit()

        flash('Se actualizó el registro ' + varNombre)
    return redirect(url_for('index'))
//////////////////////////
#compra
/
#reservaciones 
/////
entrega
////////

@app.route('/')
def Empleados():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM Empleados WHERE id_empleado = %s', (id_empleado,))
    conempleado = CC.fetchall() 
    print (conempleado)
    return render_template('index.html', Listaempleado=conempleado)

@app.route('/Guardar Empleado', methods=['POST'])
def guardarEmpleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ap = request.form['ap']
        am = request.form['am']
        print(nombre,ap,am)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO Empleados (id_) VALUES (%s, %s)', (nombre,ap,am))
        mysql.connection.commit()

    flash('la solicitud fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_compra>')
def eliminarSolicitud(id_compra):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM compra_de_Materiales WHERE id_compra = %s', (id_compra,))
    mysql.connection.commit()
    flash('la solicitud fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<string:id_Compra>')
def editarSolicitud(id_Compra):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM Compra_de_Materiales WHERE id_Solicitud = %s', (id_Compra,))
    consultaID = cursorID.fetchone()

    return render_template('ActualizarCompra.html', solicitud_de_materiales=consultaID)


#ejecucion
if __name__ == '__main__':
    app.run(port= 5000)