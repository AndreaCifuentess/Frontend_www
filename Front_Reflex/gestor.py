import reflex as rx
from .formulario import formulario_tarea
from .editar import editar_tarea
from typing import List

# Definir el modelo de datos
class Task(rx.Base):
    titulo: str
    description: str
    completado: str
    fecha_creacion: str

# Definir el estado
class State(rx.State):
    tasks: List[Task] = [
        Task(titulo="Danilo Sousa", description="danilo@example.com", fecha_creacion="2024-12-06", completado="Sí"),
        Task(titulo="Zahra Ambessa", description="zahra@example.com", fecha_creacion="2024-12-07", completado="No"),
    ]
    

# Función para mostrar cada tarea
def show_task(task: Task, index: int):
    return rx.table.row(
        rx.table.cell(task.titulo),
        rx.table.cell(task.description),
        rx.table.cell(task.fecha_creacion),
        rx.table.cell(task.completado),
        rx.table.cell(
           rx.dialog.root(
             rx.dialog.trigger(rx.icon("pencil", size=25, color="blue")),
                rx.dialog.content(
                    rx.dialog.title("Edita la Tarea", text_align="center"),
                    rx.dialog.description(
                        "Edita los detalles de la tarea.",
                        size="2", margin_bottom="16px", text_align="center"
                    ),
                    editar_tarea(),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                            ),
                        ),
                        spacing="3",
                        margin_top="16px",
                        justify="end",
                ),
            ),
         ),
       ),
         rx.table.cell(
            rx.icon("archive-x", size=25, color="blue")
        ),             
    )


# Página para gestionar las tareas
@rx.page(route='/gestor', title='Gestor Tareas')
def tareas() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Gestor de Tareas",
                text_align="center",
                font_size="3em",
                font_weight="bold",
                margin_top="15px"
            ),
            # Modal para agregar tareas
            rx.dialog.root(
                rx.dialog.trigger(rx.button("Agregar Tarea", size="4")),
                rx.dialog.content(
                    rx.dialog.title("Agregar Tarea", text_align="center"),
                    rx.dialog.description(
                        "Agrega los detalles de la nueva tarea.",
                        size="2", margin_bottom="16px", text_align="center"
                    ),
                    formulario_tarea(),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                            ),
                        ),
                        spacing="3",
                        margin_top="16px",
                        justify="end",
                    ),
                ),
            ),
            # Tabla de tareas
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Titulo"),
                        rx.table.column_header_cell("Descripción"),
                        rx.table.column_header_cell("Fecha agregado"),
                        rx.table.column_header_cell("Estado"),
                        rx.table.column_header_cell("Editar"),
                        rx.table.column_header_cell("Borrar"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(
                        State.tasks,
                        lambda task, index: show_task(task, index)
                    )
                ),
                variant="surface",
                size="3",
                border_radius="10px",
                box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
                width="100%",
            ),
            height="100vh",
            align_items="center",
            width="80%",
            spacing="6"
        ),
        display="flex",
        align_items="center",
        justify_content="center",
        height="100vh",
        background="rgba(173, 220, 230, 0.2)",
    )
