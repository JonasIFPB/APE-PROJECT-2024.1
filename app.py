from PIL import Image
import pages
from main import Main
from customtkinter import *


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

    box_mun = CTkComboBox(master = janela, height = 30, border_color = '#00DB53', values = ['22055', '20672', '20273', '21415', '19879', '20036', '20575', '19585', '20958', '22110', '20397', '21938',
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

    cod_cargo = CTkLabel(master = janela, text='Indique o código do Cargo:', font=('Arial', 25), text_color='#00DB53')
    cod_cargo.pack(pady = 5, padx = 20, anchor = 'w')
    box_cargo = CTkComboBox(master = janela, height = 30, border_color = '#00DB53', values = ['13', '12', '11'])
    box_cargo.pack(pady =5, padx = 20, anchor='w')

    def janelaCandidatos():
        cargo = box_cargo.get()
        municipio = box_mun.get()
        janela.destroy()
        window2(municipio, cargo)


    botao = CTkButton(master = janela, text = 'Procurar Candidatos', corner_radius = 30, fg_color = 'transparent', border_color = '#00DB53', border_width = 2, hover_color = '#DB0A00', font = ('Arial', 20), height = 50, cursor = 'hand2', command = janelaCandidatos)
    botao.pack(pady = 20, padx = 20, anchor = 'center')

    proc_codigos = CTkLabel(master = janela, text='Procurar por código:', font=('Arial', 25), text_color='#00DB53')
    proc_codigos.pack(pady = 10, padx = 20, anchor = 'center')
    codigo = CTkComboBox( master = janela, height = 30, border_color = '#00DB53', values = ['44660', '18369', '22345', '10', '10444', '15000', '11777', '22999', '10500', '13131', '45777', '15610', '77234', '15551', '40555', '11333', '43222', '11000', '44555', '40', '13666', '40155', '45080', '40456', '15111', '15', '44333', '77666', '55345', '11111', '10111', '15234', '40100', '13777', '55111', '12', '40123', '33145', '10200', '27', '40111', '50000', '22333', '55444', '77555', '55321', '15200', '11999', '25800', '45222', '22', '20200', '44123', '40000', '77777', '10222', '20333', '13123', '12434', '45444', '20789', '55666', '77000', '15222', '22222', '13190', '11345', '55333', '15444', '44444', '40444', '50500', '13222', '15123', '36555', '22144', '10888', '40888', '20444', '55000', '13456', '10555', '15615', '11', '25888', '40027', '12444', '15789', '10100', '10333', '12112', '44222', '15455', '44777', '13', '11123', '44666', '15113', '77888', '40999', '20222', '11456', '12555', '20111', '20666', '70112', '11888', '13013', '10136', '45555', '20234', '44567', '15456', '77023', '10234', '12012', '70555', '70000', '55233', '15555', '36007', '45345', '12222', '10580', '77222', '22580', '65000', '45333', '55777', '77117', '40789', '12234', '55789', '13444', '13007', '45013', '10220', '33999', '22555', '77244', '11125', '20456', '65456', '12345', '10999', '22000', '44111', '55555', '50555', '55133', '10110', '40777', '45', '10000', '15666', '11113', '44999', '44100', '22122', '40666', '40222', '40333', '10777', '20000', '11222', '12369', '13200', '10151', '40007', '11444', '20123', '45245', '43123', '65', '45456', '12666', '65777', '18123', '77456', '55678', '13000', '15132', '20', '10603', '27333', '45678', '11555', '12111', '45369', '77123', '15154', '10456', '55640', '10123', '15678', '40455', '27788', '13313', '45200', '22456', '10345', '55765', '20700', '12123', '45666', '30100', '10981', '11114', '45500', '15015', '55222', '33111', '44000', '10321', '15380', '10112', '29', '15151', '27700', '70171', '15777', '70777', '12126', '20567', '15999', '12000', '18000', '29000', '44888', '65123', '45000', '70123', '11234', '45123', '15321', '11160', '77111', '22111', '55500', '10600', '33789', '44789', '10023', '15611', '25777', '12999', '44', '10666', '44044', '20601', '11666', '18333', '15333', '22666', '20368', '77775', '27777', '36666', '18789', '18019', '44007', '33330', '77677', '10005', '10101', '18888', '45111', '30444', '50001', '45645', '70456', '22444', '70700', '15004', '13888', '13111', '22214', '40234', '77890', '45178', '22123', '13789', '36', '10432', '43555', '15258', '20888', '18999', '40001', '55', '40607', '15115', '10322', '40511', '15612', '43777', '33444', '23456', '45045', '33010', '20555', '15888', '70007', '30999', '80000', '22522', '36444', '45145', '50321', '30657', '10223', '44678', '11022', '10192', '55155', '25111', '18456', '13333', '16420', '13555', '55114', '33000', '10611', '40400', '13244', '11789', '33669', '15313', '33109', '36333', '22888', '33456', '15119', '40122', '18018', '22190', '43000', '22051', '55147', '40125', '15244', '12777', '40140', '12333', '18', '77100', '40640', '44601', '25080', '11121', '25123', '50456', '20147', '11369', '33555', '18777', '40244', '55455', '20020', '33345', '33159', '55888', '11213', '70004', '15981', '55456', '20443', '65111', '10630', '15040', '77333', '40004', '27123', '10010', '70222', '15500', '29120', '12254', '18111', '55123', '36111', '22400', '15020', '30302', '43456', '33190', '43146', '77999', '70229', '55110', '40190', '55100', '10789', '40051', '13567', '29111', '55024', '15800', '22010', '33007', '29999', '27444', '55276', '70111', '70500', '70', '55234', '30123', '40151', '40258', '22234', '30111', '22211', '55999', '44332', '11236', '13001', '13551', '40112', '22611', '40200', '50777', '70133', '40900', '55101', '25', '70888','55013', '11122', '45999', '40252', '15144', '30003', '20202', '30300', '43333', '25333', '65050', '44357', '15112', '15190', '55122', '22277', '33123', '77321', '20454', '77', '12888', '25999', '18222', '20777', '15768', '20345', '44773', '10134', '22789', '55389', '33578', '33888', '77789', '15369', '20001', '22110', '10231', '70234', '70100', '11370', '27457', '18115', '44400', '20022', '12456', '27127', '15106', '40800', '70444', '50250', '11112', '45789', '11811', '13999', '12136', '77444', '40633', '11340', '10400', '45888', '30', '44112', '44620', '30456', '22204', '50123', '10171', '44113', '80', '50444', '10145', '77713', '22777', '70789', '15460', '10156', '15070', '11211', '15300', '18666', '33234', '10141', '65321', '10244', '40147', '10916', '44441', '11190', '50', '18555', '70614', '22193', '30555', '11224', '70300', '44234', '20999', '44910', '20115', '44440', '70345', '50050', '13226', '22022', '15601', '25000', '36765', '65555', '70193', '15345', '40620', '22101', '13611', '44066', '12678', '20122', '40852', '20321', '45917', '30789', '30241', '40567', '10133', '40002', '44244', '65432', '18444', '65789', '13676', '13713', '50180', '30330', '13321', '18140', '45122', '70999', '55157', '10654', '13100', '70670', '77324', '25666', '65255', '40192', '44456', '55677', '65666', '70333', '10190', '43001', '15402', '22678', '12155', '20101', '44744', '20337', '27192', '44147', '11100', '27999', '11400', '40544', '33777', '18370', '10344', '36600', '30800', '13120', '65333', '27111', '33571', '55699', '33301', '50222', '44104', '10001', '20220', '40069', '13741', '13233', '40006', '13570', '11012', '44345', '36010', '18020', '33858', '12156', '22221', '36777', '55055', '13300', '44040', '43111', '30777', '10300', '12120', '13650', '10567', '11722', '45677', '22114', '40345', '10610', '18882', '45690', '15602', '11357', '70369', '44144', '45450', '44676', '77500', '11117', '55602', '10434', '13031', '11007', '80180', '30333', '12789', '15121', '36800', '36147', '15650', '11321', '13500', '36999', '30293', '10122', '40321', '44321', '15845', '25222', '20504', '44545', '40040', '11233', '12011', '13113', '33333', '77247', '40166', '12203', '10615', '22369', '10017', '15133', '40610', '15233', '15614', '45132', '36100', '10606', '44600', '29567', '10007', '70144', '20800', '11105', '10115', '25678', '10675', '27000', '55558', '40224', '20110', '22770', '10852', '15630', '15621', '12611', '40337', '45372', '55007', '55127', '70011', '50133', '80123', '29333', '45133', '22610', '22112', '30000', '45466', '15102', '77443', '15156', '12121', '15100', '12321', '18700', '77889', '20678', '15192', '20259', '10113', '40369', '70457', '10258', '70666', '20400', '12225', '44483', '15153', '70015', '45879', '13513', '45008', '15344', '55616', '36022', '33222', '43131', '13400', '45115', '77567', '12388', '10240', '11601', '27133', '45510', '15215', '55190', '44544', '10565', '44258', '13457', '70676', '10147', '44466', '22001', '77689', '11544', '45321', '13024', '77199', '22500', '11011', '40678', '22801', '11611', '10221', '50150', '10369', '40133', '70772', '12567', '40278', '44351', '13258', '12002', '11229', '36888', '77161', '25090', '13221', '44623', '25444', '10612', '20025', '40404', '55770', '50333', '70678', '15050', '15433', '27007', '65100', '33258', '15670', '44500', '10270', '11008', '18100', '10492', '50024', '20100', '13234', '23333', '45610', '40013', '44223', '77007', '11438', '77755', '70654', '77277', '12010', '65222', '77700', '13133', '20230', '12134', '33192', '27555', '77345', '15605', '30222', '15544', '70221', '70567', '44190', '45234', '45605', '45007', '55235', '18190', '12300', '22422', '36345', '11258', '36000', '10229', '12662', '10210', '40015', '11311', '13021', '77800', '20528', '12612', '40118', '25625', '22133', '70010', '20180', '12127', '20500', '20369', '36108', '44228', '22220', '18125', '10678', '10167', '10022', '40110', '11223', '13012', '22981', '15607', '29444', '77766', '13900', '30321', '77124', '15044', '55121', '13678', '55800', '65888', '13130', '77224', '18345', '77900', '30001', '13455', '27234', '33331', '11119', '43133', '18024', '27222', '27321', '77190', '20127', '36190', '30134', '77200', '36122', '27888', '11255', '30022', '44122', '13229', '13011', '15186', '15622', '20580', '43557', '70105', '20193', '11110', '18110', '11634', '80100', '22223', '15523', '44800', '36789', '15218', '27027', '10211', '13245', '65444', '18500', '30230', '15232', '13737', '77011', '12278', '40232', '13369', '11124', '45224', '22134', '44110', '40600', '36700', '70070', '44001', '12100', '11800', '27456', '11610', '43444', '15600', '30225', '10423', '55200', '20002', '20340', '45600', '10313', '13213', '27400', '70077', '22200', '50059', '12232', '11212', '40120', '40611', '33666', '13155', '10987', '11193', '77134', '11155', '25555', '10103', '40677', '15620', '55002', '50234', '11567', '11115', '13290', '15150', '20144', '22044', '20007', '10182', '15350', '77753', '55645', '36006', '29456', '50255', '27775', '44369', '22567', '44200', '77040', '22230', '44238', '11364', '44604', '10116', '18186', '18736', '44644', '40121', '45229', '18188', '20440', '10125', '20112', '70400', '25025', '15155', '12013', '44771', '40615', '77010', '70321', '50208', '11566', '45421', '15152', '15193', '13023', '18677', '33366', '55690', '45620', '12180', '10800', '12223', '45100', '20987', '65678', '44233', '13122', '12788', '20012', '22002', '11600', '33100', '29777', '22007', '20233', '30303', '15001', '55300', '15116', '15251', '22322', '15246', '15025', '65133', '40217', '77229', '15579', '45015', '33102', '15212', '13', '110', '33567', '70110', '18234', '12122', '55987', '18013', '12543', '36222', '27500', '29123', '25015', '44756', '13279', '15124', '40199', '36258', '77077', '44092', '27900', '43789', '10013', '44256', '20612', '15688', '45889', '15606', '44569', '11202', '45107', '40688', '12007', '36192', '12190', '44602', '18400', '40022', '10700', '45699', '45244', '45147', '55315', '10380', '13154', '29888', '15160', '30122', '55432', '44566', '70230', '12604', '13613', '10236', '11911', '77299', '55935', '11231', '27100', '20670', '16000', '55434', '29061', '44442', '45602', '36456', '27577', '36369', '22225', '45223', '36050', '33400', '50888', '70200', '33223', '30015', '55670', '20157', '55700', '11010', '55511', '45012', '13124', '11001', '15051', '22800', '15147', '15400', '70770', '77227', '40612', '40177', '36012', '55501', '30774', '40010', '15022', '36003', '29359', '50013', '55112', '15223', '27277', '11118', '50229', '15398', '44477', '22502', '22100', '29300', '15159', '15221', '15289', '11300', '40130', '13700', '36024', '33622', '55244', '11678', '33300', '12797', '20021', '36233', '27789', '11200', '15225', '40240', '45144', '18766', '11815', '10377', '30010', '44611', '33033', '18180', '10566', '15174', '55001', '40700', '50134', '50100', '70787', '22147', '44900', '40275', '77133', '13857', '27190', '10033', '43043', '11127', '10225', '50111', '12580', '27171', '12511', '20244', '22419', '10622', '18136', '10107', '77343', '40780', '30005', '40114', '40065', '65569', '40141', '15963', '36567', '70001', '70190', '44634', '80800', '55454', '55600', '20190', '40115', '12455', '10121', '22715', '11580', '11050', '12327', '45237', '10178', '15281', '11033', '44220', '40603', '11322', '12146', '18200', '22321', '40497', '22177', '30310', '36321', '77715', '33011', '27447', '15510', '12370', '20155', '30730', '36790', '33700', '29321', '11655', '11785', '55012', '20969', '30083', '13140', '33678', '20013', '10623', '13223', '10899', '70008', '15645', '20606', '77145', '77523', '77221', '65999', '30234', '30500', '12866', '36123', '29666', '36036', '10006', '10237', '12340', '77618', '15012', '40813', '44424', '15567', '36500', '15661', '11625', '11826', '55604', '70156', '13271', '10413', '10180', '18083', '55575', '40144', '77338', '22233', '15007', '65225', '12022', '11445', '40500', '40440', '33733', '22300', '27001', '10453', '55229', '22224', '15220', '45160', '22215', '70246', '40605', '55192', '22432', '44156', '29555', '44178', '45300', '12778', '45151', '33321', '44009', '70003', '10673', '13466', '30030', '10118', '12630', '77778', '18321', '33233', '30155', '27010', '18880', '77457', '12152', '44445', '18613', '55221', '27678', '33500', '15245', '30373', '70707', '27061', '18271', '77899', '44945', '77088', '70115', '11203', '15603', '15655', '77877', '44700', '80080', '15787', '11192', '11511', '44131', '70263', '40457', '11128', '77146', '77379', '27011', '55556', '11147', '30193', '33987', '55660'])
    codigo.pack(pady =5, padx = 20, anchor='w')

    botao_codigo = CTkButton(master = janela, text = 'Procurar por Código', corner_radius = 30, fg_color = 'transparent', border_color = '#00DB53', border_width = 2, hover_color = '#DB0A00', font = ('Arial', 20), height = 50, cursor = 'hand2')
    botao_codigo.pack(pady = 20, padx = 20, anchor = 'center')
    
    botao_html = CTkButton(master = janela, text = 'Ver Estatisticas', corner_radius = 30, fg_color = 'transparent', border_color = '#DB0A00', border_width = 2, hover_color = '#00DB53', font = ('Arial', 20), height = 50, width = 300, cursor = 'hand2')
    botao_html.pack(pady = 10, padx = 20, anchor = 'center')

    janela.mainloop()

    
    
def window2(municipio, cargo):

    #JANELA
    janela2 = CTk()
    janela2.title('Resultados dos Candidatos')
    image = Image.open('img/tse.png')
    img = CTkImage(light_image = image, dark_image = image, size = (150, 75))
    logo_label = CTkLabel(master = janela2, image = img, text = '')
    logo_label.pack(pady = (20, 10))
    #TEXTO 
    listaCandidatos = CTkLabel(master = janela2, text = 'Lista de candidatos referente ao', font = ('Arial', 25), text_color='#00DB53')
    muncarg = CTkLabel(master = janela2, text='município e cargo selecionados:', font = ('Arial', 25), text_color='#00DB53')
    especifico = CTkLabel(master = janela2, text='''nome, nome na urna, número e partido(respectivamente)''', font = ('Arial', 25), text_color='#00DB53')
    listaCandidatos.pack(pady = 10, padx = 20, anchor = 'center')
    muncarg.pack(pady = 0, padx = 20, anchor = 'center')
    especifico.pack(pady = 0, padx = 20, anchor = 'center')
    #COMOBOX
    main = Main()
    candidatos = main.municipios_cargos(municipio, cargo)
    boxCandidatos = CTkComboBox(master = janela2, height = 30, width = 400, border_color = '#00DB53', values = candidatos)
    boxCandidatos.pack(pady = 25, padx = 20, anchor='center')

    janela2.geometry('500x650')
    janela2.mainloop()


window()

# Printar os candidatos referentes aos cargos e municipios
# Dar a opção de procurar o candidato pelo código
# Botão para ver as estátisticas
