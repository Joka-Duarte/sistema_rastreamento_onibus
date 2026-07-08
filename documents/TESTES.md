# Casos de Teste e Integração 🧪

Este documento apresenta a estratégia de validação do **Sistema de Rastreamento de Ônibus**. O objetivo desta etapa é fornecer uma **Prova de Conceito (PoC)** que ateste a viabilidade da nossa arquitetura e o cumprimento das regras de negócio solicitadas.

> 📄 **Documentação Oficial:** O detalhamento formal dos cenários, pré-condições e resultados esperados está disponível no [Documento de Casos de Teste e Integração (PDF)](./Documento_de_Casos_de_Teste_e_Integração.pdf).

---

## 🛠️ Estratégia de Validação (Prova de Conceito)

Para mitigar riscos arquiteturais antes do desenvolvimento das interfaces nativas no Android Studio, a equipe construiu um **Mock Client (Simulador Web)** integrado ao servidor Python (Flask) real. 

Isso nos permitiu homologar o Contrato da API RESTful (comunicação JSON via HTTP) e validar o processamento assíncrono do backend de forma rápida e visual.

A validação foi dividida em duas frentes estruturais:

---

## 🔌 1. Testes de Integração (TI)

Focados em provar que o "App Android" consegue conversar perfeitamente com o "Servidor Python", garantindo a resiliência dos dados trafegados na rede.

* **TI01 - Ingestão de Lote de Telemetria (Batch):** Valida a rota `POST` do backend. O simulador envia um payload JSON contendo as coordenadas GPS e o *timestamp*. O teste garante que o servidor processa o lote e retorna o status `201 Created`.
* **TI02 - Consulta de Veículos Ativos:** Valida a rota `GET` do backend. O simulador do passageiro solicita a posição dos ônibus de uma rota específica, testando a capacidade do servidor de devolver os dados estruturados (`200 OK`) ou lidar com linhas vazias (`404 Not Found`).

---

## 👤 2. Casos de Teste Funcionais (CT)

Focados na experiência do usuário e na validação das regras de negócio (Requisitos Funcionais) processadas tanto no servidor quanto no aplicativo.

* **CT01 - Defasagem Temporal no Mapa (RF03):** Valida a inteligência do *ViewModel* do passageiro. Ao simular uma perda de sinal (o ônibus para de enviar dados), o sistema calcula matematicamente a diferença de tempo e altera automaticamente o ícone do ônibus de Verde (Tempo Real) para Cinza (Atrasado).
* **CT02 - Moderação Algorítmica da Comunidade (RF04):** Valida a autolimpeza do sistema. Um aviso criado por um passageiro recebe votos simulados. Assim que a proporção de votos "Já Passou" ultrapassa o dobro de votos "Útil" (com mínimo de 5 votos), o servidor oculta o alerta da interface sem intervenção humana.
* **CT03 - Proteção de Emissão de Alerta Oficial (RF04):** Valida a hierarquia de usuários. O motorista utiliza uma rota restrita para enviar um alerta de "Problema Mecânico". O sistema exibe o aviso com destaque visual (Alerta Oficial) e suprime os botões de votação, impedindo que a comunidade oculte informações operacionais.

---
*Testes desenvolvidos para a disciplina de Engenharia de Software 2026/1.*