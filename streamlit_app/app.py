import streamlit as st
import pandas as pd
import requests

# Configuração da página
st.set_page_config(page_title="Cadastro de Produtos", layout="wide", page_icon="🛒")

# CSS personalizado para o layout
st.markdown("""
    <style>
    /* Estilo para o título da página */
    .css-1v3fvcr {
        font-size: 40px;
        color: #1ABC9C;
    }
    /* Estilo para os headers */
    h1, h2, h3 {
        color: #FFFFFF;
    }
    /* Estilo para o background da página */
    .reportview-container {
        background-color: #2C3E50;
    }
    /* Estilo para a barra lateral */
    .sidebar .sidebar-content {
        background-color: #34495E;
    }
    </style>
""", unsafe_allow_html=True)

# Função para obter os dados da API
API_URL = "http://127.0.0.1:8000/api/produtos/"

# Função para obter os produtos de uma categoria
def get_produtos_by_categoria(categoria):
    response = requests.get(f"{API_URL}?categoria={categoria}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao carregar dados!")
        return []

# Função para adicionar um novo produto
def add_produto(nome, preco, descricao, categoria):
    data = {"nome": nome, "preco": preco, "descricao": descricao, "categoria": categoria}
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        st.success("Produto cadastrado com sucesso!")
    else:
        st.error(f"Erro ao cadastrar produto! Código: {response.status_code}, Detalhes: {response.json()}")

# Barra lateral para navegação de categorias
with st.sidebar:
    st.title("Menu de Navegação")
    categoria_selecionada = st.selectbox("Escolha uma categoria", ["Monitores", "Gabinete", "Cabos de Vídeo Adaptadores", "Headsets com Fio USB", "Mouses Wireless"])

# Título principal
st.title("Cadastro de Produtos 🛒")

# Seção para exibir as categorias
if categoria_selecionada:
    st.header(f"Produtos da categoria: {categoria_selecionada}")
    produtos = get_produtos_by_categoria(categoria_selecionada)

    # Exibindo os produtos da categoria selecionada
    if produtos:
        df = pd.DataFrame(produtos)
        st.dataframe(df)
    else:
        st.warning(f"Não há produtos cadastrados na categoria '{categoria_selecionada}'.")

# Seção para adicionar um novo produto
with st.expander("Adicionar Novo Produto"):
    st.subheader("Preencha os dados do novo produto")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço do Produto", min_value=0.0, step=0.1)
    descricao = st.text_area("Descrição do Produto")
    categoria = st.selectbox("Categoria do Produto", ["Monitores", "Gabinete", "Cabos de Vídeo Adaptadores", "Headsets com Fio USB", "Mouses Wireless"])
    
    if st.button("Cadastrar Produto"):
        if nome and preco and descricao and categoria:
            add_produto(nome, preco, descricao, categoria)
        else:
            st.warning("Por favor, preencha todos os campos.")
