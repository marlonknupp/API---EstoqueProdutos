import streamlit as st
import requests

# URL da API Django
url = 'http://127.0.0.1:8000/api/categorias/'  # Atualize com a URL correta da sua API

# Tentar obter os dados da API
try:
    response = requests.get(url)
    response.raise_for_status()  # Lança um erro se a requisição falhar
    categorias = response.json()  # Converte a resposta para JSON
except requests.exceptions.RequestException as e:
    st.error(f"Erro ao conectar com a API: {e}")
    categorias = []  # Se der erro, categorias será uma lista vazia

# Criar um dicionário para mapear categorias aos produtos (se os dados forem válidos)
categoria_dict = {
    categoria['nome']: categoria.get('produtos', [])  # Garante que 'produtos' sempre exista
    for categoria in categorias
}

# Adicionando a cor de fundo azul claro e a faixa azul acima do catálogo de produtos
st.markdown(
    """
    <style>
    /* Cor de fundo azul clara para toda a página */
    .main {
        background-color: #e6f7ff;  /* Azul claro */
    }

    .catalog-banner {
        background-color: #0056b3;
        color: white;
        padding: 20px;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    <div class="catalog-banner">
        Catálogo de Produtos 🛍️
    </div>
    """,
    unsafe_allow_html=True
)

# Criar expanders para cada categoria
for categoria, produtos in categoria_dict.items():
    with st.expander(f"📂 {categoria}", expanded=False):
        if produtos:
            for produto in produtos:
                with st.container():

                    st.markdown(f"<h6 style='margin-bottom:3px; font-size:15px;'>{produto.get('nome', 'Produto sem nome')}</h6>", unsafe_allow_html=True)
                    st.write(f"**Descrição:** {produto.get('descricao', 'Sem descrição disponível')}")

                    preco = produto.get('preco', 0)
                    try:
                        preco = float(preco)
                        st.write(f"**Preço:** R${preco:.2f}")
                    except ValueError:
                        st.write("**Preço:** Não disponível")
                    
                    st.divider()
        else:
            st.warning("Nenhum produto disponível nesta categoria.")
