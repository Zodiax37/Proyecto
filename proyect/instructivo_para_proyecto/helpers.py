from flask import Flask, flash, redirect, render_template, request, session
from functools import wraps
from cs50 import SQL
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np


db = SQL("sqlite:///base.db")


# def grafico(resultados):

#     #Declaramos el tamaño de cada 'rebanada' y en sumatoria todos deben dar al 100%
#     resultados
#     #En este punto señalamos que posicion debe 'resaltarse' y el valor, si se coloca 0, se omite
#     explode = (0.1, 0, 0, 0)

#     fig1, ax1 = plt.subplots()
#     #Creamos el grafico, añadiendo los valores
#     ax1.pie(sizes, explode=explode, labels=medios_transporte, autopct='%1.1f%%',
#             shadow=True, startangle=90)
#     #señalamos la forma, en este caso 'equal' es para dar forma circular
#     ax1.axis('equal')
#     plt.title("Principal Medio de Transporte")
#     plt.legend()
#     plt.savefig('grafica_pastel.png')
#     plt.show()


def apology(mensaje, code):
    """Render message as an apology to user."""
    """https://http.cat/"""

    return render_template("apology.html", top=code, bottom=mensaje)


def validaresp(listarespuestas):
    prograweb = 0
    progaestruc = 0
    electronic = 0
    numpreg = len(listarespuestas)
    for r in listarespuestas:
        if r == "Programacion_web":
            prograweb += 1
        if r == "Programacion_estructurada":
            progaestruc += 1
        if r == "Electronica":
            electronic += 1
    listresultados = []
    frweb = (prograweb / numpreg) * 100
    frestr = (progaestruc / numpreg) * 100
    frelect = (electronic / numpreg) * 100
    listresultados.append(frweb)
    listresultados.append(frestr)
    listresultados.append(frelect)
    print(f"{listresultados}")

    resultados = {"Programacion_web" : frweb,"Programacion_estructurada" : frestr,"Electronica" : frelect}
    # pastel = grafico(listresultados)
    return render_template("mostrar.html", resultados=resultados)


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
