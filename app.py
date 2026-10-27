from datetime import date
import random
import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌", layout="centered")

# Memória de navegação e cupons sorteados
if "pagina" not in st.session_state:
    # ========================================================
# TRILHA SONORA DE FUNDO (ÁUDIO PERSISTENTE EM LOOP)
# ========================================================
# Pode utilizar uma hiperligação direta para um ficheiro .mp3 na web ou um caminho/base64 local
URL_MUSICA = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3"

audio_player_html = f"""
    <audio id="bg-audio" loop preload="auto">
        <source src="{URL_MUSICA}" type="audio/mp3">
    </audio>
    <script>
        const audio = document.getElementById('bg-audio');
        if (audio) {{
            audio.volume = 0.35; // Volume a 35% para ficar suave
            // Tenta reproduzir automaticamente caso já tenha ocorrido interação prévia
            audio.play().catch(() => {{
                // Caso o navegador bloqueie o autoplay, inicia no primeiro clique na página
                document.addEventListener('click', () => {{
                    audio.play();
                }}, {{ once: true }});
            }});
        }}
    </script>
"""
components.html(audio_player_html, height=0, width=0)
    st.session_state.pagina = 1
if "cupons_obtidos" not in st.session_state:
    st.session_state.cupons_obtidos = []
if "ultimo_cupom" not in st.session_state:
    st.session_state.ultimo_cupom = None

# ========================================================
# ESTILO GLOBAL: AURORA BOREAL, GLASSMORPHISM E TIPOGRAFIA
# ========================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Great+Vibes&display=swap');

    /* Ocultar barra superior e rodapé nativos do Streamlit */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    #MainMenu { visibility: hidden !important; }

    /* Fundo Aurora Boreal e Céu Noturno Profundo */
    .stApp {
        background: 
            radial-gradient(circle at 10% 25%, rgba(5, 255, 161, 0.22) 0%, transparent 45%),
            radial-gradient(circle at 85% 30%, rgba(123, 44, 191, 0.28) 0%, transparent 50%),
            radial-gradient(circle at 50% 85%, rgba(0, 245, 212, 0.18) 0%, transparent 55%),
            linear-gradient(170deg, #040914 0%, #061e29 45%, #120924 100%) !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #e2e8f0 !important;
    }

    /* Títulos em Outfit */
    h1, h2, h3, .stTitle {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px !important;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(0, 245, 212, 0.35) !important;
    }

    /* Container Card Glassmorphism */
    .card-glass {
        background: rgba(15, 23, 42, 0.58) !important;
        backdrop-filter: blur(18px) !important;
        -webkit-backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 24px !important;
        padding: 34px 28px !important;
        margin-bottom: 24px !important;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    }

    /* Tag de Status / Badge */
    .badge-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(5, 255, 161, 0.12);
        color: #05ffa1;
        border: 1px solid rgba(5, 255, 161, 0.3);
        border-radius: 9999px;
        padding: 6px 14px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 14px;
        letter-spacing: 0.3px;
    }

    /* Cartão do Cupom Sorteado */
    .cupom-card {
        background: linear-gradient(135deg, rgba(255, 42, 109, 0.15), rgba(123, 44, 191, 0.22));
        border: 1.5px dashed rgba(255, 215, 0, 0.55);
        border-radius: 18px;
        padding: 20px;
        margin: 18px 0;
        text-align: center;
        box-shadow: 0 8px 30px rgba(255, 42, 109, 0.25);
        animation: surgirCupom 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes surgirCupom {
        from { opacity: 0; transform: translateY(12px) scale(0.96); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .cupom-titulo {
        color: #ffd166;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    .cupom-texto {
        font-size: 19px;
        font-weight: 600;
        color: #ffffff;
    }

    /* Customização dos Botões Streamlit */
    div.stButton > button {
        background: linear-gradient(135deg, #05ffa1 0%, #00b4d8 100%) !important;
        color: #041019 !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border-radius: 14px !important;
        border: none !important;
        padding: 14px 24px !important;
        box-shadow: 0 8px 25px rgba(5, 255, 161, 0.35) !important;
        transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 12px 32px rgba(5, 255, 161, 0.55) !important;
    }

    /* Botão Secundário / Navegação */
    .botao-secundario div.stButton > button {
        background: linear-gradient(135deg, #7b2cbf 0%, #3a0ca3 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 8px 25px rgba(123, 44, 191, 0.4) !important;
    }
    .botao-secundario div.stButton > button:hover {
        box-shadow: 0 12px 32px rgba(123, 44, 191, 0.65) !important;
    }

    /* Carta Manuscrita na Página 5 */
    .carta-tinteiro {
        font-family: 'Great Vibes', cursive !important;
        font-size: 28px !important;
        line-height: 1.7 !important;
        color: #fffaf0 !important;
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.22) !important;
        border-radius: 24px !important;
        padding: 55px 34px 40px 34px !important;
        position: relative;
        margin-top: 35px;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.5), inset 0 1px 2px rgba(255, 255, 255, 0.2) !important;
        text-shadow: 0 0 10px rgba(255, 249, 234, 0.2) !important;
    }

    .lacre-cera {
        position: absolute;
        top: -24px;
        left: 50%;
        transform: translateX(-50%);
        width: 50px;
        height: 50px;
        background: radial-gradient(circle at 35% 35%, #ff2a6d, #9b111e);
        border-radius: 50%;
        box-shadow: 0 4px 18px rgba(0,0,0,0.6), inset 0 2px 4px rgba(255,255,255,0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        border: 2px solid rgba(255, 215, 0, 0.7);
    }

    @media (max-width: 600px) {
        .carta-tinteiro {
            font-size: 23px !important;
            line-height: 1.6 !important;
            padding: 45px 22px 30px 22px !important;
        }
    }

    /* Rádio options estilizados */
    div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        padding: 12px 18px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 8px;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] > label:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(5, 255, 161, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Céu de Estrelas Cintilantes em Canvas Fundo (apenas nas páginas 2 a 5)
if st.session_state.pagina >= 2:
    components.html("""
    <canvas id="sky" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:-1;"></canvas>
    <script>
      const c = document.getElementById('sky');
      const ctx = c.getContext('2d');
      function resize() { c.width = window.innerWidth; c.height = window.innerHeight; }
      window.addEventListener('resize', resize);
      resize();

      const stars = Array.from({length: 65}, () => ({
        x: Math.random() * c.width,
        y: Math.random() * c.height,
        r: Math.random() * 1.6 + 0.4,
        alpha: Math.random(),
        speed: Math.random() * 0.02 + 0.005
      }));

      function anim() {
        ctx.clearRect(0, 0, c.width, c.height);
        stars.forEach(s => {
          s.alpha += s.speed;
          const a = (Math.sin(s.alpha) + 1) / 2;
          ctx.fillStyle = `rgba(255, 255, 255, ${a * 0.85})`;
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
          ctx.fill();
        });
        requestAnimationFrame(anim);
      }
      anim();
    </script>
    """, height=0)


# ========================================================
# PÁGINA 1: ABERTURA COM CORAÇÃO DE SEDA
# ========================================================
if st.session_state.pagina == 1:
    st.markdown("""
        <style>
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
                background: linear-gradient(135deg, #ff2a6d, #7b2cbf) !important;
                color: #ffffff !important;
                border-radius: 50px !important;
                padding: 16px 24px !important;
                font-size: 17px !important;
                box-shadow: 0 0 35px rgba(255, 42, 109, 0.7) !important;
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
      body, html { width: 100%; height: 100%; overflow: hidden; background: radial-gradient(ellipse at center, #140924 0%, #040914 100%); }
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

      let time = 0;
      const numRibbons = 42;

      function draw() {
        ctx.fillStyle = 'rgba(4, 9, 20, 0.28)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        time += 0.022;

        const baseSize = Math.min(canvas.width, canvas.height);
        const pulse = 1 + 0.035 * Math.sin(time * 2);
        const scale = (baseSize / 36) * pulse;
        const centerX = canvas.width / 2;
        const centerY = (canvas.height / 2) - (canvas.height * 0.04);

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
    st.markdown("""
        <div class="card-glass">
            <span class="badge-tag">💫 NOSSA HISTÓRIA</span>
            <h1 style="margin: 6px 0 12px 0;">Oi, meu amor! ❤️</h1>
            <p style="font-size: 16px; color: #cbd5e1; line-height: 1.6;">
                Esse cantinho foi programado com carinho exclusivamente para você, guardando cada memória do nosso caminho.
            </p>
        </div>
    """, unsafe_allow_html=True)

    data_inicio = date(2025, 2, 9)
    dias = (date.today() - data_inicio).days

    st.markdown(f"""
        <div class="card-glass" style="text-align: center; border-color: rgba(5, 255, 161, 0.3);">
            <div style="font-size: 14px; text-transform: uppercase; color: #05ffa1; font-weight: 700; letter-spacing: 1px;">Tempo Compartilhado</div>
            <div style="font-size: 52px; font-weight: 800; font-family: 'Outfit'; color: #ffffff; text-shadow: 0 0 25px rgba(5, 255, 161, 0.5); margin: 8px 0;">
                {dias} dias
            </div>
            <p style="margin: 0; color: #94a3b8; font-size: 15px;">E cada dia ao seu lado é o melhor capítulo da minha história. ✨</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="botao-secundario">', unsafe_allow_html=True)
    if st.button("Ver Meus Cupons Especiais 🎁 ➔", use_container_width=True):
        st.session_state.pagina = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ========================================================
# PÁGINA 3: CUPONS DE MIMOS
# ========================================================
elif st.session_state.pagina == 3:
    st.markdown("""
        <div class="card-glass">
            <span class="badge-tag">🎟️ ETAPA 1</span>
            <h1 style="margin: 6px 0 10px 0;">Seus Cupons de Amor</h1>
            <p style="font-size: 15px; color: #cbd5e1; margin-bottom: 0;">
                Você merece todos os mimos do mundo! Clique abaixo para resgatar um vale-presente:
            </p>
        </div>
    """, unsafe_allow_html=True)

    cupons = [
        "Vale um cafuné gostoso até dormir 💤",
        "Vale uma massagem relaxante com óleos 💆‍♂️",
        "Vale escolher o sabor da pizza hoje 🍕",
        "Vale um abraço quentinho de 5 minutos 🫂",
        "Vale um dia inteiro sem eu reclamar de nada 😇",
        "Vale uma sobremesa especial por minha conta 🍫"
    ]

    if st.button("✨ Sortear um Cupom! 🎉", use_container_width=True):
        sorteado = random.choice(cupons)
        st.session_state.ultimo_cupom = sorteado
        if sorteado not in st.session_state.cupons_obtidos:
            st.session_state.cupons_obtidos.append(sorteado)
        st.balloons()

    # Exibição do cupom sorteado com efeito card brilhante
    if st.session_state.ultimo_cupom:
        st.markdown(f"""
            <div class="cupom-card">
                <div class="cupom-titulo">★ Cupom Desbloqueado ★</div>
                <div class="cupom-texto">{st.session_state.ultimo_cupom}</div>
            </div>
        """, unsafe_allow_html=True)

    # Mini galeria dos cupons já sorteados
    if st.session_state.cupons_obtidos:
        st.markdown("<p style='font-size: 13px; color: #94a3b8; font-weight: 600; text-transform: uppercase; margin-top: 20px;'>Cupons Resgatados:</p>", unsafe_allow_html=True)
        for c in st.session_state.cupons_obtidos:
            st.markdown(f"<div style='background: rgba(255,255,255,0.06); border-radius: 10px; padding: 10px 14px; margin-bottom: 6px; font-size: 14px;'>🎟️ {c}</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("""
        <div class="card-glass" style="margin-top: 25px; padding: 22px 24px;">
            <p style="font-size: 14px; color: #cbd5e1; margin: 0;">
                Agora preciso testar a sua memória antes de liberar a surpresa secreta... 🤫
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="botao-secundario">', unsafe_allow_html=True)
    if st.button("Ir para o Quiz do Casal 🧠 ➔", use_container_width=True):
        st.session_state.pagina = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ========================================================
# PÁGINA 4: O QUIZ DO AMOR
# ========================================================
elif st.session_state.pagina == 4:
    st.markdown("""
        <div class="card-glass" style="margin-bottom: 20px;">
            <span class="badge-tag">🧩 ETAPA 2</span>
            <h1 style="margin: 6px 0 10px 0;">Quiz do Amor</h1>
            <p style="font-size: 15px; color: #cbd5e1; margin: 0;">
                Responda acertando as opções certas para quebrar o lacre da cartinha secreta:
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Perguntas com fundo visível
    p1 = st.radio(
        "1) Onde foi o nosso primeiro beijo?",
        ["No cinema", "Na pracinha", "No carro", "Na minha casa"],
        index=None
    )

    st.write("")

    p2 = st.radio(
        "2) Quem se apaixonou primeiro?",
        ["Você", "Eu", "Os dois no mesmo instante"],
        index=None
    )

    st.write("")

    if st.button("🔓 Confirmar Respostas", use_container_width=True):
        if p1 == "Na minha casa" and p2 == "Você":
            st.session_state.quiz_resolvido = True
            st.snow()
        else:
            st.session_state.quiz_resolvido = False
            st.warning("Hum... quase! Dá uma pensadinha com mais carinho 😂")

    if st.session_state.get("quiz_resolvido", False):
        st.markdown("""
            <div style="background: rgba(5, 255, 161, 0.15); border: 1px solid #05ffa1; border-radius: 14px; padding: 14px 18px; margin: 16px 0; color: #05ffa1; font-weight: 600; text-align: center;">
                ✨ Parabéns! Você acertou tudo e quebrou o selo da carta!
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <style>
                .botao-carta button {
                    background: linear-gradient(135deg, #ff2a6d 0%, #ffd166 100%) !important;
                    color: #120924 !important;
                    font-size: 17px !important;
                    box-shadow: 0 0 35px rgba(255, 42, 109, 0.8) !important;
                    animation: pulsar 1.5s infinite ease-in-out !important;
                }
                @keyframes pulsar {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.02); }
                    100% { transform: scale(1); }
                }
            </style>
            <div class="botao-carta">
        """, unsafe_allow_html=True)
        if st.button("💌 ABRIR MINHA CARTA SECRETA 💌", use_container_width=True):
            st.session_state.pagina = 5
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ========================================================
# PÁGINA 5: A CARTA SECRETA COM FOGOS E LACRE
# ========================================================
elif st.session_state.pagina == 5:
    # Efeito de corações e fogos translúcidos
    efeito_explosao = """
    <canvas id="fireworks" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999;"></canvas>
    <script>
      const c = document.getElementById('fireworks');
      const cx = c.getContext('2d');
      c.width = window.innerWidth;
      c.height = window.innerHeight;

      const items = [];
      const colors = ['#05ffa1', '#00f5d4', '#ff2a6d', '#ffd166', '#ffffff', '#7b2cbf'];

      for(let i = 0; i < 90; i++) {
        items.push({
          x: c.width / 2,
          y: c.height / 2,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 0.7) * 18,
          size: Math.random() * 12 + 8,
          color: colors[Math.floor(Math.random() * colors.length)],
          rot: Math.random() * Math.PI,
          vrot: (Math.random() - 0.5) * 0.1,
          alpha: 1,
          isHeart: Math.random() > 0.4
        });
      }

      function drawHeart(ctx, x, y, size) {
        ctx.beginPath();
        const top = size * 0.3;
        ctx.moveTo(x, y + top);
        ctx.bezierCurveTo(x, y, x - size / 2, y, x - size / 2, y + top);
        ctx.bezierCurveTo(x - size / 2, y + (size + top) / 2, x, y + size, x, y + size);
        ctx.bezierCurveTo(x, y + size, x + size / 2, y + (size + top) / 2, x + size / 2, y + top);
        ctx.bezierCurveTo(x + size / 2, y, x, y, x, y + top);
        ctx.closePath();
        ctx.fill();
      }

      function anim() {
        cx.clearRect(0, 0, c.width, c.height);
        let alive = false;
        items.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.22;
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

    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <span class="badge-tag">💌 DESTINATÁRIO ESPECIAL</span>
            <h1>Para o Amor da Minha Vida</h1>
        </div>
    """, unsafe_allow_html=True)

    # Carta Manuscrita Estilizada com o texto personalizado completo
    st.markdown("""
    <div class="carta-tinteiro">
        <div class="lacre-cera">❤️</div>
        Meu amor,<br><br>
        Se você está lendo isso, é porque você passou por todas as etapas (e provou que tem boa memória!). Chegou a uma das minhas partes favoritas deste aplicativo: um pedacinho do meu coração escrito para você.<br><br>
        Eu criei esse pequeno aplicativo em Python pensando em cada detalhe de nós dois.<br><br>
        Às vezes, acho que nem as palavras mais bonitas seriam suficientes para explicar o quanto você é especial para mim.<br><br>
        Entre tantos caminhos que a vida poderia me levar, sou feliz por ter encontrado você. Você faz parte dos meus pensamentos, dos meus planos e dos sonhos que quero realizar.<br><br>
        Eu amo os detalhes, os momentos simples, as conversas, as risadas e até aqueles dias em que tudo o que precisamos é ficar juntinhos.<br><br>
        Não quero apenas viver os dias bons com você. Quero construir uma história, superar desafios, celebrar conquistas e continuar escolhendo você, mesmo quando a vida não for tão fácil.<br><br>
        Que nunca nos faltem carinho, cumplicidade, respeito, paciência e motivos para sorrir juntos.<br><br>
        Se eu pudesse te dar uma coisa neste momento, seria a oportunidade de enxergar a si mesmo pelos meus olhos. Assim você entenderia o quanto é importante para mim e o tamanho do amor que guardo aqui dentro.<br><br>
        Obrigada por fazer parte da minha vida, por ser meu amor e por compartilhar comigo um pedacinho tão bonito da sua história.<br><br>
        E se eu pudesse voltar no tempo e escolher novamente, entre tantas possibilidades, meu coração ainda procuraria você.<br><br>
        Eu te amo, hoje, amanhã e em todos os capítulos que ainda vamos escrever juntos.<br><br>
        <i>Sua namorada e programadora favorita.</i> 💕
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown('<div class="botao-secundario">', unsafe_allow_html=True)
    if st.button("🔄 Voltar ao Início", use_container_width=True):
        st.session_state.pagina = 1
        st.session_state.quiz_resolvido = False
        st.session_state.cupons_obtidos = []
        st.session_state.ultimo_cupom = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
