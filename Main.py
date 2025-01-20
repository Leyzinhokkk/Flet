import flet as ft

def main(page: ft.Page):

    def enviar_formulario(e):

        nome = nome_input.value
        email = email_input.value
        mensagem = mensagem_input.value

        if not nome or not email or not mensagem:
            resultado_texto.value = "Por favor, preencha todos os campos!"
            resultado_texto.color = "red"
        else:
            resultado_texto.value = "Formulário enviado com sucesso!"
            resultado_texto.color = "green"
        
        # Atualizando a interface
        page.update()

    nome_input = ft.TextField(label="Nome", width=400)
    email_input = ft.TextField(label="Email", width=400)
    mensagem_input = ft.TextField(label="Mensagem", multiline=True, width=400, height=100)

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_formulario)

    resultado_texto = ft.Text("")

       page.add(
        ft.Column(
            [
                ft.Text("Formulário de Contato", size=24, weight="bold"),
                nome_input,
                email_input,
                mensagem_input,
                botao_enviar,
                resultado_texto,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

ft.app(target=main)
