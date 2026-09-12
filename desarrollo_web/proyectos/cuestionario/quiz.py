from random import shuffle
from flask import Flask, session, redirect, url_for, render_template, request
from db_scripts import get_question_after, get_quizzes, check_answer

def start_quiz(quiz_id):
    '''crea los valores deseados en el diccionario session'''
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session['answers'] = 0 # contador de respuestas correctas
    session['total'] = 0 # Contador de preguntas respondidas.

def end_quiz():
    session.clear()

def quiz_form():
    cuestionarios = get_quizzes()
    return render_template('start.html', lista_cuestionarios=cuestionarios)

def question_form(pregunta):
    respuestas = [
        pregunta[2], pregunta[3], pregunta[4], pregunta[5]
    ]
    shuffle(respuestas)
    return render_template('test.html', pregunta=pregunta[1], quest_id=pregunta[0], lista_respuestas=respuestas)

def index():
    if request.method == 'GET':
        start_quiz(-1)
        return quiz_form()
    else:
        quest_id = request.form.get('quiz')
        start_quiz(quest_id)

        return redirect(url_for('test'))

def save_answers():
    answer = request.form.get('ans_text')
    quest_id = request.form.get('q_id')

    session['last_question'] = quest_id
    session['total'] += 1

    # comprueba si la respuesta coincide con el id correcto para esto
    if check_answer(quest_id, answer):
        session['answers'] += 1

def test():
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            save_answers()

        next_question = get_question_after(session['last_question'], session['quiz'])

        if next_question is None or len(next_question) == 0:
            return redirect(url_for('result'))
        else:            
            return question_form(next_question)

def result():
    html = render_template('result.html', correctas=session['answers'], total=session['total'])
    end_quiz()
    return html

app = Flask(__name__)  
app.add_url_rule('/', 'index', index, methods=['post', 'get'])   
app.add_url_rule('/test', 'test', test, methods=['post', 'get'])
app.add_url_rule('/result', 'result', result)

app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
   app.run(debug=True)