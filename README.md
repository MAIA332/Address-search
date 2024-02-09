# Address-search

Métodos de comparação de strings aplicados em forma de API, com fim de busca e formatação de endereços, baseado em uma base de dados pré definida

## Objetivo

O objetivo deste projeto é fonecer através de API uma forma de formatar endereços, seja reorganizando as informações já passadas ou consultar através de uma informação incompleta

## Como Usar

1. Clone ou faça o download do repositório para sua máquina local.
2. Instale as dependências necessárias com `pip install -r requirements.txt`.

3. Inicie a API com 
```
uvicorn api:app --reload
``` 

## Principais funções:

### 1. Transcrição
- **URL:** `/address/`
- **Método**: ```POST```
- **Descrição:** Essa rota é responsável por receber a informação incompleta ou mal formatada de endereço e retornar o endereço correto, com base no banco de dados.
- **Body**: 
```
{
  "name": "Rua Recanto do Paraíso Centro de cotia"
}
```

### Resposta:

```
Rua Recanto do Paraíso, Centro, Cotia - SP, 06727-187, Brazil
```


<p align="center">
  Feito com ❤️ por Lukas Maia
</p>


