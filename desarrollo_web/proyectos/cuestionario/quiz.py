from random import shuffle
from flask import Flask, session, redirect, url_for, render_template, request
from db_scripts import get_question_after, get_quizzes, check_answer

def index():
    cuestionarios = [
        (1, 'Fundamentos de python'),
        (2, 'Diccionarios'),
        (3, 'Carrera')   
    ]

    return render_template('start.html', lista_cuestionarios=cuestionarios)

def test():
    enunciado = '¿Cuántos lados tiene un triángulo?'
    respuestas = ['uno', 'dos', 'tres']

    return render_template(
        'test.html', 
        pregunta=enunciado, 
        lista_respuestas=respuestas, 
        q_id=1, 
        quest_id=2
    )

def result():
   return render_template('result.html', correctas=5, total=10)

app = Flask(__name__)  
app.add_url_rule('/', 'index', index) 
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == '__main__':
   app.run(debug=True)