import json
import random

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

lista_categoria = ["celular", "Televisão", "console", "notebook", "tablet"]
class Produto:
    def __init__(self,nome,quantidade,preco,categoria,descricao):
        self.id = random.randint(000000,999999)
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria
        self.descricao = descricao


    def cadastar(self):
        lista_categoria = ["celular", "Televisão", "console", "notebook", "tablet"]

        if not self.nome:
            raise ValueError("Nome não pode ser vazio")

        if self.quantidade < 0:
            raise ValueError("estoque não pode ser negativado")

        if self.preco <= 0:
            raise ValueError("valor zerado ou negativo são proibidos")

        if self.categoria not in lista_categoria:
            raise ValueError("categoria inválid")

        novo_produto = {
            "ID": self.id,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preço": self.preco,
            "descrição": self.descricao,
            "categoria": self.categoria
        }
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


            produto = Produto(nome=nome, quantidade=quantidade, preco=preco, descricao=descricao, categoria=categoria)

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
    app.run(debug=False,port=5001)