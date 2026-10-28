🔐 Laboratório de Criptografia de Arquivos com Python
Projeto desenvolvido como parte de um desafio prático de Cibersegurança da DIO.

O objetivo deste laboratório foi compreender, em um ambiente controlado, o funcionamento básico da criptografia e descriptografia de arquivos utilizando Python.

⚠️ Este projeto possui finalidade exclusivamente educacional. Todos os testes foram realizados em uma máquina virtual Kali Linux e utilizando apenas arquivos descartáveis criados especificamente para o laboratório.

🎯 Objetivos
Compreender o processo de criptografia de arquivos.
Utilizar Python para manipulação de arquivos.
Explorar o algoritmo AES em um cenário controlado.
Entender a importância das chaves criptográficas.
Realizar o processo de recuperação de um arquivo criptografado.
Praticar o uso do Kali Linux e de ambientes virtuais Python.
🛠️ Tecnologias utilizadas
Python 3
Kali Linux
VirtualBox
pyaes
Git
GitHub
📂 Estrutura do projeto
.
├── encrypter.py
├── decrypter.py
├── teste.txt
└── README.md
encrypter.py
Script utilizado no laboratório para ler o arquivo de teste, criptografar seu conteúdo utilizando AES e gerar uma versão criptografada.

decrypter.py
Script responsável pelo processo inverso, utilizando a mesma chave para recuperar o conteúdo original do arquivo de teste.

teste.txt
Arquivo descartável utilizado exclusivamente para demonstrar o processo de criptografia e descriptografia.

🧪 Ambiente de laboratório
Para evitar qualquer impacto sobre arquivos reais, o projeto foi executado dentro de uma máquina virtual Kali Linux.

Também foi criado um ambiente virtual Python (venv) para isolar as dependências utilizadas no exercício.

O laboratório foi mantido em um diretório próprio:

~/ransomware-lab
Os testes foram realizados somente sobre o arquivo teste.txt.

🔄 Fluxo do experimento
teste.txt
    ↓
encrypter.py
    ↓
teste.txt.ransomwaretroll
    ↓
decrypter.py
    ↓
teste.txt
Primeiro, o arquivo de teste é lido pelo script de criptografia e seu conteúdo é transformado em dados cifrados.

Depois, o script de descriptografia utiliza a chave correspondente para recuperar o conteúdo original.

🧠 O que aprendi
Durante o desenvolvimento deste laboratório, pude praticar conceitos importantes de cibersegurança e Python, incluindo:

criação e utilização de uma máquina virtual para testes;
navegação e utilização do terminal Linux;
criação de ambientes virtuais Python;
instalação e gerenciamento de dependências com pip;
leitura e escrita de arquivos em modo binário;
utilização de AES para criptografia;
importância da chave no processo de criptografia e descriptografia;
análise do ciclo de criptografia e recuperação de um arquivo;
importância de ambientes isolados para experimentos de segurança.
Mais do que executar os scripts, o laboratório ajudou a visualizar de forma prática como a criptografia altera um arquivo e como a utilização da chave correta permite recuperar seu conteúdo.

🔒 Boas práticas e segurança
Este projeto foi desenvolvido apenas para fins educacionais.

Os scripts foram testados exclusivamente em um ambiente isolado e sobre um arquivo criado especificamente para o laboratório.

Não utilize este projeto sobre arquivos, sistemas ou ambientes que não sejam de sua propriedade ou para os quais você não possua autorização explícita.

📚 Referência
Projeto desenvolvido a partir do desafio educacional disponibilizado pela Digital Innovation One (DIO).

Repositório de referência:
Desafio Ransomware - DIO
