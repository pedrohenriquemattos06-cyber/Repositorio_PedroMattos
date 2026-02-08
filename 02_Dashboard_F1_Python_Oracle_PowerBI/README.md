<img width="1322" height="738" alt="dashboard_f1_pagina1" src="https://github.com/user-attachments/assets/886fa842-9031-434b-b091-cdabf6a67dff" />

🏎️ F1 Data Analytics Dashboard: Python + Oracle + Power BI
Este projeto automatiza a extração de dados da API OpenF1 e transforma dados brutos em insights de performance através de um dashboard interativo.

🛠️ Tecnologias Utilizadas
Linguagem: Python (Extração e Integração via requests e oracledb).

Banco de Dados: Oracle XE 21c (Modelagem, Views e Procedures PL/SQL).

Visualização: Power BI (KPIs de liderança e análise de performance).

Metodologia: ITIL v4 (Processos de entrega de serviço de dados confiáveis).

📂 Estrutura do Repositório

/python_scripts: Scripts de integração que realizam o merge entre os endpoints de drivers e positions.

/sql_scripts: Scripts de criação de tabelas (STG e Produção), Procedures de carga e Views otimizadas para o Power BI.

/dashboard: Arquivo .pbit (template) do dashboard configurado .

🚀 Funcionalidades Principais
Carga Automatizada: Script Python que busca dados dos 5 primeiros GPs da temporada.

Medidas DAX Personalizadas: Cálculo de "Ganhos de Posição" (Saldo de Ultrapassagens).

Identidade Visual: Dashboard personalizado com as cores hexadecimais oficiais das equipes da F1.

-------------------------------------------------------------------------------------------------------------------------------------------------------

Para utilizar basta Rodar a integração python e a proc do Oracle para abastecer as tabelas, sendo os dados exibidos no BI
