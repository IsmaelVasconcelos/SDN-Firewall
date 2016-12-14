import código_funcional
id_s = input("Digite o id do switche: ")
nw_src = input("Digite o ip de Origem: ")
nw_dst = input("Digite o ip de Destino: ")
actions = input("Digite a acao - ALLOW ou DENY: ")
nw_proto = input("Digite o protocolo: ")
priority = input("Digite a prioridade: ")
while True:
    opcao = input("Digite a opcao: ")
    if opcao == "1":
        initial_status ()
        escolha = input("Voce deseja execultar outra funcao: ")
        if escolha == "sim":
            continue
        else:
            break
    elif opcao == "2":
        status_switche ()
        escolha = input("Voce deseja execultar outra funcao: ")
        if escolha == "sim":
            continue
        else:
            break
    elif opcao == "3":
        rules()
        escolha = input("Voce deseja execultar outra funcao: ")
        if escolha == "sim":
            continue
        else:
            break
    elif opcao == "4":
        acquiring_all_rules ()
        escolha = input("Voce deseja execultar outra funcao: ")
        if escolha == "sim":
            continue
        else:
            break
    elif opcao == "5":
        acquiring_log_output ()
        escolha = input("Voce deseja execultar outra funcao: ")
        if escolha == "sim":
            continue
        else:
            break
    elif opcao == "6":
        changing_log_output ()
        escolha = input("Voce deseja execultar outra funcao: ")
        if escolha == "sim":
            continue
        else:
            break
    elif opcao == "7":
        delete ()
