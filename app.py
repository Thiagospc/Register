# bibliotecas
import PySimpleGUI as sg
import mysql.connector as mc

# import de outras arquivos
from layout import layout_oficial
from var_textos import show, dados
from layout import dic
from banco import lista, total

# estrutura da janela
window = sg.Window('Cadastro', layout=layout_oficial, return_keyboard_events=True, margins=(0, 0), resizable=True, finalize=True)
window.maximize()

id = 0

# condições
while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED or event == "Fechar" or event == "Sair":
        break
    if event == "Sobre": 
        sg.Popup(show)

    if event =='RAZAO': # preenchimentos automaticos
        item = values[event]

        valor = [i["muni"] for i in dic[item]]
        window['municipio'].update(value='vazio', values=valor)
        valor = [i["rg_"] for i in dic[item]]
        window['rg'].update(value='vazio', values=valor)
        valor = [i["prod"] for i in dic[item]]
        window['produto'].update(value='vazio', values=valor)
        valor = [i["stts"] for i in dic[item]]
        window['status'].update(value='vazio', values=valor)
        valor = [i["cnpj_"] for i in dic[item]]
        window['cnpj'].update(value='vazio', values=valor)
        valor = [i["insc_est"] for i in dic[item]]
        window['insc_estadual'].update(value='vazio', values=valor)

        def padrao_zero():
            # 1
            window['RECEITAS_PRE'].update(value=0)
            window['comp_ins_pre'].update(value=0)
            window['comp_tot_pre'].update(value=0)
            window['tot_inv_pre'].update(value=0)

            # 2
            window['RECEITAS_REL'].update(value=0)
            window['comp_ins_rel'].update(value=0)
            window['comp_tot_rel'].update(value=0)
            window['tot_inv_rel'].update(value=0)

            # 3
            window['DESTINO'].update(value=0)
            window['ins_dief'].update(value=0)
            window['comp_tot_int_pre'].update(value=0)
            window['inv_finan'].update(value=0)

            # 4
            window['DIEF'].update(value=0)
            window['perfil'].update(value=0)
            window['comp_tot_int_rel'].update(value=0)
            window['inv_fixos'].update(value=0)

            # 5
            window['VEN_INT_PRE'].update(value=0)
            window['comp_ins_int_pre'].update(value=0)
            window['comp_tot_inte_pre'].update(value=0)
            window['maqui_e_eq'].update(value=0)

            # 6
            window['VEN_INT_REL'].update(value=0)
            window['comp_ins_int_rel'].update(value=0)
            window['comp_tot_inte_rel'].update(value=0)
            window['icms'].update(value=0)
            # 7
            window['VEN_INTE_PRE'].update(value=0)
            window['comp_ins_inte_pre'].update(value=0)
            window['comp_tot_ext_pre'].update(value=0)
            window['renun_proj'].update(value=0)
            
            # 8
            window['VEN_INTE_REL'].update(value=0)
            window['comp_ins_inte_rel'].update(value=0)
            window['comp_tot_ext_rel'].update(value=0)
            window['renun_rel'].update(value=0)
            window['EMPREGO'].update(value=0)
            
            # 9
            window['VEN_EXT_PRE'].update(value=0)
            window['comp_ins_ext_pre'].update(value=0)
            window['acomp'].update(value=0)
            window['proj_amp'].update(value=0)
            window['CAGED'].update(value=0)


            # 10
            window['VEN_EXT_REL'].update(value=0)
            window['comp_ins_ext_rel'].update(value=0)
            window['proj_imp'].update(value=0)
            window['RAIS'].update(value=0)

            # 11
            window['FOLHA_PRE'].update(value=0)
            window['FOLHA_REL'].update(value=0)
        
        padrao_zero()

    if event == "Enviar": # recolhe informações para envios do bando mysql
        from banco import conexao

        if conexao.is_connected():
            db_info = conexao.get_server_info()
            print(f"conexão estabelecida com mysql {db_info}")
            
            # chaves dos inputs
            
            def testando_informacoes():
                razao_social = values['RAZAO']
                municipio = values['municipio']
                rg = values['rg']
                produto = values['produto']
                status = values['status']
                cnpj = values['cnpj']
                insc_estadual = values['insc_estadual']  
                              
            


            def inserindo_no_banco():
                # váriaveis
                razao_social = values['RAZAO']
                municipio = values['municipio']
                ano = values['ANO']
                emp_pre = values['EMPREGO']
                caged = values['CAGED']
                rais = values['RAIS']
                valor_fol_pre = values['FOLHA_PRE']
                valor_fol_rel = values['FOLHA_REL']

                               
                if ano == '':
                    ano = 0
                elif emp_pre == '':
                    emp_pre = 0
                elif caged == '':
                    caged = 0
                elif rais == '':
                    rais = 0
                elif valor_fol_pre == '':
                    valor_fol_pre = 0.00
                elif valor_fol_rel == '':
                    valor_fol_rel = 0.00
                else:
                    pass

                receitas_pre = values['RECEITAS_PRE']
                receitas_rel = values['RECEITAS_REL']
                destino = values['DESTINO']
                dief = values['DIEF']
                venda_int_pre = values['VEN_INT_PRE']
                venda_int_rel = values['VEN_INT_REL']
                venda_intere_pre = values['VEN_INTE_PRE']
                venda_intere_rel = values['VEN_INTE_REL']
                venda_ext_pre = values['VEN_EXT_PRE']
                venda_ext_rel = values['VEN_EXT_REL']

                if receitas_pre == '':
                    receitas_pre = 0
                elif receitas_rel == '':
                    receitas_rel = 0.00
                elif dief == '':
                    dief = 0.00
                elif venda_int_pre == '':
                    venda_int_pre = 0.00
                elif venda_intere_pre == '':
                    venda_intere_pre = 0.00
                elif venda_intere_rel == '':
                    venda_intere_rel = 0.00
                elif venda_ext_pre == '':
                    venda_ext_pre = 0.00
                elif venda_ext_rel == '':
                    venda_ext_rel = 0.00
                else:
                    pass

                comp_ins_pre = values['comp_ins_pre']
                comp_ins_rel = values['comp_ins_rel']
                ins_dief = values['ins_dief']
                perfil = values['perfil']
                comp_ins_int_pre = values['comp_ins_int_pre']
                comp_ins_int_rel = values['comp_ins_int_rel']
                comp_ins_inte_pre = values['comp_ins_inte_pre']
                comp_ins_inte_rel = values['comp_ins_inte_rel']
                comp_ins_ext_pre = values['comp_ins_ext_pre']
                comp_ins_ext_rel = values['comp_ins_ext_rel']

                if comp_ins_pre == '':
                    comp_ins_pre = 0
                elif comp_ins_rel == '':
                    comp_ins_rel = 0.00
                elif ins_dief == '':
                    ins_dief = 0.00
                elif perfil == '':
                    perfil = 0.00
                elif comp_ins_int_pre == '':
                    comp_ins_int_pre = 0.00
                elif comp_ins_int_rel == '':
                    comp_ins_int_rel = 0.00
                elif comp_ins_inte_pre == '':
                    comp_ins_inte_pre = 0.00
                elif comp_ins_inte_rel == '':
                    comp_ins_inte_rel = 0.00
                elif comp_ins_ext_pre == '':
                    comp_ins_ext_pre = 0.00
                elif comp_ins_ext_rel == '':
                    comp_ins_ext_rel = 0.00
                else:
                    pass

                comp_tot_pre = values['comp_tot_pre']
                comp_tot_rel = values['comp_tot_rel']
                comp_tot_int_pre = values['comp_tot_int_pre']
                comp_tot_int_rel = values['comp_tot_int_rel']
                comp_tot_inte_pre = values['comp_tot_inte_pre']
                comp_tot_inte_rel = values['comp_tot_inte_rel']
                comp_tot_ext_pre = values['comp_tot_ext_pre']
                comp_tot_ext_rel = values['comp_tot_ext_rel']

                if comp_tot_pre == '':
                    comp_tot_pre = 0
                elif comp_tot_rel == '':
                    comp_tot_rel = 0.00
                elif comp_tot_int_pre == '':
                    comp_tot_int_pre = 0.00
                elif comp_tot_int_rel == '':
                    comp_tot_int_rel = 0.00
                elif comp_tot_inte_pre == '':
                    comp_tot_inte_pre = 0.00
                elif comp_tot_inte_rel == '':
                    comp_tot_inte_rel = 0.00
                elif comp_tot_ext_pre == '':
                    comp_tot_ext_pre = 0.00
                elif comp_tot_ext_rel == '':
                    comp_tot_ext_rel = 0.00
                else:
                    pass

                acomp = values['acomp']
                proj_imp = values['proj_imp']
                tot_inv_pre = values['tot_inv_pre']
                tot_inv_rel = values['tot_inv_rel']
                inv_finan = values['inv_finan']
                inv_fixos = values['inv_fixos']
                maqui_e_eq = values['maqui_e_eq']
                icms = values['icms']
                renun_proj = values['renun_proj']
                renun_rel = values['renun_rel']
                proj_amp = values['proj_amp']

                if acomp == '':
                    acomp = '-'
                elif proj_imp == '':
                    proj_imp = '-'
                elif tot_inv_pre == '':
                    tot_inv_pre = 0.00
                elif tot_inv_rel == '':
                    tot_inv_rel = 0.00
                elif inv_finan == '':
                    inv_finan = 0.00
                elif inv_fixos == '':
                    inv_fixos = 0.00
                elif maqui_e_eq == '':
                    maqui_e_eq = 0.00
                elif icms == '':
                    icms = 0.00
                elif renun_proj == '':
                    renun_proj = 0.00
                elif renun_rel == '':
                    renun_rel  = 0.00
                elif proj_amp == '':
                    proj_amp = '-'
                else:
                    pass

                for x in range(total):
                    if lista[x][1] == razao_social and lista[x][4] == municipio:
                        global id
                        id = (lista[x][0])

                # insert
                cursor = conexao.cursor()
                
                cursor.execute("insert into receitas values (default, '%s', '%d', '%f', '%f', '%s', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%d', '%d', '%d', '%f', '%f', '%d')" % (str(razao_social), int(ano), float(receitas_pre), float(receitas_rel), str(destino), float(dief), float(venda_int_pre), float(venda_int_rel), float(venda_intere_pre), float(venda_intere_rel), float(venda_ext_pre), float(venda_ext_pre), int(emp_pre), int(caged), int(rais), float(valor_fol_pre), float(valor_fol_rel), int(id)))
                cursor.execute("insert into insumos values (default, '%s', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%d')" % (str(razao_social), int(ano), float(comp_ins_pre), float(comp_ins_rel), float(ins_dief), float(perfil), float(comp_ins_int_pre), float(comp_ins_int_rel), float(comp_ins_inte_pre), float(comp_ins_inte_rel), float(comp_ins_ext_pre), float(comp_ins_ext_rel), int(id)))
                cursor.execute("insert into compras_totais values (default, '%s', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%s', '%s', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%s', '%d')" % (str(razao_social), int(ano), float(comp_tot_pre), float(comp_tot_rel), float(comp_tot_int_pre), float(comp_tot_int_rel), float(comp_tot_inte_pre), float(comp_tot_inte_rel), float(comp_tot_ext_pre), float(comp_tot_ext_rel), str(acomp), str(proj_imp), float(tot_inv_pre), float(tot_inv_rel), float(inv_finan), float(inv_fixos), float(maqui_e_eq), float(icms), float(renun_proj), float(renun_rel), str(proj_amp), int(id)))  

           
            inserindo_no_banco()
            print(dados)



window.close()

