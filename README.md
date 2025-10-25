
## Visão Geral do Projeto
Este projeto demonstra a implementação de um pipeline completo de Integração Contínua (CI) e Entrega Contínua (CD) para uma aplicação simples em FastAPI. Foi utiliazado GitHub Actions para automatizar o build e a atualização do manifesto GitOps, e ArgoCD para implementar o princípio GitOps no deploy em um cluster Kubernetes local (Rancher Desktop).

Requisitos e Tecnologias Utilizadas:

Aplicação: FastAPI (Python)

CI/CD: GitHub Actions

Registry: Docker Hub

GitOps: Repositório de Manifestos (Git)

Orquestração: Kubernetes (Rancher Desktop)

CD Controller: ArgoCD

## Repositórios e LinksRequisito


Linkdo repositório Git com a aplicação FastAPI + Dockerfile + GitHub Actions:

https://github.com/GuEstivalet/app-fastapi

Link do repositório com os manifests (deployment.yaml, service.yaml):

https://github.com/GuEstivalet/manifests-fastapi

## Evidências do Pipeline (CI/CD)

Evidência de Build e Push da Imagem no Docker Hub

O pipeline de CI (GitHub Actions) foi configurado para autenticar-se e enviar a imagem app-fastapi para o Docker Hub, criando o repositório automaticamente.

<p align="center"> <img src="https://github.com/user-attachments/assets/7a6a3cad-46a3-4ab6-b4c7-3d8ab9e0d9f9" alt="Confirmação do Repositório da Imagem no Docker Hub" width="600"/> </p>

Evidência de Atualização Automática dos Manifests com a Nova Tag

O GitHub Actions faz o commit da nova tag SHA da imagem diretamente no repositório manifests-fastapi (GitOps) usando a SSH_PRIVATE_KEY e o usuário github-actions[bot].

<p align="center"> <img src="https://github.com/user-attachments/assets/fc44f1dc-0ced-4c54-a142-0d515a49f85b" alt="Confirmação do sucesso: Último commit é a imagem" width="800"/> </p>

## Evidências do Deploy (ArgoCD e Kubernetes)

Captura de Tela do ArgoCD com a Aplicação Sincronizada

Após a correção da sintaxe YAML, o ArgoCD conseguiu ler o manifesto GitOps e concluiu a sincronização, movendo a aplicação para o status Healthy.

<img width="718" height="513" alt="image" src="https://github.com/user-attachments/assets/f2db7316-1f19-4ba6-aa34-50060b490bb2" />


Print do kubectl get pods com a Aplicação Rodando

A prova de que o Kubernetes conseguiu puxar a imagem do Docker Hub (graças ao ImagePullSecret corrigido) e iniciar o contêiner.

kubectl get pods

<p align="center"> <img src="https://github.com/user-attachments/assets/3bec77db-649f-4a1f-8370-a2589d3d366e" alt="Print do kubectl get pods" width="400"/> </p> Status: 1/1 e Running

