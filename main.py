import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Login do sistema")

titulo = ctk.CTkLabel(janela, text='Bem vindo à Car Monkey Studio', font=("roboto", 24, "bold"))
titulo.pack(pady=40)

email = ctk.CTkEntry(janela, placeholder_text="Seu e-mail", width=300, height=40)
email.pack(pady=10)

senha = ctk.CTkEntry(janela, placeholder_text="Sua senha",show="*", width=300, height=40)
senha.pack(pady=10)

def fazer_login():
    email_digitado = email.get()
    senha_digitada = senha.get()

    print(f"Tentativa de login com: {email_digitado}")

botao = ctk.CTkButton(janela, text="Entrar", command=fazer_login, width=300, height=40)
botao.pack(pady=20)

janela.mainloop()
