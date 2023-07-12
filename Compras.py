@app.route('/')
def logicap():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM compra_de_materiales')
    concompra = CC.fetchall() 
    print (concompra)
    return render_template('index.html', Listascompra=concompra)

@app.route('/SolicitudCompra', methods=['POST'])
def guardarCompra():
    if request.method == 'POST':
        estadocompra = request.form['estadocompra']
        materialId = request.form['materialId']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        proveedorId = request.form['proveedorId']
        fecha = request.form['fecha']
        print(estadocompra,materialId,cantidad,precio,proveedorId,fecha)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO compra_de_materiales (estadocompra,materialId,cantidad,precio,proveedorId,fecha) VALUES (%s, %s, %s, %s, %s)', (estadocompra,materialId,cantidad,precio,proveedorId,fecha))
        mysql.connection.commit()

    flash('la compra fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_compra>')
def eliminarSolicitud(id_compra):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM compra_de_materiales WHERE id_compra = %s', (id_compra,))
    mysql.connection.commit()
    flash('la solicitud fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<string:id_compra>')
def editarSolicitud(id_compra):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM compra_de_materiales WHERE id_solicitud = %s', (id_compra,))
    consultaID = cursorID.fetchone()

    return render_template('ActualizarCompra.html', compra_de_materiales=consultaID)

