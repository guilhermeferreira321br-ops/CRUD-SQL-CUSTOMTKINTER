from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from repository import (inserir_dados, excluir_dados,
buscar_usuario_por_id, ler_todos_usuarios, atualizar_os_dados)



# 1°- FUNÇÃO CADASTRO DE USUÁRIOS
def cadastrar_usuarios():
    nome_user = entry_nome.get().strip()
    email_user = entry_email.get().lower().strip()
    telefone_user = entry_telefone.get().strip()

    if not nome_user and not email_user and not telefone_user:
        CTkMessagebox(title="Informação", message="Preencha todos os campos vazios!")
        return

    if not nome_user:
        CTkMessagebox(title="Informação", message="O preenchimento do campo 'Nome' é obrigatório.")
        return

    if not email_user:
        CTkMessagebox(title="Informação", message="Por favor, informe o seu e-mail.")
        return

    if "@" not in email_user or "." not in email_user:
        CTkMessagebox(title="Informação", message="Formato do e-mail inválido. Certifique-se de incluir '@' e '.'")
        return

    if not telefone_user:
        CTkMessagebox(title="Informação", message="Por favor, insira um telefone válido.")
        return

    resultado1 = inserir_dados(nome_user, email_user, telefone_user)

    if resultado1:
        CTkMessagebox(title="Sucesso", message="Tudo pronto! Seu cadastro foi finalizado com sucesso.", icon="check", option_1="Ok")
        ler_dados()

        entry_nome.delete(0, "end")
        entry_email.delete(0, "end")
        entry_telefone.delete(0, "end")
    else:
        CTkMessagebox(title="Informação", message="Este endereço de e-mail já está em uso.")




# 2°- FUNÇÃO BUSCAR USUARIO POR ID
def buscar_id_usuario():
    pegar_id = entry_buscar.get().strip()

    if not pegar_id:
        CTkMessagebox(title="Informação", message="Por favor, informe o ID do usuário que deseja consultar.")
        return
    resultado2 = buscar_usuario_por_id(pegar_id)


    if resultado2 is None:
        CTkMessagebox(title="Informação", message="Nenhum usuário foi encontrado com o ID informado.")
        return
    elif resultado2 is False:
        CTkMessagebox(title="Erro", message="Ocorreu uma falha inesperada no banco de dados.", icon="cancel")
        return
    else:
        textbox_resultados.delete("1.0", "end")

        texto = f"""
        ================================================

        ID: {resultado2[0]}

        NOME: {resultado2[1]}

        EMAIL: {resultado2[2]}

        TELEFONE: {resultado2[3]}

        ================================================
        """

        textbox_resultados.insert("end", texto)

        entry_buscar.delete(0, "end")






# 3°- FUNÇÃO LER OS DADOS DO BANCO DE DADOS
def ler_dados():
    resultado3 = ler_todos_usuarios()

    if resultado3 is False:
        CTkMessagebox(title="Erro", message="Ocorreu uma falha inesperada no banco de dados.", icon="cancel")
    elif not resultado3:
        textbox_resultados.delete("1.0", "end")


    else:
        textbox_resultados.delete("1.0", "end")

        cabecalho = (
            "ID | NOME | EMAIL | TELEFONE\n"
            "-------------------------------------------------------------\n\n"
        )
        textbox_resultados.insert("end", cabecalho)

        for usuario in resultado3:
            linha = (
                f"{usuario[0]} | "
                f"{usuario[1]} | "
                f"{usuario[2]} | "
                f"{usuario[3]}\n\n"
            )

            textbox_resultados.insert("end", linha)



# 4°- FUNÇÃO ATUALZIAR DADOS
def atualizar_dados():
    informar_id = entry_id.get().strip()
    nome_usuario = entry_usuario.get().strip()
    email_usuario = entry_email_atualizar.get().strip()
    telefone_usuario = entry_telefone_atualizar.get().strip()

    if not informar_id:
        CTkMessagebox(title="Informação", message="Por favor, informe o ID do usuário que deseja atualizar.")
        return

    if not nome_usuario:
        CTkMessagebox(title="Informação", message="Insira o nome do cliente para atualização.")
        return

    if not email_usuario:
        CTkMessagebox(title="Informação", message="Solicitamos que informe o endereço de e-mail do usuário.")
        return

    if "@" not in email_usuario or "." not in email_usuario:
        CTkMessagebox(title="Informação", message="E-mail inválido. Certifique-se de incluir '@' e '.' no endereço.")
        return

    if not telefone_usuario:
        CTkMessagebox(title="Informação", message="Por favor, informe o número de telefone do usuário com DDD")
        return


    resultado4 = atualizar_os_dados(informar_id, nome_usuario, email_usuario, telefone_usuario)
    if resultado4:
        CTkMessagebox(title="Sucesso", message="Os dados do usuário foram atualizados com sucesso.", icon="check", option_1="Ok")
        ler_dados()


        entry_id.delete(0, "end")
        entry_usuario.delete(0, "end")
        entry_email_atualizar.delete(0, "end")
        entry_telefone_atualizar.delete(0, "end")
    else:
        CTkMessagebox(title="Informação", message="O e-mail informado já está em uso por outro cadastro.")



# 5°- FUNÇÃO EXCLUIR DADOS
def excluir_os_dados():
    excluir_pelo_id = entry_buscar.get().strip()

    if not excluir_pelo_id:
        CTkMessagebox(title="Informação", message="Por favor, informe o ID do usuário que deseja remover.")
        return
    resultado5 = excluir_dados(excluir_pelo_id)

    if resultado5 is False:
        CTkMessagebox(title="Erro", message="Ocorreu uma falha inesperada no banco de dados.", icon="cancel", option_1="Ok")
        return


    if resultado5 is None:
        CTkMessagebox(title="Informação", message="Usuário não localizado.")
        return


    if resultado5 is True:
        CTkMessagebox(title="Sucesso", message="Usuário removido da base de dados com sucesso.", icon="check", option_1="Ok")
        ler_dados()

        entry_buscar.delete(0, "end")







# ======================================================== # =============================================================



janela = ctk.CTk()
janela.geometry("1200x850")
janela.title("System Engineer")
janela.configure(fg_color="#0B1120")
ctk.set_appearance_mode("dark")



# =========================
# MENU LATERAL
# =========================

frame_menu = ctk.CTkFrame(
    janela,
    width=250,
    corner_radius=25,
    fg_color="#09111F",
    border_width=3,
    border_color="#1E293B"
)
frame_menu.pack(side="left", fill="y", padx=10, pady=10)

titulo_logo = ctk.CTkLabel(
    frame_menu,
    text=" ⚙️\nSYSTEM\nENGINEER",
    font=("Segoe UI", 30, "bold"),
    text_color="#38BDF8"
)
titulo_logo.pack(pady=(40, 20))

subtitulo = ctk.CTkLabel(
    frame_menu,
    text="Gerenciamento de Usuários\n• CRUD em Python",
    font=("Segoe UI", 14, "bold"),
    text_color="#dcdcdc"
)
subtitulo.pack(pady=20)

btn_menu_cadastro = ctk.CTkButton(
    frame_menu,
    text="Cadastro",
    fg_color="#2563EB",
    hover_color="#1E293B",
    text_color="#F8FAFC",
    height=35
)
btn_menu_cadastro.pack(fill="x", padx=15, pady=10)

btn_menu_busca = ctk.CTkButton(
    frame_menu,
    text="Buscar / Excluir",
    fg_color="#2563EB",
    hover_color="#1E293B",
    text_color="#E2E8F0",
    border_width=1,
    border_color="#27364F",
    height=35

)
btn_menu_busca.pack(fill="x", padx=15, pady=10)

btn_menu_atualizar = ctk.CTkButton(
    frame_menu,
    text="Atualizar",
    fg_color="#2563EB",
    hover_color="#1E293B",
    text_color="#E2E8F0",
    border_width=1,
    border_color="#27364F",
    height=35
)
btn_menu_atualizar.pack(fill="x", padx=15, pady=10)


# =========================
# ÁREA PRINCIPAL
# =========================

frame_principal = ctk.CTkFrame(janela, fg_color="transparent")
frame_principal.pack(side="right", fill="both", expand=True, padx=10, pady=10)


# =========================
# CADASTRO
# =========================

frame_cadastro = ctk.CTkFrame(
    frame_principal,
    corner_radius=15,
    fg_color="#101A2E",
    border_color="#1E293B",
    border_width=3
)
frame_cadastro.pack(fill="x", pady=10)

ctk.CTkLabel(
    frame_cadastro,
    text="👤 Cadastro de Usuário",
    font=("Arial", 24, "bold"),
    text_color="#F1F5F9"
).pack(anchor="w", padx=20, pady=15)

entry_nome = ctk.CTkEntry(
    frame_cadastro,
    width=250,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Digite o nome..."
)
entry_nome.pack(side="left", padx=15, pady=15)

entry_email = ctk.CTkEntry(
    frame_cadastro,
    width=250,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Digite o e-mail..."
)
entry_email.pack(side="left", padx=15, pady=15)

entry_telefone = ctk.CTkEntry(
    frame_cadastro,
    width=250,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Digite o telefone..."
)
entry_telefone.pack(side="left", padx=15, pady=15)

btn_cadastrar = ctk.CTkButton(
    frame_cadastro,
    text="Cadastrar",
    fg_color="#2563EB",
    hover_color="#1E293B",
    text_color="#ffffff",
    command=cadastrar_usuarios,
    height=35,
    font=("Segoe UI", 14)
)
btn_cadastrar.pack(side="left", padx=15)


# =========================
# BUSCAR / EXCLUIR
# =========================

frame_busca = ctk.CTkFrame(
    frame_principal,
    corner_radius=15,
    fg_color="#101A2E",
    border_color="#1E293B",
    border_width=2
)
frame_busca.pack(fill="x", pady=10)

ctk.CTkLabel(
    frame_busca,
    text=" 🔍 Buscar / 🗑 Excluir Usuário",
    font=("Arial", 22, "bold"),
    text_color="#F1F5F9"
).pack(anchor="w", padx=20, pady=15)

entry_buscar = ctk.CTkEntry(
    frame_busca,
    width=350,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Digite o ID..."
)
entry_buscar.pack(side="left", padx=20, pady=15)

btn_buscar = ctk.CTkButton(
    frame_busca,
    text="Buscar",
    fg_color="#0284C7",
    hover_color="#668b8b",
    text_color="#ffffff",
    command=buscar_id_usuario,
    height=35,
    font=("Segoe UI", 14)
)
btn_buscar.pack(side="left", padx=10)

btn_excluir = ctk.CTkButton(
    frame_busca,
    text="Excluir",
    fg_color="#DC2626",
    hover_color="#cd6889",
    text_color="#ffffff",
    command=excluir_os_dados,
    height=35,
    font=("Segoe UI", 13)
)
btn_excluir.pack(side="left", padx=10)


# =========================
# ATUALIZAR
# =========================

frame_atualizar = ctk.CTkFrame(
    frame_principal,
    corner_radius=15,
    fg_color="#101A2E",
    border_color="#1E293B",
    border_width=2
)
frame_atualizar.pack(fill="x", pady=10)

ctk.CTkLabel(
    frame_atualizar,
    text=" 🔄 Atualizar Usuário",
    font=("Arial", 22, "bold"),
    text_color="#F1F5F9"
).pack(anchor="w", padx=20, pady=15)

entry_id = ctk.CTkEntry(
    frame_atualizar,
    width=70,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="ID"
)
entry_id.pack(side="left", padx=10, pady=15)

entry_usuario = ctk.CTkEntry(
    frame_atualizar,
    width=260,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Nome"
)
entry_usuario.pack(side="left", padx=10)

entry_email_atualizar = ctk.CTkEntry(
    frame_atualizar,
    width=280,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Email"
)
entry_email_atualizar.pack(side="left", padx=10)

entry_telefone_atualizar = ctk.CTkEntry(
    frame_atualizar,
    width=210,
    fg_color="#0B1324",
    border_color="#293A56",
    text_color="#F8FAFC",
    placeholder_text_color="#64748B",
    placeholder_text="Telefone"
)
entry_telefone_atualizar.pack(side="left", padx=10)

btn_atualizar = ctk.CTkButton(
    frame_atualizar,
    text="Atualizar",
    fg_color="#006400",
    hover_color="#15803D",
    text_color="#ffffff",
    command=atualizar_dados,
    height=35,
    font=("Segoe UI", 14)
)
btn_atualizar.pack(side="left", padx=15)


# =========================
# RESULTADOS
# =========================

frame_resultados = ctk.CTkFrame(
    frame_principal,
    corner_radius=15,
    fg_color="#101A2E",
    border_color="#1E293B",
    border_width=2
)
frame_resultados.pack(fill="both", expand=True, pady=10)

ctk.CTkLabel(
    frame_resultados,
    text="Resultados",
    font=("Arial", 22, "bold"),
    text_color="#F1F5F9"
).pack(anchor="w", padx=20, pady=15)

textbox_resultados = ctk.CTkTextbox(
    frame_resultados,
    height=220,
    fg_color="#080E1A",
    border_color="#22324B",
    border_width=1,
    text_color="#E2E8F0"
)
textbox_resultados.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)







credito = ctk.CTkLabel(
    frame_menu,
    text="</>   Criado por\n       Guilherme Ferreira",
    font=("Arial", 13),
    text_color="#ffffff",
    justify="left"
)

credito.pack(side="bottom", pady=25)



janela.mainloop()