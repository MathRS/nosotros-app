import streamlit as st
import requests
from datetime import datetime

# ------------------------
# Funções auxiliares
# ------------------------

def get_text_from_gdrive(gdrive_url):
    try:
        file_id = gdrive_url.split('/d/')[1].split('/')[0]
        download_url = f"https://drive.google.com/file/d/1UjUsI2tRqSr5e4pUexi0lprmfUZBYvNI/view?usp=sharing"
        response = requests.get(download_url)
        if response.status_code == 200:
            return response.text
        else:
            return "Erro ao baixar o arquivo."
    except Exception as e:
        return f"Erro ao processar o link: {e}"

def get_elapsed():
    start_date = datetime(2024, 1, 13)
    now = datetime.now()
    delta = now - start_date

    days = delta.days
    seconds = delta.seconds
    minutes = seconds // 60
    hours = minutes // 60
    seconds = seconds % 60
    minutes = minutes % 60

    weeks = days // 7
    months = days // 30
    years = days // 365

    return years, months, weeks, days, hours, minutes, seconds

def extract_gdrive_image_url(gdrive_url):
    try:
        file_id = gdrive_url.split('/d/')[1].split('/')[0]
        return f"https://drive.google.com/uc?export=view&id={file_id}"
    except:
        return None


# ------------------------
# Estilo CSS personalizado
# ------------------------

st.markdown(
    """
    <style>
    /* Fundo azul escuro para toda a página */
    .main {
        background-color: #001f3f;
        color: white;
    }

    /* Contador com texto branco */
    .contador, .contador * {
        color: white !important;
        font-weight: bold;
        font-size: 20px;
    }

    /* Slider com números em branco */
    .stSlider > div[data-testid="stVerticalBlock"] {
        color: white !important;
    }

    /* Remove cor padrão de links para branco */
    a {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# Configuração da página
# ------------------------

# ------------------------
# 1. Título
# ------------------------
st.markdown("# Nosotros")

# ------------------------
# 2. Carrossel de imagens
# ------------------------
st.markdown("## Nós")

image_links = [
  "https://nosotros-app.onrender.com/imagem/imagem1",
  "https://nosotros-app.onrender.com/imagem/imagem2",
  "https://nosotros-app.onrender.com/imagem/imagem3",
  "https://nosotros-app.onrender.com/imagem/imagem4",
  "https://nosotros-app.onrender.com/imagem/imagem5",
  "https://nosotros-app.onrender.com/imagem/imagem6",
  "https://nosotros-app.onrender.com/imagem/imagem7",
  "https://nosotros-app.onrender.com/imagem/imagem8",
  "https://nosotros-app.onrender.com/imagem/imagem9",
  "https://nosotros-app.onrender.com/imagem/imagem10",
  "https://nosotros-app.onrender.com/imagem/imagem11",
  "https://nosotros-app.onrender.com/imagem/imagem12",
  "https://nosotros-app.onrender.com/imagem/imagem13",
  "https://nosotros-app.onrender.com/imagem/imagem14",
  "https://nosotros-app.onrender.com/imagem/imagem15",
  "https://nosotros-app.onrender.com/imagem/imagem16",
  "https://nosotros-app.onrender.com/imagem/imagem17",
  "https://nosotros-app.onrender.com/imagem/imagem18",
  "https://nosotros-app.onrender.com/imagem/imagem19",
  "https://nosotros-app.onrender.com/imagem/imagem20",
  "https://nosotros-app.onrender.com/imagem/imagem21",
  "https://nosotros-app.onrender.com/imagem/imagem22",
  "https://nosotros-app.onrender.com/imagem/imagem23",
  "https://nosotros-app.onrender.com/imagem/imagem24",
  "https://nosotros-app.onrender.com/imagem/imagem25",
  "https://nosotros-app.onrender.com/imagem/imagem26",
  "https://nosotros-app.onrender.com/imagem/imagem27",
  "https://nosotros-app.onrender.com/imagem/imagem28",
  "https://nosotros-app.onrender.com/imagem/imagem29",
  "https://nosotros-app.onrender.com/imagem/imagem30",
  "https://nosotros-app.onrender.com/imagem/imagem31",
  "https://nosotros-app.onrender.com/imagem/imagem32",
  "https://nosotros-app.onrender.com/imagem/imagem33",
  "https://nosotros-app.onrender.com/imagem/imagem34",
  "https://nosotros-app.onrender.com/imagem/imagem35",
  "https://nosotros-app.onrender.com/imagem/imagem36",
  "https://nosotros-app.onrender.com/imagem/imagem37",
  "https://nosotros-app.onrender.com/imagem/imagem38",
  "https://nosotros-app.onrender.com/imagem/imagem39",
  "https://nosotros-app.onrender.com/imagem/imagem40",
  "https://nosotros-app.onrender.com/imagem/imagem41",
  "https://nosotros-app.onrender.com/imagem/imagem42",
  "https://nosotros-app.onrender.com/imagem/imagem43",
  "https://nosotros-app.onrender.com/imagem/imagem44",
  "https://nosotros-app.onrender.com/imagem/imagem45",
  "https://nosotros-app.onrender.com/imagem/imagem46",
  "https://nosotros-app.onrender.com/imagem/imagem47",
  "https://nosotros-app.onrender.com/imagem/imagem48",
  "https://nosotros-app.onrender.com/imagem/imagem49",
  "https://nosotros-app.onrender.com/imagem/imagem50",
  "https://nosotros-app.onrender.com/imagem/imagem51",
  "https://nosotros-app.onrender.com/imagem/imagem52",
  "https://nosotros-app.onrender.com/imagem/imagem53",
  "https://nosotros-app.onrender.com/imagem/imagem54",
  "https://nosotros-app.onrender.com/imagem/imagem55",
  "https://nosotros-app.onrender.com/imagem/imagem56",
  "https://nosotros-app.onrender.com/imagem/imagem57",
  "https://nosotros-app.onrender.com/imagem/imagem58",
  "https://nosotros-app.onrender.com/imagem/imagem59",
  "https://nosotros-app.onrender.com/imagem/imagem60",
  "https://nosotros-app.onrender.com/imagem/imagem61",
  "https://nosotros-app.onrender.com/imagem/imagem62",
  "https://nosotros-app.onrender.com/imagem/imagem63",
  "https://nosotros-app.onrender.com/imagem/imagem64",
  "https://nosotros-app.onrender.com/imagem/imagem65",
  "https://nosotros-app.onrender.com/imagem/imagem66",
  "https://nosotros-app.onrender.com/imagem/imagem67",
  "https://nosotros-app.onrender.com/imagem/imagem68",
  "https://nosotros-app.onrender.com/imagem/imagem69",
  "https://nosotros-app.onrender.com/imagem/imagem70",
  "https://nosotros-app.onrender.com/imagem/imagem71",
  "https://nosotros-app.onrender.com/imagem/imagem72",
  "https://nosotros-app.onrender.com/imagem/imagem73",
  "https://nosotros-app.onrender.com/imagem/imagem74",
  "https://nosotros-app.onrender.com/imagem/imagem75",
  "https://nosotros-app.onrender.com/imagem/imagem76",
  "https://nosotros-app.onrender.com/imagem/imagem77",
  "https://nosotros-app.onrender.com/imagem/imagem78",
  "https://nosotros-app.onrender.com/imagem/imagem79",
  "https://nosotros-app.onrender.com/imagem/imagem80",
  "https://nosotros-app.onrender.com/imagem/imagem81",
  "https://nosotros-app.onrender.com/imagem/imagem82",
  "https://nosotros-app.onrender.com/imagem/imagem83",
  "https://nosotros-app.onrender.com/imagem/imagem84",
  "https://nosotros-app.onrender.com/imagem/imagem85",
  "https://nosotros-app.onrender.com/imagem/imagem86",
  "https://nosotros-app.onrender.com/imagem/imagem87",
  "https://nosotros-app.onrender.com/imagem/imagem88",
  "https://nosotros-app.onrender.com/imagem/imagem89",
  "https://nosotros-app.onrender.com/imagem/imagem90",
  "https://nosotros-app.onrender.com/imagem/imagem91",
  "https://nosotros-app.onrender.com/imagem/imagem92",
  "https://nosotros-app.onrender.com/imagem/imagem93"
]

image_urls = [extract_gdrive_image_url(url) for url in image_links if extract_gdrive_image_url(url)]

if image_urls:
    current = st.slider("Escolha a imagem", min_value=0, max_value=len(image_urls)-1, step=1, label_visibility="collapsed")
    st.image(image_urls[current], use_column_width=True)
else:
    st.warning("Nenhuma imagem válida fornecida. Verifique os links.")

# ------------------------
# 3. Contador de tempo com atualização automática
# ------------------------

from streamlit_autorefresh import st_autorefresh

# Atualização automática a cada 1 segundo
st_autorefresh(interval=1000, key="contador_refresco")

# Data de referência
data_inicial = datetime(2024, 1, 13)
agora = datetime.now()

# Calcula diferença total
diferenca = agora - data_inicial

# Calcular anos completos (sem considerar anos bissextos com precisão extrema)
anos = agora.year - data_inicial.year
# Verifica se ainda não passou o mês e dia do início no ano atual
if (agora.month, agora.day) < (data_inicial.month, data_inicial.day):
    anos -= 1

# Data inicial ajustada com os anos completos
data_com_anos = datetime(data_inicial.year + anos, data_inicial.month, data_inicial.day)
restante = agora - data_com_anos

# Dias, horas, minutos, segundos restantes depois de contar os anos
dias = restante.days
segundos_totais = restante.seconds
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

# Interface
st.title("Desde 13/01/2024 ja se passaram...")
st.markdown(f"### {anos} anos, {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")

# ------------------------
# 4. Texto de arquivo .txt
# ------------------------
st.markdown("---")
st.markdown("## Meu bem...")

st.markdown(""" Minha Princesa 

Lembre-se sempre que vc é, todos os dias e momentos, a minha melhor escolha da vida!!!!
estamos juntos até o céu!
quero vc hj e pra sempre.
sempre vou cuidar de vc meu amorzinho!
vc é minha promessa mais linda 

EU TE AMO PARA SEMPRE MEU FUTURO """)
