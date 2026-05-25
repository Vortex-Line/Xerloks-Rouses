Guia de Início Rápido
=====================

Este guia orienta o desenvolvedor na configuração inicial da plataforma **vortex-line**.

Instalação do SDK (Python)
--------------------------

Se você preferir utilizar o nosso SDK oficial em vez de chamadas HTTP puras, instale o pacote via pip:

.. code-block:: bash

   pip install vortex-line-sdk

Configuração Inicial
--------------------

Importe o cliente e configure suas credenciais de ambiente:

.. code-block:: python

   from vortex_line import VortexClient

   client = VortexClient(api_key="SEU_TOKEN_AQUI")

   # Exemplo rápido de checagem
   result = client.verify(url="https://site-suspeito.com")
   print(f"Veredito: {result.verdict}")

