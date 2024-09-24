from PIL import Image
from main import Main
from customtkinter import *
import pages


def window():
    janela = CTk()
    janela.title('Consulta de Candidatos 2024')
    janela.geometry("500x700")

    set_appearance_mode('dark')
    image = Image.open('img/tse.png')
    img = CTkImage(light_image = image, dark_image = image, size = (150, 75))
    logo_label = CTkLabel(master = janela, image = img, text = '')
    logo_label.pack(pady = (20, 10))

    proc_candidatos = CTkLabel(master = janela, text='Procurar candidatos:', font=('Arial', 25), text_color='#00DB53')
    proc_candidatos.pack(pady = 15, padx = 20, anchor = 'center')
    cod_mun = CTkLabel(master = janela, text='Indique o código do município:', font=('Arial', 25), text_color='#00DB53')
    cod_mun.pack(pady = 5, padx = 20, anchor = 'w')
    #Adicionando os valores de forma automática
    
    main = Main()
    muns = main.pegando_mun()
    cargo = main.pegando_cargo()
    cod = main.pegando_cod()
    box_mun = CTkComboBox(master = janela, height = 30, border_color = '#00DB53', values = muns) 

    box_mun.pack(pady =5, padx = 20, anchor='w')
    cod_cargo = CTkLabel(master = janela, text='Indique o código do Cargo:', font=('Arial', 25), text_color='#00DB53')
    cod_cargo.pack(pady = 5, padx = 20, anchor = 'w')


    box_cargo = CTkComboBox(master = janela, height = 30, border_color = '#00DB53', values = cargo)
    box_cargo.pack(pady =5, padx = 20, anchor='w')

    def Candidatos():
        cargo = box_cargo.get()
        municipio = box_mun.get()
        janela.destroy()
        candidatos(municipio, cargo)

    def CandidatosCodigo():
        cod = codigo.get()
        janela.destroy()
        codCandidato(cod)

    botao = CTkButton(master = janela, text = 'Procurar Candidatos', corner_radius = 30, fg_color = 'transparent', border_color = '#00DB53', border_width = 2, hover_color = '#DB0A00', font = ('Arial', 20), height = 50, cursor = 'hand2', command = Candidatos)
    botao.pack(pady = 20, padx = 20, anchor = 'center')

    proc_codigos = CTkLabel(master = janela, text='Procurar por código:', font=('Arial', 25), text_color='#00DB53')
    proc_codigos.pack(pady = 10, padx = 20, anchor = 'center')
    codigo = CTkComboBox( master = janela, height = 30, border_color = '#00DB53', values = cod)
    codigo.pack(pady =5, padx = 20, anchor='w')

    botao_codigo = CTkButton(master = janela, text = 'Procurar por Código', corner_radius = 30, fg_color = 'transparent', border_color = '#00DB53', border_width = 2, hover_color = '#DB0A00', font = ('Arial', 20), height = 50, cursor = 'hand2', command = CandidatosCodigo)
    botao_codigo.pack(pady = 20, padx = 20, anchor = 'center')
    
    botao_html = CTkButton(master = janela, text = 'Ver Estatisticas', corner_radius = 30, fg_color = 'transparent', border_color = '#DB0A00', border_width = 2, hover_color = '#00DB53', font = ('Arial', 20), height = 50, width = 300, cursor = 'hand2')
    botao_html.pack(pady = 10, padx = 20, anchor = 'center')

    janela.mainloop()

    
    
#PEGANDO CANDIDATOS PELO MUNICIPIO E CARGO
def candidatos(municipio, cargo):
    main = Main()
    candidatos = main.municipios_cargos(municipio, cargo)
    pages.getdata(candidatos)
    
#PEGANDO CANDIDATOS PELO CÓDIGO
def codCandidato(codigos):
    main = Main()
    candidatos = main.cod_candidatos(codigos)
    pages.getdata(candidatos)


window()

# Printar os candidatos referentes aos cargos e municipios
# Dar a opção de procurar o candidato pelo código
# Botão para ver as estátisticas
