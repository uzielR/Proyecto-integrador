@app.route('/')
def logicap():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM entrega_de_materiales WHERE id_entrega = %s', (id_entrega,))
    conentrega = CC.fetchall() 
    print (conentrega)
    return render_template('index.html', Listaentrega=conentrega)

@app.route('/SolicitudEntrega', methods=['POST'])
def guardarEntrega():
    if request.method == 'POST':
        idsolicitud= request.form['id_solicitud']
        idmaterial = request.form['id_material']
        cantidad= request.form['cantidad']
        recibidopor = request.form['recibido_por']
        entregadopor = request.form['entregado_por']
        fechaentrega = request.form['fecha_entrega']
        print()

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO Entrega_materiales (id_solicitud, id_material, cantidad, recibido_por, fecha_entrega) VALUES (%s, %s, %s, %s, %s)', (idsolicitud, idmaterial, cantidad, recibidopor, fechaentrega))
        mysql.connection.commit()

    flash('la solicitud fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_entrega>')
def eliminarEntrega(id_entrega):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM Entrega_de_materiales WHERE id_entrega = %s', (id_entrega,))
    mysql.connection.commit()
    flash('la solicitud fue eliminada correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<string:id_entrega>')
def editarEntrega(id_entrega):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM entrega_de_materiales WHERE id_entrega = %s', (id_entrega,))
    consultaID = cursorID.fetchone()

    return render_template('ActualizarEntrega.html', entrega_de_materiales=consultaID)
