<h1>Projeto de Sistemas Distribuídos - Experimento gRPC (UFF)</h1>

<h2>Arquivos Base colocados por vitto baroni </h2>
<ul>
    <li><strong><code>benchmark.proto</code>:</strong> É o nosso "contrato". Ele define as regras de comunicação e o formato dos dados trocados entre o cliente e o servidor.</li>
    <li><strong><code>server.py</code>:</strong> É a lógica do servidor remoto que recebe os bytes, calcula o tamanho do payload e devolve um timestamp UTC.</li>
</ul>

<hr>

<h2>Passo a Passo para Configurar o Ambiente</h2>
<p> Sigam os passos abaixo pra conseguirem usar o servidor localmente pc de vocês</p></p>

<h3>1. Criar e ativar o ambiente virtual</h3>
<p>Isso evita conflitos com outras bibliotecas do seu Python.</p>
<pre><code>python -m venv venv

# Se usar Windows:
venv\Scripts\activate

# Se usar Linux/Mac:
source venv/bin/activate
</code></pre>

<h3>2. Instalar as dependências do gRPC e de Análise</h3>
<pre><code>pip install grpcio grpcio-tools pandas matplotlib</code></pre>
<p>é interessante copiar e colar tudo, já que dei uma olhada nas outras questões, e vi que precisará cirar um gráfico, e o matplotlib é perfeito pra isso</p>

<h3>3. Compilar o Contrato</h3>
<p>Execute o comando abaixo na raiz do projeto. O gRPC vai ler o <code>benchmark.proto</code> e gerar automaticamente os dois arquivos de comunicação (<code>_pb2.py</code> e <code>_pb2_grpc.py</code>) que o servidor precisa para existir.</p>
<pre><code>python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. benchmark.proto</code></pre>
<hr>

<h2>Como testar o Servidor ?</h2>
<p>Com o ambiente configurado e os arquivos gerados, inicie o servidor passando o seu IP local:</p>
<pre><code>python server.py --host 127.0.0.1 ( EXEMPLO DE HOST ) </code></pre>
<p><strong>OBS : Se não colocar a parte do host, ele funciona normalmente no ip local, mas pra fim de testes com o cluster da uff, seria interessante colocar as informações de ip do host, como mostra nos slides do copetti </strong></p>
