# Sistema de Rastreamento de Ônibus 🚌

Este projeto foi desenvolvido como parte da disciplina de **Engenharia de Software 2026/1** na **Universidade Federal do Pampa (Unipampa)**. O objetivo é mitigar a falta de informações precisas sobre a localização do transporte público municipal em Bagé/RS.

## 📋 Sobre o Projeto

O sistema consiste em uma solução de rastreamento híbrida que utiliza os sensores de GPS dos dispositivos móveis de motoristas e cobradores para fornecer dados de localização em tempo real aos passageiros. O projeto foca em resiliência de rede e transparência na qualidade dos dados para o usuário final.

## 📂 Estrutura do Repositório

O repositório está organizado nas seguintes pastas:

* **`/assets`**: Identidade visual, ícones do sistema e capturas de tela das interfaces.
* **`/backend`**: Código-fonte do servidor central responsável pelo processamento das coordenadas e gerenciamento dos avisos.
* **`/diagrams`**: Documentação visual em UML, incluindo Diagramas de Casos de Uso, Classes e Sequência.
* **`/documents`**: Documentação técnica, incluindo a [Especificação de Requisitos](./documents/Documento_de_Especificação_de_Requisitos.pdf) baseada em Sommerville (2019).
* **`/software`**:
    * `android-passenger/`: Aplicativo Android para consulta de localização e avisos.
    * `android-driver/`: Aplicativo Android para transmissão de GPS e sincronização offline.

## 🚀 Funcionalidades Principais

* **Transmissão de Localização (RF01)**: Envio automático de coordenadas a cada 15 segundos, com suporte a armazenamento local e sincronização automática em caso de queda de internet.
* **Visualização Dinâmica (RF02)**: Exibição dos ônibus no mapa com lógica de cores (ícone colorido para dados recentes e ícone cinza para dados com mais de 2 minutos).
* **Avisos da Comunidade (RF03)**: Sistema colaborativo para reporte de problemas nas linhas, com moderação automática baseada em votos de relevância.

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Java (Android Nativo).
* **Interface**: XML Layouts.
* **Gerenciador de Dependências**: Gradle.
* **Compatibilidade**: Android 8.0 ou superior.

## 👥 Equipe

* João Oliveira Duarte
* Lorhan Santos de Lima
* Raul Etcheverry Reis
* Vanessa Manzke Otte

## 📚 Referências

* SOMMERVILLE, I. **Engenharia de Software**. 10. ed. São Paulo: Pearson, 2019.