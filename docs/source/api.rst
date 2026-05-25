API de Integração
=================

Desenvolvedores podem utilizar a API da **vortex-line** para validar a confiabilidade de URLs e textos automaticamente.

Endpoint de Validação
---------------------

``POST /api/v1/verify``

Exemplo de Requisição
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "url": "https://exemplo-boato.com",
     "text_content": "Texto suspeito capturado na rede social."
   }

Exemplo de Resposta
~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "status": "verified_false",
     "confidence_score": 0.98,
     "explanation": "Este conteúdo foi desmentido por agências parceiras."
   }
