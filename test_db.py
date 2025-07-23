from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/planillas_db'

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM diarios"))
        filas = result.mappings().all()  # <- acá la magia
        print("Conexión exitosa:", filas)
except Exception as e:
    print("Error:", e)
