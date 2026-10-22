import json
import random
import sqlite3
from pathlib import Path
from uuid import  uuid4


from flask import Flask,render_template,request

app = Flask(__name__)

def abrir_arquivo():
    try:
        with open("estoque.json","r",encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def salvar_arquivo(estoque):
    with open("estoque.json","w",encoding="utf-8") as arquivo:
        json.dump(estoque,arquivo,indent=4,ensure_ascii=False)

registro_ID = []
lista_categoria = ["celular", "Televisão", "console", "notebook", "tablet"]
class Produto:
    def __init__(self,nome,quantidade,preco,categoria,descricao,imagem):
        self.id = random.randint(000000,999999)
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria
        self.descricao = descricao
        self.imagem = imagem


    def cadastar(self):
        lista_categoria = ["celular", "Televisão", "console", "notebook", "tablet"]

        if self.id in registro_ID:
            while self.id in registro_ID:
                self.id += 1

        registro_ID.append(self.id)

        if not self.nome:
            raise ValueError("Nome não pode ser vazio")

        if self.quantidade < 0:
            raise ValueError("estoque não pode ser negativado")

        if self.preco <= 0:
            raise ValueError("valor zerado ou negativo são proibidos")

        if self.categoria not in lista_categoria:
            raise ValueError("categoria inválid")

        caminho_imagem = None

        if self.imagem and self.imagem.filename:
            extensao = Path(self.imagem.filename).suffix.lower()

            if extensao not in {".jpg", ".jpeg", ".png", ".webp"}:
                raise ValueError("Formato não suportado")

            pasta = Path(app.static_folder) / "uploads"
            pasta.mkdir(parents=True, exist_ok=True)

            nome_arquivo = f"{uuid4().hex}{extensao}"

            self.imagem.save(pasta / nome_arquivo)
            caminho_imagem = f"uploads/{nome_arquivo}"

        self.imagem = caminho_imagem

        novo_produto = {
            "ID": self.id,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preço": self.preco,
            "descrição": self.descricao,
            "categoria": self.categoria,
            "imagem": self.imagem
        }
        con = sqlite3.connect("estoque.db")

        try:
            cur = con.cursor()

            cur.execute(
                """
                INSERT INTO PRODUTO
                    (ID, NOME, QUANTIDADE, PRECO, DESCRICAO, CATEGORIA,IMAGEM)
                VALUES (?, ?, ?, ?, ?, ?,?)
                """,
                (
                    self.id,
                    self.nome,
                    self.quantidade,
                    self.preco,
                    self.descricao,
                    self.categoria,
                    self.imagem
                )
            )

            con.commit()
        finally:
            con.close()

        estoque = abrir_arquivo()
        estoque.append(novo_produto)
        salvar_arquivo(estoque)



@app.route("/cadastrar",methods=["GET","POST"])
def cadastrar_produto():
    erro = None
    mensagem = None
    try:
        if request.method == "POST":
            nome = request.form.get("nome", "")
            quantidade = int(request.form.get("quantidade"))
            preco = float(request.form.get("preco", ""))
            descricao = request.form.get("descricao","")
            categoria = request.form.get("categoria","")
            imagem = request.files.get("imagem")


            produto = Produto(nome=nome, quantidade=quantidade, preco=preco, descricao=descricao, categoria=categoria, imagem=imagem)

            produto.cadastar()
            mensagem = "Produto cadastrado!"
    except ValueError as error:
        erro = str(error)

    return render_template(
        "cadastrar.html",
        erro=erro,
        mensagem=mensagem,
        lista_categoria=lista_categoria
    )


if __name__ == "__main__":
    app.run(debug=True,port=5001)