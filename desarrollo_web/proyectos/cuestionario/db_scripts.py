import sqlite3
from random import randint

db_name = 'quiz.sqlite'
conn = None
cursor = None

def get_question_after(question_id=0, quiz_id=1):
    """Devuelve la siguiente pregunta del cuestionario."""

    open()

    query = '''
    SELECT
        quiz_content.id,
        question.question,
        question.answer,
        question.wrong1,
        question.wrong2,
        question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id = question.id
    AND quiz_content.id > ?
    AND quiz_content.quiz_id = ?
    ORDER BY quiz_content.id
    '''

    cursor.execute(query, [question_id, quiz_id])

    result = cursor.fetchone()

    close()

    return result

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    '''borrar tablas'''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    
def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
 
    do('''CREATE TABLE IF NOT EXISTS quiz (
           id INTEGER PRIMARY KEY,
           name VARCHAR)''')
 
    do('''CREATE TABLE IF NOT EXISTS question (
               id INTEGER PRIMARY KEY,
               question VARCHAR,
               answer VARCHAR,
               wrong1 VARCHAR,
               wrong2 VARCHAR,
               wrong3 VARCHAR)''')
 
    do('''CREATE TABLE IF NOT EXISTS quiz_content (
               id INTEGER PRIMARY KEY,
               quiz_id INTEGER,
               question_id INTEGER,
               FOREIGN KEY (quiz_id) REFERENCES quiz (id),
               FOREIGN KEY (question_id) REFERENCES question (id) )''')
    close()

def add_questions():
    questions = [
        ('¿2+2?', '4', '3', '5', '6'),
        ('¿4+2?', '6', '5', '7', '8'),
        ('¿6+2?', '8', '7', '9', '10'),
        ('¿Cuántos meses en un año tienen 28 días?', 'Todos', 'Uno', 'Ninguno', 'Dos'),
        ('¿Qué aspecto tendrá el acantilado verde si se cae en el Mar Rojo?', 'Mojado', 'Rojo', 'No cambiará', 'Púrpura'),
        ('¿Con qué mano es mejor mezclar el té?', 'Con una cuchara', 'Derecha', 'Izquierda', 'Cualquiera'),
        ('¿Qué no tiene longitud, profundidad, ancho, o altura pero puede medirse?', 'Tiempo', 'Estupidez', 'El mar','Aire'),
        ('¿Cuándo es posible sacar agua con una red?', 'Cuando el agua está congelada', 'Cuando no hay peces', 'Cuando los peces de colores nadan lejos', 'Cuando la red se rompe'),
        ('¿Qué es más grande que un elefante y no pesa nada?', 'La sombra de un elefante','Un globo','Un paracaídas', 'Una nube')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()
 
def add_quiz():
    quizes = [
        ('Pruebas', ),
        ('propio juego', ),
        ('¿Quién quiere ser millonario?', ),
        ('El más inteligente', )
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()
 
def add_links2():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    
    answer = input("¿Añadir un enlace (y/n)?")
    
    while answer != 'n':
        quiz_id = int(input("quiz id: "))
        question_id = int(input("question id: "))
        
        cursor.execute(query, [quiz_id, question_id])
        
        conn.commit()
        
        answer = input("¿Añadir un enlace (y/n)?")
    close()

def add_links():
    links = [
        (1,1),
        (1,2),
        (1,3),
        (2,4),
        (2,5),
        (2,6)
    ]
    open()
    cursor.executemany('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)''', links)
    conn.commit()
    close()

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def get_quizzes():
    """Devuelve todos los cuestionarios disponibles."""
    open()

    cursor.execute('''SELECT * FROM quiz''')

    result = cursor.fetchall()

    close()
    return result

def check_answer(q_id, ans_text):
    query = '''
        SELECT question.answer
        FROM quiz_content, question
        WHERE quiz_content.id = ?
        AND quiz_content.question_id = question.id
    '''

    open()
    cursor.execute(query, (q_id,))
    result = cursor.fetchone()
    close()
    
    return result[0] == ans_text

def get_random_quiz_id():
    query = ''' 
    SELECT quiz_id FROM quiz_content
    '''

    open()
    cursor.execute(query)
    ids = cursor.fetchall()

    rand_num = randint(0, len(ids) - 1)
    rand_id = ids[rand_num][0]
    close()
    return rand_id

def main():
    clear_db()
    create()
    
    add_questions()
    add_quiz()
    add_links()
    show_tables()

if __name__ == "__main__":
    main()