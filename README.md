# Sistema de Rastreamento de Ônibus 🚌

Este projeto foi desenvolvido como parte da disciplina de **Engenharia de Software 2026/1** na **Universidade Federal do Pampa (Unipampa)**. O objetivo é mitigar a falta de informações precisas sobre a localização do transporte público municipal em Bagé/RS.

## 📋 Sobre o Projeto

O sistema consiste em uma solução de rastreamento híbrida que utiliza os sensores de GPS dos dispositivos móveis de motoristas e cobradores para fornecer dados de localização em tempo real aos passageiros. O projeto foca em resiliência de rede e transparência na qualidade dos dados para o usuário final.

## 📂 Estrutura do Repositório e Documentação Oficial

O repositório está organizado para separar claramente o código-fonte da documentação e arquitetura. Clique nos links abaixo para acessar os documentos gerados pela equipe:

* **`/assets`**: Identidade visual, ícones do sistema e capturas de tela das interfaces.
* **`/backend`**: Código-fonte do servidor central (Python/Flask) responsável pelo processamento de coordenadas, moderação algorítmica de avisos e o **Simulador Web (Mock Client)** utilizado para a Prova de Conceito (PoC).
* **`/diagrams`**: Documentação visual em UML (Casos de Uso, Classes, Sequência) e representações da Macro e Microarquitetura do sistema.
* **`/documents`**: Documentação técnica e contratual do projeto:
  * 📄 [Proposta Original do Trabalho Prático](./documents/Trabalho_Prático_ES_2026-1.pdf)
  * 📄 [Documento de Especificação de Requisitos](./documents/Documento_de_Especificação_de_Requisitos.pdf)
  * 📝 [Resumo de Requisitos (MD)](./documents/REQUISITOS.md)
  * 📄 [Documento de Arquitetura de Software (DAS)](./documents/Documento_de_Arquiteturas.pdf)
  * 📝 [Especificação da Arquitetura (MD)](./documents/ARQUITETURA.md)
  * 📝 [Diagramas do Sistema (MD)](./documents/DIAGRAMAS.md)
  * 📝 [Contrato de API REST (MD)](./documents/CONTRATO_API.md)
  * 📄 [Documento de Casos de Teste e Integração](./documents/Documento_de_Casos_de_Teste_e_Integracao.pdf)
  * 📝 [Plano de Validação e Testes (MD)](./documents/TESTES.md)
  
* **`/frontend`**: Código-fonte do aplicativo Android nativo, incluindo a lógica de renderização do mapa, cálculo de defasagem temporal e interface de avisos da comunidade.

## 🚀 Funcionalidades Principais

* **Transmissão de Localização Resiliente**: Envio automático de coordenadas do motorista a cada 15 segundos. O aplicativo utiliza o padrão *Store and Forward*, armazenando dados localmente em caso de queda de internet e sincronizando automaticamente no retorno do sinal.
* **Visualização Dinâmica no Mapa**: Exibição dos ônibus no mapa com lógica de defasagem temporal (ícone colorido para posições em tempo real e ícone cinza para defasagens maiores que 2 minutos).
* **Avisos da Comunidade Algorítmicos**: Sistema colaborativo para reporte de problemas nas linhas, utilizando moderação automática baseada na proporção de votos de relevância ("Útil" vs "Desatualizado") e proteção hierárquica para Alertas Oficiais da operação.

## 🛠️ Tecnologias e Arquitetura

O sistema opera sob o padrão **Cliente-Servidor**, utilizando a seguinte stack:

* **Frontend Mobile**: Java (Android Nativo) estruturado no padrão de arquitetura **MVVM** (Model-View-ViewModel).
* **Persistência Local e Rede**: SQLite nativo (offline) e biblioteca Retrofit para requisições HTTPS.
* **Backend (Servidor)**: Python com o microframework Flask, operando em Arquitetura em Camadas.
* **Integração**: API RESTful utilizando formato de dados JSON.
* **Compatibilidade**: Android 8.0 ou superior.

## 👥 Equipe

* João Oliveira Duarte
* Lorhan Santos de Lima
* Raul Etcheverry Reis
* Vanessa Manzke Otte

## 📚 Referências

* SOMMERVILLE, I. **Engenharia de Software**. 10. ed. São Paulo: Pearson, 2019.