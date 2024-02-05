from flask import Flask,render_template,url_for,redirect,request
import speech_recognition as sr
import json
import requests
import sqlite3
import time
app = Flask(__name__)

@app.route("/")
def hell():
    return render_template('./index.html')

@app.route('/home')
def home():
    return render_template('./index.html')

@app.route('/contact')
def contact():
    return render_template('./contact.html')

@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/login')
def login():
    return render_template('./login.html')

@app.route('/user')
def user():
    return render_template('./user_details.html')

check = False

@app.route("/erase")
def erase():
    global check
    check = True
    conn = sqlite3.connect('./web.db')
    c = conn.cursor()
    c.execute("DELETE FROM vocabulary")
    conn.commit()
    return redirect(url_for('history'))

@app.route('/history')
def history():
    data=''
    global check
    if(check):
        data += "History cleared"
        check = False
    conn = sqlite3.connect('./web.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM vocabulary"):
        # data = ", ".join([row[0] for row in c.execute("SELECT * FROM words")])
        data += str(row)
    return render_template('history.html', word = str(data))



@app.route("/Login", methods = ['POST', 'GET']) 
def Login():
    username = ''
    password = ''
    email = ''
    if request.method == 'POST':
        username = request.form['username'] #can also use request.form.get('username')
        password = request.form['password']
        email = request.form['email']
        conn = sqlite3.connect('./userlogin.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username,password,email))
        c.execute("SELECT username FROM users ")
        result = c.fetchall()
    return render_template('./user_index.html', word = str(result[len(result)-1]))


@app.route("/well/<name>")   
def well(name):
    return render_template('output.html', name = name)

def find(word, action):
    conn = sqlite3.connect('./web.db')
    c = conn.cursor()
    check_word = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}'"
    word_count = ((c.execute(check_word)).fetchone())[0]
    r=""
    if(action == 'synonyms' or action =="antonyms"):
        if(word_count!=0):
            check_syn = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}' AND {action} IS NULL"
            syn_count = ((c.execute(check_syn)).fetchone())[0]
            if(syn_count!=0):
                r = str((get_dictionary_response(word))[action][0:3])
                update_synonym = f"UPDATE vocabulary SET {action}='{r}' WHERE word='{word}'"
            else:
                syn = f"SELECT {action} FROM vocabulary WHERE word='{word}'"
                r = ((c.execute(syn)).fetchone())[0]
        else:
            word_insert = "INSERT INTO vocabulary (word) VALUES (?)"
            c.execute(word_insert, (word,))
            r = str((get_dictionary_response(word))[action][0:3])
            update_synonym = f"UPDATE vocabulary SET {action}=? WHERE word=?"
            c.execute(update_synonym, (r, word))
        conn.commit()

    if(action == "sentence" or action == "definition"):
        if(word_count!=0):
            check_syn = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}' AND {action} IS NULL"
            syn_count = ((c.execute(check_syn)).fetchone())[0]
            if(syn_count!=0):
                if(action=="sentence"):
                    r = str((get_dictionary_response(word))["examples"])
                if(action=="definition"):
                    r = str((get_dictionary_response(word))["meaning"])
                update_synonym = f"UPDATE vocabulary SET {action}='{r}' WHERE word='{word}'"
            else:
                syn = f"SELECT {action} FROM vocabulary WHERE word='{word}'"
                r = ((c.execute(syn)).fetchone())[0]
        else:
            word_insert = "INSERT INTO vocabulary (word) VALUES (?)"
            c.execute(word_insert, (word,))
            if(action=="sentence"):
                r = str((get_dictionary_response(word))["examples"])
            if(action=="definition"):
                r = str((get_dictionary_response(word))["meaning"])
            update_synonym = f"UPDATE vocabulary SET {action}=? WHERE word=?"
            c.execute(update_synonym, (r, word))
        conn.commit()
    
    return r

# @app.route('/record', methods=['POST'])
def record():
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Recording...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            my_list = text.strip().split()
            action = my_list[0]
            word = my_list[2]
            # r = "not found"
            r = find(word, action)
            print(r)
            action = action[0].upper() + action[1:len(action)]
            return r,action,word
            return render_template('output.html',name=r)
            return redirect(url_for('well',name = f'{action} of '+ word + " : " + r))
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "Could not understand audio"
        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))
            return "Could not request results"



@app.route('/x',  methods = ['POST', 'GET'])
def x():
    word = ''
    r=''
    if request.method == 'POST':

        word = request.form['word']
        action = request.form['action']

        # changed here on feb - 3
        # written separate func for finding the meta data to satisfy DRY
        if(action=="record"):
            r,action,word = record()
        else:
            r = find(word, action)
    action = action[0].upper() + action[1:len(action)]
    return redirect(url_for('well',name = f'{action} of '+ word + " : " + r))

def get_dictionary_response(word):
    word_metadata = {}
    definition = "sorry, no definition is available."
    example = "sorry, no examples are available."
    synonyms = ["sorry, no synonyms are available."]
    antonyms = ["sorry, no antonyms are available."]
    url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b3b73004-8412-455e-a40a-2cfb3d87e9ee"
    response = requests.get(url)
    api_response = json.loads(response.text)
    if response.status_code == 200:
        for data in api_response:
            if data["meta"]["id"] == word:
                if len(data["meta"]["syns"]) != 0:
                    synonyms = data["meta"]["syns"][0]
                if len(data["meta"]["ants"]) != 0:
                    antonyms = data["meta"]["ants"][0]
                for results in data["def"][0]["sseq"][0][0][1]["dt"]:
                    if results[0] == "text":
                        definition = results[1]
                    if results[0] == "vis":
                        example = results[1][0]["t"].replace("{it}", "*").\
                            replace("{/it}", "*")
    word_metadata["meaning"] = definition
    word_metadata["examples"] = example
    word_metadata["antonyms"] = antonyms
    word_metadata["synonyms"] = synonyms
    return word_metadata


if __name__ == "__main__":
    check = False;
    app.run(port = '4000', debug = True)
