# Descrição da Arquitetura do Sistema de Rastreamento de Ônibus

Este documento descreve as decisões arquiteturais, estruturais e tecnológicas do Sistema de Rastreamento de Ônibus de Bagé/RS. O objetivo é garantir um sistema resiliente, escalável e de fácil manutenção pela equipe.

---

## 1. Padrões Escolhidos e Stack Tecnológica

Para atender aos requisitos não funcionais de resiliência e performance, o sistema adota a seguinte stack tecnológica base:

* **Frontend (Mobile):** Desenvolvimento Nativo Android em **Java**.
* **Arquitetura Frontend:** Padrão **MVVM** (Model-View-ViewModel) para separação de responsabilidades.
* **Persistência Local (Offline):** **SQLite** nativo do Android.
* **Comunicação de Rede:** Biblioteca **Retrofit** (para requisições HTTP REST).
* **Backend (Servidor):** **Python** utilizando o microframework **Flask**.
* **Macroarquitetura:** **Cliente-Servidor**, operando através de uma API RESTful utilizando o formato JSON.

---

## 2. Macroarquitetura: Diagrama de Implantação

Este diagrama ilustra a visão geral do sistema, detalhando onde os componentes são executados fisicamente (dispositivos vs. nuvem) e como se comunicam através da rede.

```mermaid
flowchart TD
    %% Nós de Rede
    subgraph Dispositivos ["Dispositivos Móveis (Clientes Android)"]
        M["App Motorista\n(Produtor de Dados)"]
        P["App Passageiro\n(Consumidor de Dados)"]
    end

    subgraph Nuvem ["Servidor Central (Cloud)"]
        API["Backend REST API\n(Python/Flask)"]
        BD[("Banco de Dados\nRelacional")]
    end

    %% Conexões
    M -- "POST (JSON via HTTPS)" --> API
    P -- "GET (JSON via HTTPS)" --> API
    API <--> BD
```

---

## 3. Microarquitetura Frontend (Android): Padrão MVVM

Este diagrama detalha a organização interna das camadas lógicas do aplicativo Android (/ui, /viewmodel, /data), garantindo que a interface gráfica fique isolada das operações de banco de dados e rede.

```mermaid
flowchart TD
    %% Camadas do MVVM
    subgraph View ["View (/ui)"]
        UI["Telas e XML\n(Activity/Fragment)"]
    end

    subgraph ViewModel ["ViewModel (/viewmodel)"]
        VM["Lógica de Apresentação\n(Ex: Calcula Cor do Ícone)"]
    end

    subgraph Model ["Model (/data e /network)"]
        Repo["SyncManager\n(Repositório Central)"]
        Retrofit["API Externa\n(Retrofit)"]
        SQLite[("Banco Local\n(SQLite)")]
    end

    %% Fluxo de Dados Unidirecional
    UI -- "Observa mudanças" --> VM
    VM -- "Solicita Rota" --> Repo
    Repo -- "Requisita API" --> Retrofit
    Repo -- "Salva/Lê Offline" --> SQLite
```

---

## 4. Microarquitetura Backend: Padrão em Camadas

Este diagrama demonstra o fluxo de processamento de uma requisição no servidor Python. A separação garante que a validação, as regras de negócio e as consultas SQL não se misturem no mesmo arquivo.

```mermaid
flowchart TD
    %% Camadas do Servidor
    Req(("Requisição\nAndroid"))
    
    subgraph Backend ["Servidor Flask"]
        direction TB
        Rotas["1. Rotas (Controllers)\n(Recebe JSON e valida headers)"]
        Service["2. Serviços (Business Logic)\n(Aplica regras de negócio)"]
        Repo["3. Repositório (Data Access)\n(Escreve queries SQL)"]
    end

    BD[("Banco de Dados\nPrincipal")]

    %% Fluxo
    Req --> Rotas
    Rotas --> Service
    Service --> Repo
    Repo <--> BD
```