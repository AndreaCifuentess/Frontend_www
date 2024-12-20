import reflex as rx
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
if not BACKEND_URL:
    raise ValueError("La variable de entorno BACKEND_URL no está definida.")

# Función para eliminar la tarea del servidor.
async def eliminar_tarea(task_id: int, on_confirm: callable):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f'{BACKEND_URL}/eliminar_tarea/{task_id}')
        if response.status_code == 200:
            print(f"Tarea {task_id} eliminada correctamente.")
            await on_confirm()  # Actualiza las tareas después de eliminar
        else:
            print(f"Error al eliminar la tarea: {response.text}")
    except Exception as e:
        print(f"Error al intentar eliminar la tarea: {e}")

# Función para mostrar el modal de confirmación de eliminación
def eliminar(task_id: int, on_confirm: callable):
    return rx.dialog.root(
        rx.dialog.trigger(rx.icon("archive-x", size=25, color="blue")),  
        rx.dialog.content(
            rx.dialog.title("Confirmar Eliminación", text_align="center"),
            rx.dialog.description(
                "¿Estás segura de que deseas eliminar esta tarea? Esta acción no se puede deshacer.",
                size="2", margin_bottom="16px", text_align="center"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                    ),
                ),
                rx.button(
                    "Eliminar",
                    color="red",
                    on_click=lambda: eliminar_tarea(task_id, on_confirm),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
    )
