from datetime import date
import random
import streamlit as st

# Configura a página para ficar bonita no celular
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌")

st.title("Oi, meu amor! ❤️")
st.write("Eu fiz esse aplicativo usando **Python** especialmente para você!")

# 1. CONTADOR DE DIAS (Mude aqui a data que começaram a namorar: Ano, Mês, Dia)
data_inicio = date(2025, 2, 09)
dias = (date.today() - data_inicio).days

st.info(f"✨ Nós já estamos juntos há **{dias} dias**!")

# 2. POTE DE CUPONS
st.subheader("🎫 Tire um cupom de presente:")
if st.button("Clique para sortear um mimo!"):
    cupons = [
        "Vale um cafuné até você dormir 💤",
        "Vale uma massagem nas costas 💆‍♂️",
        "Vale eu pagar a pizza hoje 🍕",
        "Vale um abraço apertado de 5 minutos 🫂",
        "Vale um dia sem eu reclamar de nada 😇"
    ]
    st.success(f"👉 **{random.choice(cupons)}**")
    st.balloons()  # Solta balões de festa na tela do celular dele!

# 3. QUIZ DO CASAL
st.subheader("🧠 Mini Quiz: Será que você lembra?")
resposta = st.radio("Quem se apaixonou primeiro?", ["Você", "Eu", "Os dois ao mesmo tempo"])

if st.button("Confirmar resposta"):
    if resposta == "Você":  # Escolha a alternativa certa
        st.success("Acertou! Não resistiu aos meus encantos! 🥰")
        st.snow()  # Faz nevar na tela dele!
    else:
        st.error("Errou feio! Admite que foi você! 😂")

# 4. CARTINHA
st.subheader("💌 Minha cartinha para você:")
st.write("""
Obrigada por ser meu melhor amigo, meu porto seguro e a melhor parte do meu dia. 
Te amo daqui até o infinito!  
Com todo meu amor, **da sua programadora favorita.** 💕
""")
