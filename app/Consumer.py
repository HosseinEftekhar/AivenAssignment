"""
this module is repeating code to run on consumer pod or container or VM.
it gets messages from kafka topic and insert it into postgres
"""
from config.Constants import CONSTANT_OBJ
from config.log import log
from config.Postgres import PG_Connection
from config.Connection import create_consumer
import sys
if __name__ == "__main__":
    ### consumer of topic ####
    try:
        consumer = create_consumer(CONSTANT_OBJ.KafkaTopic, CONSTANT_OBJ.KafkaHost, CONSTANT_OBJ.KafkaPort,
                               CONSTANT_OBJ.KafkaGroupID, CONSTANT_OBJ.KafkaPartitionID)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.msg(f"Error in creating consumer obj in line no {exc_tb.tb_lineno} \n {e}")
        exit(1)
    ### instance of postgres connection #########
    try:
        pg_con = PG_Connection(CONSTANT_OBJ.PostgresUser, CONSTANT_OBJ.PostgresPassword, CONSTANT_OBJ.PostgresHost
                           , CONSTANT_OBJ.PostgresPort, CONSTANT_OBJ.PostgresDB)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.msg(f"Error in creating postgres connection obj in line no {exc_tb.tb_lineno} \n {e}")
        exit(1)
    ####### loging and then inserting each message to postgres ########
    try:
        for msg in consumer:
            log.msg(msg.value)
            pg_con.insert(msg.value['CheckTime'], msg.value['Returncode'], msg.value['ReturnTime'],
                          msg.value['RegexResult'], msg.value['APIAddress'])
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.msg(f"Error in inserting msg to postgres in line no {exc_tb.tb_lineno} \n {e}")
        exit(1)
