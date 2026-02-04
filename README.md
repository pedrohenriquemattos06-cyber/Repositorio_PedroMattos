🚗 Sistema de Gestão de Manutenção de Frota (PL/SQL & Crystal Reports)
Este projeto demonstra a implementação de um back-end robusto em Oracle SQL/PL/SQL integrado a um relatório profissional em Crystal Reports. O sistema automatiza o controle de odômetro, alertas de manutenção preventiva e análise de custos de uma frota de veículos.

🛠️ Tecnologias Utilizadas
Banco de Dados: Oracle Database (PL/SQL).

Editor de Código: VS Code com extensões Oracle.

Relatórios: SAP Crystal Reports.

Conceitos Aplicados: Triggers, Procedures, Views, Joins complexos e Formatação Condicional.

📊 Estrutura do Projeto
1. Camada de Banco de Dados (DML/DDL)
O banco foi modelado para garantir integridade referencial e performance.

Procedures: Implementação de lógica para registro de manutenções com atualização automática de odômetro e validação de consistência (não permite KM retroativa).

Triggers: Automação que monitora a quilometragem atual e gera alertas preventivos sempre que um veículo atinge o limite do plano de manutenção (ex: a cada 10.000km).

Views: Camada de abstração criada especificamente para consumo de BI/Relatórios, realizando cálculos de "KMs rodados desde a última revisão" e classificação de prioridade em tempo real.

2. Camada de Apresentação (Crystal Reports)
Relatório desenvolvido com foco em suporte a decisões gerenciais, simulando módulos de ERPs de mercado como o Mega ERP.

Destaques Visuais: Formatação condicional de cores (Semáforo) para identificar veículos críticos.

Lógica de Negócio: Tratamento de status para veículos "VENDIDOS/BAIXADOS" e totalização de custos.

Layout: Cabeçalho profissional com banner, logotipo e campos especiais de data/hora de emissão.

🚀 Como Executar
Execute os scripts SQL contidos na pasta /scripts em seu ambiente Oracle.

Configure a conexão OLE DB/ODBC no Crystal Reports apontando para a View VW_DASHBOARD_FROTA.

Abra o arquivo .rpt para visualizar o dashboard formatado.

Exemplo de Lógica PL/SQL (Trigger de Alerta)
SQL
-- Trecho simplificado da lógica de monitoramento
IF :NEW.KM_ATUAL >= (v_ultima_km_manut + v_intervalo) THEN
    INSERT INTO TB_FROTA_ALERTAS (ID_VEICULO, MENSAGEM)
    VALUES (:NEW.ID_VEICULO, 'Necessário realizar manutenção preventiva.');
END IF;
💡 Próximos Passos
Pretendo expandir este projeto integrando uma interface em Python para facilitar o cadastro de veículos pelo usuário final, aproveitando o interesse em automação para o setor automotivo.
