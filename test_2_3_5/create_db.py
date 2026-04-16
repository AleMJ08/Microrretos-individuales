#!/usr/bin/env python3
"""
create_db.py
Crea la base de datos `reto_alejandro.db`, crea la tabla LOGS (id, evento)
 e inserta 30 eventos inventados.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / 'reto_alejandro.db'

EVENTS = [
    "Inicio del sistema",
    "Usuario admin inició sesión",
    "Carga de configuración completa",
    "Error: falta archivo de recursos",
    "Conexión a la API establecida",
    "Tarea programada ejecutada",
    "Backup automático realizado",
    "Alerta: uso de CPU alto",
    "Servicio de correo reiniciado",
    "Actualización de dependencias completada",
    "Nuevo usuario registrado",
    "Se generó informe mensual",
    "Sesión de usuario finalizada",
    "Archivo subido correctamente",
    "Descarga fallida por timeout",
    "Permisos de archivo actualizados",
    "Cache limpiada",
    "Base de datos optimizada",
    "Token de acceso renovado",
    "Petición inválida recibida",
    "Integración con tercero probada",
    "Registro de auditoría creado",
    "Prueba de rendimiento ejecutada",
    "Sesión SSH establecida",
    "Cierre de mantenimiento programado",
    "Modo depuración activado",
    "Reporte de seguridad enviado",
    "Migración de datos iniciada",
    "Migración de datos finalizada",
    "Reinicio del servidor completado",
]


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Crear tabla LOGS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS LOGS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evento TEXT NOT NULL
    )
    """)

    # Vaciar tabla por si ya existía - opcional: comentar si no se desea borrar
    cur.execute("DELETE FROM LOGS")

    # Insertar eventos
    cur.executemany("INSERT INTO LOGS (evento) VALUES (?)", ((e,) for e in EVENTS))
    conn.commit()

    # Verificación rápida
    cur.execute("SELECT COUNT(*) FROM LOGS")
    count = cur.fetchone()[0]

    print(f"Base de datos creada en: {DB_PATH}")
    print(f"Filas en LOGS: {count}")

    # Mostrar las primeras 5 filas
    cur.execute("SELECT id, evento FROM LOGS ORDER BY id LIMIT 5")
    rows = cur.fetchall()
    print("Primeras 5 filas:")
    for r in rows:
        print(r)

    conn.close()


if __name__ == '__main__':
    main()
