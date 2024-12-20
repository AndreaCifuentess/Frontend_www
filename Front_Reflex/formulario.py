import reflex as rx
import httpx  
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

    @rx.event
    async def crear_tarea(self):
        data = {
            "titulo": self.titulo,
            "descripcion": self.descripcion
        }
        self.loader = True
        self.error = False
        self.submission_status = ""  
    
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(f'{BACKEND_URL}/tareas', json=data, headers={"Content-Type": "application/json"})
            if response.status_code == 200:
                # Si la tarea fue creada correctamente
                self.submission_status = "Tarea creada con éxito"
                self.titulo = "" 
                self.descripcion = ""  
                self.response = response.json()
            else:
                self.submission_status = f"Error: {response.text}"
                self.error = True
        except Exception as e:
            self.submission_status = f"Error: {str(e)}"
            self.error = True
        finally:
            self.loader = False

# Método para el formulario de tarea
def formulario_tarea() -> rx.Component:
        return rx.fragment(
            # Campo para el título
            rx.input(
                placeholder="Nombre de la tarea",
                id="nombre_tarea",
                margin_bottom="12px",
                width="100%",
                padding="8px",
                border="1px solid #ccc",
                border_radius="4px",
                box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",
                value=CrearTareaState.titulo,  
                on_change=CrearTareaState.set_titulo  
            ),
            # Campo para la descripción
            rx.input(
                placeholder="Descripción",
                id="descripcion_tarea",
                margin_bottom="12px",
                width="100%",
                padding="8px",
                border="1px solid #ccc",
                border_radius="4px",
                box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",
                value=CrearTareaState.descripcion, 
                on_change=CrearTareaState.set_descripcion 
            ),
            # Botón para guardar la tarea
            rx.button(
                "Guardar Tarea",
                margin_top="20px",
                padding="10px 20px",
                margin="auto",
                display="block",
                on_click= CrearTareaState.crear_tarea
            ),
            # Mostrar mensaje de éxito o error
            rx.cond(
                CrearTareaState.submission_status != "",  
                rx.text(CrearTareaState.submission_status,  
                        color="green", 
                        margin_top="10px"),
                rx.text("")  
            ),
            rx.cond(
                CrearTareaState.loader,  
                rx.text("Cargando...", color="blue", margin_top="10px"),
                rx.text("")  
            ),
            spacing="16px",
            margin="20px",
            padding="20px",
            border="1px solid #ddd",
            border_radius="8px",
            background_color="#f9f9f9",
            box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
        )