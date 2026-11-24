import json
import random
from pathlib import Path
from django.conf import settings

RUTA_JSON = Path(settings.BASE_DIR) / "tareas.json"


def cargar_tareas():
    if not RUTA_JSON.exists():
        return []
    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_tareas(tareas):
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def generar_id(tareas):
    ids_usados = {tarea["id"] for tarea in tareas}

    while True:
        nuevo_id = random.randint(1, 99999)

        if nuevo_id not in ids_usados:
            return nuevo_id