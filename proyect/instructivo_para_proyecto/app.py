import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from datetime import datetime as Times
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, validaresp




# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "l5qGfXFue2"

Session(app)

db = SQL("sqlite:///base.db")


@app.route("/")
def index():
    """Algo"""
    session.clear()
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""


    session.clear()


    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Se debe ingresar un usuario", 102)


        elif not request.form.get("password"):
            return apology("Se debe ingresar una contraseña", 102)

        rows = db.execute("SELECT * FROM usuario WHERE username LIKE (?)",
                          request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("El usuario ingresado no existe o la contraseña es incorrecta", code=401)
        else:
            session["user_id"] = rows[0]["id"]
            return redirect("/home")

    else:
        return render_template("login.html")


@app.route("/registrarp", methods=["GET", "POST"])
def registrar():
    """Register user"""
    session.clear()
    if (request.method == "POST"):

        correoh = request.form.get('correo')
        nombre_usu = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        confirmacion = request.form.get('confirmacion')

        if not correoh:
            return apology("Se debe ingresar un correo", 203)

        if not nombre_usu:
            return apology("Se debe ingresar un nombre de usuario", 400)

        if not contraseña:
            return apology("Se debe de ingresar una contraseña", 417)

        if not confirmacion:
            return apology("Es necesario que confirme su contraseña", 417)

        if contraseña != confirmacion:
            return apology("Las contraseñas no coinciden", 102)

        correobd = db.execute(
            "SELECT * FROM usuarios_csx50 WHERE correo LIKE (?)", correoh)

        if not correobd:
            return apology("Usted no puede ingresar a esta pagina", 412)

        verificarcorreo = db.execute(
            "SELECT * FROM usuario WHERE mail = (?)", correoh)
        if len(verificarcorreo) != 0:
            return apology("Un correo no puede tener más de un usuario", 423)

        if (len(nombre_usu) <= 3):
            return apology("Su usuario debe ser mayor a 3 caracteres", 411)
        if (len(contraseña) < 6):
            return apology("Su contraseña debe ser mayor a 6 caracteres", 411)
        # if (c == ' ' for c in nombre_usu):
        #     return apology("Su usuario no debe contener espacios", 406)
        cifra = generate_password_hash(contraseña)

        verificar = db.execute(
            "SELECT * FROM usuario WHERE username = (?)", nombre_usu)

        if len(verificar) == 1:
            return apology("Ese usuario ya existe", 200)
        else:
            result = db.execute(
                "INSERT INTO usuario (username, password, mail) VALUES (?, ?, ?)", nombre_usu, cifra, correoh)
            result2 = db.execute("SELECT * FROM usuario WHERE username = ?",
                                 request.form.get("usuario"))
            session["user_id"] = result2[0]["id"]
            return redirect("/home")
    else:
        return render_template("registrarp.html")


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


@app.route("/tematicas/<string:temat>/", methods=["GET", "POST"])
@login_required
def tematicas(temat):

    if (request.method == "POST"):
        comentario = request.form.get('comentario')
        concept = db.execute(
            "SELECT concepto FROM concepts WHERE tipo LIKE (?)", temat)
        rows = db.execute(
            "SELECT * FROM posts WHERE tipotheme LIKE (?)", temat)
        rowsaut = db.execute(
            "SELECT * FROM usuario INNER JOIN posts ON posts.id_autor = usuario.id WHERE posts.tipotheme LIKE (?)", temat)
        selectc = db.execute(
            "SELECT * FROM comentarios INNER JOIN posts ON posts.id = comentarios.id_post INNER JOIN usuario ON usuario.id = comentarios.id_usuario")
        idp = request.form.get("flexCheckChecked")

        if not comentario:
            return apology("No puede ingresar un comentario vacio", 200)

        db.execute("INSERT INTO comentarios (txt_coment, id_usuario, id_post, fecha_comnt) VALUES (?, ?, ?, ?)",
                                   comentario, session["user_id"], idp, Times.now())
        temat2 = temat.replace("_", " ")

        print(f"{temat}")
        return redirect(f"/tematicas/{temat}")

        # return render_template("tematicas.html", concept=concept, rows=rows, rowsaut=rowsaut, temat=temat, selectc=selectc)

    else:
        concept = db.execute(
            "SELECT concepto FROM concepts WHERE tipo LIKE (?)", temat)
        rows = db.execute(
            "SELECT * FROM posts WHERE tipotheme LIKE (?)", temat)
        rowsaut = db.execute(
            "SELECT * FROM usuario INNER JOIN posts ON posts.id_autor = usuario.id WHERE posts.tipotheme LIKE (?)", temat)
        selectc = db.execute(
            "SELECT * FROM comentarios INNER JOIN posts ON posts.id = comentarios.id_post INNER JOIN usuario ON usuario.id = comentarios.id_usuario")
        temat2 = temat.replace("_", " ")

        return render_template("tematicas.html", concept=concept, rows=rows, rowsaut=rowsaut, temat=temat2, selectc=selectc)



@app.route("/logout")
def logout():
    """Log user out"""

    if session.get("user_id") is None:
        return apology("¿Cómo vas a salir si no estás adentro?", 102)
    else:

        session.clear()

    return redirect("/")


@app.route("/publicar", methods=["GET", "POST"])
@login_required
def publicar():
    if (request.method == "POST"):
        titulo = request.form.get('titulo')
        cuerpo = request.form.get('proyecto')
        herramientas = request.form.get('herramientas')
        tipo = request.form.get('tipo')
        if not titulo:
            return apology("Ingrese el titulo de proyecto", 406)
        if not cuerpo:
            return apology("Ingrese la descripcion del proyecto", 406)
        if not herramientas:
            return apology("Ingrese las herramientas posibles de proyecto", 406)
        if tipo == "Tipo de proyecto":
            return apology("Ingrese el tipo de proyecto", 406)
        result = db.execute(
            "INSERT INTO posts (titulo, cuerpo, tipotheme, herramientas_pro, id_autor) VALUES (?, ?, ?, ?, ?)", titulo, cuerpo, tipo, herramientas, session["user_id"])
        return redirect("/home")
    else:
        return render_template("publicar.html")


@app.route("/know", methods=["GET", "POST"])
@login_required
def know():
    pregunta1 = {"Ingeniería Sistemas" : "Programacion_web",
                "Ingeniería en computación" :"Programacion_estructurada",
                "Ingeniería Electronica" : "Electronica" ,
                "Ingeniería Civil" : "Electronica" ,
                "Ingeniería Industrial" : "Programacion_estructurada",
                "Ingeniería Mecanica" : "Electronica",
                "Otra..." : "0" }

    pregunta2 = {"C/C++" : "Programacion_estructurada",
                "Java" : "Programacion_estructurada",
                "JavaScript" : "Programacion_web",
                "Python" : "Electronica",
                "C#" : "Programacion_estructurada",
                "PHP": "Programacion_web"}

    pregunta3 = {"Trabajos que involucran trabajos mecánicos sobre un material" : "Electronica",
                "Trabajos de exclusivo funcionamiento digital": "Programacion_web",
                "Instalacion de software" : "Programacion_estructurada"}

    pregunta4 = {"Lectura" : "Programacion_web",
                "Innovación tecnológica" : "Electronica",
                "Videojuegos" : "Programacion_estructurada",
                "Aprender sobre el funcionamiento visual de internet" : "Programacion_web",
                "Los robots son tuanis" : "Electronica",
                "Interes por conocer como funcionaba un videojuego" : "Programacion_estructurada"}

    pregunta5 = {"Sistemas informaticos" : "Programacion_estructurada",
                "Paginas web" : "Programacion_web",
                "Circuitos" : "Electronica",
                "Lo que hay detras de los Videojuegos": "Programacion_estructurada"}

    todasrespuestas = []


    if request.method == "POST":
        respuestas1 = request.form.get("pregunta1")
        respuestas2 = request.form.get("pregunta2")
        respuestas3 = request.form.get("pregunta3")
        respuestas4 = request.form.get("pregunta4")
        respuestas5 = request.form.get("pregunta5")

        if not respuestas1:
            return apology("Responda todas las preguntas", 204)
        else:
            todasrespuestas.append(respuestas1)

        if not respuestas2:
            return apology("Responda todas las preguntas", 204)
        else:
            todasrespuestas.append(respuestas2)

        if not respuestas3:
            return apology("Responda todas las preguntas", 204)
        else:
            todasrespuestas.append(respuestas3)

        if not respuestas4:
            return apology("Responda todas las preguntas", 204)
        else:
            todasrespuestas.append(respuestas4)

        if not respuestas5:
            return apology("Responda todas las preguntas", 204)
        else:
            todasrespuestas.append(respuestas5)
        # if respuestas1 ==
        # listarespuestas = {'pregunta1': recibir_form('flexRadioDefault', "No puede dejar una pregunta sin responder", 204), 'pregunta2': recibir_form(
        #     'flexRadioDefault', "No puede dejar una pregunta sin responder", 204)}
        # print(listarespuestas)
        # print(validaresp(listarespuestas))
        return validaresp(todasrespuestas)
        # print(f"{valresult}")
        # return redirect("/know")
    else:
        return render_template("know.html", pregunta1=pregunta1, pregunta2=pregunta2, pregunta3=pregunta3, pregunta4=pregunta4, pregunta5=pregunta5)


if __name__ == '__main__':
    app.run(debug=True)
