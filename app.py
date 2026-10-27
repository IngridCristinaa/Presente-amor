from datetime import date
import random
import streamlit as st

# Configura a página do celular
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌")

# Memória para saber em qual página ele está (começa na página 1)
if "pagina" not in st.session_state:
    st.session_state.pagina = 1

# ==========================================
# PÁGINA 1: BOAS-VINDAS E DIAS JUNTOS
# ==========================================
if st.session_state.pagina == 1:
    st.title("Oi, meu amor! ❤️")
    st.write("Preparei um presente interativo para você. Vamos ver se você consegue chegar até o final!")
    
    # SUA DATA (Ano, Mês, Dia sem zero na frente)
    data_inicio = date(2025, 2, 9)
    dias = (date.today() - data_inicio).days
    
    st.info(f"✨ Nós já estamos juntos há **{dias} dias**!")
    st.write("A cada dia eu tenho mais certeza de que você é o amor da minha vida.")
    
    st.write("")
    if st.button("Começar surpresa! ➡️"):
        st.session_state.pagina = 2
        st.rerun()

# ==========================================
# PÁGINA 2: OS CUPONS DE PRESENTE
# ==========================================
elif st.session_state.pagina == 2:
    st.title("🎫 Etapa 1: Seus Cupons")
    st.write("Antes do teste, você ganhou alguns mimos. Clique para sortear:")
    
    cupons = [
        "Vale um cafuné até você dormir 💤",
        "Vale uma massagem relaxante 💆‍♂️",
        "Vale eu escolher o filme hoje 🎬",
        "Vale uma pizza por minha conta 🍕",
        "Vale um abraço quentinho de 5 minutos 🫂"
    ]
    
    if st.button("Sortear cupom! 🎁"):
        cupom_sorteado = random.choice(cupons)
        st.success(f"👉 **{cupom_sorteado}**")
        st.balloons()
    
    st.write("---")
    st.write("Agora é a hora da verdade...")
    if st.button("Ir para o Quiz do Casal 🧠 ➡️"):
        st.session_state.pagina = 3
        st.rerun()

# ==========================================
# PÁGINA 3: O QUIZ (BLOQUEIO DA CARTINHA)
# ==========================================
elif st.session_state.pagina == 3:
    st.title("🧠 Etapa 2: Quiz do Casal")
    st.write("A cartinha secreta só será destrancada se você responder a este teste!")
    
    # PERGUNTA 1
    p1 = st.radio(
        "1) Onde foi o nosso primeiro beijo?",
        ["No cinema", "Na pracinha", "No carro", "Na casa de amigos"]
    )
    
    # PERGUNTA 2
    p2 = st.radio(
        "2) Quem é mais dorminhoco(a)?",
        ["Você", "Eu", "Os dois iguais"]
    )
    
    st.write("")
    if st.button("Confirmar Respostas e Destrancar Cartinha 🔓"):
        # PERSONALIZAÇÃO: Escolha as respostas certas aqui
        if p1 == "No carro" and p2 == "Você":
            st.session_state.quiz_resolvido = True
            st.success("✅ Parabéns, você lembrou de tudo perfeitamente!")
            st.snow()
        else:
            st.warning("Hum... quase lá! Dê uma olhadinha com carinho nas respostas 😂")

    # O botão para a carta só aparece se ele acertou o quiz!
    if st.session_state.get("quiz_resolvido", False):
        st.write("---")
        if st.button("Ler Minha Cartinha Secreta 💌 ➡️"):
            st.session_state.pagina = 4
            st.rerun()

# ==========================================
# PÁGINA 4: A CARTINHA SECRETA (FINAL)
# ==========================================
elif st.session_state.pagina == 4:
    st.balloons()  # Chuva de balões logo na abertura!
    st.title("💌 Para o Amor da Minha Vida")
    
    # PERSONALIZE A SUA CARTINHA AQUI:
    st.markdown("""
    Meu amor,
    
    Se você está lendo isso, é porque você passou por todas as etapas (e provou que tem boa memória!).
    
    Eu criei esse pequeno aplicativo em Python pensando em cada detalhe de nós dois.
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
