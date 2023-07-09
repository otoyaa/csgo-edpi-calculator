import flet as ft
from flet import Page
from flet import TextField
from flet import Column
from flet import Container

def main(page: Page):
    page.vertical_alignment = "center" # type: ignore
    page.horizontal_alignment = "center" # type: ignore
    page.window_width = 400
    page.window_height = 400
    page.window_frameless = True

    def edpi_calculator(mouse_dpi, in_game_sensibility):
        return float(mouse_dpi) * float(in_game_sensibility)
    
    def show_edpi_calculator_result(e):
        calculator_result = edpi_calculator(_dpi_text_label.value, _in_game_sensibility.value)
        _result.value = f"result: {calculator_result}"
        page.update(_result)
    
    _dpi_text_label = TextField(
        label="your dpi",
        icon=ft.icons.MOUSE,
        width=250,
        hint_text="ex: 400, 800 dpi",
        border="none", # type: ignore
    )
    
    _in_game_sensibility = TextField(
        label="csgo sensibility",
        icon=ft.icons.GAMEPAD_ROUNDED,
        width=250,
        hint_text="ex: 1.375, 2 sensibility",
        border="none", # type: ignore
    )    
    _calculator_buttom = ft.ElevatedButton(
        text="calculator",
        elevation=30,
        on_click=show_edpi_calculator_result
    )
    
    _result = ft.Text(
        value = "result:"
    )
    
    page.add(
        _dpi_text_label, 
        _in_game_sensibility,
        _calculator_buttom,
        _result)
    
if __name__ == "__main__":
    ft.app(main)
    
        