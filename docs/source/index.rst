.. vortex-line documentation master file

===========================
Documentação do vortex-line
===========================

O **vortex-line** é uma ferramenta de código aberto desenvolvida para verificar a veracidade de conteúdos na internet de forma local e independente, **sem o uso de APIs externas** de terceiros.

🚀 Começo Rápido
================

Instalação
----------

Instale o pacote diretamente do repositório ou gerenciador local:

.. code-block:: bash

   pip install vortex-line

Uso Básico
----------

Analise um texto ou link diretamente pelo seu código:

.. code-block:: python

   from vortex_line import Verificador

   # Inicializa o motor de análise local
   verificador = Verificador()

   # Analisa o conteúdo de forma offline
   resultado = verificador.analisar("Texto suspeito para checagem")
   print(resultado.score_confiabilidade)


🛠️ Como Funciona (Sem APIs)
===========================

O grande diferencial do **vortex-line** é a autonomia. O sistema não consome serviços externos (como Google, OpenAI ou ferramentas pagas). 

Ele opera através de quatro pilares locais:

* **Análise Heurística**: Identifica padrões textuais e sensacionalismo comuns em notícias falsas.
* **Processamento de Linguagem Natural (PLN) Local**: Processa a sintaxe, léxico e o tom do texto usando modelos matemáticos embarcados.
* **Banco de Dados Estático**: Compara assinaturas e estruturas de boatos conhecidos previamente catalogados.
* **Análise de Reputação Estrutural**: Verifica a integridade de URLs e códigos-fonte sem realizar requisições rastreáveis.


📂 Estrutura do Projeto
=======================

.. code-block:: text

   vortex-line/
   ├── docs/               # Arquivos desta documentação (index.rst)
   ├── vortex_line/        # Código-fonte principal
   │   ├── motor/          # Algoritmos de checagem local
   │   └── dados/          # Base de dados estática e regras
   ├── tests/              # Testes unitários
   └── README.md           # Visão geral do repositório
