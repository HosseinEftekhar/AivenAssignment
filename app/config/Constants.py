import os
import sys

from .log import log

"""
this module gets all environment variables (defined in .env in DEV Area ) and map it to some variables in constants class.
at the end an obj of class gets created to be used in other files in this project
"""

class Constants:
    APIAddress = None
    run_state = None
    KafkaHost = None
    KafkaTopic = None
    ZookeeperHost = None
    PostgresHost = None
    PostgresUser = None
    PostgresPassword = None
    PostgresDB = None
    CheckPeriod = None
    KafkaPort = None
    KafkaGroupID = None
    KafkaPartitionID = None
    PostgresPort = None
    LogFile = None

    def __init__(self):
        try:
            self.run_state = os.environ.get("RunState")
            self.KafkaHost = os.environ.get("KafkaHost")
            self.KafkaTopic = os.environ.get("KafkaTopic")
            self.ZookeeperHost = os.environ.get("ZookeeperHost")
            self.PostgresHost = os.environ.get("PostgresHost")
            self.PostgresUser = os.environ.get("PostgresUser")
            self.PostgresPassword = os.environ.get("PostgresPassword")
            self.PostgresDB = os.environ.get("PostgresDB")
            self.CheckPeriod = os.environ.get("CheckPeriod")
            self.APIAddress = os.environ.get("APIAddress")
            self.KafkaPort = os.environ.get("KafkaPort")
            self.KafkaGroupID = os.environ.get("KafkaGroupID")
            self.KafkaPartitionID = os.environ.get("KafkaPartitionID")
            self.PostgresPort = os.environ.get("PostgresPort")
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            log.msg(f"Error in getting environment variables from os in line no {exc_tb.tb_lineno} \n {e}")
            exit(1)


CONSTANT_OBJ = Constants()
