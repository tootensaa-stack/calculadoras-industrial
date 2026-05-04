print("===Calculadora===")


def calcular_eficiencia(producao_real, producao_meta):
    if producao_meta == 0:
        return 0
    return (producao_real / producao_meta) * 100


def calcular_diferenca(producao_real, producao_meta):
    return producao_meta - producao_real


continuar = "s"
while continuar == "s":
    turno = input("qual o turno?(Manhã, tarde ou noite): ")
    producao_real = float(input("Digite a produção real: "))
    producao_meta = float(input("Digite a meta: "))
    eficiência = calcular_eficiencia(producao_real, producao_meta)
    diferença = calcular_diferenca(producao_real, producao_meta)
    print(f"\nTurno: {turno.upper()}")
    if eficiência >= 90:
        print(f"Eficiência: {eficiência:.1f}% - Ótimo!")
    elif eficiência >= 70:
        print(f"Eficiência: {eficiência:.1f}% - Atenção!")
    else:
        print(f"Eficiência: {eficiência:.1f}% - Crítico!")

    if diferença > 0:
        print(f"Faltaram {diferença:.0f} unidades.")
    else:
        print("meta atingida ou ultrapassada.")
    continuar = input("Deseja calcular para outro turno? (s/n): ")
print("\nRelatorio finalizado.")
