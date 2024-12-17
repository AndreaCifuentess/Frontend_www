import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                    rx.heading(
                        "Bienvenid@", 
                        font_size="8em", 
                        color="blue.600", 
                        font_weight="bold"
                    ),
                rx.spacer(height="7rem"),
                rx.center(
                    rx.link(
                        "Ir al Gestor de Tareas", 
                        font_size="2em", 
                        href='/gestor', 
                        color="teal.500", 
                        font_weight="bold", 
                        _hover={"color": "teal.700"}, 
                        padding="1rem", 
                        margin="1rem", 
                        text_align="center",
                    ),
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
            ),
            background="rgba(173, 216, 230, 0.2)",
            height="100vh",
            align_items="center",
            justify_content="center",
        ),
    )

app = rx.App()
app.add_page(index)
