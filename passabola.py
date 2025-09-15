from datetime import datetime # Biblioteca que encontramos para auxiliar no calculo da idade da jogaodra.

jogadoras = [] # Lista que armazena o perfil de cada jogadora cadastrada.

def input_nome():
    """Solicita e valida o nome da jogadora."""
    while True:
        nome = input("Nome da jogadora: ").strip()
        if nome and nome.replace(" ", "").isalpha():
            return nome
        print("⚠️ Nome inválido! Use apenas letras e não deixe em branco.")

def input_email():
    """Solicita e valida o e-mail da jogadora."""
    while True:
        email = input("E-mail: ").strip()
        if "@" in email and "." in email:
            return email
        print("⚠️ E-mail inválido! Digite no formato correto (ex: exemplo@email.com).")

def input_senha():
    """Solicita e valida a senha."""
    while True:
        senha = input("Senha: ").strip()
        if len(senha) >= 4:
            return senha
        print("⚠️ A senha deve ter pelo menos 4 caracteres.")

def input_data_nascimento():
    """Solicita e valida a data de nascimento no formato dd/mm/aaaa."""
    while True:
        data_str = input("Data de nascimento (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return data_str
        except ValueError:
            print("⚠️ Data inválida! Use o formato dd/mm/aaaa e valores reais (ex: 31/12/2005).")

def input_altura():
    """Solicita e valida a altura da jogadora."""
    while True:
        try:
            altura_string = input("Altura (em metros, ex: 1.65): ").strip().replace(",",".")
            if not altura_string:
                print("⚠️ Altura não pode ficar em branco.")
                continue
            altura = float(altura_string)
            if 1.0 <= altura <= 3.0:
                return altura
            print("⚠️ Altura fora do intervalo esperado.")
        except ValueError:
            print("⚠️ Digite um valor numérico válido para altura.")

def input_peso():
    """Solicita e valida o peso da jogadora."""
    while True:
        try:
            peso_string = input("Peso (em kg, ex: 60): ").strip()
            if not peso_string:
                print("⚠️ Peso não pode ficar em branco.")
                continue
            peso = int(peso_string)
            if 20 <= peso <= 200:
                return peso
            print("⚠️ Peso fora do intervalo esperado.")
        except ValueError:
            print("⚠️ Digite um valor numérico válido para o peso.")

def input_texto(campo):
    """Função genérica para solicitar um texto não numérico."""
    while True:
        valor = input(f"{campo}: ").strip()
        if valor and not valor.isnumeric():
            return valor
        print(f"⚠️ {campo} inválido! Digite um texto válido e não deixe em branco.")

def input_inteiro_positivo(campo):
    """Função genérica para solicitar um número inteiro não negativo."""
    while True:
        try:
            numero_string = input(f"{campo}: ").strip()
            if not numero_string:
                print(f"⚠️ {campo} não pode ficar em branco.")
                continue
            numero = int(numero_string)
            if numero >= 0:
                return numero
            print(f"⚠️ {campo} não pode ser negativo.")
        except ValueError:
            print(f"⚠️ Digite um número válido para {campo}.")

def obter_nome_para_ordenacao(jogadora):
    """Fornece o nome da jogadora para ser usado como critério de ordenação."""
    return jogadora['nome']

def calcular_idade(data_nascimento_str):
    """Calcula a idade de uma pessoa a partir da sua data de nascimento."""
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# --- Funções de Cadastro, Listagem, Edição e Exclusão ---

def cadastrar_jogadora():
    """Coleta todos os dados e cadastra uma nova jogadora."""
    print("\n--- Novo Cadastro ---")
    nome = input_nome()
    email = input_email()
    senha = input_senha()
    data_nascimento = input_data_nascimento()
    idade = calcular_idade(data_nascimento)
    altura = input_altura()
    peso = input_peso()
    nacionalidade = input_texto("Nacionalidade")
    pe_dominante = input_texto("Pé dominante (Direito/Esquerdo)")
    biografia = input("Breve Biografia / Estilo de Jogo: ").strip()
    posicao = input_texto("Posição")
    clube = input_texto("Clube atual")
    link = input("Link do vídeo (YouTube): ").strip()
    gols = input_inteiro_positivo("Gols marcados")
    assistencias = input_inteiro_positivo("Assistências")
    jogos = input_inteiro_positivo("Jogos disputados")

    jogadora = {
        "nome": nome, "email": email, "senha": senha,
        "data_nascimento": data_nascimento, "altura": altura, "peso": peso,
        "nacionalidade": nacionalidade, "pe_dominante": pe_dominante,
        "biografia": biografia, "idade": idade, "posicao": posicao, "clube": clube,
        "link": link,
        "estatisticas": {"gols": gols, "assistencias": assistencias, "jogos": jogos}
    }
    jogadoras.append(jogadora)
    print(f"\n✅ Jogadora {nome} cadastrada com sucesso!\n")

def listar_jogadoras():
    """Exibe a lista de todas as jogadoras cadastradas."""
    if not jogadoras:
        print("\n ⚠️ Nenhuma jogadora cadastrada.")
        return

    jogadoras_ordenadas = sorted(jogadoras, key=obter_nome_para_ordenacao)
    
    print("\n=== LISTA DE JOGADORAS ===")
    for numero, jogadora in enumerate(jogadoras_ordenadas, 1):
        print(f"{numero}. {jogadora['nome']} ({jogadora['idade']} anos) - {jogadora['posicao']} | Clube: {jogadora['clube']}")
        print(f"   📏 Altura: {jogadora['altura']:.2f}m | ⚖️ Peso: {jogadora['peso']}kg | 🦶 Pé dominante: {jogadora['pe_dominante']}")
        print(f"   📧 Email: {jogadora['email']} | 📅 Nascimento: {jogadora['data_nascimento']} | 🌍 Nacionalidade: {jogadora['nacionalidade']}")
        print(f"   📝 Biografia: {jogadora['biografia']}")
        print(f"   📊 Estatísticas: {jogadora['estatisticas']['gols']} G | {jogadora['estatisticas']['assistencias']} A | {jogadora['estatisticas']['jogos']} Jogos")
        print(f"   🎥 Vídeo: {jogadora['link']}\n")

def editar_jogadora():
    """Permite editar os dados de uma jogadora existente."""
    if not jogadoras:
        print("\n ⚠️ Nenhuma jogadora cadastrada.")
        return

    nome_busca = input("Digite o nome da jogadora que deseja editar: ").strip()
    jogadora_encontrada = None
    for j in jogadoras:
        if j['nome'].lower() == nome_busca.lower():
            jogadora_encontrada = j
            break
    
    if jogadora_encontrada:
        jogadora = jogadora_encontrada
        print(f"\nEditando '{jogadora['nome']}'. Pressione Enter para manter o valor atual.\n")
        
        jogadora['nome'] = input(f"Nome [{jogadora['nome']}]: ").strip() or jogadora['nome']
        jogadora['email'] = input(f"Email [{jogadora['email']}]: ").strip() or jogadora['email']
        jogadora['senha'] = input(f"Senha [****]: ").strip() or jogadora['senha']
        
        nova_data_nascimento = input(f"Data de Nascimento [{jogadora['data_nascimento']}]: ").strip()
        if nova_data_nascimento:
            try:
                datetime.strptime(nova_data_nascimento, '%d/%m/%Y')
                jogadora['data_nascimento'] = nova_data_nascimento
                jogadora['idade'] = calcular_idade(nova_data_nascimento)
                print(f"Idade atualizada automaticamente para {jogadora['idade']} anos.")
            except ValueError:
                print("⚠️ Formato de data inválido. Mantendo o valor original.")

        nova_altura_string = input(f"Altura [{jogadora['altura']:.2f}m]: ").strip().replace(",",".")
        if nova_altura_string:
            try: jogadora['altura'] = float(nova_altura_string)
            except ValueError: print("⚠️ Altura inválida, mantendo valor atual.")
        
        novo_peso_string = input(f"Peso [{jogadora['peso']}kg]: ").strip()
        if novo_peso_string:
            try: jogadora['peso'] = int(novo_peso_string)
            except ValueError: print("⚠️ Peso inválido, mantendo valor atual.")
        
        jogadora['nacionalidade'] = input(f"Nacionalidade [{jogadora['nacionalidade']}]: ").strip() or jogadora['nacionalidade']
        jogadora['pe_dominante'] = input(f"Pé dominante [{jogadora['pe_dominante']}]: ").strip() or jogadora['pe_dominante']
        jogadora['biografia'] = input(f"Biografia [{jogadora['biografia']}]: ").strip() or jogadora['biografia']
        jogadora['posicao'] = input(f"Posição [{jogadora['posicao']}]: ").strip() or jogadora['posicao']
        jogadora['clube'] = input(f"Clube atual [{jogadora['clube']}]: ").strip() or jogadora['clube']
        jogadora['link'] = input(f"Link do vídeo [{jogadora['link']}]: ").strip() or jogadora['link']
        
        print(f"\n✅ Jogadora {jogadora['nome']} atualizada com sucesso!\n")
    else:
        print("\n ⚠️ Jogadora não encontrada.")


def excluir_jogadora():
    """Exclui o cadastro de uma jogadora."""
    if not jogadoras:
        print("\n ⚠️ Nenhuma jogadora cadastrada.")
        return
        
    nome_busca = input("Digite o nome da jogadora que deseja excluir: ").strip()
    for jogadora in list(jogadoras):
        if jogadora['nome'].lower() == nome_busca.lower():
            jogadoras.remove(jogadora)
            print(f"✅ Jogadora {jogadora['nome']} excluída com sucesso!")
            return
            
    print("\n ⚠️ Jogadora não encontrada.")

# --- Funções de Busca / Filtro ---

def exibir_resultados(jogadoras_encontradas, criterio, valor):
    """Função auxiliar para mostrar os resultados de uma busca."""
    if jogadoras_encontradas:
        print(f"\n=== Jogadoras encontradas para {criterio} '{valor}' ===")
        for jogadora in jogadoras_encontradas:
            print(f"- {jogadora['nome']} ({jogadora['idade']} anos) | {jogadora['posicao']} | Clube: {jogadora['clube']}")
    else:
        print(f"\n ⚠️ Nenhuma jogadora encontrada com {criterio} '{valor}'.")

def buscar_por_nome():
    """Busca jogadoras cujo nome contém o texto digitado."""
    nome = input_texto("Digite o nome para buscar")
    encontradas = []
    for jogadora in jogadoras: 
        if nome.lower() in jogadora['nome'].lower():
            encontradas.append(jogadora)
    exibir_resultados(encontradas, "nome", nome)

def buscar_por_posicao():
    """Busca jogadoras de uma posição específica."""
    posicao = input_texto("Digite a posição para buscar")
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['posicao'].lower() == posicao.lower():
            encontradas.append(jogadora)       
    exibir_resultados(encontradas, "posição", posicao)

def buscar_por_idade():
    """Busca jogadoras com uma idade específica."""
    idade = input_inteiro_positivo("Buscar jogadoras com idade igual a")   
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['idade'] == idade:
            encontradas.append(jogadora)           
    exibir_resultados(encontradas, "idade", idade)

def buscar_por_clube():
    """Busca jogadoras de um clube específico."""
    clube = input_texto("Digite o nome do clube") 
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['clube'].lower() == clube.lower():
            encontradas.append(jogadora)       
    exibir_resultados(encontradas, "clube", clube)

def buscar_por_nacionalidade():
    """Busca jogadoras de uma nacionalidade específica."""
    nacionalidade = input_texto("Digite a nacionalidade")   
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['nacionalidade'].lower() == nacionalidade.lower():
            encontradas.append(jogadora)           
    exibir_resultados(encontradas, "nacionalidade", nacionalidade)

def buscar_por_faixa_de_altura():
    """Busca jogadoras dentro de uma faixa de altura (mínima e máxima)."""
    try:
        min_altura = float(input("Altura mínima (ex: 1.60): ").replace(",","."))
        max_altura = float(input("Altura máxima (ex: 1.75): ").replace(",","."))     
        encontradas = []
        for jogadora in jogadoras:
            if min_altura <= jogadora['altura'] <= max_altura:
                encontradas.append(jogadora)               
        exibir_resultados(encontradas, "altura entre", f"{min_altura:.2f}m e {max_altura:.2f}m")
    except ValueError:
        print("⚠️ Valores de altura inválidos.")

def buscar_por_faixa_de_peso():
    """Busca jogadoras dentro de uma faixa de peso (mínimo e máximo)."""
    try:
        min_peso = int(input("Peso mínimo (em kg, ex: 55): "))
        max_peso = int(input("Peso máximo (em kg, ex: 70): "))
        
        encontradas = []
        for jogadora in jogadoras:
            if min_peso <= jogadora['peso'] <= max_peso:
                encontradas.append(jogadora)               
        exibir_resultados(encontradas, "peso entre", f"{min_peso}kg e {max_peso}kg")
    except ValueError:
        print("⚠️ Valores de peso inválidos.")

def buscar_por_pe_dominante():
    """Busca jogadoras com um pé dominante específico."""
    pe = input_texto("Pé dominante (Direito/Esquerdo)")
    
    encontradas = []
    for jogadora in jogadoras:
        if jogadora['pe_dominante'].lower() == pe.lower():
            encontradas.append(jogadora)
            
    exibir_resultados(encontradas, "pé dominante", pe)

# --- Funções de Menu ---

def menu_filtrar_jogadoras():
    """Exibe o submenu de filtros."""
    if not jogadoras:
        print("\n ⚠️ Nenhuma jogadora cadastrada para filtrar.")
        return

    while True:
        print("\n--- Menu de Filtros ---")
        print("1 - Buscar por Nome")
        print("2 - Buscar por Posição")
        print("3 - Buscar por Idade")
        print("4 - Buscar por Clube")
        print("5 - Buscar por Nacionalidade")
        print("6 - Buscar por Faixa de Altura")
        print("7 - Buscar por Faixa de Peso")
        print("8 - Buscar por Pé Dominante")
        print("9 - Voltar ao Menu Principal")

        opcao = input("Escolha uma opção de filtro: ").strip()

        if opcao == '1': buscar_por_nome()
        elif opcao == '2': buscar_por_posicao()
        elif opcao == '3': buscar_por_idade()
        elif opcao == '4': buscar_por_clube()
        elif opcao == '5': buscar_por_nacionalidade()
        elif opcao == '6': buscar_por_faixa_de_altura()
        elif opcao == '7': buscar_por_faixa_de_peso()
        elif opcao == '8': buscar_por_pe_dominante()
        elif opcao == '9': break
        else: print("⚠️ Opção inválida. Tente novamente.")

def menu():
    """Exibe o menu principal e gerencia a navegação do usuário."""
    while True:
        print("\n=== Passa a Bola - Plataforma de Talentos ===")
        print("1 - Cadastrar Jogadora")
        print("2 - Listar Todas as Jogadoras")
        print("3 - Filtrar Jogadoras")
        print("4 - Editar Jogadora")
        print("5 - Excluir Jogadora") 
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1": cadastrar_jogadora()
        elif opcao == "2": listar_jogadoras()
        elif opcao == "3": menu_filtrar_jogadoras()
        elif opcao == "4": editar_jogadora()
        elif opcao == "5": excluir_jogadora()
        elif opcao == "6": 
            print("👋 Encerrando o Passa a Bola. Até mais!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Para inicializar o programa
if __name__ == "__main__": 
    menu()