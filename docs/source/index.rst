.. vortex-line documentation master file

Documentação do vortex-line
===========================

O **vortex-line** é uma ferramenta de código aberto desenvolvida para verificar a veracidade de conteúdos na internet de forma local e independente, **sem o uso de APIs externas** de terceiros.

.. toctree::
   :maxdepth: 2
   :caption: Sumário:

   instalacao
   funcionamento
   arquitetura

🚀 Começo Rápido
---------------

Instalação
~~~~~~~~~~

Instale o pacote diretamente do repositório ou gerenciador local:

.. code-block:: bash

   pip install vortex-line

Uso Básico
~~~~~~~~~~

Analise um texto ou link diretamente pelo seu código:

.. code-block:: python

   from vortex_line import Verificador

   # Inicializa o motor de análise local
   verificador = Verificador()

   # Analisa o conteúdo de forma offline
   resultado = verificador.analisar("Texto suspeito para checagem")
   print(resultado.score_confiabilidade)
