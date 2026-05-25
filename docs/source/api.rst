API de Integração Avançada
==========================

A API da **vortex-line** permite que portais de notícias, redes sociais e desenvolvedores verifiquem a autenticidade de conteúdos (textos, links e mídias) de forma automatizada.

Autenticação
------------

Todas as requisições devem incluir o token de acesso no cabeçalho HTTP:

.. code-block:: http

   Authorization: Bearer SEU_TOKEN_AQUI

Serviço de Verificação de Conteúdo
----------------------------------

.. http:post:: /api/v1/verify

   Analisa um link ou texto suspeito utilizando nossos modelos de IA e bancos de dados integrados.

   **Exemplo de Requisição (JSON):**

   .. code-block:: json

      {
        "url": "https://exemplo-boato.com",
        "text_content": "Texto suspeito capturado na rede social.",
        "allow_human_review": true
      }

   **Parâmetros do Corpo (Request Body):**

   * ``url`` *(string, opcional)*: O link completo da página que contém o boato.
   * ``text_content`` *(string, opcional)*: O texto completo ou trecho a ser analisado.
   * ``allow_human_review`` *(boolean, opcional)*: Se ``true``, encaminha para analistas humanos caso a IA fique em dúvida.

   **Exemplo de Resposta (JSON - 200 OK):**

   .. code-block:: json

      {
        "id": "chk_8f9a2c3b",
        "status": "verified_false",
        "confidence_score": 0.983,
        "created_at": "2026-05-25T15:30:00Z",
        "analysis": {
          "verdict": "FALSO",
          "explanation": "Este conteúdo foi desmentido oficialmente por 3 agências de checagem parceiras.",
          "sources": [
            "https://agenciaparceira.org"
          ]
        }
      }

Códigos de Retorno HTTP
----------------------

* **200 OK**: Análise processada com sucesso.
* **400 Bad Request**: Parâmetros inválidos ou ausentes.
* **401 Unauthorized**: Token de autenticação ausente ou inválido.
* **429 Too Many Requests**: Limite de requisições por minuto atingido.
