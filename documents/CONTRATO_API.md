# Contrato de API - Sistema de Rastreamento de Ônibus

Este documento define os endpoints REST para a comunicação entre os
aplicativos Android e o servidor. A API consome e produz dados
exclusivamente no formato JSON.

---

## 1. Sincronização de Telemetria (App Motorista)

Responsável por receber os lotes de coordenadas de GPS gerados pelo
dispositivo do motorista. Atende ao cenário de conexão online e
recuperação após modo offline (Store and Forward).

- **URL:** `/api/v1/telemetria/batch`
- **Método:** `POST`
- **Headers:** `Content-Type: application/json`

### Corpo da Requisição

```json
{
  "idLinha": "RU01",
  "idVeiculo": "V-204",
  "coordenadas": [
    {
      "latitude": -31.33005,
      "longitude": -54.10001,
      "timestampCaptura": "2026-05-19T14:30:00Z"
    },
    {
      "latitude": -31.33010,
      "longitude": -54.10015,
      "timestampCaptura": "2026-05-19T14:30:15Z"
    }
  ]
}
```

### Respostas Esperadas

#### `201 Created` — Sucesso

```json
{
  "status": "sucesso",
  "mensagem": "2 coordenadas processadas e salvas.",
  "timestampSincronizacao": "2026-05-19T14:31:00Z"
}
```

#### `400 Bad Request` — Erro de Validação

```json
{
  "status": "erro",
  "mensagem": "O campo 'idLinha' é obrigatório."
}
```

#### `500 Internal Server Error` — Erro Interno

```json
{
  "status": "erro",
  "mensagem": "Erro interno no servidor. Tente novamente mais tarde."
}
```

---

## 2. Consulta de Rota (App Passageiro)

Responsável por fornecer ao aplicativo do passageiro a última
localização conhecida de todos os veículos operando em uma linha
específica.

- **URL:** `/api/v1/linhas/{idLinha}/veiculos`
- **Método:** `GET`
- **Headers:** `Accept: application/json`

### Corpo da Requisição

Não se aplica — requisições `GET` não possuem corpo.

### Respostas Esperadas

#### `200 OK` — Sucesso (com ou sem ônibus ativos)

```json
{
  "idLinha": "RU01",
  "totalVeiculosAtivos": 1,
  "veiculos": [
    {
      "idVeiculo": "V-204",
      "ultimaLatitude": -31.33010,
      "ultimaLongitude": -54.10015,
      "timestampCaptura": "2026-05-19T14:30:15Z"
    }
  ]
}
```

> Quando não há ônibus ativos, `totalVeiculosAtivos` retorna `0`
> e `veiculos` retorna um array vazio `[]`.

#### `404 Not Found` — Linha Inexistente

Retornado somente quando o `idLinha` não existe no sistema.

```json
{
  "status": "erro",
  "mensagem": "Linha 'RU01' não encontrada."
}
```

#### `500 Internal Server Error` — Erro Interno

```json
{
  "status": "erro",
  "mensagem": "Erro interno no servidor. Tente novamente mais tarde."
}
```
````