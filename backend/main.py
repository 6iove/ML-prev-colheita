from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

'''
Inicialização da API
'''
app = FastAPI(
    title="API de Previsão de Colheita",
    version = "1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)


'''
Carregando o modelo
'''
try:
    modelo = joblib.load("modelo/dados_fazenda.pkl")
except Exception as e:
    modelo = None
    print(f"Erro ao carregar modelo: {e}")
   
    
'''
Modelo de entrada
'''
class DadosColheita(BaseModel):
    year: float
    max_temp: float
    min_temp: float
    max_wind_speed: float
    min_wind_speed: float
    precipitation: float
    par: float
    root_soil_wetness: float
    surface_soil_wetness: float
    humidity: float
    earth_skin_temp: float
    div_chittagong: bool
    div_khulna: bool
    div_rajshahi: bool
    div_rangpur: bool
    div_sylhet: bool
    

'''
Rota inicial
'''
@app.get("/")
def home():
    return{"mensagem": "API de previsão de colheita funcionando."}


'''
Predição
'''
@app.post("/predict")
def prever_colheita(dados: DadosColheita):
    if modelo is None:
        raise HTTPException(
            status_code=500, 
            detail="Modelo não carregado."
        )
    
    entrada = pd.DataFrame({
        "year": [dados.year],
        "Max temp": [dados.max_temp],
        "Min temp": [dados.min_temp],
        "Max Wind Speed": [dados.max_wind_speed],
        "Min wind speed": [dados.min_wind_speed],
        "Precipitation Corrected Sum": [dados.precipitation],
        "All Sky Surface Total PAR": [dados.par],
        "Root Zone Soil Wetness": [dados.root_soil_wetness],
        "Surface Soil Wetness": [dados.surface_soil_wetness],
        "Humidity": [dados.humidity],
        "Earth Skin Temp": [dados.earth_skin_temp],
        "Division_Chittagong": [dados.div_chittagong],
        "Division_Khulna": [dados.div_khulna],
        "Division_Rajshahi": [dados.div_rajshahi],
        "Division_Rangpur": [dados.div_rangpur],
        "Division_Sylhet": [dados.div_sylhet]
    })
    
    try:
        previsao = modelo.predict(entrada)
        
        return {
            "crop_yield_previsto": round(float(previsao[0]), 4)
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )