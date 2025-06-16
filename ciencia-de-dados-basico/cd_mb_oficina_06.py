import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
    "Idade": [28, 34, 29, None, 42],
    "Cidade": ["São Paulo", "Rio de Janeiro", None, "Curitiba", "Belo Horizonte"],
    "Vendas": [150, 200, 300, 400, None],
}

# 1. Crie um DataFrame com base nos dados fornecidos;
df = pd.DataFrame(dados)
print(df)

# 2. Filtre os clientes que têm mais de 30 anos;
maiores_30 = df.query("Idade > 30")
print(maiores_30)

# 3. Calcule a média de idade dos clientes;
media_idade = df["Idade"].mean()
print(f"Média de idade: {media_idade:.2f}")

# 4. Substitua valores faltantes na coluna Cidade por ‘Desconhecido’;
df.fillna({"Cidade": "Desconhecido"}, inplace=True)
print(df)

# 5. Calcule a soma total das vendas.
soma_vendas = df["Vendas"].sum()
print(f"Soma das vendas: {soma_vendas}")
