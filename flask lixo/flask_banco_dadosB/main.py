from flask import Flask, render_template, request, redirect
import mysql.connector as db

app = Flask(__name__)

conexao = db.connect(
    host="localhost",
    user="estudante",
    passwd="ifcbrusque",
    database="3infoB"
)
cursor = conexao.cursor(dictionary=True)

@app.route('/')
def home():
    meus_animais=[ 
                    {"id_animal":"1", "nome":"gato"}, 
                    {"id_animal":"2", "nome":"cachorro"} 
                 ]
    
    conteudo = render_template("index.html", animais=meus_animais)
    return conteudo 

@app.route("/cadastrar", methods=['GET',"POST"])
def cadastrar():

    novoAnimal = request.form["nome_incluir"]
    sql = f"INSERT INTO `3infoB`.`animais` (`nome`) VALUES ('{novoAnimal}');"
    cursor.execute(sql)
    conexao.commit()

    conteudo = render_template("index.html")
    return conteudo

if __name__ == '__main__':
    app.run(debug=True)