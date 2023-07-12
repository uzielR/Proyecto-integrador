

@app.route('/')
def logicap():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM reservacion_de_materiales')
    conreservacion = CC.fetchall() 
    print (conreservacion)
    return render_template('index.html', Listareservacion=conreservacion)

@app.route('/ReservarMaterial', methods=['POST'])
def guardarSolicitud():
    if request.method == 'POST':
        materialId = request.form['materialId']
        cantidadSolictud = request.form['cantidad']
        solicitante = request.form['solicitanteId']
        estado = request.form['estado']
        fecha = request.form['fecha']
        print(materialId,cantidadSolictud,solicitante,estado,fecha)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO reservacion_de_materiales (materialId, cantidad, solicitante, estado, fechas) VALUES (%s, %s, %s, %s, %s)', (materialId,cantidadSolictud,solicitante,estado,fecha))
        mysql.connection.commit()

    flash('la solicitud fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_reservacion>')
def eliminarSolicitud(id_solicitud):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM reservacion_de_materiales WHERE id_reservacion = %s', (id_reservacion,))
    mysql.connection.commit()
    flash('Se eliminó la solicitud')
    return redirect(url_for('index'))

@app.route('/editar/<string:id_reservacion>')
def editarSolicitud(id_reservacion):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM reservacion_de_materiales WHERE id_reservacion = %s', (id_reservacion,))
    consultaID = cursorID.fetchone()

    return render_template('editarSolicitud.html', reservacion_de_materiales=consultaID)