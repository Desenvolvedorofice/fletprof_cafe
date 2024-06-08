import flet as ft

def main(page: ft.Page):
    page.title = "Programa com Menu"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 1980
    page.window_height = 1080
    
    def show_menu(e=None):
        message_container.content = ft.Column(
            controls=[
                ft.Text("AMOXICILINA", size=35),
                ft.ElevatedButton("Calcular dose", on_click=btt1, width=200, height=50),
                ft.ElevatedButton("FOTO", on_click=btt2, width=200, height=50),
                ft.ElevatedButton("Sair", on_click=on_exit_click, width=200, height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        page.update()
    
        
    def btt1(e=None):
        def calculate(e=None):
            try:
                number = float(entry.value)
                result = number / 3
                result = round(result, 2)
                result_label.value = f"Tomar {result} ml de 8/8h por 7 dias"
            except ValueError:
                result_label.value = "Por favor, insira um número válido."
            page.update()

        message_container.content = ft.Column(
            controls=[
                ft.Text("Insira o peso:", size=24),
                entry := ft.TextField(width=150, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton("Calcular", on_click=calculate, width=200, height=50),
                ft.Container(result_label := ft.Text(""), bgcolor=ft.colors.BLACK12, margin=3, border_radius=10, padding=15),
                ft.ElevatedButton("Voltar", on_click=lambda e: show_menu(), width=200, height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        page.update()
        
            
    def btt2(e=None):
        message_container.content = ft.Column(
            controls=[
                # ft.Text("Você clicou no botão 2", size=24),
                ft.Image(src="C:/Users/Desen/OneDrive/Imagens/amox.jpeg", width=1280, height=720),
                ft.Text("Caixa da Amoxicilina", size=20),
                ft.ElevatedButton("Voltar", on_click=lambda e: show_menu(), width=200, height=50),
                ft.ElevatedButton("Próximo", on_click=btt3, width=200, height=50),
                ft.ElevatedButton("MENU", on_click=lambda e: show_menu(), width=200, height=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        page.update()


    def btt3(e=None):
        message_container.content = ft.Column(
            controls=[
                ft.Text("FIM", size=25),
                ft.ElevatedButton("Voltar", on_click=btt2, width=200, height=50),
                ft.ElevatedButton("MENU", on_click=show_menu, width=200, height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        page.update()    

    def on_exit_click(e=None):
        page.window_close()

    message_container = ft.Container()
    show_menu()

    page.add(message_container)

ft.app(target=main)
