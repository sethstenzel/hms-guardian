import sqlite3
import pandas as pd

class Databases:
    def __init__(self):
        pass

    @staticmethod
    def initialize_applications_db(db_path: str):
        """
        Creates the SQLite database and 'applications' table if they do not exist.
        
        Parameters:
            db_path (str): Path to the SQLite database file.
        """
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            application_name TEXT,
            application_daily INT,
            application_daily_max INT,
            application_weekly INT,
            application_weekly_max INT,
            application_time_blocks TEXT,
            application_message TEXT
        )
        """)

        conn.commit()
        conn.close()


    def read_applications_db(self, db_path:str = "applications_db.sqlite") -> pd.DataFrame:
        """
        Opens an SQLite database and reads the 'application_name', 'application_daily', 
        'application_weekly', 'application_time_blocks', and 'application_message' columns 
        from the 'applications' table.
        
        If the database does not exist, it is created with the required table structure.
        
        Parameters:
            db_path (str): Path to the SQLite database file.
        
        Returns:
            pd.DataFrame: DataFrame containing the selected columns as strings.
        """
        try:
            # Ensure database and table exist
            self.initialize_applications_db(db_path)
            
            # Connect to the SQLite database
            conn = sqlite3.connect(db_path)
            
            # Define the query
            query = """
            SELECT application_name, 
                application_name,
                application_daily,
                application_daily_max,
                application_weekly,
                application_weekly_max,
                application_time_blocks,
                application_message
            FROM applications
            """
            
            df = pd.read_sql_query(query, conn)
            
            return df
        except Exception as e:
            print(f"Error reading database: {e}")
            return pd.DataFrame()
        finally:
            conn.close()