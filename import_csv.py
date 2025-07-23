import pandas as pd
from app.models import Diario
from app import Session
from datetime import datetime

df = pd.read_csv('data/diarios.csv')

session = Session()

for _, row in df.iterrows():
    nuevo = Diario(
        fecha=datetime.strptime(row['fecha'], '%Y-%m-%d'),
        actividad=row['actividad'],
        cantidad=row['cantidad']
    )
    session.add(nuevo)

session.commit()
session.close()
print("Importación completa.")
