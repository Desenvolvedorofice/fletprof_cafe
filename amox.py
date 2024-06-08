import flet as ft
import matplotlib.pyplot as plt
import io
from base64 import b64encode
import random as rd

def main(page: ft.Page):
    page.title = "Programa com Menu"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 1980
    page.window_height = 1080
    page.padding = 10
    page.spacing = 20

    # Inicialize as variáveis globais
    global image_size, image_zoomed
    image_size = [200, 300]  # [largura, altura]
    image_zoomed = False  # Para controlar o estado do zoom

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
                ft.Text("Insira o peso em kg:", size=24),
                entry := ft.TextField(width=150, text_align=ft.TextAlign.CENTER),
                ft.Container(result_label := ft.Text(""), bgcolor=ft.colors.BLACK12, margin=3, border_radius=10, padding=15),
                ft.Container(
                    content=ft.ElevatedButton("Calcular", on_click=calculate, width=200, height=50),
                    padding=ft.padding.only(top=10)  # Ajuste o padding conforme necessário
                ),
                ft.ElevatedButton("Voltar", on_click=show_menu, width=200, height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,  # Adiciona espaçamento vertical entre os elementos
        )
        page.update()


    def btt2(e=None):
        image_controls = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ADD, on_click=zoom_in),
                        ft.Image(src="https://i.imgur.com/Q54Lf9y.jpg", width=image_size[0], height=image_size[1]),
                        ft.IconButton(icon=ft.icons.REMOVE, on_click=zoom_out),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text("Caixa da Amoxicilina", size=20),
                ft.ElevatedButton("Voltar", on_click=show_menu, width=200, height=50),
                ft.ElevatedButton("Próximo", on_click=btt3, width=200, height=50),
                ft.ElevatedButton("MENU", on_click=show_menu, width=200, height=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True  # Expande a coluna para ocupar todo o espaço disponível
        )
        message_container.content = image_controls
        page.update()

    def zoom_in(e):
        global image_size, image_zoomed
        if not image_zoomed:
            image_size[0] += 50
            image_size[1] += 50
            image_zoomed = True
            btt2()

    def zoom_out(e):
        global image_size, image_zoomed
        if image_zoomed:
            image_size[0] -= 50
            image_size[1] -= 50
            image_zoomed = False
            btt2()

    def btt3(e=None):
        chart_src = generate_bar_chart()
        message_container.content = ft.Column(
            controls=[
                ft.Text("Meia Vida", size=25),
                ft.Image(src=chart_src, width=600, height=400),
                ft.ElevatedButton("Voltar", on_click=btt2, width=200, height=50),
                ft.ElevatedButton("MENU", on_click=show_menu, width=200, height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
        page.update()
    def generate_bar_chart():
        # Dados do gráfico
        categories = ['A', 'B', 'C', 'D', 'E']
        values = [rd.randint(10, 90) for _ in range(5)]

        # Criar o gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_xlabel('Tipos')
        ax.set_ylabel('Tempo (h)')
        ax.set_title('Gráfico de meia vida')

        # Salvar o gráfico em um buffer de bytes
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)

        # Codificar a imagem em base64
        image_base64 = b64encode(buf.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{image_base64}"
    def on_exit_click(e=None):
        page.window_close()

    message_container = ft.Container(expand=True)
    show_menu()

    page.add(message_container)

ft.app(target=main, host="0.0.0.0", port=8551)

