import openpyxl
#Carregando um arquivo(book)
book = openpyxl.load_workbook('Planilha vendas de animais.xlsx')
#selecionando uma pagina
vendas_page = book['Vendas']
#Imprimindo os dados da planilha em cada linha
for rows in vendas_page.iter_rows(min_row=2):
    #listar as informações com print
    print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
    #listar as informações da planilha
    for cell in rows:
        print(cell.value)
        #alterar um valor da planilha
        if cell.value == 'Lagarto':
            cell.value = 'Dragão de Comoda'
#salvar a planilha
book.save('Planilha vendas de animais.xlsx')