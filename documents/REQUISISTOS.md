# Especificação de Requisitos 📋

Este documento apresenta o resumo dos requisitos elicitados e analisados para o **Sistema de Rastreamento de Ônibus**. A especificação completa, contendo justificativas, validações e detalhamento técnico com base na metodologia de Sommerville (2019), encontra-se no documento oficial em anexo.

> 📄 **Acesse o documento completo:** [Documento_de_Especificação_de_Requisitos.pdf](./Documento_de_Especificação_de_Requisitos.pdf)

---

## 🎯 Escopo do Sistema

O objetivo principal do software é resolver a incerteza dos passageiros quanto aos horários do transporte público municipal, oferecendo uma solução de rastreamento em tempo real que seja resiliente a falhas de rede (zonas de sombra) e que não drene a bateria dos dispositivos móveis dos trabalhadores do transporte.

### Atores Principais
* **Passageiro (Consumidor):** Usuário do transporte público que necessita saber a localização exata do ônibus e as condições da linha.
* **Motorista/Cobrador (Produtor):** Trabalhador responsável por operar o aplicativo em segundo plano para transmitir a localização do veículo.

---

## 👤 Resumo dos Requisitos de Usuário (RU)

Os requisitos de usuário definem as necessidades em linguagem natural a partir da perspectiva de quem utiliza o sistema:

* **RU01 - Previsibilidade:** O passageiro precisa ver os ônibus de uma linha específica no mapa para planejar sua ida ao ponto.
* **RU02 - Operação sem Interação:** O motorista precisa de um sistema "Ligar e Esquecer" para iniciar a transmissão sem desviar a atenção do trânsito.
* **RU03 - Resiliência:** O sistema deve lidar de forma transparente com a perda de sinal de internet, informando aos passageiros sobre a defasagem dos dados.
* **RU04 - Colaboração Assíncrona:** A comunidade deve poder alertar sobre problemas na linha (ex: pneu furado, atrasos) de forma objetiva, sem fóruns de discussão.

---

## ⚙️ Resumo dos Requisitos Funcionais de Sistema (RF)

Traduzem as necessidades dos usuários em funcionalidades técnicas implementáveis na arquitetura:

* **RF01 - Seleção de Itinerário:** Associação obrigatória do dispositivo transmissor (Motorista) a uma linha específica antes do início da rota.
* **RF02 - Transmissão de Localização (Store and Forward):** Captura de coordenadas GPS acompanhadas de carimbo de hora (*Timestamp*) a cada 15 segundos. Em caso de perda de conexão, os dados são armazenados localmente (SQLite) e enviados em lote quando o sinal for restabelecido.
* **RF03 - Visualização e Defasagem:** O aplicativo do passageiro calcula a diferença entre o *Timestamp* da captura e a hora atual. Dados com defasagem $\le$ 2 minutos recebem ícones coloridos (Tempo Real); dados com defasagem $>$ 2 minutos recebem ícones cinza (Atraso).
* **RF04 - Moderação Algorítmica de Avisos:** Sistema de criação de alertas fixos e votação ("Útil" vs. "Desatualizado"). O backend oculta automaticamente alertas cuja contagem de votos negativos seja superior ao dobro de votos positivos (com um mínimo de 5 votos totais).

---

## 🛡️ Principais Requisitos Não Funcionais (RNF)

* **Eficiência (Bateria):** O consumo do aplicativo transmissor não deve ultrapassar 8\% de bateria por hora de uso em segundo plano.
* **Confiabilidade:** O rastreamento deve permanecer ativo mesmo com o dispositivo do motorista bloqueado.
* **Segurança:** Toda a transmissão de telemetria e consulta de dados ocorrerá exclusivamente sob protocolo criptografado (HTTPS).
* **Portabilidade:** Os aplicativos móveis devem ser compatíveis, no mínimo, com a versão Android 8.0, visando atender a dispositivos de entrada.