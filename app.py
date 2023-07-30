# from flask import Flask,render_template,url_for,redirect,request
# import json
# import requests
# import sqlite3
# app = Flask(__name__)

# @app.route("/")
# def hell():
#     return render_template('./index.html')

# @app.route('/home')
# def home():
#     return render_template('./index.html')

# @app.route('/contact')
# def contact():
#     return render_template('./contact.html')

# @app.route('/about')
# def about():
#     return render_template('./about.html')

# @app.route('/login')
# def login():
#     return render_template('./login.html')

# @app.route('/user')
# def user():
#     return render_template('./user_details.html')

# check = False

# @app.route("/erase")
# def erase():
#     global check
#     check = True
#     conn = sqlite3.connect('./web.db')
#     c = conn.cursor()
#     c.execute("DELETE FROM words")
#     conn.commit()
#     return redirect(url_for('history'))

# @app.route('/history')
# def history():
#     data=''
#     global check
#     if(check):
#         data += "History cleared"
#         check = False
#     conn = sqlite3.connect('./web.db')
#     c = conn.cursor()
#     for row in c.execute("SELECT * FROM words"):
#         data = " , ".join([row[0] for row in c.execute("SELECT * FROM words")])
#     return render_template('history.html', word = str(data))



# @app.route("/Login", methods = ['POST', 'GET']) 
# def Login():
#     username = ''
#     password = ''
#     email = ''
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         conn = sqlite3.connect('./userlogin.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username,password,email))
#         c.execute("SELECT username FROM users ")
#         result = c.fetchall()
#     return render_template('./user_index.html', word = str(result[len(result)-1]))


# @app.route("/well/<name>")   
# def well(name):
#     return render_template('output.html', name = name)
# '''
#     # <!DOCTYPE html>
#     # <html style="background-color: #33475b">
#     # <body>
#     # <h1 style = 'color:White'>{name}</h1>
#     # </body>
#     # </html>
#     # '''

# @app.route("/Synonyms", methods = ['POST', 'GET'])   
# def Synonyms():
#     word = ''
#     if request.method == 'POST':
#         word = request.form['word']
#         conn = sqlite3.connect('./web.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO words VALUES (?)", (word,))
#         conn.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well',name = 'Synonyms of '+ word + " : " +str(r["synonyms"])))


# @app.route("/Antonyms", methods = ['POST', 'GET'])
# def Antonyms():
#     word = ''
#     if request.method == 'POST':
#         word = request.form['word']
#         conn = sqlite3.connect('./web.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO words VALUES (?)", (word,))
#         conn.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well',name = 'Antonyms of '+ word + " : " +str(r["antonyms"])))


# @app.route("/Definition", methods = ['POST', 'GET'])
# def Definition():
#     word = ''
#     if request.method == 'POST':
#         word = request.form['word']
#         conn = sqlite3.connect('./web.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO words VALUES (?)", (word,))
#         conn.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well',name = 'Definition of '+ word + " : " +r["meaning"]))


# @app.route("/Sentence", methods = ['POST', 'GET'])
# def Sentence():
#     word = ''
#     r = 0
#     if request.method == 'POST':
#         word = request.form['word']
#         conn = sqlite3.connect('./web.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO words VALUES (?)", (word,))
#         conn.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well',name = 'Example of '+ word + " : " +r["examples"]))

# def get_dictionary_response(word):
#     word_metadata = {}
#     definition = "sorry, no definition is available."
#     example = "sorry, no examples are available."
#     synonyms = ["sorry, no synonyms are available."]
#     antonyms = ["sorry, no antonyms are available."]
#     # api_key = os.getenv("KEY_THESAURUS")
#     url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b3b73004-8412-455e-a40a-2cfb3d87e9ee"
#     response = requests.get(url)
#     api_response = json.loads(response.text)
#     if response.status_code == 200:
#         for data in api_response:
#             try:
#                 if data["meta"]["id"] == word:
#                     try:
#                         if len(data["meta"]["syns"]) != 0:
#                             synonyms = data["meta"]["syns"][0]
#                         if len(data["meta"]["ants"]) != 0:
#                             antonyms = data["meta"]["ants"][0]
#                         for results in data["def"][0]["sseq"][0][0][1]["dt"]:
#                             if results[0] == "text":
#                                 definition = results[1]
#                             if results[0] == "vis":
#                                 example = results[1][0]["t"].replace("{it}", "*").\
#                                     replace("{/it}", "*")
#                     except KeyError as e:
#                         print(e)
#             except TypeError as e:
#                 print(e)
#             break
#     word_metadata["meaning"] = definition
#     word_metadata["examples"] = example
#     word_metadata["antonyms"] = antonyms
#     word_metadata["synonyms"] = synonyms
#     return word_metadata


# if __name__ == "__main__":
#     check = False;
#     app.run(port = '4000', debug = True)










# # from flask import Flask, render_template, url_for, redirect, request
# # import json
# # import requests
# # from flask_sqlalchemy import SQLAlchemy

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
# # db = SQLAlchemy(app)


# # class Words(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     word = db.Column(db.String(100))


# # class Users(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(50), unique=True)
# #     password = db.Column(db.String(50))
# #     email = db.Column(db.String(120), unique=True)


# # @app.route("/hell")
# # def hell():
# #     return render_template('index.html')


# # @app.route('/home')
# # def home():
# #     return render_template('index.html')


# # @app.route('/contact')
# # def contact():
# #     return render_template('contact.html')


# # @app.route('/about')
# # def about():
# #     return render_template('about.html')


# # @app.route('/login')
# # def login():
# #     return render_template('login.html')


# # @app.route('/user')
# # def user():
# #     return render_template('user_details.html')


# # @app.route('/history')
# # def history():
# #     data = ''
# #     words = Words.query.all()
# #     for word in words:
# #         data += str(word.word)
# #     return render_template('history.html', word=str(data))


# # @app.route("/Login", methods=['POST', 'GET'])
# # def Login():
# #     username = ''
# #     password = ''
# #     email = ''
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         email = request.form['email']
# #         user = Users(username=username, password=password, email=email)
# #         db.session.add(user)
# #         db.session.commit()
# #         result = Users.query.with_entities(Users.username).all()
# #     return render_template('user_index.html', word=str(result[-1][0]))


# # @app.route("/well/<name>")
# # def well(name):
# #     return f'''
# #         # <!DOCTYPE html>
# #         # <html style="background-color: #33475b">
# #         # <body>
# #         # <h1 style = 'color:White'>{name}</h1>
# #         # </body>
# #         # </html>
# #         # '''


# # @app.route("/Synonyms", methods=['POST', 'GET'])
# # def Synonyms():
# #     word = ''
# #     if request.method == 'POST':
# #         word = request.form['word']
# #         word_entry = Words(word=word)
# #         db.session.add(word_entry)
# #         db.session.commit()
# #         r = get_dictionary_response(word)
# #     return redirect(url_for('well', name='Synonyms of ' + word + " : " + str(r["synonyms"])))


# # @app.route("/Antonyms", methods=['POST', 'GET'])
# # def Antonyms():
# #     word = ''
# #     if request.method == 'POST':
# #         word = request.form['word']
# #         word_entry = Words(word=word)
# #         db.session.add(word_entry)
# #         db.session.commit()
# #         r = get_dictionary_response(word)
# #     return redirect(url_for('well', name='Antonyms of ' + word + " : " + str(r["antonyms"])))


# # @app.route("/Definition", methods=['POST', 'GET'])
# # def Definition():
# #     word = ''
# #     if request.method == 'POST':
# #         word = request.form['word']
# #         word_entry = Words(word=word)
# #         db.session.add(word_entry)
# #         db.session.commit()
# #         r = get_dictionary_response(word)
# #     return redirect(url_for('well', name='Definition of ' + word + " : " + r["meaning"]))


# # @app.route("/Sentence", methods=['POST', 'GET'])
# # def Sentence():
# #     word = ''
# #     r = 0
# #     if request.method == 'POST':
# #         word = request.form['word']
# #         word_entry = Words(word=word)
# #         db.session.add(word_entry)
# #         db.session.commit()
# #         r = get_dictionary_response(word)
# #     return redirect(url_for('well',name = 'Example of '+ word + " : " +r["examples"]))

# # def get_dictionary_response(word):
# #     word_metadata = {}
# #     definition = "sorry, no definition is available."
# #     example = "sorry, no examples are available."
# #     synonyms = ["sorry, no synonyms are available."]
# #     antonyms = ["sorry, no antonyms are available."]
# #     # api_key = os.getenv("KEY_THESAURUS")
# #     url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b3b73004-8412-455e-a40a-2cfb3d87e9ee"
# #     response = requests.get(url)
# #     api_response = json.loads(response.text)
# #     if response.status_code == 200:
# #         for data in api_response:
# #             try:
# #                 if data["meta"]["id"] == word:
# #                     try:
# #                         if len(data["meta"]["syns"]) != 0:
# #                             synonyms = data["meta"]["syns"][0]
# #                         if len(data["meta"]["ants"]) != 0:
# #                             antonyms = data["meta"]["ants"][0]
# #                         for results in data["def"][0]["sseq"][0][0][1]["dt"]:
# #                             if results[0] == "text":
# #                                 definition = results[1]
# #                             if results[0] == "vis":
# #                                 example = results[1][0]["t"].replace("{it}", "*").\
# #                                     replace("{/it}", "*")
# #                     except KeyError as e:
# #                         print(e)
# #             except TypeError as e:
# #                 print(e)
# #             break
# #     word_metadata["meaning"] = definition
# #     word_metadata["examples"] = example
# #     word_metadata["antonyms"] = antonyms
# #     word_metadata["synonyms"] = synonyms
# #     return word_metadata


# # if __name__ == "__main__":
# #     app.run(port = '4000', debug = True)





























from flask import Flask,render_template,url_for,redirect,request
import json
import requests
import sqlite3
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
        username = request.form['username']
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
'''
    # <!DOCTYPE html>
    # <html style="background-color: #33475b">
    # <body>
    # <h1 style = 'color:White'>{name}</h1>
    # </body>
    # </html>
    # '''

@app.route("/Synonyms", methods = ['POST', 'GET'])   
def Synonyms():
    word = ''
    r=''
    if request.method == 'POST':
        word = request.form['word']
        conn = sqlite3.connect('./web.db')
        c = conn.cursor()
        check_word = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}'"
        word_count = ((c.execute(check_word)).fetchone())[0]
        if(word_count!=0):
            check_syn = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}' AND synonyms IS NULL"
            syn_count = ((c.execute(check_syn)).fetchone())[0]
            if(syn_count!=0):
                r = str((get_dictionary_response(word))["synonyms"][0:3])
                update_synonym = f"UPDATE vocabulary SET synonyms='{r}' WHERE word='{word}'"
            else:
                syn = f"SELECT synonyms FROM vocabulary WHERE word='{word}'"
                r = ((c.execute(syn)).fetchone())[0]
        else:
            word_insert = "INSERT INTO vocabulary (word) VALUES (?)"
            c.execute(word_insert, (word,))
            r = str((get_dictionary_response(word))["synonyms"][0:3])
            update_synonym = "UPDATE vocabulary SET synonyms=? WHERE word=?"
            c.execute(update_synonym, (r, word))
        conn.commit()
    return redirect(url_for('well',name = 'Synonyms of '+ word + " : " + r))


@app.route("/Antonyms", methods = ['POST', 'GET'])
def Antonyms():
    word = ''
    r=''
    if request.method == 'POST':
        word = request.form['word']
        conn = sqlite3.connect('./web.db')
        c = conn.cursor()
        check_word = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}'"
        word_count = ((c.execute(check_word)).fetchone())[0]
        if(word_count!=0):
            check_syn = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}' AND antonyms IS NULL"
            syn_count = ((c.execute(check_syn)).fetchone())[0]
            if(syn_count!=0):
                r = str((get_dictionary_response(word))["antonyms"][0:3])
                update_synonym = f"UPDATE vocabulary SET antonyms='{r}' WHERE word='{word}'"
            else:
                syn = f"SELECT antonyms FROM vocabulary WHERE word='{word}'"
                r = ((c.execute(syn)).fetchone())[0]
        else:
            word_insert = "INSERT INTO vocabulary (word) VALUES (?)"
            c.execute(word_insert, (word,))
            r = str((get_dictionary_response(word))["antonyms"][0:3])
            update_synonym = "UPDATE vocabulary SET antonyms=? WHERE word=?"
            c.execute(update_synonym, (r, word))
        conn.commit()
    return redirect(url_for('well',name = 'Antonyms of '+ word + " : " +r))


@app.route("/Definition", methods = ['POST', 'GET'])
def Definition():
    word = ''
    r=''
    if request.method == 'POST':
        word = request.form['word']
        conn = sqlite3.connect('./web.db')
        c = conn.cursor()
        check_word = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}'"
        word_count = ((c.execute(check_word)).fetchone())[0]
        if(word_count!=0):
            check_syn = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}' AND definition IS NULL"
            syn_count = ((c.execute(check_syn)).fetchone())[0]
            if(syn_count!=0):
                r = str((get_dictionary_response(word))["meaning"])
                update_synonym = f"UPDATE vocabulary SET definition='{r}' WHERE word='{word}'"
            else:
                syn = f"SELECT definition FROM vocabulary WHERE word='{word}'"
                r = ((c.execute(syn)).fetchone())[0]
        else:
            word_insert = "INSERT INTO vocabulary (word) VALUES (?)"
            c.execute(word_insert, (word,))
            r = str((get_dictionary_response(word))["meaning"])
            update_synonym = "UPDATE vocabulary SET definition=? WHERE word=?"
            c.execute(update_synonym, (r, word))
        conn.commit()
    return redirect(url_for('well',name = 'Definition of '+ word + " : " +r))


@app.route("/Sentence", methods = ['POST', 'GET'])
def Sentence():
    word = ''
    r = ''
    if request.method == 'POST':
        word = request.form['word']
        conn = sqlite3.connect('./web.db')
        c = conn.cursor()
        check_word = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}'"
        word_count = ((c.execute(check_word)).fetchone())[0]
        if(word_count!=0):
            check_syn = f"SELECT COUNT(*) FROM vocabulary WHERE word='{word}' AND sentence IS NULL"
            syn_count = ((c.execute(check_syn)).fetchone())[0]
            if(syn_count!=0):
                r = str((get_dictionary_response(word))["examples"])
                update_synonym = f"UPDATE vocabulary SET sentence='{r}' WHERE word='{word}'"
            else:
                syn = f"SELECT sentence FROM vocabulary WHERE word='{word}'"
                r = ((c.execute(syn)).fetchone())[0]
        else:
            word_insert = "INSERT INTO vocabulary (word) VALUES (?)"
            c.execute(word_insert, (word,))
            r = str((get_dictionary_response(word))["examples"])
            update_synonym = "UPDATE vocabulary SET sentence=? WHERE word=?"
            c.execute(update_synonym, (r, word))
        conn.commit()
    return redirect(url_for('well',name = 'Example of '+ word + " : " +r))

def get_dictionary_response(word):
    word_metadata = {}
    definition = "sorry, no definition is available."
    example = "sorry, no examples are available."
    synonyms = ["sorry, no synonyms are available."]
    antonyms = ["sorry, no antonyms are available."]
    # api_key = os.getenv("KEY_THESAURUS")
    url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b3b73004-8412-455e-a40a-2cfb3d87e9ee"
    response = requests.get(url)
    api_response = json.loads(response.text)
    if response.status_code == 200:
        for data in api_response:
            try:
                if data["meta"]["id"] == word:
                    try:
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
                    except KeyError as e:
                        print(e)
            except TypeError as e:
                print(e)
            break
    word_metadata["meaning"] = definition
    word_metadata["examples"] = example
    word_metadata["antonyms"] = antonyms
    word_metadata["synonyms"] = synonyms
    return word_metadata


if __name__ == "__main__":
    check = False;
    app.run(port = '4000', debug = True)










# from flask import Flask, render_template, url_for, redirect, request
# import json
# import requests
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
# db = SQLAlchemy(app)


# class Words(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     word = db.Column(db.String(100))


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(50))
#     email = db.Column(db.String(120), unique=True)


# @app.route("/hell")
# def hell():
#     return render_template('index.html')


# @app.route('/home')
# def home():
#     return render_template('index.html')


# @app.route('/contact')
# def contact():
#     return render_template('contact.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/login')
# def login():
#     return render_template('login.html')


# @app.route('/user')
# def user():
#     return render_template('user_details.html')


# @app.route('/history')
# def history():
#     data = ''
#     words = Words.query.all()
#     for word in words:
#         data += str(word.word)
#     return render_template('history.html', word=str(data))


# @app.route("/Login", methods=['POST', 'GET'])
# def Login():
#     username = ''
#     password = ''
#     email = ''
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         user = Users(username=username, password=password, email=email)
#         db.session.add(user)
#         db.session.commit()
#         result = Users.query.with_entities(Users.username).all()
#     return render_template('user_index.html', word=str(result[-1][0]))


# @app.route("/well/<name>")
# def well(name):
#     return f'''
#         # <!DOCTYPE html>
#         # <html style="background-color: #33475b">
#         # <body>
#         # <h1 style = 'color:White'>{name}</h1>
#         # </body>
#         # </html>
#         # '''


# @app.route("/Synonyms", methods=['POST', 'GET'])
# def Synonyms():
#     word = ''
#     if request.method == 'POST':
#         word = request.form['word']
#         word_entry = Words(word=word)
#         db.session.add(word_entry)
#         db.session.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well', name='Synonyms of ' + word + " : " + str(r["synonyms"])))


# @app.route("/Antonyms", methods=['POST', 'GET'])
# def Antonyms():
#     word = ''
#     if request.method == 'POST':
#         word = request.form['word']
#         word_entry = Words(word=word)
#         db.session.add(word_entry)
#         db.session.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well', name='Antonyms of ' + word + " : " + str(r["antonyms"])))


# @app.route("/Definition", methods=['POST', 'GET'])
# def Definition():
#     word = ''
#     if request.method == 'POST':
#         word = request.form['word']
#         word_entry = Words(word=word)
#         db.session.add(word_entry)
#         db.session.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well', name='Definition of ' + word + " : " + r["meaning"]))


# @app.route("/Sentence", methods=['POST', 'GET'])
# def Sentence():
#     word = ''
#     r = 0
#     if request.method == 'POST':
#         word = request.form['word']
#         word_entry = Words(word=word)
#         db.session.add(word_entry)
#         db.session.commit()
#         r = get_dictionary_response(word)
#     return redirect(url_for('well',name = 'Example of '+ word + " : " +r["examples"]))

# def get_dictionary_response(word):
#     word_metadata = {}
#     definition = "sorry, no definition is available."
#     example = "sorry, no examples are available."
#     synonyms = ["sorry, no synonyms are available."]
#     antonyms = ["sorry, no antonyms are available."]
#     # api_key = os.getenv("KEY_THESAURUS")
#     url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b3b73004-8412-455e-a40a-2cfb3d87e9ee"
#     response = requests.get(url)
#     api_response = json.loads(response.text)
#     if response.status_code == 200:
#         for data in api_response:
#             try:
#                 if data["meta"]["id"] == word:
#                     try:
#                         if len(data["meta"]["syns"]) != 0:
#                             synonyms = data["meta"]["syns"][0]
#                         if len(data["meta"]["ants"]) != 0:
#                             antonyms = data["meta"]["ants"][0]
#                         for results in data["def"][0]["sseq"][0][0][1]["dt"]:
#                             if results[0] == "text":
#                                 definition = results[1]
#                             if results[0] == "vis":
#                                 example = results[1][0]["t"].replace("{it}", "*").\
#                                     replace("{/it}", "*")
#                     except KeyError as e:
#                         print(e)
#             except TypeError as e:
#                 print(e)
#             break
#     word_metadata["meaning"] = definition
#     word_metadata["examples"] = example
#     word_metadata["antonyms"] = antonyms
#     word_metadata["synonyms"] = synonyms
#     return word_metadata


# if __name__ == "__main__":
#     app.run(port = '4000', debug = True)

