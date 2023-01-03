import openpyxl
#Carregando um arquivo(book)
wb = openpyxl.load_workbook('Planilha vendas de animais.xlsx')
#listar as paginas
print(wb.sheetnames)
#pegar a pagina especifica para alterar o nome
ss_sheet = wb['Fruit']
#Alterar o nome
ss_sheet.title = 'Financeiro'
#salva a planilha
wb.save('Planilha vendas de animais.xlsx')