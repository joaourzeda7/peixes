from flask import Flask, render_template
import logging

app = Flask(__name__)

# Configuração básica de logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Página inicial
@app.route('/')
def index():
    logger.debug("Página inicial carregada")  # Usando logging em vez de print
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Erro ao carregar a página inicial: {e}")
        return "Erro ao carregar a página", 500

# Página sobre os peixes abissais
@app.route('/sobre')
def sobre():
    try:
        return render_template('sobre.html')
    except Exception as e:
        logger.error(f"Erro ao carregar a página 'Sobre': {e}")
        return "Erro ao carregar a página", 500

# Página de aparições recentes
@app.route('/aparicoes')
def aparicoes():
    try:
        return render_template('aparicoes.html')
    except Exception as e:
        logger.error(f"Erro ao carregar a página 'Aparições': {e}")
        return "Erro ao carregar a página", 500

if __name__ == '__main__':
    app.run(debug=True)