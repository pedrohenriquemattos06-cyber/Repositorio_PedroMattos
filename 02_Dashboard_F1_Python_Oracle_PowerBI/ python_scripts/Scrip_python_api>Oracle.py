import oracledb
import requests

# Configurações do seu Banco Oracle XE
db_config = {
    "user": "estudos",
    "password": "ORACLE",
    "dsn": "localhost:1521/xe"
}

def get_points(position):
    """Retorna a pontuação oficial da F1 para os 10 primeiros"""
    pts = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
    return pts.get(position, 0)

def upload_f1_data_with_results():
    # 1. Busca as 5 primeiras corridas de 2024
    races_url = "https://api.openf1.org/v1/sessions?year=2024&session_name=Race"
    try:
        sessions = requests.get(races_url).json()[:5]
    except Exception as e:
        print(f"Erro ao conectar na API: {e}")
        return

    conn = None
    try:
        conn = oracledb.connect(**db_config)
        cursor = conn.cursor()

        # Limpa a staging para evitar duplicidade de carga
        cursor.execute("TRUNCATE TABLE STG_F1_CARGA")
        
        insert_sql = """
            INSERT INTO STG_F1_CARGA (
                STG_NOME_PILOTO, STG_SIGLA_PILOTO, STG_EQUIPE, 
                STG_CIRCUITO, STG_ANO, STG_POS_LARGADA, 
                STG_POS_CHEGADA, STG_PONTOS, STG_STATUS_FINAL
            ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
        """

        for session in sessions:
            s_key = session['session_key']
            c_name = session['circuit_short_name']
            year = str(session['year'])
            
            print(f"Processando {c_name} (Sessão: {s_key})...")

            # Busca Pilotos e Posições daquela corrida específica
            drivers = requests.get(f"https://api.openf1.org/v1/drivers?session_key={s_key}").json()
            positions = requests.get(f"https://api.openf1.org/v1/position?session_key={s_key}").json()

            rows_to_insert = []
            for d in drivers:
                d_number = d['driver_number']
                
                # Filtra os registros de posição deste piloto no GP
                p_history = [p for p in positions if p['driver_number'] == d_number]
                
                if p_history:
                    # Primeira posição registrada (Largada) e Última (Chegada)
                    start_pos = p_history[0]['position']
                    final_pos = p_history[-1]['position']
                    points = get_points(final_pos)
                else:
                    start_pos, final_pos, points = 0, 0, 0

                rows_to_insert.append((
                    d['full_name'], d['name_acronym'], d['team_name'],
                    c_name, year, str(start_pos), str(final_pos), str(points), "Finished"
                ))

            cursor.executemany(insert_sql, rows_to_insert)
            print(f"-> {len(rows_to_insert)} registros inseridos para {c_name}.")

        conn.commit()
        print("\n--- SUCESSO: DADOS COM POSIÇÕES CARREGADOS NA STAGING ---")

    except Exception as e:
        print(f"Erro no processamento: {e}")
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    upload_f1_data_with_results()
