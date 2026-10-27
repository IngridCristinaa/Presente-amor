from datetime import date
import random
import streamlit as st

# Configura a página para ficar bonita no celular
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌")

st.title("Oi, meu amor! ❤️")
st.write("Eu fiz esse aplicativo usando **Python** especialmente para você!")

# 1. CONTADOR DE DIAS (Mude aqui a data que começaram a namorar: Ano, Mês, Dia)
data_inicio = date(2025, 2, 9)
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
Meu amor,
Se você está lendo isso, é porque chegou a uma
das minhas partes favoritas deste aplicativo:
um pedacinho do meu coração escrito para você.
Às vezes, acho que nem as palavras mais bonitas
seriam suficientes para explicar o quanto você
é especial para mim.
Entre tantos caminhos que a vida poderia me
levar, sou feliz por ter encontrado você.
Você faz parte dos meus pensamentos, dos meus
planos e dos sonhos que quero realizar.
Eu amo os detalhes, os momentos simples,
as conversas, as risadas e até aqueles dias
em que tudo o que precisamos é ficar juntinhos.
Não quero apenas viver os dias bons com você.
Quero construir uma história, superar desafios,
celebrar conquistas e continuar escolhendo você,
mesmo quando a vida não for tão fácil.
Que nunca nos faltem carinho, cumplicidade,
respeito, paciência e motivos para sorrir juntos.
Se eu pudesse te dar uma coisa neste momento,
seria a oportunidade de enxergar a si mesmo
pelos meus olhos. Assim você entenderia o quanto
é importante para mim e o tamanho do amor
que guardo aqui dentro.
Obrigada por fazer parte da minha vida,
por ser meu amor e por compartilhar comigo
um pedacinho tão bonito da sua história.
E se eu pudesse voltar no tempo e escolher
novamente, entre tantas possibilidades,
meu coração ainda procuraria você.
Eu te amo, hoje, amanhã e em todos os
capítulos que ainda vamos escrever juntos.

Com todo meu amor, **da sua programadora favorita.** 💕
""")
