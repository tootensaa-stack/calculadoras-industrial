print("Faixas box")
total_faixas = 0
metragem_total = 0


def calcular_faixa(largura, comprimento):
    if largura < 0 or comprimento < 0:
        return "Dimensões inválidas"
    tamanho = (largura + comprimento) * 2
    return tamanho


continuar = "s"
while continuar == "s":
    largura = float(input("Digite a largura da faixa: "))
    comprimento = float(input("Digite o comprimento da faixa: "))

    if comprimento < 0 or largura < 0:
        print("Dimenções inválidas. Por favor, insira valores positivos.")
    else:
        resultado = calcular_faixa(largura, comprimento)
        print(f"O tamanho da faixa é: {resultado:.2f} metros")
        total_faixas += 1
        metragem_total += resultado
    continuar = input("Deseja calcular para outra faixa? (s/n): ")

print(f"\nRelatorio finalizado.")
print(f"Total de faixas calculadas: {total_faixas}")
print(f"Metragem total: {metragem_total:.2f} metros")
