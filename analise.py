import matplotlib
matplotlib.use("Agg")  # backend sem interface gráfica, funciona no cluster

import argparse
import csv
from collections import defaultdict

import matplotlib.pyplot as plt


def carregar_medias(caminho_log):
    valores = defaultdict(list)

    with open(caminho_log, newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            tamanho = int(linha["tamanho_bytes"])
            rtt = float(linha["rtt_ms"])
            valores[tamanho].append(rtt)

    tamanhos = sorted(valores.keys())
    medias = [sum(valores[t]) / len(valores[t]) for t in tamanhos]
    return tamanhos, medias


def gerar_grafico(tamanhos, medias, saida):
    rotulos = [f"{t:,}".replace(",", ".") for t in tamanhos]

    figura, eixo = plt.subplots(figsize=(8, 5))
    barras = eixo.bar(rotulos, medias, color="#4C72B0")

    eixo.set_xlabel("Tamanho da mensagem (bytes)")
    eixo.set_ylabel("RTT médio (ms)")
    eixo.set_title("RTT médio por tamanho de mensagem — 20 chamadas por tamanho")
    eixo.grid(axis="y", linestyle="--", alpha=0.4)

    for barra, media in zip(barras, medias):
        eixo.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height(),
            f"{media:.2f}",
            ha="center",
            va="bottom",
        )

    figura.tight_layout()
    figura.savefig(saida, dpi=150)
    print(f"[analise] Gráfico salvo em {saida}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análise dos resultados do experimento gRPC")
    parser.add_argument("--log", default="benchmark.log", help="Arquivo CSV de log")
    parser.add_argument("--saida", default="grafico.png", help="Arquivo PNG de saída")
    args = parser.parse_args()

    tamanhos, medias = carregar_medias(args.log)

    print("\nRTT médio por tamanho:")
    for tamanho, media in zip(tamanhos, medias):
        print(f"  {tamanho:>9} bytes -> {media:7.3f} ms")

    gerar_grafico(tamanhos, medias, args.saida)