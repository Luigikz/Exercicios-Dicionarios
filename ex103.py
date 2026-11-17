import csv


def carregar_moedas(caminho="moedas.csv"):
    moedas = {}

    with open(caminho, mode="r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if len(linha) < 4:
                continue  # ignora linhas vazias ou incompletas

            sigla, nome_en, nome_pt, cotacao = (c.strip() for c in linha[:4])
            moedas[sigla.upper()] = {
                "nome": nome_pt,
                "cotacao": float(cotacao),  # valor de 1 unidade da moeda em R$
            }

    return moedas


def main():
    moedas = carregar_moedas()

    valor = float(input("Informe o valor em R$: ").replace(",", "."))
    sigla = input("Informe a sigla da moeda de destino (ex: USD, EUR): ").strip().upper()

    if sigla not in moedas:
        print(f"Moeda '{sigla}' não encontrada.")
        return

    moeda = moedas[sigla]
    convertido = valor / moeda["cotacao"]

    print()
    print(f"Moeda: {moeda['nome']} ({sigla})")
    print(f"R$ {valor:.2f} = {convertido:.2f} {sigla}")


main()