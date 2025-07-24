pip install pandas sqlalchemy
    # Install the specific database driver, e.g., for PostgreSQL:
pip install psycopg2-binary
    # Or for MySQL:
pip install pymysql
    # Or for SQL Server:
pip install pyodbc

from sqlalchemy import create_engine
import pandas as pd

    # Replace with your database connection details
    # Example for PostgreSQL:
    # db_connection_str = 'postgresql+psycopg2://user:password@host:port/database_name'
    # Example for MySQL:
    # db_connection_str = 'mysql+pymysql://user:password@host:port/database_name'
    # Example for SQLite (file-based):
    db_connection_str = 'sqlite:///your_database.db'

    engine = create_engine(db_connection_str)
    try:
        df = pd.read_sql_table('your_table_name', con=engine)
        print("DataFrame loaded successfully:")
        print(df.head())
    except Exception as e:
        print(f"Error loading table: {e}")
    finally:
        # Close the connection if necessary (though SQLAlchemy handles connection pooling)
        engine.dispose()


