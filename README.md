# **Data4Food**

> Uma plataforma de inteligência artificial projetada para prever e mitigar crises de insegurança alimentar em escala global.

## 📖 **Sobre o Projeto**

O **Data4Food** é uma solução tecnológica desenvolvida para o desafio **Global Solutions da FIAP**. O projeto visa combater a falta de sistemas integrados de alerta precoce sobre riscos de insegurança alimentar, um dos maiores desafios globais da atualidade.

## 🌐 **O Desafio**

Milhões de pessoas vivem em situação de fome ou insegurança alimentar severa. De acordo com o relatório "O Estado da Segurança Alimentar e Nutrição no Mundo 2023" da FAO, mais de 735 milhões de pessoas no mundo enfrentam fome crônica. Esta crise é agravada por uma combinação de fatores como eventos climáticos extremos, conflitos e choques econômicos. Um exemplo recente foi a seca no Corno da África entre 2021 e 2023, que deixou mais de 23 milhões de pessoas em situação de insegurança alimentar.

## 💡 **Nossa Solução**

Propomos o desenvolvimento da plataforma **Data4Food**, um sistema que integra e analisa dados climáticos, econômicos e sociais para prever riscos de crise alimentar e emitir alertas antecipados. A plataforma utiliza inteligência artificial para analisar dados sobre produção agrícola e clima, gerando alertas em tempo real.

O objetivo é oferecer uma ferramenta para que governos, ONGs e produtores rurais atuem rapidamente, transformando dados em ações para reduzir a fome e aumentar a resiliência.

### 🌱 **Objetivos de Desenvolvimento Sustentável (ODS)**

A solução está diretamente alinhada aos Objetivos de Desenvolvimento Sustentável da ONU, especialmente o **ODS 2 (Fome Zero e Agricultura Sustentável)** e o **ODS 13 (Ação Contra a Mudança Global do Clima)**.

## ✨ **Funcionalidades Principais**

* **Previsão de Crises:** Antecipa crises alimentares antes que se agravem.
* **Dashboard Interativo:** Apresenta análises, indicadores e gráficos interativos em React ou Vue.js.
* **Mapas Interativos:** Visualização geoespacial de dados com Leaflet ou Mapbox.
* **Alertas Automatizados:** Notificam os usuários sobre eventos críticos, como riscos de desabastecimento ou alterações climáticas severas.
* **Relatórios Automatizados:** Gera documentos em PDF ou Excel para análises periódicas.

## 🏗️ **Arquitetura e Tecnologias**

A solução é construída sobre uma arquitetura de nuvem moderna e escalável.

### **Fontes de Dados**

* **NASA/NOAA:** Dados meteorológicos e climáticos.
* **INMET/IBGE/ONU:** Indicadores socioeconômicos e ambientais.
* **CEASA/FAO Price Index:** Dados sobre preços e oferta de alimentos.

### **Tecnologias Utilizadas**

```
Processamento e Armazenamento:
  - ETL:          Apache Airflow, Spark
  - Data Lake:    AWS S3 ou GCS
  - Banco Fixo:   PostgreSQL + PostGIS
  - Banco NoSQL:  MongoDB

Inteligência Artificial:
  - Frameworks:   TensorFlow, Scikit-learn
  - Linguagem:    Python

Backend e API:
  - API:          REST API
  - Alertas:      Webhooks, Twilio, Firebase Messaging

Infraestrutura e DevOps:
  - Cloud:        AWS
  - Containers:   Docker
```

## 👥 **Equipe**

* **Gustavo Sousa** - RM 566473
* **Vinicios Silva** - RM 564534
* **Vinicius Perez** - RM 563324

## 📄 **Licença**

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
