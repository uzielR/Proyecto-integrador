#importacion del framework
from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt


#inicializacion del app
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='dbflask'
mysql= SQL SERVER(app)

#declaracion de ruta / http://localhost:5000 - tipo insert 

@app.route('/')
class logicap:
    def logicap():
     return render_template('logicap.html')
    
    def __init__(self) -> None:
        pass
            
    def guardarcliente (self,nom,pro,can):
        
       conx=self.logicap()
       
       if(nom == "" or pro=="" or can ==""):
           messagebox.showwarning("aviso","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom,pro,can)
           qrisert="insert into clientes (nombre,producto,cantidad) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
    def guardarempleado (self,nom1,area,pue):
        
       conx=self.logicap()
       
       if(nom1 == "" or area==""  or pue==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom1,area,pue)
           qrisert="insert into empleados (nombre,area,puesto) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
           
    def guardarprovedor (self,nom2,pro2,can2):
        
       conx=self.logicap()
       
       if(nom2 == "" or pro2=="" or can2 ==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom2,pro2,can2)
           qrisert="insert into provedores (nombrep,productop,cantidadp) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
           
    def registraentrada (self,nom3,area2,serie,can3,fecha):
        
       conx=self.logicap()
       
       if(nom3 == "" or area2=="" or serie =="" or can3 =="" or fecha =="" ):
           messagebox.showwarning("aviso","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom3,area2,serie,can3,fecha)
           qrisert="insert into entradas (nombre,area,serie,cantidad,fecha) values (?,?,?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
#ejecucion
if __name__ == '__main__':
    app.run(port=5000)