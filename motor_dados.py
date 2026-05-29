import csv  

meta_por_venda = 2000.00

# Variáveis para guardar os totais da empresa (começam zeradas)
faturamento_total = 0.0
total_metas_batidas = 0

print("--- INICIANDO MOTOR DE DADOS ---")

with open('vendas.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    for linha in leitor:
        # DEFESA: Ignora linhas vazias ou corrompidas
        if len(linha) < 2:
            continue
            
        nome_cliente = linha[0]
        texto_valor = linha[1]
        
        # DEFESA: Pula o cabeçalho
        if texto_valor == "Valor":
            continue
            
        valor_venda = float(texto_valor) 
        
        # O motor soma o valor da venda atual ao faturamento total acumulado
        faturamento_total = faturamento_total + valor_venda
        
        if valor_venda >= meta_por_venda:
            total_metas_batidas = total_metas_batidas + 1
            print(f"[+] {nome_cliente} comprou R$ {valor_venda} -> Meta Atingida")
        else:
            print(f"[-] {nome_cliente} comprou R$ {valor_venda} -> Abaixo da meta")

print("\n======================================")
print("       RESUMO EXECUTIVO GERADO        ")
print("======================================")
print(f"Faturamento Total: R$ {faturamento_total}")
print(f"Clientes que bateram a meta: {total_metas_batidas}")
print("======================================")
