const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Dicionário com as imagens protegidas
const imagens = {
  "imagem1": "https://drive.google.com/uc?export=view&id=16Y3LOzL27Kw7AWujAEXrtuigXYgHl37e",
  "imagem2": "https://drive.google.com/uc?export=view&id=1uh1nO26WwK96W3Y8ldpi8zU3_eZnZeXB",
  "imagem3": "https://drive.google.com/uc?export=view&id=1NiiprzckDCrc4bnG4iqig5lhnTMOtqNL",
  "imagem4": "https://drive.google.com/uc?export=view&id=1DrDZcQPyKpndchHc0W7Rw7pBfP_igiZE",
  "imagem5": "https://drive.google.com/uc?export=view&id=1AlquhekxMYQ2YWhzZxWYq1gsahiZwg75",
  "imagem6": "https://drive.google.com/uc?export=view&id=1yc2wICnIxe0nw2z0mRJyAi6ErPCHWEiK",
  "imagem7": "https://drive.google.com/uc?export=view&id=1LFlTvIGYdl4ZfdV11ijBCKzMcSfGXk4H",
  "imagem8": "https://drive.google.com/uc?export=view&id=1J8T1EjW8OF8CSvTg-wdtytXaKzkpjA-0",
  "imagem9": "https://drive.google.com/uc?export=view&id=1M4m8Xf0FyFcsZj0t5xXih_vuZiwd8AM6",
  "imagem10": "https://drive.google.com/uc?export=view&id=1xDv26JKNVbv8hxsnQPdqtLYLzcEtaIC5",
  "imagem11": "https://drive.google.com/uc?export=view&id=10H3a6VASrWur7pZxX4oag1tnxYtp59KE",
  "imagem12": "https://drive.google.com/uc?export=view&id=120mfN1paOoOri7EXhoZGIF73Dz5QjKJx",
  "imagem13": "https://drive.google.com/uc?export=view&id=1c-aBh4047OXMv_MFY9JPybTzx80WVXo8",
  "imagem14": "https://drive.google.com/uc?export=view&id=1irHc-FDP30v1XhYVxIDI7TNeJKRR-n5U",
  "imagem15": "https://drive.google.com/uc?export=view&id=1-lhF6EbgmtpY248i1AOvHtBFcbBWPuf3",
  "imagem16": "https://drive.google.com/uc?export=view&id=1gFrGU-tr2vLfSf8CxGCE0-7yfkZO1aZ4",
  "imagem17": "https://drive.google.com/uc?export=view&id=12bAn28UofPGuwdbZGdM8H5BJbGqmuCUw",
  "imagem18": "https://drive.google.com/uc?export=view&id=1cZW851RP-S2hENct8m4iZndbyuWogQDv",
  "imagem19": "https://drive.google.com/uc?export=view&id=1TUBagaxavqKn6fPYHfiOC8N4d0cTKSvh",
  "imagem20": "https://drive.google.com/uc?export=view&id=1sh9q219vVN540AUBaz0LAMO8VZ8onN1U",
  "imagem21": "https://drive.google.com/uc?export=view&id=1mDKl3Pwdval3kJdQ7aGICnjCkNOelFDj",
  "imagem22": "https://drive.google.com/uc?export=view&id=1LO4Dz6NxCDI5FClkBmdODAmYegfiwuK8",
  "imagem23": "https://drive.google.com/uc?export=view&id=1yHph32yqczZsSzEah8FRym52zEhQ7KE-",
  "imagem24": "https://drive.google.com/uc?export=view&id=1rWMOEHACr3iU9fXoV_dJLc3ZV5vS4tVT",
  "imagem25": "https://drive.google.com/uc?export=view&id=1RfOdwOu0hrR3pD2jGgrKoueThHaABgSz",
  "imagem26": "https://drive.google.com/uc?export=view&id=1easBPDyMJ2b0n8sE8wT6wBfNSKgCBqKR",
  "imagem27": "https://drive.google.com/uc?export=view&id=14K23c0vzFoLk4tzDnGAiAGrcL93dwjN8",
  "imagem28": "https://drive.google.com/uc?export=view&id=19A8iVMADFOpH9YYM2mCee72GBq76h32i",
  "imagem29": "https://drive.google.com/uc?export=view&id=1_XG7mMP8mZ2kW0qQWoRsJpqPNcU7l4sI",
  "imagem30": "https://drive.google.com/uc?export=view&id=1vv7qUpdpiXnVLG46NwJroDlIPSxyvDSg",
  "imagem31": "https://drive.google.com/uc?export=view&id=1cv9ri4mT4Ffv89yBZKJYHgziAO4le4Ib",
  "imagem32": "https://drive.google.com/uc?export=view&id=1f3PzuqwrGZ96xaTwlScAzZO5sTJM-rfL",
  "imagem33": "https://drive.google.com/uc?export=view&id=1Y9VR0dkOFxk-CyyVet6e_9vwcI9NtLDy",
  "imagem34": "https://drive.google.com/uc?export=view&id=1n3V_yq_sXuP7Cl4GRtlAxlkMFdMTyiFQ",
  "imagem35": "https://drive.google.com/uc?export=view&id=1a0hYzhPworf86MWcPlhvIrWxJAkX56y5",
  "imagem36": "https://drive.google.com/uc?export=view&id=1ZSg_nd7bJV9BBh7FqtFTpvL-JmURRy_6",
  "imagem37": "https://drive.google.com/uc?export=view&id=1kaNHrvZFshYY7ZioR23Xwg6uGrAY224f",
  "imagem38": "https://drive.google.com/uc?export=view&id=1nNEsF0UlfDtpF8SaPeZWDaswXHpzhHeE",
  "imagem39": "https://drive.google.com/uc?export=view&id=1NnIhvsVPDenqS0vJyWGo16ijIY2LGwX0",
  "imagem40": "https://drive.google.com/uc?export=view&id=1jZrZLt85upVVTVU8rk7cb8RNsJ_IM-II",
  "imagem41": "https://drive.google.com/uc?export=view&id=1eY-WpVvGuXt50j9G_9p1rUymLZPVcrmR",
  "imagem42": "https://drive.google.com/uc?export=view&id=1GL-5lFNOzO1O4epydHM7kTrzNeCWXYhB",
  "imagem43": "https://drive.google.com/uc?export=view&id=17WM4ODFtiLQXQ_kY-kmttY1bCs58W9m5",
  "imagem44": "https://drive.google.com/uc?export=view&id=1bo3IlMGLBTCzmSh26gmLU1GvYo9bx8bz",
  "imagem45": "https://drive.google.com/uc?export=view&id=1eGy8vDw6A1SU0-CUMAC-nl7B94hz4KH2",
  "imagem46": "https://drive.google.com/uc?export=view&id=10LqwNbDwqCN9j66bXC7dSkh0mEYteva1",
  "imagem47": "https://drive.google.com/uc?export=view&id=1NDb6OEO6d6XYtV1q-bWmNoPnLToUoTd9",
  "imagem48": "https://drive.google.com/uc?export=view&id=1tujpudtNXGHNNDH3bA4Eoy85y77lUVQM",
  "imagem49": "https://drive.google.com/uc?export=view&id=18RmLNt9d12hAr2nTcj92UFyxLhPi1piD",
  "imagem50": "https://drive.google.com/uc?export=view&id=1KDC3knS2XfSAJi2qgf_FSB_JHhvagqNY",
  "imagem51": "https://drive.google.com/uc?export=view&id=1QMNEpKaJ3SZmklGTpkZ51UdVCs-AvtK6",
  "imagem52": "https://drive.google.com/uc?export=view&id=1b9xaWjaOLGI13PkWYahgM1UtfJXiyTlW",
  "imagem53": "https://drive.google.com/uc?export=view&id=1j8n6aCL3kF9t1vRvovOG9QaqzoLokeQ6",
  "imagem54": "https://drive.google.com/uc?export=view&id=1o5xkGAyCcNjKtq-j16G20PlIQYdGeBcY",
  "imagem55": "https://drive.google.com/uc?export=view&id=1XHPcUAlaV0D5v1gktMAaNY4TamzWKwVA",
  "imagem56": "https://drive.google.com/uc?export=view&id=1JYytKRQLlOdQcDvewU5des6qo8ycZSZq",
  "imagem57": "https://drive.google.com/uc?export=view&id=1_svdowiw43V6ZgBv4q0tPZj8JkxJjzck",
  "imagem58": "https://drive.google.com/uc?export=view&id=17mVutbJTYSTrjUxsMc4IV3AN9YzWXGEG",
  "imagem59": "https://drive.google.com/uc?export=view&id=1XCz3gbiUqUG5HyiAMcrz_w_iyiumKLG0",
  "imagem60": "https://drive.google.com/uc?export=view&id=1RpRyCC6m0EekMb9saQDKJ2KCIGwq2pVk",
  "imagem61": "https://drive.google.com/uc?export=view&id=15D6-9gSklmY3qg8tQaenP-u9EnSzxG5n",
  "imagem62": "https://drive.google.com/uc?export=view&id=11m1JC0gjudwxQfrQRxPcsaev1sMqaKFs",
  "imagem63": "https://drive.google.com/uc?export=view&id=1g9JytVGaJEMCMPh_9l1OyaBS_oE9ccxn",
  "imagem64": "https://drive.google.com/uc?export=view&id=1SgkFwCz_2EkR5SQlBp5szS6LsZqnRiw-",
  "imagem65": "https://drive.google.com/uc?export=view&id=1XEICl17uuFB1-Z81UkzGDrMOzC74a0Wh",
  "imagem66": "https://drive.google.com/uc?export=view&id=1t9jXmLpYAbO1h8dUxmlyqAUzRSStGQCr",
  "imagem67": "https://drive.google.com/uc?export=view&id=1M0Sp3czHM4dyecPLvvKuRoXQKJ_1qccy",
  "imagem68": "https://drive.google.com/uc?export=view&id=1yuJA3X-YpV33JhYBu75POjpUFHcRWIUr",
  "imagem69": "https://drive.google.com/uc?export=view&id=1GAqFbXfdapujHR2AgNakwnRmXf0Nt8fz",
  "imagem70": "https://drive.google.com/uc?export=view&id=16gxbC-C-05l-GpAD3dI7EZ23-UrOECrI",
  "imagem71": "https://drive.google.com/uc?export=view&id=1Qm-sWj6tk0qHMuy9M8YrsuJL1VLfdxWN",
  "imagem72": "https://drive.google.com/uc?export=view&id=1O3iYlMsXTpwWGq1cxqDhELZ5R4_87aNL",
  "imagem73": "https://drive.google.com/uc?export=view&id=1oJdRh8oTnZe6remLTnbbi8AAl5oTt0xz",
  "imagem74": "https://drive.google.com/uc?export=view&id=1mH8wBdPoiYd70YN6wYAprD-EuHDuYv9D",
  "imagem75": "https://drive.google.com/uc?export=view&id=1yv5P8Y7WHqSlJoSEMaFifCGrp95WWiVp",
  "imagem76": "https://drive.google.com/uc?export=view&id=1KcTI_ddblB-Z4KgUMVHzyeOGjREbqfW-",
  "imagem77": "https://drive.google.com/uc?export=view&id=1CAMPLzP0NYAgTRNNcxqOcOZ9VMhDQx0p",
  "imagem78": "https://drive.google.com/uc?export=view&id=1BcBwbkoqdsV5yVU856xLFHrH3rNAh589",
  "imagem79": "https://drive.google.com/uc?export=view&id=1lIHMaaIrsv59K6SRKPZiT_zmR9XOFQ4N",
  "imagem80": "https://drive.google.com/uc?export=view&id=1s-cvSgvNnRcqfcFim4WS-xlyRvjJ04du",
  "imagem81": "https://drive.google.com/uc?export=view&id=19LNQC68EgC_K6JtTCyrXfT9VK-mF5Ghz",
  "imagem82": "https://drive.google.com/uc?export=view&id=1iVXkxjwbErXIx0waf_taM0r_ofTFwuyV",
  "imagem83": "https://drive.google.com/uc?export=view&id=1DTi2xDYSHHN9jVdRcTMNkUlgGgdNbDJI",
  "imagem84": "https://drive.google.com/uc?export=view&id=1TF-P3yY3qCMtGuvyanImtVZqoaATcZTs",
  "imagem85": "https://drive.google.com/uc?export=view&id=18s4g4R1syBzLtFK_th0-sJ-bMqzncRol",
  "imagem86": "https://drive.google.com/uc?export=view&id=1FA9hiCOdEeMmFAapUVqhrUJgIsY_Jtqp",
  "imagem87": "https://drive.google.com/uc?export=view&id=1GU4ewL4PWQ7fyYBNqpKZ6-Z5cXZ2Ytmp",
  "imagem88": "https://drive.google.com/uc?export=view&id=1FbstqKnE4MZitjF6LtUE6fkN-E4UxwN2",
  "imagem89": "https://drive.google.com/uc?export=view&id=1tVcpOvMC9e-mGem2iN_M0ih8DRNpetJ3",
  "imagem90": "https://drive.google.com/uc?export=view&id=1NfxjncPBglauZAG6rrPkMimJdhdlbY0N",
  "imagem91": "https://drive.google.com/uc?export=view&id=1vMmYx5sHUwcDyjnqkkNr-geHQ8WxTxkC",
  "imagem92": "https://drive.google.com/uc?export=view&id=1OU4oz7LkyYr1db_3NAl_AtYZ01sZnLVP",
  "imagem93": "https://drive.google.com/uc?export=view&id=1V8I69HWkWgAo6F7R9otbLKtCJn1mtHtf"

};

app.get('/imagem/:id', async (req, res) => {
  const idPublico = req.params.id;
  const idDrive = imagens[idPublico];

  if (!idDrive) return res.status(404).send('Imagem não encontrada');

  const url = `https://drive.google.com/uc?export=view&id=${idDrive}`;

  try {
    const response = await axios.get(url, { responseType: 'stream' });
    res.setHeader('Content-Type', response.headers['content-type']);
    response.data.pipe(res);
  } catch (err) {
    res.status(500).send('Erro ao carregar imagem');
  }
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
