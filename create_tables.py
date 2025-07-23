# crear_tablas.py
from app import engine, Session
from app.models import Base, Usuario, Diario
from sqlalchemy.exc import IntegrityError
from datetime import date

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas (si no existían)")

# Insertar usuario de prueba
with Session() as session:
    if not session.query(Usuario).first():
        demo_user = Usuario(username="admin", password="1234")  # Solo para pruebas
        session.add(demo_user)
        try:
            session.commit()
            print("👤 Usuario admin/1234 creado")
        except IntegrityError:
            session.rollback()
            print("⚠️ Usuario ya existente")

    if not session.query(Diario).first():
        registros = [
            Diario(fecha=date(2025, 7, 20), actividad="Inicio de obra", cantidad=15.5),
            Diario(fecha=date(2025, 7, 21), actividad="Movimiento de suelo", cantidad=28.0)
        ]
        session.add_all(registros)
        session.commit()
        print("📋 Registros de prueba cargados en 'diarios'")
