# ML-prev-colheita

Este projeto utiliza um modelo de Machine Learning para prever o rendimento de uma colheita (*Crop Yield*) com base em dados climáticos e da região de cultivo. 

O sistema é dividio em partes:

- **Backend:** API desenvolvida com FastAPI responsável por carregar o modelo treinado e realizar as predições. 
- **Fronted:** Interface desenvolvida em HTML, CSS e JavaScript para que o usuário informe os dados e visualize o resultado. 

---

## Tecnologias utilizadas

### Backend

- Python 3.10+
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Frontend

- HTML5
- CSS3
- JavaScript

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/6iove/ML-prev-colheita.git
```

---

## Configurando o Backend

Entre na pasta:

```bash
cd backend
```

Crie um ambiente virtual (opcional):

### Windows

```bash
python -m venv ven
```

Ative o ambiente:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv ven
```

Ative o ambinte:
```bash
source venv/bin/ativate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Executando o Backend

Ainda dentro da pasta **backend**, execute: 

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

A documentação automática pode ser acessada em:

```
http://127.0.0.1:8000/docs
```

---

## Executando o Frontend 

Abra a pasta **frontend**:

```bash
cd frontend
```

O arquivo `index.html` pode ser aberto diretamente no navegador ou executado por um servidor local, como a extensão **Live Server** do Visual Studio Code.

Caso utilize o Live Server: 

1. Abra a pasta `frontend` no VS Code.
2. Clique com o botão direito em `index.html`.
3. Selecione **Open with Live Server**.

O frontend fará requisições para a API em:

```
http://127.0.0.1:8000/predict
```

Por isso, **o backend deve estar em execução antes de utilizar a interface**.

---

## Funcionamento 

1. O usuário preenche os dados climáticos no frontend.
2. O frontend envia uma requisição para a API utilizando o método **POST**.
3. A API recebe os dados.
4. O modelo de Machine Learning realiza a previsão.
5. A API retorna o rendimento previsto.
6. O frontend exibe o resultado ao usuário.

---
## Observações 

- O arquivo `dados_fazenda.pkl` deve estar localizado na pasta `backend/modelo`.
- O modelo foi treinado previamente em um notebook do Google Colab e exportado utilizando `joblib`.
- É necessário iniciar o backend antes de utilizar o frontend.
