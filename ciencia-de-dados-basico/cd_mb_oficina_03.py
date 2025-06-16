# 1. Questão: Suponha que você tem um array que armazena os nomes de cinco frutas: [“Maçã”, “Banana”, “Cereja”, “Damasco”, “Uva”]. 
# Como você adicionaria uma nova fruta ao final do array e como removeria a fruta da terceira posição?
frutas = ["Maçã", "Banana", "Cereja", "Damasco", "Uva"]
frutas.append("Goiaba") # adicionando ao final
frutas.pop(2) # removendo da terceira posição
print(frutas)

# 2. Questão: Imagine um array que armazena os nomes de três cores: “Azul”, “Vermelho” e “Amarelo”. 
# Como você adicionaria a cor “Verde” ao início da lista e como removeria a segunda cor?
cores = ["Azul", "Vermelho", "Amarelo"]
cores.insert(0, "Verde") # inserindo no inicio da lista
cores.pop(1) # removendo a segunda cor
print(cores)

# 3. Questão: Considere uma pilha utilizada para gerenciar uma sequência de livros. 
# Se você adicionar três livros à pilha e depois remover o livro no topo, qual livro será o próximo no topo da pilha? Dê um exemplo com os livros “Livro A”, “Livro B” e “Livro C”.
pilha = []
pilha.append("Livro A")
pilha.append("Livro B")
pilha.append("Livro C") # 'empilhando' 3 livros
topo = pilha.pop() # tirando elemento do topo da pilha
print(f"O Livro no topo é: {pilha[-1]}")

# 4. Questão: Imagine uma fila utilizada para gerenciar a ordem de atendimento em um consultório médico. 
# Se quatro pacientes são adicionados à fila e dois são atendidos, quem serão os próximos dois pacientes na ordem de atendimento? Considere os pacientes “Paciente 1”, “Paciente 2”, “Paciente 3” e “Paciente 4”.
fila = []

fila.append("Paciente 1")
fila.append("Paciente 2")
fila.append("Paciente 3")
fila.append("Paciente 4")

# dois pacientes atendidos
fila.pop(0)
fila.pop(0)

print(f"Os próximos pacientes a serem atendidos são: {fila[0]} e {fila[1]}")