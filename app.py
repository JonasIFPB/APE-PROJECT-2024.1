from PIL import Image
from customtkinter import *

def window():
    janela = CTk()
    janela.geometry("400x500")

    set_appearance_mode('dark')
    image = Image.open('img/tse.png')
    img = CTkImage(light_image = image, dark_image = image, size = (150, 75))
    logo_label = CTkLabel(master = janela, image = img, text = '')
    logo_label.pack(pady = (20, 10))

    cod_mun = CTkLabel(master = janela, text='Indique o código do município:', font=('Arial', 25), text_color='#00DB53')
    cod_mun.pack(pady = 20, padx = 20, anchor = 'w')

    box_mun = CTkComboBox(master = janela, fg_color = '#DB0A00', border_color = '#00DB53', values = ['22055', '20672', '20273', '21415', '19879', '20036', '20575', '19585', '20958', '22110', '20397', '21938',
    '19895', '20516', '19003', '20850', '19810', '21270', '19798', '21512', '19739', '19364', '19062', '21911',
    '19224', '19682', '21555', '20052', '19860', '22012', '19615', '20494', '19933', '21750', '21393', '19658',
    '20478', '19828', '20419', '21652', '19216', '19518', '20877', '19259', '19437', '22314', '22071', '19526',
    '22276', '19070', '21458', '20834', '21539', '21334', '19089', '19194', '21210', '20311', '19054', '19666',
    '19160', '21172', '19950', '21474', '19712', '20532', '19984', '22250', '22217', '20214', '20230', '20133',
    '21032', '19020', '19623', '22390', '19330', '19755', '19771', '22136', '21970', '19704', '22233', '20699',
    '19453', '19917', '19542', '20079', '20630', '21830', '19801', '19372', '21377', '21156', '21792', '19178',
    '19232', '22179', '19976', '20354', '19356', '21490', '20710', '21296', '19577', '19283', '22438', '22357',
    '19488', '22098', '19305', '20290', '20613', '20818', '19291', '20117', '20451', '22195', '22330', '19844',
    '21598', '19674', '19313', '20257', '20796', '22039', '21636', '20591', '19470', '22292', '19119', '21059',
    '19135', '19046', '20990', '19968', '19720', '20656', '19763', '20915', '20893', '19151', '20559', '21318',
    '21253', '20338', '21091', '20370', '19631', '21130', '20095', '19550', '19097', '20150', '19038', '19267',
    '19240', '19402', '21350', '21016', '21997', '20435', '22373', '19747', '21954', '19607', '20010', '21717',
    '19690', '21113', '20001', '22411', '21873', '19534', '21890', '21814', '19992', '19925', '19887', '19500',
    '19410', '19429', '21199', '21571', '19321', '20737', '19143', '19780', '19348', '19127', '21237', '19593',
    '21610', '19461', '19640', '19941', '21075', '19909', '19011', '19399', '19186', '19496', '19380', '21431',
    '21679', '20974', '19275', '19208', '19852', '21733', '19100', '19569', '22152', '20753', '19836', '21776',
    '20770', '21857', '21695', '20931', '19445', '20176', '20192']) 
    box_mun.pack(pady =5, padx = 20, anchor='w')

    janela.mainloop()


window()