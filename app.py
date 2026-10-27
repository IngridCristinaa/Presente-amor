from datetime import date
import random
import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌", layout="wide")

# Memória de navegação
if "pagina" not in st.session_state:
    st.session_state.pagina = 1

# ========================================================
# ESTILOS GERAIS (AURORA BOREAL, CANETA DE TINTEIRO E ANIMAÇÕES)
# ========================================================
if st.session_state.pagina >= 2:
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

            /* Fundo Aurora Boreal */
            .stApp {
                background: 
                    radial-gradient(circle at 15% 20%, rgba(0, 255, 179, 0.25) 0%, transparent 45%),
                    radial-gradient(circle at 85% 30%, rgba(168, 85, 247, 0.25) 0%, transparent 50%),
                    radial-gradient(circle at 50% 80%, rgba(0, 217, 255, 0.22) 0%, transparent 55%),
                    linear-gradient(160deg, rgba(6, 14, 28, 0.88) 0%, rgba(5, 32, 44, 0.85) 50%, rgba(20, 10, 38, 0.88) 100%) !important;
                background-attachment: fixed !important;
                background-size: cover !important;
            }

            /* Efeito da Carta se Desdobrando suavemente em 3D */
            @keyframes desdobrarCarta {
                0% {
                    opacity: 0;
                    transform: translateY(50px) scale(0.85) rotateX(15deg);
                    box-shadow: 0 0 0 rgba(255, 42, 109, 0);
                }
                70% {
                    transform: translateY(-8px) scale(1.02) rotateX(0deg);
                    box-shadow: 0 0 45px rgba(255, 215, 0, 0.45);
                }
                100% {
                    opacity: 1;
                    transform: translateY(0) scale(1) rotateX(0deg);
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
                }
            }

            /* Cartinha Manuscrita */
            .carta-tinteiro {
                font-family: 'Great Vibes', cursive !important;
                font-size: 29px !important;
                line-height: 1.8 !important;
                color: #fff9ea !important;
                background: rgba(255, 255, 255, 0.08) !important;
                backdrop-filter: blur(16px) !important;
                border: 1px solid rgba(255, 255, 255, 0.25) !important;
                border-radius: 24px !important;
                padding: 45px 30px 35px 30px !important;
                text-shadow: 0 0 10px rgba(255, 249, 234, 0.35) !important;
                animation: desdobrarCarta 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
                position: relative;
                margin-top: 25px;
            }

            /* Lacre de Cera Real no topo da carta */
            .lacre-cera {
                position: absolute;
                top: -24px;
                left: 50%;
                transform: translateX(-50%);
                width: 50px;
                height: 50px;
                background: radial-gradient(circle at 35% 35%, #e63946, #9b111e);
                border-radius: 50%;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5), inset 0 2px 4px rgba(255,255,255,0.4);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 22px;
                border: 2px solid rgba(255, 215, 0, 0.6);
            }

            @media (max-width: 600px) {
                .carta-tinteiro {
                    font-size: 24px !important;
                    line-height: 1.7 !important;
                    padding: 38px 20px 25px 20px !important;
                }
            }

            /* Botão com pulsação de ouro quando destrancado */
            @keyframes pulsarOuro {
                0% { box-shadow: 0 0 15px rgba(255, 215, 0, 0.4); transform: scale(1); }
                50% { box-shadow: 0 0 35px rgba(255, 42, 109, 0.9); transform: scale(1.03); }
                100% { box-shadow: 0 0 15px rgba(255, 215, 0, 0.4); transform: scale(1); }
            }

            .botao-carta > button {
                animation: pulsarOuro 1.6s infinite ease-in-out !important;
                background: linear-gradient(135deg, #ff2a6d, #ffd166) !important;
                color: #210d1b !important;
                font-weight: 900 !important;
                border: none !important;
            }

            h1, h2, h3 {
                color: #ffffff !important;
                text-shadow: 0 0 15px rgba(0, 255, 179, 0.4) !important;
            }
        </style>
    """, unsafe_allow_html=True)


# ========================================================
# PÁGINA 1: LENÇÓIS DE SEDA DE LUZ FLUTUANDO (TELA CHEIA)
# ========================================================
if st.session_state.pagina == 1:
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
            }
        </style>
    """, unsafe_allow_html=True)

    animacao_lencois = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      body, html { width: 100%; height: 100%; overflow: hidden; background: radial-gradient(ellipse at center, #18091d 0%, #060309 100%); }
      canvas { display: block; width: 100vw; height: 100vh; }
    </style>
    </head>
    <body>
    <canvas id="c"></canvas>
    <script>
      const canvas = document.getElementById('c');
      const ctx = canvas.getContext('2d');
      function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
      window.addEventListener('resize', resize);
      resize();

      function heart(t) {
        const x = 16 * Math.pow(Math.sin(t), 3);
        const y = -(13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t));
        return { x, y };
      }

      const STEPS = 140;
      const basePoints = [];
      for (let i = 0; i <= STEPS; i++) {
        const t = (i / STEPS) * Math.PI * 2;
        const p = heart(t);
        const dt = 0.01;
        const pNext = heart(t + dt);
        const dx = pNext.x - p.x;
        const dy = pNext.y - p.y;
        const len = Math.hypot(dx, dy) || 1;
        basePoints.push({ x: p.x, y: p.y, nx: -dy / len, ny: dx / len, t: t });
      }

      const sparks = [];
      for (let i = 0; i < 45; i++) {
        sparks.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.5 - 0.1,
          size: Math.random() * 2 + 0.8,
          alpha: Math.random()
        });
      }

      let time = 0;
      const numRibbons = 42;

      function draw() {
        ctx.fillStyle = 'rgba(6, 3, 9, 0.28)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        time += 0.022;

        const baseSize = Math.min(canvas.width, canvas.height);
        const pulse = 1 + 0.035 * Math.sin(time * 2);
        const scale = (baseSize / 36) * pulse;
        const centerX = canvas.width / 2;
        const centerY = (canvas.height / 2) - (canvas.height * 0.04);

        ctx.save();
        sparks.forEach(s => {
          s.x += s.vx + Math.sin(time + s.y * 0.01) * 0.2;
          s.y += s.vy;
          if (s.y < 0) s.y = canvas.height;
          if (s.x < 0) s.x = canvas.width;
          if (s.x > canvas.width) s.x = 0;

          ctx.fillStyle = `rgba(255, 230, 240, ${0.3 + 0.3 * Math.sin(time * 2 + s.alpha * 10)})`;
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
          ctx.fill();
        });
        ctx.restore();

        ctx.save();
        ctx.globalCompositeOperation = 'screen';

        for (let j = 0; j < numRibbons; j++) {
          const layerOffset = j * 0.08;
          ctx.beginPath();

          const hue = 325 + Math.sin(j * 0.15 + time) * 35;
          const alpha = 0.085 + 0.04 * Math.sin(time * 1.5 + j * 0.1);
          ctx.strokeStyle = `hsla(${hue}, 95%, 68%, ${alpha})`;
          ctx.lineWidth = 1.6 + 0.8 * Math.sin(j * 0.2);

          for (let i = 0; i <= STEPS; i++) {
            const bp = basePoints[i];
            const wave1 = Math.sin(bp.t * 3.5 + time * 1.8 + layerOffset * 2.5) * 16;
            const wave2 = Math.cos(bp.t * 2.0 - time * 1.2 + layerOffset * 1.8) * 10;
            const flutter = Math.sin(bp.t * 8.0 + time * 3.0 + j * 0.5) * 3.5;
            const totalDisplacement = (wave1 + wave2 + flutter) * (baseSize / 550);

            const px = centerX + (bp.x * scale) + (bp.nx * totalDisplacement);
            const py = centerY + (bp.y * scale) + (bp.ny * totalDisplacement);

            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
          }
          ctx.closePath();
          ctx.stroke();
        }

        ctx.restore();
        requestAnimationFrame(draw);
      }
      draw();
    </script>
    </body>
    </html>
    """
    components.html(animacao_lencois)

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
# PÁGINA 5: A CARTA SECRETA (FEITA À MÃO COM CANETA DE TINTEIRO)
# ========================================================
elif st.session_state.pagina == 5:
    # Explosão mágica de corações e partículas de ouro em tela
    efeito_explosao = """
    <canvas id="fireworks" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999;"></canvas>
    <script>
      const c = document.getElementById('fireworks');
      const cx = c.getContext('2d');
      c.width = window.innerWidth;
      c.height = window.innerHeight;

      const items = [];
      const colors = ['#ff2a6d', '#ffd166', '#ff62a5', '#ffffff', '#00f5d4'];

      // Cria corações e faíscas de ouro explodindo
      for(let i = 0; i < 90; i++) {
        items.push({
          x: c.width / 2,
          y: c.height / 2,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 0.7) * 18,
          size: Math.random() * 14 + 10,
          color: colors[Math.floor(Math.random() * colors.length)],
          rot: Math.random() * Math.PI,
          vrot: (Math.random() - 0.5) * 0.1,
          alpha: 1,
          isHeart: Math.random() > 0.4
        });
      }

      function drawHeart(ctx, x, y, size) {
        ctx.beginPath();
        const topCurveHeight = size * 0.3;
        ctx.moveTo(x, y + topCurveHeight);
        ctx.bezierCurveTo(x, y, x - size / 2, y, x - size / 2, y + topCurveHeight);
        ctx.bezierCurveTo(x - size / 2, y + (size + topCurveHeight) / 2, x, y + size, x, y + size);
        ctx.bezierCurveTo(x, y + size, x + size / 2, y + (size + topCurveHeight) / 2, x + size / 2, y + topCurveHeight);
        ctx.bezierCurveTo(x + size / 2, y, x, y, x, y + topCurveHeight);
        ctx.closePath();
        ctx.fill();
      }

      function anim() {
        cx.clearRect(0, 0, c.width, c.height);
        let alive = false;
        items.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.22; // gravidade suave
          p.vx *= 0.98;
          p.alpha -= 0.009;
          p.rot += p.vrot;

          if(p.alpha > 0) {
            alive = true;
            cx.save();
            cx.globalAlpha = Math.max(0, p.alpha);
            cx.fillStyle = p.color;
            cx.shadowBlur = 10;
            cx.shadowColor = p.color;
            cx.translate(p.x, p.y);
            cx.rotate(p.rot);

            if(p.isHeart) {
              drawHeart(cx, 0, -p.size/2, p.size);
            } else {
              cx.beginPath();
              cx.arc(0, 0, p.size / 3.5, 0, Math.PI * 2);
              cx.fill();
            }
            cx.restore();
          }
        });
        if(alive) requestAnimationFrame(anim);
      }
      anim();
    </script>
    """
    components.html(efeito_explosao, height=1)

    st.title("💌 Para o Amor da Minha Vida")

    # AQUI ESTÁ A CARTA COM O LACRE DE CERA REAL:
    st.markdown("""
    <div class="carta-tinteiro">
        <div class="lacre-cera">❤️</div>
        Meu amor,<br><br>
    
    Se você está lendo isso, é porque você passou por todas as etapas (e provou que tem boa memória!).<br><br>
    
    Eu criei esse pequeno aplicativo em Python pensando em cada detalhe de nós dois.<br><br>
Meu amor,<br><br>
Se você está lendo isso, é porque chegou a uma<br><br>
das minhas partes favoritas deste aplicativo:<br><br>
um pedacinho do meu coração escrito para você.<br><br>

Às vezes, acho que nem as palavras mais bonitas<br><br>
seriam suficientes para explicar o quanto você<br><br>
é especial para mim.<br><br>

Entre tantos caminhos que a vida poderia me<br><br>
levar, sou feliz por ter encontrado você.<br><br>
Você faz parte dos meus pensamentos, dos meus<br><br>
planos e dos sonhos que quero realizar.<br><br>

Eu amo os detalhes, os momentos simples,<br><br>
as conversas, as risadas e até aqueles dias<br><br>
em que tudo o que precisamos é ficar juntinhos.<br><br>

Não quero apenas viver os dias bons com você.<br><br>
Quero construir uma história, superar desafios,<br><br>
celebrar conquistas e continuar escolhendo você,<br><br>
mesmo quando a vida não for tão fácil.<br><br>

Que nunca nos faltem carinho, cumplicidade,<br><br>
respeito, paciência e motivos para sorrir juntos.<br><br>

Se eu pudesse te dar uma coisa neste momento,<br><br>
seria a oportunidade de enxergar a si mesmo<br><br>
pelos meus olhos. Assim você entenderia o quanto<br><br>
é importante para mim e o tamanho do amor<br><br>
que guardo aqui dentro.<br><br>

Obrigada por fazer parte da minha vida,<br><br>
por ser meu amor e por compartilhar comigo<br><br>
um pedacinho tão bonito da sua história.<br><br>

E se eu pudesse voltar no tempo e escolher<br><br>
novamente, entre tantas possibilidades,<br><br>
meu coração ainda procuraria você.<br><br>

Eu te amo, hoje, amanhã e em todos os<br><br>
capítulos que ainda vamos escrever juntos.<br><br>

<i>Sua namorada e programadora favorita.</i> 💕
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 Voltar ao Início", use_container_width=True):
        st.session_state.pagina = 1
        st.session_state.quiz_resolvido = False
        st.rerun()
