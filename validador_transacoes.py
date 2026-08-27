transacoes = [150.0, 3200.5, 12500.0, 450.0, -50.0, 800.0, 0]
print("Iniciando validações de transações!")
for transacao in transacoes:
    if transacao > 10000.00:
        print(f"[ALERTA!] Transação suspeita de R$ {transacao}: Encaminhada para auditoria.")
        continue
    if transacao <= 0 : 
        print(f"[ERRO CRÍTICO] Transação inválida encontrada R$ {transacao}. Interrompendo bot...")
        break
    else :
        print(f"[SUCESSO] Transação de R$ {transacao} processada.")
    