import time
from datetime import date
import random
import streamlit as st
import streamlit.components.v1 as components

# ========================================================
# CONFIGURAÇÃO GERAL DA PÁGINA
# ========================================================
st.set_page_config(page_title="Para Meu Amor ❤️", page_icon="💌", layout="centered")

# ========================================================
# ESTADO DA SESSÃO (MEMÓRIA DE NAVEGAÇÃO)
# ========================================================
if "pagina" not in st.session_state:
    st.session_state.pagina = 1

if "cupons_obtidos" not in st.session_state:
    st.session_state.cupons_obtidos = []

if "ultimo_cupom" not in st.session_state:
    st.session_state.ultimo_cupom = None

# ========================================================
# TRILHA SONORA DE FUNDO (INICIA NO CARREGAMENTO)
# ========================================================
motor_audio_html = """
<script>
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;
    let musicaIniciada = false;

    function tocarNota(frequencia, atraso, duracao, volume) {
        if (!audioCtx) return;
        try {
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(frequencia, audioCtx.currentTime + atraso);

            gain.gain.setValueAtTime(0.0001, audioCtx.currentTime + atraso);
            gain.gain.exponentialRampToValueAtTime(volume, audioCtx.currentTime + atraso + 0.08);
            gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + atraso + duracao);

            osc.connect(gain);
            gain.connect(audioCtx.destination);

            osc.start(audioCtx.currentTime + atraso);
            osc.stop(audioCtx.currentTime + atraso + duracao);
        } catch(e) {}
    }

    function iniciarCicloHarmonico() {
        if (musicaIniciada) return;
        musicaIniciada = true;

        const escala = [261.63, 329.63, 392.00, 493.88, 523.25, 392.00, 329.63];
        let passo = 0;

        setInterval(() => {
            if (audioCtx && audioCtx.state === 'running') {
                const freq = escala[passo % escala.length];
                tocarNota(freq, 0, 1.4, 0.045);
                passo++;
            }
        }, 520);
    }

    function inicializarAudio() {
        if (!audioCtx) {
            audioCtx = new AudioContext();
        }
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        iniciarCicloHarmonico();
    }

    // Tenta tocar imediatamente ao abrir o link
    window.addEventListener('load', inicializarAudio);
    document.addEventListener('DOMContentLoaded', inicializarAudio);
    setTimeout(inicializarAudio, 100);

    // Caso o navegador bloqueie autoplay estrito, destrava no primeiro movimento/toque
    window.addEventListener('click', inicializarAudio, { once: true });
    window.addEventListener('touchstart', inicializarAudio, { once: true });
    window.parent.document.addEventListener('click', inicializarAudio, { once: true });
</script>
"""
components.html(motor_audio_html, height=0, width=0)

# ========================================================
# ESTILOS CSS GLOBAIS (AURORA BOREAL, GLASSMORPHISM, FONTES)
# ========================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Great+Vibes&display=swap');

    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    #MainMenu { visibility: hidden !important; }

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

    h1, h2, h3, .stTitle {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px !important;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(0, 245, 212, 0.35) !important;
    }

    .card-glass {
        background: rgba(15, 23, 42, 0.58) !important;
        backdrop-filter: blur(18px) !important;
        -webkit-backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 24px !important;
        padding: 30px 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    }

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
        margin-bottom: 12px;
        letter-spacing: 0.3px;
    }

    .cupom-card {
        background: linear-gradient(135deg, rgba(255, 42, 109, 0.2), rgba(123, 44, 191, 0.3));
        border: 2px dashed rgba(255, 215, 0, 0.7);
        border-radius: 20px;
        padding: 24px;
        margin: 18px 0;
        text-align: center;
        box-shadow: 0 10px 35px rgba(255, 42, 109, 0.35);
        animation: surgirCupom 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes surgirCupom {
        from { opacity: 0; transform: translateY(14px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .cupom-titulo {
        color: #ffd166;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .cupom-texto {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
    }

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

    /* Legibilidade do Quiz */
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] p,
    div[data-testid="stRadio"] span,
    div[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 16px !important;
    }

    div[data-testid="stWidgetLabel"] p {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #05ffa1 !important;
        margin-bottom: 12px !important;
    }

    div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.08) !important;
        padding: 14px 18px !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.16) !important;
        margin-bottom: 10px !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }

    div[role="radiogroup"] > label:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        border-color: #05ffa1 !important;
    }

    /* Carta Manuscrita */
    @keyframes desdobrarCarta {
        0% {
            opacity: 0;
            transform: translateY(40px) scale(0.9) rotateX(15deg);
        }
        70% {
            transform: translateY(-6px) scale(1.01) rotateX(0deg);
            box-shadow: 0 0 40px rgba(255, 215, 0, 0.35);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1) rotateX(0deg);
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.5);
        }
    }

    .carta-tinteiro {
        font-family: 'Great Vibes', cursive !important;
        font-size: 28px !important;
        line-height: 1.7 !important;
        color: #fffaf0 !important;
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.22) !important;
        border-radius: 24px !important;
        padding: 55px 34px 40px 34px !important;
        position: relative;
        margin-top: 35px;
        animation: desdobrarCarta 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
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
            padding: 45px 20px 30px 20px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Fundo de estrelas cintilantes nas páginas 2 a 5
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
# PÁGINA 2: SEUS CUPONS (ESPERA 5s E VAI P/ O QUIZ)
# ========================================================
elif st.session_state.pagina == 2:
    st.markdown("""
        <div class="card-glass">
            <span class="badge-tag">🎟️ ETAPA 1</span>
            <h1 style="margin: 6px 0 10px 0;">Seus Cupons de Amor</h1>
            <p style="font-size: 15px; color: #cbd5e1; margin-bottom: 0;">
                Você merece todos os mimos! Clique no botão abaixo para tirar o seu vale-presente:
            </p>
        </div>
    """, unsafe_allow_html=True)

    cupons = [
        "Vale um cafuné gostoso até dormir 💤",
        "Vale uma massagem relaxante com óleos 💆‍♂️",
        "Vale escolher o jantar de hoje",
        "Vale um abraço quentinho de 5 minutos 🫂",
        "Vale um dia inteiro sem eu reclamar de nada 😇",
        "Vale uma sobremesa especial por minha conta 🍫"
    ]

    if st.button("✨ Tirar Meu Cupom! 🎉", use_container_width=True):
        sorteado = random.choice(cupons)
        st.session_state.ultimo_cupom = sorteado
        if sorteado not in st.session_state.cupons_obtidos:
            st.session_state.cupons_obtidos.append(sorteado)
        st.balloons()

    if st.session_state.ultimo_cupom:
        st.markdown(f"""
            <div class="cupom-card">
                <div class="cupom-titulo">★ Cupom Sorteado ★</div>
                <div class="cupom-texto">{st.session_state.ultimo_cupom}</div>
            </div>
        """, unsafe_allow_html=True)

        st.info("⏳ Guardando seu cupom... Preparando o quiz em 5 segundos!")
        barra = st.progress(0)
        for i in range(100):
            time.sleep(0.05)  # 5 segundos no total
            barra.progress(i + 1)
        
        # Avança automaticamente para o Quiz 1
        st.session_state.pagina = 3
        st.rerun()

# ========================================================
# PÁGINA 3: QUIZ - PERGUNTA 1 (ESPERA 3s AO ACERTAR)
# ========================================================
elif st.session_state.pagina == 3:
    st.markdown("""
        <div class="card-glass">
            <span class="badge-tag">🧩 ETAPA 2 • PARTE 1/2</span>
            <h1 style="margin: 6px 0 10px 0;">Quiz do Amor</h1>
            <p style="font-size: 15px; color: #cbd5e1; margin: 0;">
                Teste de memória: responda para avançar à pergunta final!
            </p>
        </div>
    """, unsafe_allow_html=True)

    p1 = st.radio(
        "1) Onde foi o nosso primeiro beijo?",
        ["No cinema", "Na pracinha", "No carro", "Na minha casa"],
        index=None
    )

    st.write("")
    if st.button("Confirmar Resposta 🔓", use_container_width=True):
        if p1 == "Na minha casa":
            st.success("✅ Exatamente! Você se lembrou perfeitamente!")
            st.info("Avançando para a pergunta 2 em 3 segundos...")
            barra = st.progress(0)
            for i in range(100):
                time.sleep(0.03)  # 3 segundos
                barra.progress(i + 1)
            st.session_state.pagina = 4
            st.rerun()
        elif p1 is not None:
            st.warning("Hum... quase! Pense com mais carinho 😂")
        else:
            st.info("Selecione uma opção antes de confirmar!")

# ========================================================
# PÁGINA 4: QUIZ - PERGUNTA 2 (FITA SE ABRINDO E TRANSIÇÃO DIRETA)
# ========================================================
elif st.session_state.pagina == 4:
    st.markdown("""
        <div class="card-glass">
            <span class="badge-tag">🧩 ETAPA 2 • PARTE 2/2</span>
            <h1 style="margin: 6px 0 10px 0;">Última Pergunta!</h1>
            <p style="font-size: 15px; color: #cbd5e1; margin: 0;">
                Acerte para desatar a fita e liberar a carta secreta:
            </p>
        </div>
    """, unsafe_allow_html=True)

    p2 = st.radio(
        "2) Quem se apaixonou primeiro?",
        ["Você", "Eu", "Os dois no mesmo instante"],
        index=None
    )

    st.write("")
    if st.button("Revelar Surpresa Final ❤️", use_container_width=True):
        if p2 == "Você":
            # EFEITO VISUAL: Fita vermelha acetinada envolvendo as bordas da tela inteira com o laço sendo puxado
            animacao_fita_laco = """
            <div id="ribbon-box" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 999999; overflow: hidden;">
                <style>
                    /* Moldura de fitas vermelhas nas 4 bordas */
                    .fita-borda {
                        position: absolute;
                        background: linear-gradient(135deg, #d62246 0%, #a00d28 100%);
                        box-shadow: 0 0 20px rgba(214, 34, 70, 0.8), inset 0 0 8px rgba(255, 215, 0, 0.5);
                        border: 1px dashed rgba(255, 215, 0, 0.6);
                        transition: all 2.6s cubic-bezier(0.25, 1, 0.5, 1);
                    }
                    .borda-topo { top: 0; left: 0; width: 100vw; height: 26px; }
                    .borda-baixo { bottom: 0; left: 0; width: 100vw; height: 26px; }
                    .borda-esq { top: 0; left: 0; width: 26px; height: 100vh; }
                    .borda-dir { top: 0; right: 0; width: 26px; height: 100vh; }

                    /* O laço central acetinado com puxada sutil */
                    @keyframes puxarLaco {
                        0% { transform: translate(-50%, -50%) scale(1) rotate(0deg); opacity: 1; }
                        35% { transform: translate(-50%, -50%) scale(1.15) rotate(-5deg); opacity: 1; filter: drop-shadow(0 0 35px #ffd166); }
                        65% { transform: translate(-50%, -65%) scale(0.9) rotate(8deg); opacity: 0.9; }
                        100% { transform: translate(-50%, -180%) scale(0.3) rotate(-25deg); opacity: 0; }
                    }
                    @keyframes recolherBordas {
                        0% { opacity: 1; }
                        60% { opacity: 1; }
                        100% { opacity: 0; transform: scale(1.08); }
                    }
                    .laco-container {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        animation: puxarLaco 3.1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
                    }
                    .no-laco {
                        width: 75px;
                        height: 75px;
                        background: radial-gradient(circle at 35% 35%, #ff2a6d, #9b111e);
                        border-radius: 50%;
                        border: 3px solid #ffd166;
                        box-shadow: 0 8px 30px rgba(0,0,0,0.6), 0 0 25px rgba(255, 42, 109, 0.9);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 34px;
                    }
                    .orelhas-laco {
                        display: flex;
                        gap: 25px;
                        margin-bottom: -32px;
                    }
                    .orelha {
                        width: 90px;
                        height: 55px;
                        background: linear-gradient(135deg, #e63946, #800f1a);
                        border-radius: 50%;
                        border: 2px solid #ffd166;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
                    }
                    .fita-borda { animation: recolherBordas 3.1s ease-in-out forwards; }
                </style>
                <div class="fita-borda borda-topo"></div>
                <div class="fita-borda borda-baixo"></div>
                <div class="fita-borda borda-esq"></div>
                <div class="fita-borda borda-dir"></div>
                <div class="laco-container">
                    <div class="orelhas-laco">
                        <div class="orelha" style="transform: rotate(-30deg);"></div>
                        <div class="orelha" style="transform: rotate(30deg);"></div>
                    </div>
                    <div class="no-laco">🎀</div>
                </div>
            </div>
            """
            components.html(animacao_fita_laco, height=200)
            
            st.success("✨ Acertou em cheio! Desatando o laço da carta...")
            time.sleep(3.0)  # Tempo para a animação do laço se abrir com suavidade
            st.session_state.pagina = 5
            st.rerun()
        elif p2 is not None:
            st.warning("Hum... quase! Dá uma pensadinha com mais carinho 😂")
        else:
            st.info("Selecione uma opção antes de confirmar!")

# ========================================================
# PÁGINA 5: A CARTA SECRETA (COM SOM DE FOLHEAR DE LIVRO)
# ========================================================
elif st.session_state.pagina == 5:
    # Efeito Sonoro Acústico: Papel / Folhear de livro suave passando
    som_livro_folhear = """
    <script>
        try {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            const ctx = new AudioCtx();

            function criarFolheada(inicio, duracao, frequenciaCorte, vol) {
                const bufferSize = ctx.sampleRate * duracao;
                const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = (Math.random() * 2 - 1) * 0.9;
                }
                const noise = ctx.createBufferSource();
                noise.buffer = buffer;

                const filter = ctx.createBiquadFilter();
                filter.type = 'bandpass';
                filter.Q.value = 1.6;
                filter.frequency.setValueAtTime(frequenciaCorte, ctx.currentTime + inicio);
                filter.frequency.exponentialRampToValueAtTime(320, ctx.currentTime + inicio + duracao);

                const gain = ctx.createGain();
                gain.gain.setValueAtTime(0.001, ctx.currentTime + inicio);
                gain.gain.linearRampToValueAtTime(vol, ctx.currentTime + inicio + (duracao * 0.35));
                gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + inicio + duracao);

                noise.connect(filter);
                filter.connect(gain);
                gain.connect(ctx.destination);

                noise.start(ctx.currentTime + inicio);
            }

            // Simula o atrito duplo realista de passar página de livro
            criarFolheada(0.1, 0.45, 1100, 0.28);
            criarFolheada(0.42, 0.55, 850, 0.35);
        } catch(e) {}
    </script>
    """
    components.html(som_livro_folhear, height=0, width=0)

    # Explosão de corações translúcidos
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

    # Carta Manuscrita Estilizada com Lacre
    st.markdown("""
    <div class="carta-tinteiro">
        <div class="lacre-cera">❤️</div>
        Meu amor,<br><br>
        Se você está lendo isso, é porque passou por todas as etapas (e provou que tem boa memória!). Chegou a uma das minhas partes favoritas deste aplicativo: um pedacinho do meu coração escrito para você.<br><br>
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
    if st.button("🔄 Voltar ao Início", use_container_width=True):
        st.session_state.pagina = 1
        st.session_state.cupons_obtidos = []
        st.session_state.ultimo_cupom = None
        st.rerun()
        st.session_state.ultimo_cupom = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
