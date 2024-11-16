# AUTOMAÇÃO ROBÓTICA DE PROCESSOS (RPA): Gerenciamento e Monitoramento de Automações

**Autor:** Fernando Emerson Vale dos Santos
**Data:** 11/2024
**Local:** Rio de Janeiro

## Resumo
Este repositório contém o código-fonte do projeto de TCC que visa desenvolver uma **plataforma de gerenciamento, monitoramento e controle de robôs de RPA (Robotic Process Automation)**. O objetivo principal é centralizar a gestão dos robôs, permitindo o monitoramento em tempo real, visualização de logs e controle das execuções.

> **Nota:** Esta plataforma foi projetada inicialmente para atender a projetos ou scripts de automação desenvolvidos em **Python**.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

## Visão Geral

Com o crescimento da utilização de RPA nas empresas, a necessidade de uma plataforma centralizada para o gerenciamento dos robôs tornou-se evidente. Este projeto visa solucionar problemas comuns, como a dificuldade de monitorar múltiplos robôs em operação e a falta de controle centralizado, oferecendo uma solução específica para scripts Python.

## Funcionalidades

A plataforma oferece as seguintes funcionalidades principais:

- Dashboard centralizado para visualização do status das automações.
- Monitoramento em tempo real dos robôs.
- Gerenciamento de automações, incluindo edição, remoção e criação.
- Upload de scripts Python para configuração de automações.
- Visualização de logs de execução e histórico.
- Execução manual dos robôs.
- Visualização dos workers disponíveis para execução.

## Tecnologias Utilizadas
- **Python 3.11:** Linguagem de programação para desenvolvimento dos robôs e API.
- **FastAPI:** Framework para criação da API REST.
- **Angular 18:** Front-end para interface de usuário.
- **Tailwind CSS:** Framework CSS para estilização.
- **Celery:** Gerenciamento de tarefas assíncronas.
- **Redis:** Sistema de mensageria (broker) para o Celery.
- **Docker:** Plataforma de contêinerização para implantação.
- **MySQL:** Banco de dados relacional.

### Dependências Necessárias
- Docker e Docker Compose instalados.

### Comando para execução
```bash
docker-compose up --build
