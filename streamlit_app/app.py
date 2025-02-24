import streamlit as st
import requests
import pandas as pd

# URL da sua API Django
API_URL = "http://127.0.0.1:8000/api/pecas/"

# Função para obter os dados da API
def get_produtos():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao carregar dados!")
        return []

# Função para adicionar um novo produto
def add_produto(nome, preco):
    data = {"nome": nome, "preco": preco}
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        st.success("Produto cadastrado com sucesso!")
    else:
        st.error("Erro ao cadastrar produto!")

# Interface Streamlit
st.title("Cadastro de Produtos")

# Mostrar lista de produtos
st.header("Lista de Produtos")
produtos = get_produtos()

# Exibindo os produtos em uma tabela
if produtos:
    df = pd.DataFrame(produtos)
    st.dataframe(df)

# Adicionar novo produto
st.header("Adicionar Novo Produto")
nome = st.text_input("Nome do Produto")
preco = st.number_input("Preço do Produto", min_value=0.0, step=0.1)

if st.button("Cadastrar Produto"):
    if nome and preco:
        add_produto(nome, preco)
    else:
        st.warning("Por favor, preencha todos os campos.")
