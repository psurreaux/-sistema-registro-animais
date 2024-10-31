from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Inicializando o aplicativo FastAPI
app = FastAPI()

# Conectando com o banco de dados
def get_db_connection():
    conn = sqlite3.connect("animais.db")
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

# Modelo de dados para a entrada de animal
class Animal(BaseModel):
    sexo: str
    idade: int
    qualidade: str

# Endpoint para registrar um novo animal
@app.post("/animais/")
async def registrar_animal(animal: Animal):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO animais (sexo, idade, qualidade) 
        VALUES (?, ?, ?)
    ''', (animal.sexo, animal.idade, animal.qualidade))
    conn.commit()
    conn.close()
    return {"message": "Animal registrado com sucesso!"}

# Endpoint para listar todos os animais
@app.get("/animais/")
async def listar_animais():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animais")
    animais = cursor.fetchall()
    conn.close()
    return [dict(animal) for animal in animais]
