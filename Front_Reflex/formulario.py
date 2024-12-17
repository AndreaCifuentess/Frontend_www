import reflex as rx
import requests as rq
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
if not BACKEND_URL:
    raise ValueError("La variable de entorno BACKEND_URL no está definida.")

class CrearTareaState(rx.State):
    submission_status: str = ""
    loader: bool = False
    error: bool = False
    titulo: str = ""
    descripcion: str = ""
    response: dict = {}

    @rx.event(background=True)
    async def crear_tarea(self, data: dict):
        async with self:
            self.loader = True
            self.error = False
            print(data)
            try:
                response = rq.post(f'{BACKEND_URL}/tarea', json=data, headers={"Content-Type": "application/json"})
                print("Status Code:", response.status_code)
                if response.status_code == 200:
                    self.submission_status = "Tarea creada con éxito"
                    print("Respuesta del servidor:", response.json())
                    self.response = response.json()
                    print("Respuesta:", self.response)
                else:
                    self.loader = False
                    self.error = True
                    print("Error en la solicitud:", response.text)
            except Exception as e:
                self.loader = False
                self.error = True
                print("Error en la solicitud:", e)
            self.loader = False


# Método para el formulario de tarea
def formulario_tarea() -> rx.Component:
    return rx.fragment(
        rx.input(
            placeholder="Nombre de la tarea",
            id="nombre_tarea",
            margin_bottom="12px",
            width="100%",
            padding="8px",
            border="1px solid #ccc",
            border_radius="4px",
            box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",
        ),
        rx.input(
            placeholder="Descripción",
            id="descripcion_tarea",
            margin_bottom="12px",
            width="100%",
            padding="8px",
            border="1px solid #ccc",
            border_radius="4px",
            box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",
        ),
        rx.button(
            "Guardar Tarea",
            margin_top="20px",
            padding="10px 20px",
            margin="auto",
            display="block",
            #on_submit=lambda: CrearTareaState.crear_tarea(self, data),
            #reset_on_submit=True
        ),
        spacing="16px",
        margin="20px",
        padding="20px",
        border="1px solid #ddd",
        border_radius="8px",
        background_color="#f9f9f9",
        box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
    )
