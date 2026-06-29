# Modelagem e Diagramas do Sistema

Este documento apresenta a modelagem visual do **Sistema de Rastreamento de Ônibus**, detalhando como as regras de negócio e as funcionalidades solicitadas pelos usuários se traduzem na arquitetura do software.

> 📄 **Documentação Oficial:** Este arquivo é um apoio visual. Para conferir a elicitação detalhada, regras algorítmicas, métricas e a validação teórica completa, consulte o [Documento de Especificação de Requisitos Oficial](../documents/Documento_de_Especificação_de_Requisitos.pdf).

---

## 1. Diagrama de Casos de Uso

![Diagrama de Casos de Uso](./UML/1.%20Diagrama%20de%20Casos%20de%20Uso.png)
*(Se o nome do seu arquivo de imagem for diferente, ajuste o link acima)*

**O que este diagrama significa:**
Ele ilustra a visão macro das interações entre os atores (usuários) e o sistema, mapeando diretamente os Requisitos de Usuário (RU):
* **Motorista/Cobrador (Produtor):** Interage com o sistema exclusivamente para "Selecionar a Linha" e "Iniciar a Rota" (RU02). O objetivo é que essa ação seja feita com o veículo parado, sem necessidade de interação contínua.
* **Passageiro (Consumidor):** Interage com o sistema para "Visualizar Ônibus no Mapa" (RU01) e para participar da moderação de "Avisos da Comunidade" (RU04), avaliando alertas como úteis ou desatualizados.
* **Sistema (Backend):** Atua de forma invisível processando as regras de defasagem de tempo e ocultando avisos negativados pela comunidade.

---

## 2. Diagrama de Classes (Domínio)

![Diagrama de Classes](./UML/2.%20Diagrama%20de%20Classes.png)
*(Se o nome do seu arquivo de imagem for diferente, ajuste o link acima)*

**O que este diagrama significa:**
Ele representa o "esqueleto" do banco de dados e as entidades principais que transitam no código (Requisitos Funcionais):
* **Linha e Veículo:** Entidades centrais que conectam as informações. Um veículo está sempre associado a uma linha durante a operação.
* **Coordenada:** Representa a entidade gerada a cada 15 segundos (RF02). É crucial observar o atributo `timestampCaptura`, que é a chave para o aplicativo do passageiro calcular a defasagem temporal (RF03) e definir a cor do ícone no mapa.
* **Aviso:** Armazena os reportes da comunidade. Contém os atributos de contagem de votos (`votosUteis` e `votosDesatualizados`) necessários para o gatilho automático de ocultação.

---

## 3. Diagrama de Sequência

![Diagrama de Sequência](./UML/3.%20Diagrama%20de%20Sequência.png)
*(Se o nome do seu arquivo de imagem for diferente, ajuste o link acima)*

**O que este diagrama significa:**
Mostra a linha do tempo e a comunicação entre os aplicativos e o servidor. Fica evidente a separação de responsabilidades (Macroarquitetura):
1. O dispositivo do Motorista envia blocos JSON via `POST` contendo as coordenadas.
2. O Servidor valida, armazena no banco de dados e retorna o status.
3. De forma totalmente independente, o dispositivo do Passageiro faz requisições `GET` ao Servidor solicitando as últimas posições conhecidas.
4. O Servidor apenas devolve os dados brutos; a lógica de renderização e cálculo de atraso ocorre no dispositivo do Passageiro.

---
*Diagramas gerados utilizando padrões UML para o Trabalho Prático de Engenharia de Software.*