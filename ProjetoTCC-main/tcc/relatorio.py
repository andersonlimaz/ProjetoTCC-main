import psycopg2

# Conecte-se ao banco de dados PostgreSQL
conn = psycopg2.connect(
    database="Monitora1",
    user="postgres",
    password="0405",
    host="localhost",
    port="5432"
)

# Crie um cursor para executar consultas SQL
cursor = conn.cursor()

# Execute uma consulta SQL para selecionar os dados da tabela
cursor.execute("SELECT nome, email, valor, ong_parceiras FROM paginas_pagamento")

# Recupere os resultados da consulta
resultados = cursor.fetchall()

# Calcule o valor total
valor_total = sum([linha[2] for linha in resultados])

# Crie um arquivo HTML para exibir os resultados
with open("tabela.html", "w") as arquivo_html:
    arquivo_html.write("<html><head><title>Relatório de Pagamentos</title></head><body>")
    arquivo_html.write("<h1>Relatório de Pagamentos</h1>")
    arquivo_html.write("<table border='1'>")
    arquivo_html.write("<tr><th>Nome</th><th>Email</th><th>Valor</th><th>Ong Parceiras</th></tr>")
    for linha in resultados:
        arquivo_html.write("<tr>")
        for coluna in linha:
            arquivo_html.write(f"<td>{coluna}</td>")
        arquivo_html.write("</tr>")
    
    # Inclua a linha com "Valor Total" com a soma dos valores da coluna "Valor"
    arquivo_html.write("<tr><td colspan='2'><b>Valor Total:</b></td><td><b>{:.2f}</b></td><td></td></tr>".format(valor_total))
    
    arquivo_html.write("</table>")
    arquivo_html.write("</body></html>")

# Feche o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
