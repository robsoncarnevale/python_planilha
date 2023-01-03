import openpyxl
#Carregando um arquivo(book)
wb = openpyxl.load_workbook('Planilha vendas de animais.xlsx')
#listar as paginas
print(wb.sheetnames)
#pegar a pagina especifica que quer remover
remove_tab = wb['Folha3']
#remove a pagina
wb.remove(remove_tab)
#salva a planilha
wb.save('Planilha vendas de animais.xlsx')