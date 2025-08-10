# Demag Compressor Performance App

Aplicativo para análise de performance de compressores alternativos de gás natural **Demag**, inspirado em ferramentas como Ariel 7, DR Size e Power Flow.

## 🚀 Funcionalidades
- Cálculo de potência, vazão, temperaturas de descarga e mais.
- Escolha entre unidades Métricas (SI) e Imperiais (Oil & Gas).
- Gráficos interativos de Potência × Vazão e Temperatura por estágio.
- Exportação de resultados em CSV e PDF.
- Varredura automática para múltiplos pontos de vazão.
- Compatível com **Streamlit Cloud** para uso direto no navegador.

## 📦 Estrutura do Repositório
```
app.py              -> Aplicativo principal
calculations.py     -> Funções de cálculo
utils.py            -> Funções de conversão de unidades e utilidades
requirements.txt    -> Dependências
data/sample_curve.csv -> Exemplo de curva para Curve-Fit
```

## 🖥 Rodando localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁ Deploy no Streamlit Cloud
1. Crie um repositório no GitHub e envie estes arquivos.
2. No [Streamlit Cloud](https://share.streamlit.io), clique **New app**.
3. Escolha o repositório e selecione `app.py` como arquivo principal.
4. Clique em **Deploy**.

## 📸 Capturas de Tela
![Home Screen](docs/screenshot_home.png)
![Resultados](docs/screenshot_results.png)

---
Desenvolvido para análise técnica de compressores Demag.
