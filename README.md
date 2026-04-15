# Sistema de Rastreamento de Ônibus 🚌

Este projeto foi desenvolvido como parte da disciplina de **Engenharia de Software 2026/1** na **Universidade Federal do Pampa (Unipampa)**[cite: 3]. O objetivo é mitigar a falta de informações precisas sobre a localização do transporte público municipal em Bagé/RS[cite: 6].

## 📋 Sobre o Projeto

O sistema consiste em uma solução de rastreamento híbrida que utiliza os sensores de GPS dos dispositivos móveis de motoristas e cobradores para fornecer dados de localização em tempo real aos passageiros[cite: 10, 11]. O projeto foca em resiliência de rede e transparência na qualidade dos dados para o usuário final[cite: 19].

## 📂 Estrutura do Repositório

O repositório está organizado nas seguintes pastas:

* **`/assets`**: Identidade visual, ícones do sistema e capturas de tela das interfaces.
* **`/backend`**: Código-fonte do servidor central responsável pelo processamento das coordenadas e gerenciamento dos avisos[cite: 11].
* **`/diagrams`**: Documentação visual em UML, incluindo Diagramas de Casos de Uso, Classes e Sequência.
* **`/documents`**: Documentação técnica, incluindo a [Especificação de Requisitos](./documents/Documento_de_Especificação_de_Requisitos.pdf) baseada em Sommerville (2019)[cite: 1, 5].
* **`/software`**:
    * `android-passenger/`: Aplicativo Android para consulta de localização e avisos[cite: 9].
    * `android-driver/`: Aplicativo Android para transmissão de GPS e sincronização offline[cite: 10].

## 🚀 Funcionalidades Principais

* **Transmissão de Localização (RF01)**: Envio automático de coordenadas a cada 15 segundos, com suporte a armazenamento local e sincronização automática em caso de queda de internet[cite: 34, 35].
* **Visualização Dinâmica (RF02)**: Exibição dos ônibus no mapa com lógica de cores (ícone colorido para dados recentes e ícone cinza para dados com mais de 2 minutos)[cite: 46, 47].
* **Avisos da Comunidade (RF03)**: Sistema colaborativo para reporte de problemas nas linhas, com moderação automática baseada em votos de relevância[cite: 55, 63].

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Java (Android Nativo)[cite: 74].
* **Interface**: XML Layouts[cite: 74].
* **Gerenciador de Dependências**: Gradle[cite: 74].
* **Compatibilidade**: Android 8.0 ou superior[cite: 67].

## 👥 Equipe

* João Oliveira Duarte [cite: 2]
* Lorhan Santos de Lima [cite: 2]
* Raul Etcheverry Reis [cite: 2]
* Vanessa Manzke Otte [cite: 2]

## 📚 Referências

* SOMMERVILLE, I. **Engenharia de Software**. 10. ed. São Paulo: Pearson, 2019[cite: 86].