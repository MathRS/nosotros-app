import streamlit as st
import requests
from datetime import datetime

# ------------------------
# Funções auxiliares
# ------------------------

def get_text_from_gdrive(gdrive_url):
    try:
        file_id = gdrive_url.split('/d/')[1].split('/')[0]
        download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
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
st.set_page_config(layout="wide")

# ------------------------
# 1. Título
# ------------------------
st.markdown("# Nosotros")

# ------------------------
# 2. Carrossel de imagens
# ------------------------
st.markdown("## Nossa Galeria")

image_links = [
     "https://drive.google.com/uc?export=view&id=16Y3LOzL27Kw7AWujAEXrtuigXYgHl37e",
     "https://drive.google.com/uc?export=view&id=1uh1nO26WwK96W3Y8ldpi8zU3_eZnZeXB",
     "https://drive.google.com/uc?export=view&id=1NiiprzckDCrc4bnG4iqig5lhnTMOtqNL",
     "https://drive.google.com/uc?export=view&id=1DrDZcQPyKpndchHc0W7Rw7pBfP_igiZE",
     "https://drive.google.com/uc?export=view&id=1AlquhekxMYQ2YWhzZxWYq1gsahiZwg75",
     "https://drive.google.com/uc?export=view&id=1yc2wICnIxe0nw2z0mRJyAi6ErPCHWEiK",
     "https://drive.google.com/uc?export=view&id=1LFlTvIGYdl4ZfdV11ijBCKzMcSfGXk4H",
     "https://drive.google.com/uc?export=view&id=1J8T1EjW8OF8CSvTg-wdtytXaKzkpjA-0",
     "https://drive.google.com/uc?export=view&id=1M4m8Xf0FyFcsZj0t5xXih_vuZiwd8AM6",
     "https://drive.google.com/uc?export=view&id=1xDv26JKNVbv8hxsnQPdqtLYLzcEtaIC5",
     "https://drive.google.com/uc?export=view&id=10H3a6VASrWur7pZxX4oag1tnxYtp59KE",
     "https://drive.google.com/uc?export=view&id=120mfN1paOoOri7EXhoZGIF73Dz5QjKJx",
     "https://drive.google.com/uc?export=view&id=1c-aBh4047OXMv_MFY9JPybTzx80WVXo8",
     "https://drive.google.com/uc?export=view&id=1irHc-FDP30v1XhYVxIDI7TNeJKRR-n5U",
     "https://drive.google.com/uc?export=view&id=1-lhF6EbgmtpY248i1AOvHtBFcbBWPuf3",
     "https://drive.google.com/uc?export=view&id=1gFrGU-tr2vLfSf8CxGCE0-7yfkZO1aZ4",
     "https://drive.google.com/uc?export=view&id=12bAn28UofPGuwdbZGdM8H5BJbGqmuCUw",
     "https://drive.google.com/uc?export=view&id=1cZW851RP-S2hENct8m4iZndbyuWogQDv",
     "https://drive.google.com/uc?export=view&id=1TUBagaxavqKn6fPYHfiOC8N4d0cTKSvh",
     "https://drive.google.com/uc?export=view&id=1sh9q219vVN540AUBaz0LAMO8VZ8onN1U",
     "https://drive.google.com/uc?export=view&id=1mDKl3Pwdval3kJdQ7aGICnjCkNOelFDj",
     "https://drive.google.com/uc?export=view&id=1LO4Dz6NxCDI5FClkBmdODAmYegfiwuK8",
     "https://drive.google.com/uc?export=view&id=1yHph32yqczZsSzEah8FRym52zEhQ7KE-",
     "https://drive.google.com/uc?export=view&id=1rWMOEHACr3iU9fXoV_dJLc3ZV5vS4tVT",
     "https://drive.google.com/uc?export=view&id=1RfOdwOu0hrR3pD2jGgrKoueThHaABgSz",
     "https://drive.google.com/uc?export=view&id=1easBPDyMJ2b0n8sE8wT6wBfNSKgCBqKR",
     "https://drive.google.com/uc?export=view&id=14K23c0vzFoLk4tzDnGAiAGrcL93dwjN8",
     "https://drive.google.com/uc?export=view&id=19A8iVMADFOpH9YYM2mCee72GBq76h32i",
     "https://drive.google.com/uc?export=view&id=1_XG7mMP8mZ2kW0qQWoRsJpqPNcU7l4sI",
     "https://drive.google.com/uc?export=view&id=1vv7qUpdpiXnVLG46NwJroDlIPSxyvDSg",
     "https://drive.google.com/uc?export=view&id=1cv9ri4mT4Ffv89yBZKJYHgziAO4le4Ib",
     "https://drive.google.com/uc?export=view&id=1f3PzuqwrGZ96xaTwlScAzZO5sTJM-rfL",
     "https://drive.google.com/uc?export=view&id=1Y9VR0dkOFxk-CyyVet6e_9vwcI9NtLDy",
     "https://drive.google.com/uc?export=view&id=1n3V_yq_sXuP7Cl4GRtlAxlkMFdMTyiFQ",
     "https://drive.google.com/uc?export=view&id=1a0hYzhPworf86MWcPlhvIrWxJAkX56y5",
     "https://drive.google.com/uc?export=view&id=1ZSg_nd7bJV9BBh7FqtFTpvL-JmURRy_6",
     "https://drive.google.com/uc?export=view&id=1kaNHrvZFshYY7ZioR23Xwg6uGrAY224f",
     "https://drive.google.com/uc?export=view&id=1nNEsF0UlfDtpF8SaPeZWDaswXHpzhHeE",
     "https://drive.google.com/uc?export=view&id=1NnIhvsVPDenqS0vJyWGo16ijIY2LGwX0",
     "https://drive.google.com/uc?export=view&id=1jZrZLt85upVVTVU8rk7cb8RNsJ_IM-II",
     "https://drive.google.com/uc?export=view&id=1eY-WpVvGuXt50j9G_9p1rUymLZPVcrmR",
     "https://drive.google.com/uc?export=view&id=1GL-5lFNOzO1O4epydHM7kTrzNeCWXYhB",
     "https://drive.google.com/uc?export=view&id=17WM4ODFtiLQXQ_kY-kmttY1bCs58W9m5",
     "https://drive.google.com/uc?export=view&id=1bo3IlMGLBTCzmSh26gmLU1GvYo9bx8bz",
     "https://drive.google.com/uc?export=view&id=1eGy8vDw6A1SU0-CUMAC-nl7B94hz4KH2",
     "https://drive.google.com/uc?export=view&id=10LqwNbDwqCN9j66bXC7dSkh0mEYteva1",
     "https://drive.google.com/uc?export=view&id=1NDb6OEO6d6XYtV1q-bWmNoPnLToUoTd9",
     "https://drive.google.com/uc?export=view&id=1tujpudtNXGHNNDH3bA4Eoy85y77lUVQM",
     "https://drive.google.com/uc?export=view&id=18RmLNt9d12hAr2nTcj92UFyxLhPi1piD",
     "https://drive.google.com/uc?export=view&id=1KDC3knS2XfSAJi2qgf_FSB_JHhvagqNY",
     "https://drive.google.com/uc?export=view&id=1QMNEpKaJ3SZmklGTpkZ51UdVCs-AvtK6",
     "https://drive.google.com/uc?export=view&id=1b9xaWjaOLGI13PkWYahgM1UtfJXiyTlW",
     "https://drive.google.com/uc?export=view&id=1j8n6aCL3kF9t1vRvovOG9QaqzoLokeQ6",
     "https://drive.google.com/uc?export=view&id=1o5xkGAyCcNjKtq-j16G20PlIQYdGeBcY",
     "https://drive.google.com/uc?export=view&id=1XHPcUAlaV0D5v1gktMAaNY4TamzWKwVA",
     "https://drive.google.com/uc?export=view&id=1JYytKRQLlOdQcDvewU5des6qo8ycZSZq",
     "https://drive.google.com/uc?export=view&id=1_svdowiw43V6ZgBv4q0tPZj8JkxJjzck",
     "https://drive.google.com/uc?export=view&id=17mVutbJTYSTrjUxsMc4IV3AN9YzWXGEG",
     "https://drive.google.com/uc?export=view&id=1XCz3gbiUqUG5HyiAMcrz_w_iyiumKLG0",
     "https://drive.google.com/uc?export=view&id=1RpRyCC6m0EekMb9saQDKJ2KCIGwq2pVk",
     "https://drive.google.com/uc?export=view&id=15D6-9gSklmY3qg8tQaenP-u9EnSzxG5n",
     "https://drive.google.com/uc?export=view&id=11m1JC0gjudwxQfrQRxPcsaev1sMqaKFs",
     "https://drive.google.com/uc?export=view&id=1g9JytVGaJEMCMPh_9l1OyaBS_oE9ccxn",
     "https://drive.google.com/uc?export=view&id=1SgkFwCz_2EkR5SQlBp5szS6LsZqnRiw-",
     "https://drive.google.com/uc?export=view&id=1XEICl17uuFB1-Z81UkzGDrMOzC74a0Wh",
     "https://drive.google.com/uc?export=view&id=1t9jXmLpYAbO1h8dUxmlyqAUzRSStGQCr",
     "https://drive.google.com/uc?export=view&id=1M0Sp3czHM4dyecPLvvKuRoXQKJ_1qccy",
     "https://drive.google.com/uc?export=view&id=1yuJA3X-YpV33JhYBu75POjpUFHcRWIUr",
     "https://drive.google.com/uc?export=view&id=1GAqFbXfdapujHR2AgNakwnRmXf0Nt8fz",
     "https://drive.google.com/uc?export=view&id=16gxbC-C-05l-GpAD3dI7EZ23-UrOECrI",
     "https://drive.google.com/uc?export=view&id=1Qm-sWj6tk0qHMuy9M8YrsuJL1VLfdxWN",
     "https://drive.google.com/uc?export=view&id=1O3iYlMsXTpwWGq1cxqDhELZ5R4_87aNL",
     "https://drive.google.com/uc?export=view&id=1oJdRh8oTnZe6remLTnbbi8AAl5oTt0xz",
     "https://drive.google.com/uc?export=view&id=1mH8wBdPoiYd70YN6wYAprD-EuHDuYv9D",
     "https://drive.google.com/uc?export=view&id=1yv5P8Y7WHqSlJoSEMaFifCGrp95WWiVp",
     "https://drive.google.com/uc?export=view&id=1KcTI_ddblB-Z4KgUMVHzyeOGjREbqfW-",
     "https://drive.google.com/uc?export=view&id=1CAMPLzP0NYAgTRNNcxqOcOZ9VMhDQx0p",
     "https://drive.google.com/uc?export=view&id=1BcBwbkoqdsV5yVU856xLFHrH3rNAh589",
     "https://drive.google.com/uc?export=view&id=1lIHMaaIrsv59K6SRKPZiT_zmR9XOFQ4N",
     "https://drive.google.com/uc?export=view&id=1s-cvSgvNnRcqfcFim4WS-xlyRvjJ04du",
     "https://drive.google.com/uc?export=view&id=19LNQC68EgC_K6JtTCyrXfT9VK-mF5Ghz",
     "https://drive.google.com/uc?export=view&id=1iVXkxjwbErXIx0waf_taM0r_ofTFwuyV",
     "https://drive.google.com/uc?export=view&id=1DTi2xDYSHHN9jVdRcTMNkUlgGgdNbDJI",
     "https://drive.google.com/uc?export=view&id=1TF-P3yY3qCMtGuvyanImtVZqoaATcZTs",
     "https://drive.google.com/uc?export=view&id=18s4g4R1syBzLtFK_th0-sJ-bMqzncRol",
     "https://drive.google.com/uc?export=view&id=1FA9hiCOdEeMmFAapUVqhrUJgIsY_Jtqp",
     "https://drive.google.com/uc?export=view&id=1GU4ewL4PWQ7fyYBNqpKZ6-Z5cXZ2Ytmp",
     "https://drive.google.com/uc?export=view&id=1FbstqKnE4MZitjF6LtUE6fkN-E4UxwN2",
     "https://drive.google.com/uc?export=view&id=1tVcpOvMC9e-mGem2iN_M0ih8DRNpetJ3",
     "https://drive.google.com/uc?export=view&id=1NfxjncPBglauZAG6rrPkMimJdhdlbY0N",
     "https://drive.google.com/uc?export=view&id=1vMmYx5sHUwcDyjnqkkNr-geHQ8WxTxkC",
     "https://drive.google.com/uc?export=view&id=1OU4oz7LkyYr1db_3NAl_AtYZ01sZnLVP",
     "https://drive.google.com/uc?export=view&id=1V8I69HWkWgAo6F7R9otbLKtCJn1mtHtf"
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

# Atualiza a cada 1000 ms (1 segundo)
st_autorefresh(interval=1000, key="contador_refresh")

st.markdown("---")
st.markdown("## Contador desde 13/01/2024")

years, months, weeks, days, hours, minutes, seconds = get_elapsed()

st.markdown(
    f"""
    <div class="contador">
    - <b>Anos</b>: {years}  <br>
    - <b>Meses</b>: {months}  <br>
    - <b>Semanas</b>: {weeks}  <br>
    - <b>Dias</b>: {days}  <br>
    - <b>Horas</b>: {hours}  <br>
    - <b>Minutos</b>: {minutes}  <br>
    - <b>Segundos</b>: {seconds}  <br>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------
# 4. Texto de arquivo .txt
# ------------------------
st.markdown("---")
st.markdown("## Texto carregado do Google Drive")

gdrive_link = st.text_input("Cole o link público do arquivo .txt no Google Drive:")

if gdrive_link:
    texto = get_text_from_gdrive(gdrive_link)
    st.text_area("Conteúdo do arquivo:", texto, height=300)
