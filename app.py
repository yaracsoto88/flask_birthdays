import os  
from cs50 import SQL 
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Creamos una instancia de la clase Flask y la guardamos en la variable app
app = Flask(__name__)  

app.config["TEMPLATES_AUTO_RELOAD"] = True  

# Creamos una instancia de la clase SQL que se conecta a la base de datos 
db = SQL("sqlite:///birthdays.db")  

# Creamos la ruta 
@app.route("/", methods=["GET", "POST"])  
def index():

    # Comprueba que utiliza el método POST
    if request.method == "POST": 

        # Inicializamos mensaje como una cadena vacia
        mensaje = "" 
        # Obtiene los valores del formulario enviados en la solicitud POST
        nombre = request.form.get("name")  
        mes = request.form.get("month") 
        dia = request.form.get("day")  

    # Control de errores. Comprueba si el usuario no dio un nombre, mes o día.
        if not nombre:  
            mensaje = "Falta un nombre"  
        elif not mes:  
            mensaje = "Falta un mes"  
        elif not dia: 
            mensaje = "Falta un día"  
        else:
            # Si todo ha ido correctamente, inserta los valores en la tabla birthdays
            db.execute(
                "INSERT INTO birthdays (name, month, day) VALUES(?,?,?)",  
                nombre,
                mes,
                dia,
            )

        # Obtiene todos los registros de la tabla y los pasa a la plantilla
        cumpleaños = db.execute("SELECT * FROM birthdays") 
        return render_template("index.html", message=mensaje, birthdays=cumpleaños)  
    else:
        # Obtiene todos los registros de la tabla birthdays
        cumpleaños = db.execute("SELECT * FROM birthdays")
        # Y pasa la variable birthdays a la plantilla index.html
        return render_template("index.html", birthdays=cumpleaños) 
