import streamlit as st
import math
from calculadora import (
    calcular,
    parsear_expressao,
    resultado_trig_para_fracao,
    radianos_para_fracao_pi
)

# Configuração da página
st.set_page_config(
    page_title="Calculadora Python",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .result-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .result-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .fraction-display {
        font-size: 1.5rem;
        color: #ffd700;
        margin: 0.5rem 0;
    }
    .angle-display {
        font-size: 1.2rem;
        color: #87ceeb;
        margin: 0.5rem 0;
    }
    .history-item {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-size: 1.1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização do estado da sessão
if 'historico' not in st.session_state:
    st.session_state.historico = []
if 'temp_expressao' not in st.session_state:
    st.session_state.temp_expressao = ''

# Título principal
st.markdown('<h1 class="main-header">🧮 Calculadora Python</h1>', unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.header("ℹ️ Informações")
    st.markdown("""
    ### Operações Disponíveis
    
    **Básicas:**
    - `+` Adição
    - `-` Subtração
    - `*` Multiplicação
    - `/` Divisão
    - `//` Divisão inteira
    - `%` Módulo
    - `**` Potenciação
    
    **Avançadas:**
    - `sqrt(16)` Raiz quadrada
    - `sin(30)` Seno (em graus)
    - `cos(45)` Cosseno (em graus)
    - `tan(60)` Tangente (em graus)
    - `log(10)` Logaritmo natural
    - `log(100, 10)` Logaritmo com base
    
    ### Exemplos
    - `2+2`
    - `10/5`
    - `2**3`
    - `sqrt(16)`
    - `sin(30)`
    - `cos(45)`
    - `tan(60)`
    """)

# Layout principal
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Entrada")
    
    # Inicializa input_expressao se não existir
    if 'input_expressao' not in st.session_state:
        st.session_state.input_expressao = ''
    
    # Se há uma expressão temporária, usa ela e limpa
    if st.session_state.temp_expressao:
        st.session_state.input_expressao = st.session_state.temp_expressao
        st.session_state.temp_expressao = ''
    
    # Campo de entrada
    expressao = st.text_input(
        "Digite uma expressão matemática:",
        placeholder="Ex: 2+2, sin(30), sqrt(16), log(100, 10)",
        key="input_expressao"
    )
    
    # Botões de funções rápidas
    st.subheader("🔘 Funções Rápidas")
    col_func1, col_func2, col_func3, col_func4 = st.columns(4)
    
    with col_func1:
        if st.button("sin(", key="btn_sin"):
            st.session_state.temp_expressao = expressao + 'sin('
            st.rerun()
    with col_func2:
        if st.button("cos(", key="btn_cos"):
            st.session_state.temp_expressao = expressao + 'cos('
            st.rerun()
    with col_func3:
        if st.button("tan(", key="btn_tan"):
            st.session_state.temp_expressao = expressao + 'tan('
            st.rerun()
    with col_func4:
        if st.button("sqrt(", key="btn_sqrt"):
            st.session_state.temp_expressao = expressao + 'sqrt('
            st.rerun()
    
    col_func5, col_func6, col_func7, col_func8 = st.columns(4)
    with col_func5:
        if st.button("log(", key="btn_log"):
            st.session_state.temp_expressao = expressao + 'log('
            st.rerun()
    with col_func6:
        if st.button("(", key="btn_abre"):
            st.session_state.temp_expressao = expressao + '('
            st.rerun()
    with col_func7:
        if st.button(")", key="btn_fecha"):
            st.session_state.temp_expressao = expressao + ')'
            st.rerun()
    with col_func8:
        if st.button("**", key="btn_pow"):
            st.session_state.temp_expressao = expressao + '**'
            st.rerun()
    
    # Botão calcular
    calcular_btn = st.button("🚀 Calcular", type="primary", use_container_width=True)
    
    # Processamento
    if calcular_btn and expressao:
        resultado_parse = parsear_expressao(expressao)
        
        if resultado_parse:
            num1, num2, operacao = resultado_parse
            resultado = calcular(num1, num2, operacao)
            
            # Verifica se é erro
            if isinstance(resultado, str) and resultado.startswith("Erro"):
                st.error(f"❌ {resultado}")
            else:
                # Prepara dados para exibição
                resultado_frac = None
                frac_pi = None
                angulo_rad = None
                
                if operacao in ['sin', 'cos', 'tan']:
                    angulo_rad = math.radians(num1)
                    frac_pi = radianos_para_fracao_pi(angulo_rad)
                    resultado_frac = resultado_trig_para_fracao(resultado, operacao, num1)
                
                # Adiciona ao histórico
                item_historico = {
                    'expressao': expressao,
                    'operacao': operacao,
                    'resultado': resultado,
                    'resultado_frac': resultado_frac,
                    'frac_pi': frac_pi,
                    'angulo_rad': angulo_rad,
                    'num1': num1,
                    'num2': num2
                }
                st.session_state.historico.insert(0, item_historico)
                
                # Limita histórico a 20 itens
                if len(st.session_state.historico) > 20:
                    st.session_state.historico = st.session_state.historico[:20]
                
                # Exibe resultado
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(f'<div class="result-value">{expressao} =</div>', unsafe_allow_html=True)
                
                if resultado_frac:
                    st.markdown(f'<div class="fraction-display">📐 {resultado_frac} ou {resultado}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="result-value">{resultado}</div>', unsafe_allow_html=True)
                
                if frac_pi:
                    st.markdown(f'<div class="angle-display">📏 Ângulo: {frac_pi} rad ou {angulo_rad:.6f} rad</div>', unsafe_allow_html=True)
                elif angulo_rad:
                    st.markdown(f'<div class="angle-display">📏 Ângulo: {angulo_rad:.6f} rad</div>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"❌ Não foi possível interpretar a expressão '{expressao}'")
            st.info("💡 Exemplos válidos: `2+2`, `10/5`, `sqrt(16)`, `sin(30)`")

with col2:
    st.header("📚 Histórico")
    
    if st.button("🗑️ Limpar Histórico", use_container_width=True):
        st.session_state.historico = []
        st.rerun()
    
    if st.session_state.historico:
        for idx, item in enumerate(st.session_state.historico[:10]):
            with st.expander(f"{item['expressao']} = {item['resultado']}", expanded=False):
                st.write(f"**Operação:** {item['operacao']}")
                st.write(f"**Resultado:** {item['resultado']}")
                
                if item['resultado_frac']:
                    st.write(f"**Fração exata:** {item['resultado_frac']}")
                
                if item['frac_pi']:
                    st.write(f"**Ângulo:** {item['frac_pi']} rad")
                elif item['angulo_rad']:
                    st.write(f"**Ângulo:** {item['angulo_rad']:.6f} rad")
                
                if st.button(f"🔄 Usar", key=f"use_{idx}"):
                    st.session_state.temp_expressao = item['expressao']
                    st.rerun()
    else:
        st.info("Nenhum cálculo realizado ainda.")

# Rodapé
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Desenvolvido com Python 🐍 e Streamlit</p>
    <p>Suporta operações básicas e trigonométricas com exibição de frações exatas</p>
</div>
""", unsafe_allow_html=True)
