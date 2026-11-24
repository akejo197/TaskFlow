from django.shortcuts import render, redirect
from .utilidades import cargar_tareas, guardar_tareas, generar_id


def home(request):
    return redirect('listar_tareas')


def listar_tareas(request):
    tareas = cargar_tareas()
    return render(request, "tareas/listar.html", {"tareas": tareas})


def agregar_tarea(request):
    if request.method == "POST":
        nombre_tarea = request.POST.get("nombre_tarea", "").strip()
        descripcion_tarea = request.POST.get("descripcion_tarea", "").strip()

        if nombre_tarea:
            tareas = cargar_tareas()
            tareas.append({
                "id": generar_id(tareas),
                "nombre_tarea": nombre_tarea,
                "descripcion_tarea": descripcion_tarea,
                "estado": False,
            })
            guardar_tareas(tareas)

        return redirect('listar_tareas')

    return render(request, "tareas/agregar.html")


def eliminar_tarea(request, id):
    if request.method == "POST":
        pass  # tu lógica aquí
    return redirect('listar_tareas')


def marcar_tarea(request, id):
    if request.method == "POST":
        pass  # tu lógica aquí
    return redirect('listar_tareas')


def estadisticas(request):
    return render(request, "tareas/estadisticas.html")