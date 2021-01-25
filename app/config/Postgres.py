from sqlalchemy import create_engine,Table,MetaData,text,select
from .PostgresTables import PgTableList
from .log import log
from .Constants import CONSTANT_OBJ
import sys

"""
this module creates a class to connect to postgres.
postgres specifications (host address, port, user, password , ... come from env variables which in dev env is in .env file
also it creates a method to insert given values to table(s) which we defined in PostgresTables.py file
"""


class PG_Connection :
    def __init__(self,PostgresUser,PostgresPassword,PostgresHost,PostgresPort,PostgresDB):
        try:
            if (CONSTANT_OBJ.run_state=="DEV"):
                log.msg("Connecting to postgres database ...")
            self.pg_str = f"postgresql+psycopg2://{PostgresUser}:{PostgresPassword}@{PostgresHost}:{PostgresPort}/{PostgresDB}"
            self.pg_engine = create_engine(self.pg_str)
            self.pg_con = self.pg_engine.connect()
            self.pg_Meta = MetaData()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            log.msg(f"Error in connecting to postgres in line no {exc_tb.tb_lineno} \n {e}")
            exit(1)

    def insert(self,CheckTime,Returncode,ReturnTime,RegexResult,APIAddress):
        tbl = None # avoid not defined variable in exception area
        try:
            # converting dictionary to verbal message to store in database
            WordsFind = "Regex Check = {" + (", ".join(":".join((k,v)) for k,v in RegexResult.items())) + "}"
            for tbl in PgTableList: # trying to insert to all defined tables
                sql_str = f"insert into {tbl}(created,apiaddress,returncode,keywords,responsetime) values (\'{CheckTime}\',\'{APIAddress}\',{Returncode},\'{WordsFind}\',{ReturnTime})"
                log.msg("executing : " + sql_str)
                self.pg_con.execute(sql_str)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            log.msg(f"Error in inserting in table : {tbl} to postgres in line no {exc_tb.tb_lineno} \n {e}")
            exit(1)
