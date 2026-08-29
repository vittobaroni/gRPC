# bibliotecas necessárias

import grpc # grpc classico
from concurrent import futures # criar threads pra execução
import datetime # tem que usar, já que a questão pede a hora exata do sistema

#arquivos necessários quando compilou o benchmark.proto
import benchmark_pb2
import benchmark_pb2_grpc


# Classe que implementa o serviço definido no .proto
class BenchmarkServicer(benchmark_pb2_grpc.BenchmarkServiceServicer):
    
    # Método remoto exigido
    def Enviar(self, request, context):
        # Calcula o comprimento da mensagem recebida (payload)
        tamanho = len(request.payload)
        
        # Gera o timestamp UTC no formato ISO 8601
        agora_utc = datetime.datetime.now(datetime.timezone.utc)
        timestamp_iso = agora_utc.isoformat().replace("+00:00", "Z")
        
        # Imprime no terminal cada requisição processada
        print(f"[servidor] Recebido payload de {tamanho} bytes em {timestamp_iso}")
        
        # Retorna a mensagem de Confirmação com o tamanho e o timestamp
        return benchmark_pb2.Confirmacao(
            tamanho_recebido=tamanho,
            timestamp=timestamp_iso
        )

def serve():
    # Inicializa o servidor gRPC com um pool de threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    benchmark_pb2_grpc.add_BenchmarkServiceServicer_to_server(BenchmarkServicer(), server)
    
    # Define a porta em que o servidor vai rodar
    porta = '50051'
    server.add_insecure_port(f'[::]:{porta}')
    server.start()
    
    print(f"Servidor gRPC iniciado. Aguardando conexões na porta {porta}...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
