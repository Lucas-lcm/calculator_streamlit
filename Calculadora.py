import streamlit as sl

# Run aplication: streamlit run calculadora.py

# Operation tuple, for the selectbox options
opercacoes = ('','+', '-', '*', '/')

# Calculation function
def calcFunc():
    if operation == "+" and (numOne != "" or numTwo != ""):
        result = int(numOne) + int(numTwo)
        sl.metric(label= "Resultado: ", value=result)
    elif operation == "-" and (numOne != "" or numTwo != ""):
        result = int(numOne) - int(numTwo)
        sl.write(result)
    elif operation == "*" and (numOne != "" or numTwo != ""):
        result = int(numOne) * int(numTwo)
        sl.metric(label= "Resultado: ", value=result)
    elif operation == "/" and numTwo !=0 and (numOne != "" or numTwo != ""):
        result = int(numOne) / int(numTwo)
        sl.metric(label= "Resultado: ", value=result)
    elif numOne == "" or numTwo == "":
        sl.write('Aguardando valores')
    else:
        sl.write('Não foi possivel calcular!')

# Setting up columns
sl.set_page_config(layout="wide")
col1, col2, col3 = sl.columns([1, 4, 1])

with col2:
    # Subheader from the calculator
    sl.subheader('Calculadora simples de quatro operações:') 

    # Elements
    numOne = sl.text_input("Digite um número:", key="n1")

    numTwo = sl.text_input("Digite um número:", key="n2")

    operation = sl.selectbox("Qual operação deseja realizar? Selecione", key='op', options = opercacoes)

    calcFunc()

# Separator
sl.markdown("---")

# Title of the code explication
sl.header('Vamos verificar o código utilizado')

sl.text("Primeiro, vamos criar uma Tupla com as operações possíveis")

code_tupla = """
# Operatin tuple, for the selectbox options
opercacoes = ('','+', '-', '*', '/')
"""
sl.code(code_tupla, language="python")

sl.text("Agora a função que irá calcular os valores:")

code_function = """
# Calculation function
def calcFunc():
    if operation == "+" and (numOne != "" or numTwo != ""):
        result = int(numOne) + int(numTwo)
        sl.metric(label= "Resultado: ", value=result)
    elif operation == "-" and (numOne != "" or numTwo != ""):
        result = int(numOne) - int(numTwo)
        sl.write(result)
    elif operation == "*" and (numOne != "" or numTwo != ""):
        result = int(numOne) * int(numTwo)
        sl.metric(label= "Resultado: ", value=result)
    elif operation == "/" and numTwo !=0 and (numOne != "" or numTwo != ""):
        result = int(numOne) / int(numTwo)
        sl.metric(label= "Resultado: ", value=result)
    elif numOne == "" or numTwo == "":
        sl.write('Aguardando valores')
    else:
        sl.write('Não foi possivel calcular!')
"""
sl.code(code_function, language="python")

sl.text("Agora o front-end da aplicação usando Streamlit:")

code_front_end = """
# Setting up columns
sl.set_page_config(layout="wide")
col1, col2, col3 = sl.columns([1, 4, 1])

with col2:
    # Subheader from the calculator
    sl.subheader('Calculadora simples de quatro operações:') 

    # Elements
    numOne = sl.text_input("Digite um número:", key="n1")

    numTwo = sl.text_input("Digite um número:", key="n2")

    operation = sl.selectbox("Qual operação deseja realizar? Selecione", key='op', options = opercacoes)

    calcFunc()
"""
sl.code(code_front_end, language="python")

sl.text("Viu? Foi simples !")

sl.text("Primeiro o usamos o Python puro para realizar a lógica")

sl.text("Depois utuilizamos o Streamlit para criação do front-end e elementos")

sl.markdown("[Baixe o código completo dessa calculadora no meu Github](https://github.com/Lucas-lcm/calculator_streamlit)")

# Removing footer
sl.markdown("""
<style>
.css-cio0dv.egzxvld1
{
     visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Removing Bar
sl.markdown("""
<style>
.css-erpbzb.edgvbvh3
{
     visibility: hidden;
}
</style>
""", unsafe_allow_html=True)