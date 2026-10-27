from datetime import date
import random
import streamlit as st
import streamlit.components.v1 as components

# Configurações da página
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌", layout="centered")

# Controle de em qual página ele está
if "pagina" not in st.session_state:
    st.session_state.pagina = 1

# ========================================================
# PÁGINA 1: O CORAÇÃO DE LUZES DANÇANTES (ANIMAÇÃO)
# ========================================================
if st.session_state.pagina == 1:
    st.markdown("<h2 style='text-align: center; color: #ff4b72;'>✨ Um presente especial para você ✨</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Observe a mágica acontecer...</p>", unsafe_allow_html=True)

    # Animação em HTML5 e JavaScript de luzinhas dançando e formando o coração
    animacao_luzes = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {
        margin: 0;
        background: transparent;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      canvas {
        background: radial-gradient(circle, #210d1b 0%, #0c0814 100%);
        border-radius: 20px;
        box-shadow: 0 0 25px rgba(255, 75, 114, 0.4);
      }
    </style>
    </head>
    <body>
    <canvas id="c"></canvas>
    <script>
      const canvas = document.getElementById('c');
      const ctx = canvas.getContext('2d');
      const width = canvas.width = 340;
      const height = canvas.height = 360;

      const numParticles = 220;
      const particles = [];
      const colors = ['#ff2a6d', '#ff62a5', '#ffe66d', '#ffffff', '#9b5de5'];

      // Equação matemática do coração
      function getHeartPoint(angle) {
        const x = 16 * Math.pow(Math.sin(angle), 3);
        const y = -(13 * Math.cos(angle) - 5 * Math.cos(2 * angle) - 2 * Math.cos(3 * angle) - Math.cos(4 * angle));
        return { x: x, y: y };
      }

      for (let i = 0; i < numParticles; i++) {
        const angle = (Math.PI * 2 * i) / numParticles;
        const target = getHeartPoint(angle);
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          originX: target.x,
          originY: target.y,
          size: Math.random() * 2.5 + 1.5,
          color: colors[Math.floor(Math.random() * colors.length)],
          speed: Math.random() * 0.04 + 0.02,
          wobble: Math.random() * Math.PI * 2,
          radius: Math.random() * 8 + 3
        });
      }

      let tick = 0;
      function animate() {
        // Rastro de luz suave
        ctx.fillStyle = 'rgba(12, 8, 20, 0.2)';
        ctx.fillRect(0, 0, width, height);
        tick += 0.03;

        // Pulsação suave do coração
        const scale = 8.5 + Math.sin(tick * 2) * 0.7;
        const centerX = width / 2;
        const centerY = height / 2 - 10;

        particles.forEach(p => {
          p.wobble += 0.05;
          const targetX = centerX + p.originX * scale + Math.cos(p.wobble) * p.radius;
          const targetY = centerY + p.originY * scale + Math.sin(p.wobble) * p.radius;

          // Luzes deslizando em direção ao formato do coração
          p.x += (targetX - p.x) * p.speed;
          p.y += (targetY - p.y) * p.speed;

          // Efeito de brilho neon
          ctx.save();
          ctx.shadowBlur = 12;
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
    
    # Exibe a animação no centro da tela
    components.html(animacao_luzes, height=380)

    st.write("")
    if st.button("✨ Tocar para Entrar no Nosso Presente ✨", use_container_width=True):
        st.session_state.pagina = 2
        st.rerun()

# ========================================================
# PÁGINA 2: BOAS-VINDAS E CONTADOR DE DIAS
# ========================================================
if st.session_state.pagina == 2:
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
# PÁGINA 3: OS CUPONS DE PRESENTE
# ==========================================
elif st.session_state.pagina == 3:
    st.title("🎫 Etapa 1: Seus Cupons")
    st.write("Antes do teste, você ganhou alguns mimos. Clique para sortear:")
    
    cupons = [
        "Vale um cafuné até você dormir 💤",
        "Vale uma massagem relaxante 💆‍♂️",
        "Vale eu escolher o filme hoje 🎬",
        "Vale um espetinho por minha conta ",
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
# PÁGINA 4: O QUIZ (BLOQUEIO DA CARTINHA)
# ==========================================
elif st.session_state.pagina == 4:
    st.title("🧠 Etapa 2: Quiz do Casal")
    st.write("A cartinha secreta só será destrancada se você responder a este teste!")
    
    # PERGUNTA 1
    p1 = st.radio(
        "1) Onde foi o nosso primeiro beijo?",
        ["No cinema", "Na pracinha", "No carro", "Na minha casa"]
    )
    
    # PERGUNTA 2
    p2 = st.radio(
        "2) Quem é mais dorminhoco(a)?",
        ["Você", "Eu", "Os dois iguais"]
    )
    
    st.write("")
    if st.button("Confirmar Respostas e Destrancar Cartinha 🔓"):
        # PERSONALIZAÇÃO: Escolha as respostas certas aqui
        if p1 == "Na minha casa" and p2 == "Eu":
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
# PÁGINA 5: A CARTINHA SECRETA (FINAL)
# ==========================================
elif st.session_state.pagina == 5:
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
