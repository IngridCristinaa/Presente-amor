from datetime import date
import random
import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌", layout="wide")

# Memória de navegação entre as páginas
if "pagina" not in st.session_state:
    st.session_state.pagina = 1

# ========================================================
# PÁGINA 1: CORAÇÃO EM TELA CHEIA (SHOW DE LUZES)
# ========================================================
if st.session_state.pagina == 1:
    # Remove as margens e barras do Streamlit para ficar em tela cheia total
    st.markdown("""
        <style>
            header[data-testid="stHeader"] { display: none !important; }
            footer { display: none !important; }
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100vw !important;
                height: 100vh !important;
                overflow: hidden !important;
            }
            iframe {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 100vw !important;
                height: 100vh !important;
                border: none !important;
                z-index: 1 !important;
            }
            /* Botão flutuante na parte de baixo da tela */
            div.stButton {
                position: fixed !important;
                bottom: 40px !important;
                left: 50% !important;
                transform: translateX(-50%) !important;
                z-index: 99999 !important;
                width: 85% !important;
                max-width: 320px !important;
            }
            div.stButton > button {
                background: linear-gradient(135deg, #ff2a6d, #9b5de5) !important;
                color: white !important;
                border: 1px solid rgba(255,255,255,0.4) !important;
                border-radius: 50px !important;
                padding: 14px 20px !important;
                font-size: 16px !important;
                font-weight: bold !important;
                box-shadow: 0 0 25px rgba(255, 42, 109, 0.8) !important;
                width: 100% !important;
                transition: transform 0.2s ease !important;
            }
            div.stButton > button:hover {
                transform: scale(1.05) !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Animação que ocupa 100% da tela
    animacao_tela_cheia = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      body, html {
        width: 100%;
        height: 100%;
        overflow: hidden;
        background: radial-gradient(ellipse at center, #1b0a1d 0%, #07040a 100%);
      }
      canvas {
        display: block;
        width: 100vw;
        height: 100vh;
      }
    </style>
    </head>
    <body>
    <canvas id="c"></canvas>
    <script>
      const canvas = document.getElementById('c');
      const ctx = canvas.getContext('2d');

      function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      const numParticles = 280;
      const particles = [];
      const colors = ['#ff2a6d', '#ff62a5', '#ffe66d', '#ffffff', '#b388ff', '#ff85a1'];

      function getHeartPoint(angle) {
        const x = 16 * Math.pow(Math.sin(angle), 3);
        const y = -(13 * Math.cos(angle) - 5 * Math.cos(2 * angle) - 2 * Math.cos(3 * angle) - Math.cos(4 * angle));
        return { x: x, y: y };
      }

      for (let i = 0; i < numParticles; i++) {
        const angle = (Math.PI * 2 * i) / numParticles;
        const target = getHeartPoint(angle);
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          originX: target.x,
          originY: target.y,
          size: Math.random() * 2.5 + 1.2,
          color: colors[Math.floor(Math.random() * colors.length)],
          speed: Math.random() * 0.035 + 0.02,
          wobble: Math.random() * Math.PI * 2,
          radius: Math.random() * 12 + 4,
          isSparkle: Math.random() > 0.8
        });
      }

      let tick = 0;
      function animate() {
        // Rastro suave de luz
        ctx.fillStyle = 'rgba(7, 4, 10, 0.22)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        tick += 0.03;

        // Escala adaptável para qualquer tela (celular ou PC)
        const baseSize = Math.min(canvas.width, canvas.height);
        const scale = (baseSize / 38) + Math.sin(tick * 2.2) * (baseSize / 350);
        const centerX = canvas.width / 2;
        const centerY = (canvas.height / 2) - (canvas.height * 0.05);

        particles.forEach(p => {
          p.wobble += 0.05;
          const targetX = centerX + p.originX * scale + Math.cos(p.wobble) * p.radius;
          const targetY = centerY + p.originY * scale + Math.sin(p.wobble) * p.radius;

          p.x += (targetX - p.x) * p.speed;
          p.y += (targetY - p.y) * p.speed;

          ctx.save();
          ctx.shadowBlur = p.isSparkle ? 18 : 10;
          ctx.shadowColor = p.color;
          ctx.fillStyle = p.color;
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        });

        requestAnimationFrame(animate);
      }
      animate();
    </script>
    </body>
    </html>
    """

    components.html(animacao_tela_cheia)

    # Botão flutuante que avança para a próxima página
    if st.button("✨ Tocar para Começar ✨"):
        st.session_state.pagina = 2
        st.rerun()

# ========================================================
# PÁGINA 2: BOAS-VINDAS E CONTADOR DE DIAS
# ========================================================
elif st.session_state.pagina == 2:
    st.title("Oi, meu amor! ❤️")
    st.write("Esse espacinho foi programado especialmente para você, com cada memória nossa guardada.")

    # SUA DATA (Ano, Mês, Dia sem zeros na frente!)
    data_inicio = date(2025, 2, 9)
    dias = (date.today() - data_inicio).days

    st.info(f"✨ Nós já estamos juntos há **{dias} dias**!")
    st.write("E cada dia ao seu lado é o melhor capítulo da minha história.")

    st.write("")
    if st.button("Ver Meus Cupons Especiais 🎁 ➡️", use_container_width=True):
        st.session_state.pagina = 3
        st.rerun()

# ========================================================
# PÁGINA 3: CUPONS DE MIMOS
# ========================================================
elif st.session_state.pagina == 3:
    st.title("🎫 Etapa 1: Seus Cupons")
    st.write("Você merece mimos! Clique abaixo para tirar um vale-presente:")

    cupons = [
        "Vale um cafuné gostoso até dormir 💤",
        "Vale uma massagem relaxante 💆‍♂️",
        "Vale escolher o jantar de hoje",
        "Vale um abraço quentinho de 5 minutos 🫂",
        "Vale um dia inteiro sem eu reclamar de nada 😇"
    ]

    if st.button("Sortear um Cupom! 🎉", use_container_width=True):
        cupom = random.choice(cupons)
        st.success(f"👉 **{cupom}**")
        st.balloons()

    st.write("---")
    st.write("Agora preciso testar a sua memória antes de liberar a surpresa final...")
    if st.button("Ir para o Quiz do Casal 🧠 ➡️", use_container_width=True):
        st.session_state.pagina = 4
        st.rerun()

# ========================================================
# PÁGINA 4: O QUIZ (BLOQUEIO DA CARTA)
# ========================================================
elif st.session_state.pagina == 4:
    st.title("🧠 Etapa 2: Quiz do Amor")
    st.write("Responda certinho para destrancar a cartinha secreta:")

    # PERGUNTA 1
    p1 = st.radio(
        "1) Onde foi o nosso primeiro beijo?",
        ["No cinema", "Na pracinha", "No carro", "Na minha casa"]
    )

    # PERGUNTA 2
    p2 = st.radio(
        "2) Quem se apaixonou primeiro?",
        ["Você", "Eu", "Os dois no mesmo instante"]
    )

    st.write("")
    if st.button("Confirmar Respostas 🔓", use_container_width=True):
        # PERSONALIZE SUAS RESPOSTAS AQUI:
        if p1 == "Na minha casa" and p2 == "Você":
            st.session_state.quiz_resolvido = True
            st.success("✅ Você acertou tudo perfeitamente! Memória nota 10!")
            st.snow()
        else:
            st.warning("Hum... quase! Dá uma pensadinha com mais carinho 😂")

    # Só libera o botão da carta quando ele acertar tudo!
    if st.session_state.get("quiz_resolvido", False):
        st.write("---")
        if st.button("💌 Abrir Minha Carta Secreta 💌", use_container_width=True):
            st.session_state.pagina = 5
            st.rerun()

# ========================================================
# PÁGINA 5: A CARTA SECRETA
# ========================================================
elif st.session_state.pagina == 5:
    st.balloons()
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
