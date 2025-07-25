pip install pandas sqlalchemy
pip install psycopg2-binary
pip install pymysql
pip install pyodbc

from sqlalchemy import create_engine
import pandas as pd

    db_connection_str = 'sqlite:///your_database.db'

    engine = create_engine(db_connection_str)
    try:
        df = pd.read_sql_table('your_table_name', con=engine)
        print("DataFrame loaded successfully:")
        print(df.head())
    except Exception as e:
        print(f"Error loading table: {e}")
    finally:
        engine.dispose()


