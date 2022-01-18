from flask import Flask, render_template, request, flash, Response
from juego import juego_base
import time

app = Flask(__name__)



@app.route('/', methods=["GET","POST"])
def index():


    if (request.method == 'POST'):
        identificador = int(request.form.get('pregunta'))

        lista_retornada = juego_base(identificador)

        # Para verificar la fotos
        foto1 = "/static/img/" + lista_retornada[1].lower() +".svg"
        foto2 = "/static/img/" + lista_retornada[2].lower() +".svg"

        diccionario = { 'resultado':lista_retornada[0], 'respuesta1':lista_retornada[1], 'respuesta2':lista_retornada[2], 'foto1':foto1, 'foto2':foto2}
        
        return render_template("respuesta.html", diccionario=diccionario)
    

    return render_template("index.html")


@app.route('/pregunta', methods=["GET","POST"])
def respuesta():
        
    return render_template("respuesta.html")


@app.route('/progress')
def progress():

    def generate():
        x = 0
    
        while x <= 100:

            yield "data:" + str(x) + "\n\n"
            x = x + 10
            time.sleep(0.3)

    return Response(generate(), mimetype= 'text/event-stream')


@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html')

# app run
if __name__ == "__main__":
    app.run(debug=True)