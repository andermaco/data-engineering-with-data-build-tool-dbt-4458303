import duckdb
import pandas as pd


def connect_to_db(database_path: str):
    conn = duckdb.connect(database_path)
    return conn


def run_query(conn, query: str):
    return conn.sql(query)


def init_db(db_path: str):
    sql_query_import_1 = '''
    CREATE OR REPLACE TABLE parking_violation_codes AS
    SELECT *
    FROM read_csv_auto(
    'data/dof_parking_violation_codes.csv',
    normalize_names=True
    )
    '''

    sql_query_import_2 = '''
    CREATE OR REPLACE TABLE parking_violations_2023 AS
    SELECT *
    FROM read_csv_auto(
    'data/parking_violations_issued_fiscal_year_2023_sample.csv',
    normalize_names=True
    )
    '''

    with duckdb.connect(db_path) as con:
        con.sql(sql_query_import_1)
        con.sql(sql_query_import_2)


if __name__ == '__main__':

    # init_db("data/nyc_parking_violations.db")

    init_db("data/prod_nyc_parking_violations.db")

    # conn = connect_to_db("data/nyc_parking_violations.db")
    # print(run_query(conn, "SELECT COUNT(*) FROM ref_model"))
