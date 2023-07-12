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
        idmaterial = request.form['id_material']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        idproveedor = request.form['id_proveedor']
        estadocompra = request.form['estado_compra']
        fecha = request.form['fecha']
        print(idmaterial,cantidad,precio,idproveedor,estadocompra,fecha)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO compra_de_materiales (id_material,cantidad,precio,id_proveedor,estado_compra,fecha) VALUES (%s, %s, %s, %s,%s, %s)', (idmaterial,cantidad,precio,idproveedor,estadocompra,fecha))
        mysql.connection.commit()

    flash('la compra fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_compra>')
def eliminarCompra(id_compra):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM compra_de_materiales WHERE id_compra = %s', (id_compra,))
    mysql.connection.commit()
    flash('la solicitud fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<string:id_compra>')
def editarCompra(id_compra):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM compra_de_materiales WHERE id_compra = %s', (id_compra,))
    consultaID = cursorID.fetchone()

    return render_template('ActualizarCompra.html', compra_de_materiales=consultaID)

@app.route('/actualizar/<int:id_compra>', methods=['POST'])
def actualizarCompra(id_compra):
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
