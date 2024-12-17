import reflex as rx

def editar_tarea() -> rx.Component:
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
            "Editar Tarea",
            margin_top="20px",
            padding="10px 20px",
            margin="auto",
            display="block",
        ),
        spacing="16px",
        margin="20px",
        padding="20px",
        border="1px solid #ddd",
        border_radius="8px",
        background_color="#f9f9f9",
        box_shadow="0 4px 10px rgba(0, 0, 0, 0.1)",
    )
