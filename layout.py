import PySimpleGUI as sg
import json

menu = [
    ["Arquivo", ["Sobre", "Sair"]]
]

from banco import lista2
from banco import lista
from banco import dic

sg.theme('DarkBlue') # cor do programa

layout = [
    [sg.Menu(menu)],
    # 1
    [sg.Text("RAZÃO SOCIAL:"), sg.Text(" "*50), sg.Text("RECEITAS DE VENDAS PREVISTAS:"), sg.Text(" "*20), sg.Text("COMPRA TOTAIS DE INSUMOS PREVISTAS:"),  sg.Text(" "*6), sg.Text("COMPRAS TOTAIS PREVISTAS:"), sg.Text(" "*26), sg.Text("TOTAL DE INVESTIMENTO PREVISTO:")],
    [sg.Combo(list(dic.keys()), enable_events=True, size=(43,22), key='RAZAO'), sg.Input(key='RECEITAS_PRE'),  sg.Input(key='comp_ins_pre'), sg.Input(key='comp_tot_pre'), sg.Input(key='tot_inv_pre')],
    # 2
    [sg.Text("MUNUCÍPIO:"),  sg.Text(" "*56), sg.Text("RECEITAS DE VENDAS REALIZADAS:"),  sg.Text(" "*18), sg.Text("COMPRA TOTAIS INSUMOS REALIZADA:"),  sg.Text(" "*12), sg.Text("COMPRAS TOTAIS REALIZADAS:"),  sg.Text(" "*25), sg.Text("TOTAL DE INVESTIMENTO REALIZADO:")],
    [sg.Combo([], key='municipio', size=(43,22)), sg.Input(key='RECEITAS_REL'),  sg.Input(key='comp_ins_rel'), sg.Input(key='comp_tot_rel'), sg.Input(key='tot_inv_rel')],
    # 3
    [sg.Text("REGIÃO DE INTEGRAÇÃO:"),  sg.Text(" "*34), sg.Text("DESTINO DAS VENDAS:"),  sg.Text(" "*38), sg.Text("TOTAL DE COMPRAS DIEF:"), sg.Text(" "*32), sg.Text("TOTAL COMPRA INTERNA PREVISTA:"), sg.Text(" "*19), sg.Text("INVESTIMENTO FINANCEIROS")],
    [sg.Combo([], key='rg', size=(43,22)), sg.Input(key='DESTINO'),  sg.Input(key='ins_dief'), sg.Input(key='comp_tot_int_pre'), sg.Input(key='inv_finan')],
    # 4
    [sg.Text("PRODUTO:"), sg.Text(" "*57), sg.Text("RECEITA TOTAL DE VENDAS DIEF:"),  sg.Text(" "*22), sg.Text("TOTAL DE COMPRAS (PERFIL):"),  sg.Text(" "*27), sg.Text("TOTAL COMPRA INTERNA REALIZADA:"),  sg.Text(" "*16), sg.Text("INVESTIMENTOS FIXOS:")],
    [sg.Combo([], key='produto', size=(43,22)), sg.Input(key='DIEF'),  sg.Input(key='perfil'), sg.Input(key='comp_tot_int_rel'), sg.Input(key='inv_fixos')],
    # 5
    [sg.Text("STATUS DO BENEFICIO:"),  sg.Text(" "*37), sg.Text("VENDA INTERNA PREVISTA:"),  sg.Text(" "*31), sg.Text("COMPRA INTERNA INSUMO PREVISTA:"),  sg.Text(" "*14), sg.Text("TOTAL COMPRA INTERESTADUAL PREVISTA:"),  sg.Text(" "*7), sg.Text("MÁQUINAS E EQUIPAMENTOS:")],
    [sg.Combo([], key='status', size=(43,22)), sg.Input(key='VEN_INT_PRE'),  sg.Input(key='comp_ins_int_pre'), sg.Input(key='comp_tot_inte_pre'), sg.Input(key='maqui_e_eq')],
    # 6
    [sg.Text("CNPJ:"), sg.Text(" "*66), sg.Text("VENDA INTERNA REALIZADA:"),  sg.Text(" "*29), sg.Text("COMPRA INTERNA INSUMO REALIZADA:"),  sg.Text(" "*13), sg.Text("TOTAL COMPRA INTERESTADUAL REALIZADA:"),  sg.Text(" "*3), sg.Text("ICMS ESCOLHIDO:")],
    [sg.Combo([], key='cnpj', size=(43,22)), sg.Input(key='VEN_INT_REL'),  sg.Input(key='comp_ins_int_rel'), sg.Input(key='comp_tot_inte_rel'), sg.Input(key='icms')],
    # 7
    [sg.Text("ANO:"), sg.Text(" "*67), sg.Text("VENDA INTERESTADUAL PREVISTA:"),  sg.Text(" "*18), sg.Text("COMPRA INTERESTADUAL INSUMO PREVISTA:"),  sg.Text(" "*3), sg.Text("TOTAL COMPRA EXTERIOR PREVISTA:"),  sg.Text(" "*15), sg.Text("RENUNCIA PROJETADA:")],
    [sg.Input(key='ANO'), sg.Input(key='VEN_INTE_PRE'),  sg.Input(key='comp_ins_inte_pre'), sg.Input(key='comp_tot_ext_pre'), sg.Input(key='renun_proj')],
    # 8
    [sg.Text("EMPREGO PREVISTO:"), sg.Text(" "*41), sg.Text("VENDA INTERESTADUAL REALIZADA :"),  sg.Text(" "*15), sg.Text("COMPRA INTERESTADUAL INSUMO REALIZADA:"),  sg.Text(" "*1), sg.Text("TOTAL COMPRA EXTERIOR REALIZADA:"),  sg.Text(" "*13), sg.Text("RENUNCIA REALIZADA:")],
    [sg.Input(key='EMPREGO'), sg.Input(key='VEN_INTE_REL'),  sg.Input(key='comp_ins_inte_rel'), sg.Input(key='comp_tot_ext_rel'), sg.Input(key='renun_rel')],
    # 9
    [sg.Text("EMPREGO REALIZADO CAGED:"), sg.Text(" "*26), sg.Text("VENDA EXTERIOR PREVISTA:"),  sg.Text(" "*29), sg.Text("COMPRA EXTERIOR INSUMO PREVISTA:"),  sg.Text(" "*14), sg.Text("ACOMPANHAMENTO:"),  sg.Text(" "*40), sg.Text("PROJETO AMPLIAÇÃO:")],
    [sg.Input(key='CAGED'), sg.Input(key='VEN_EXT_PRE'),  sg.Input(key='comp_ins_ext_pre'), sg.Input(key='acomp'), sg.Input(key='proj_amp')],
    # 10
    [sg.Text("EMPREGO REALIZADO RAIS:"), sg.Text(" "*29), sg.Text("VENDA EXTERIOR REALIZADA:"),  sg.Text(" "*27), sg.Text("COMPRA EXTERIOR INSUMO REALIZADA:"),  sg.Text(" "*12), sg.Text("PROJETO IMPLANTAÇÃO:"), sg.Text(" "*34)],
    [sg.Input(key='RAIS'), sg.Input(key='VEN_EXT_REL'),  sg.Input(key='comp_ins_ext_rel'), sg.Input(key='proj_imp')],
    
    [sg.Text("INSCRIÇÃO ESTADUAL:")],
    [sg.Combo([], key='insc_estadual', size=(43,22))],
    # 11
    [sg.Text("VALOR FOLHA SEM ENCARGOS PREVISTO:"), sg.Text(" "*7)],
    [sg.Input(key='FOLHA_PRE')],
    [sg.Text("VALOR FOLHA SEM ENCARGOS REALIZADO:")],
    [sg.Input(key='FOLHA_REL')],
           
    [sg.Text()],
    [sg.Output(size=(43, 5))],
    [sg.Button("Enviar"), sg.Button("Fechar")]
]

layout_oficial = [
    [sg.Column(layout, size=(2000,2000), scrollable=True)]
]

