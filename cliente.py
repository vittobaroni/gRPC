import grpc
import time
import csv

import benchmark_pb2
import benchmark_pb2_grpc

channel = grpc.insecure_channel("127.0.0.1:50051")
stub = benchmark_pb2_grpc.BenchmarkServiceStub(channel)

tamanhos = [1, 10000, 100000, 1000000]

with open("benchmark.log", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "timestamp",
        "tamanho_bytes",
        "indice_chamada",
        "rtt_ms"
    ])

    for tamanho in tamanhos:
        for indice in range(20):
            dados = b"x" * tamanho
            mensagem = benchmark_pb2.Mensagem(payload=dados)

            inicio = time.perf_counter()
            confirmacao = stub.Enviar(mensagem)
            fim = time.perf_counter()

            rtt = fim - inicio
            rtt_ms = rtt * 1000

            escritor.writerow([
                confirmacao.timestamp,
                tamanho,
                indice + 1,
                rtt_ms
            ])