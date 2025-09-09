jogadoras = [] # A lista irá armazenar o perfil de cada jogadora cadastrada.


def input_nome(): #Solicita nome e valida para não conter números.

    while True:
        nome = input("Nome da jogadora: ").strip()
        if nome.replace(" ", "").isalpha():
            return nome
        print("⚠️ Nome inválido! Use apenas letras.")

def input_idade(): #Solicita idade e valida para ser número e positivo.
 
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                return idade
            print("⚠️ Idade deve ser maior que zero.")
        except ValueError:
            print("⚠️ Digite apenas números.")

def input_texto(campo): #Valida os campos de texto (posição, clube, região).

    while True:
        valor = input(f"{campo}: ").strip()
        if valor and not valor.isnumeric():
            return valor
        print(f"⚠️ {campo} inválido! Digite um texto válido.")

def input_inteiro_positivo(campo): #Valida para as estatísticas serem números inteiros positivos (gols, assistências, jogos).

    while True:
        try:
            numero = int(input(f"{campo}: "))
            if numero >= 0:
                return numero
            print(f"⚠️ {campo} não pode ser negativo.")
        except ValueError:
            print(f"⚠️ Digite um número válido para {campo}.")

def cadastrar_jogadora(): #cadastra as jogadoras com os valores recebidos nos input.

    nome = input_nome()
    idade = input_idade()
    posicao = input_texto("Posição")
    clube = input_texto("Clube atual")
    regiao = input_texto("Região")
    link = input("Link do vídeo (YouTube): ").strip()
    gols = input_inteiro_positivo("Gols marcados")
    assistencias = input_inteiro_positivo("Assistências")
    jogos = input_inteiro_positivo("Jogos disputados")

    jogadora = {
        "nome": nome,
        "idade": idade,
        "posicao": posicao,
        "clube": clube,
        "regiao": regiao, 
        "link": link,
        "estatisticas": {
            "gols": gols,
            "assistencias": assistencias,
            "jogos": jogos
        }
    }
    jogadoras.append(jogadora)
    print(f"\n✅ Jogadora {nome} cadastrada com sucesso!\n")

def listar_jogadoras(): #Mostra as jogaodras cadastradas, e ordenada.

    if not jogadoras:
        print("⚠️ Nenhuma jogadora cadastrada.")
        return

    jogadoras_ordenadas = sorted(jogadoras, key=ordenar_por_nome)

    print("\n=== LISTA DE JOGADORAS ===")
    for numero, jogadora in enumerate(jogadoras_ordenadas, 1):
        print(f"{numero}. {jogadora['nome']} ({jogadora['idade']} anos) - {jogadora['posicao']} | Clube: {jogadora['clube']} | Região: {jogadora['regiao']}")
        print(f"   Estatísticas: {jogadora['estatisticas']['gols']} G | {jogadora['estatisticas']['assistencias']} A | {jogadora['estatisticas']['jogos']} Jogos")
        print(f"   Vídeo: {jogadora['link']}\n")

def ordenar_por_nome(jogadora): #Uma função para ordenar os nomes em ordem alfabética.

    return jogadora['nome']



def buscar_por_posicao(): #Filtro para encontrar jogador na posição desejada.

    posicao = input_texto("Digite a posição para buscar")
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['posicao'].lower() == posicao.lower():
            encontradas.append(jogadora)
    if encontradas:
        print(f"\n=== Jogadoras na posição {posicao.upper()} ===")
        for jogadora in encontradas:
            print(f"- {jogadora['nome']} ({jogadora['idade']} anos) | Clube: {jogadora['clube']}")
    else:
        print("⚠️ Nenhuma jogadora encontrada nessa posição.")

def buscar_por_idade(): #Filtro para encontrar jogador na idade desejada.

    idade_pesquisa = input_inteiro_positivo("Mostrar jogadoras com idade = ")
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['idade'] == idade_pesquisa:
            encontradas.append(jogadora)
    if encontradas:
        print(f"\n=== Jogadoras com idade = {idade_pesquisa} ===")
        for jogadora in encontradas:
            print(f"- {jogadora['nome']} ({jogadora['idade']} anos) | Posição: {jogadora['posicao']}")
    else:
        print("⚠️ Nenhuma jogadora encontrada com essa idade.")

def buscar_por_clube(): # Filtro para encontrar jogador no clube desejado.

    clube = input_texto("Digite o nome do clube")
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['clube'].lower() == clube.lower():
            encontradas.append(jogadora)
    if encontradas:
        print(f"\n=== Jogadoras do clube {clube.upper()} ===")
        for jogadora in encontradas:
            print(f"- {jogadora['nome']} ({jogadora['idade']} anos) | Posição: {jogadora['posicao']}")
    else:
        print("⚠️ Nenhuma jogadora encontrada nesse clube.")


def buscar_por_regiao(): # Filtro para encontrar jogador na região desejada.
 
    regiao = input_texto("Digite a região para buscar")
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['regiao'].lower() == regiao.lower():
            encontradas.append(jogadora)
    if encontradas:
        print(f"\n=== Jogadoras da região {regiao.upper()} ===")
        for jogadora in encontradas:
            print(f"- {jogadora['nome']} ({jogadora['idade']} anos) | Posição: {jogadora['posicao']} | Clube: {jogadora['clube']}")
    else:
        print("⚠️ Nenhuma jogadora encontrada nessa região.")


def recomendar_jogadoras(): #Recomenda jogadora com mais gol+assistência.
    if not jogadoras:
        print("⚠️ Nenhuma jogadora cadastrada para gerar recomendações.")
        return

    melhores = []
    maior_total = -1

    for jogadora in jogadoras:
        total = jogadora['estatisticas']['gols'] + jogadora['estatisticas']['assistencias']
        if total > maior_total:
            melhores = [jogadora]
            maior_total = total
        elif total == maior_total:
            melhores.append(jogadora)

    print("\n=== RECOMENDAÇÃO ===")
    if len(melhores) == 1:
        jogadora = melhores[0]
        total = jogadora['estatisticas']['gols'] + jogadora['estatisticas']['assistencias']
        print(f"🏆 Destaque: {jogadora['nome']} ({jogadora['idade']} anos)")
        print(f"📍 Posição: {jogadora['posicao']} | Clube: {jogadora['clube']}")
        print(f"📊 Desempenho: {jogadora['estatisticas']['gols']} G + {jogadora['estatisticas']['assistencias']} A = {total}")
        print(f"🎥 Vídeo: {jogadora['link']}")
    else: #Caso tenha empate em jogadoras com mais gol+assistência, imprime todas as empatadas.
        print(f"🏆 Empate! Jogadoras com {maior_total} contribuições diretas:")
        for jogadora_empate in melhores:
            print(f"- {jogadora_empate['nome']} ({jogadora_empate['idade']} anos) | {jogadora_empate['posicao']} | {jogadora_empate['clube']}")


def editar_jogadora(): #Edita qualquer dado do cadastro da jogadora, mas se não quiser editar algo, dá apenas enter.
  
    if not jogadoras:
        print("⚠️ Nenhuma jogadora cadastrada.")
        return

    nome_busca = input("Digite o nome da jogadora que deseja editar: ").strip()
    for jogadora in jogadoras:
        if jogadora['nome'].lower() == nome_busca.lower():
            print(f"\nEditando {jogadora['nome']}. Digite enter para manter o valor atual.\n")

            novo_nome = input(f"Nome [{jogadora['nome']}]: ").strip()
            if novo_nome:
                jogadora['nome'] = novo_nome

            nova_idade = input(f"Idade [{jogadora['idade']}]: ").strip()
            if nova_idade:
                try:
                    jogadora['idade'] = int(nova_idade)
                except ValueError:
                    print("⚠️ Idade inválida, mantendo valor atual.")

            nova_posicao = input(f"Posição [{jogadora['posicao']}]: ").strip()
            if nova_posicao:
                jogadora['posicao'] = nova_posicao

            novo_clube = input(f"Clube atual [{jogadora['clube']}]: ").strip()
            if novo_clube:
                jogadora['clube'] = novo_clube
            
            nova_regiao = input(f"Região [{jogadora['regiao']}]: ").strip()
            if nova_regiao:
                jogadora['regiao'] = nova_regiao

            novo_link = input(f"Link do vídeo (YouTube) [{jogadora['link']}]: ").strip()
            if novo_link:
                jogadora['link'] = novo_link

            novos_gols = input(f"Gols marcados [{jogadora['estatisticas']['gols']}]: ").strip()
            if novos_gols:
                try:
                    jogadora['estatisticas']['gols'] = int(novos_gols)
                except ValueError:
                    print("⚠️ Gols inválido, mantendo valor atual.")

            novas_assistencias = input(f"Assistências [{jogadora['estatisticas']['assistencias']}]: ").strip()
            if novas_assistencias:
                try:
                    jogadora['estatisticas']['assistencias'] = int(novas_assistencias)
                except ValueError:
                    print("⚠️ Assistências inválido, mantendo valor atual.")

            novos_jogos = input(f"Jogos disputados [{jogadora['estatisticas']['jogos']}]: ").strip()
            if novos_jogos:
                try:
                    jogadora['estatisticas']['jogos'] = int(novos_jogos)
                except ValueError:
                    print("⚠️ Jogos inválido, mantendo valor atual.")

            print(f"\n✅ Jogadora {jogadora['nome']} atualizada com sucesso!\n")
            return

    print("⚠️ Jogadora não encontrada.")


def excluir_jogadora(): # Exclui uma jogadora do cadastro.
    if not jogadoras:
        print("⚠️ Nenhuma jogadora cadastrada.")
        return
    nome_busca = input("Digite o nome da jogadora que deseja excluir: ").strip()
    for jogadora in jogadoras:
        if jogadora['nome'].lower() == nome_busca.lower():
            nome_excluida = jogadora['nome']
            jogadoras.remove(jogadora)
            print(f"✅ Jogadora {nome_excluida} excluída com sucesso!")
            return
    print("⚠️ Jogadora não encontrada.")


def menu(): #Menu que mostra as opções.
    while True:
        print("\n=== LinkeFut - Plataforma de Talentos ===")
        print("1 - Cadastrar Jogadora")
        print("2 - Listar Jogadoras")
        print("3 - Buscar por Posição")
        print("4 - Buscar por Idade")
        print("5 - Buscar por Clube")
        print("6 - Buscar por Região")
        print("7 - Recomendações")
        print("8 - Editar Jogadora")
        print("9 - Excluir Jogadora") 
        print("10 - Sair")         

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_jogadora()
        elif opcao == "2":
            listar_jogadoras()
        elif opcao == "3":
            buscar_por_posicao()
        elif opcao == "4":
            buscar_por_idade()
        elif opcao == "5":
            buscar_por_clube()
        elif opcao == "6": 
            buscar_por_regiao()
        elif opcao == "7": 
            recomendar_jogadoras()
        elif opcao == "8": 
            editar_jogadora()
        elif opcao == "9": 
            excluir_jogadora()
        elif opcao == "10": 
            print("👋 Encerrando LinkeFut. Até mais!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__": 
    menu()