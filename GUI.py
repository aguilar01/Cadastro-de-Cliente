from tkinter import *




class GUI:  #classe com interface gráfica
    x_pad = 5
    y_pad = 3  # distanciamento entre o conteúdo e a borda
    width_entry = 30  #largura da janela
    window = Tk()  #Criar uma janela
    window.wm_title("Cadastro")  # Nome da aplicação
    txtNome = StringVar()  # definição das variaveis que recebem os dados inseridos pelo user
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    #texto dos labels
    lblnome = Label(window, text="Nome")  # window define qual janela o label vai aparecer
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")

    #campo para ser inserido o cadastro
    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF, width=width_entry)

    #criando barra de rolagem com a variavel listclientes
    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)

    #texto dos botões
    btnViewALL = Button(window, text="Visualizar todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    #associando os labels e textos em grid column vertical, row horizontal uma linha por vez
    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)

    #adicionando botões
    btnViewALL.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    #união do scrollbar com a listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #adicionando SWAG aparencia da interface
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=y_pad, sticky='N')

    def run(self):
        GUI.window.mainloop()


app = GUI()
app.run()
