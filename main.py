import tkinter as tk

janela = tk.Tk()

janela.title("Login - Sistema de Estoque")
janela.geometry("500x300")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="📦 Gestor+",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

tk.Label(janela, text="Usuário").pack()

entrada_usuario = tk.Entry(janela,width=30)
entrada_usuario.pack()

tk.Label(janela, text="Senha").pack()

entrada_senha = tk.Entry(janela,width=30, show="*")
entrada_senha.pack()

btn_login = tk.Button(
    janela,
    text="Entrar",
    bg="#0D6EFD",
    fg="white",
    activebackground="#0B5ED7",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bd=0,
    padx=20,
    pady=8,
    cursor="hand2"
)
btn_login.pack(pady=20)

janela.mainloop()
