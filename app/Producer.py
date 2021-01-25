"""
this module performs two tasks:
1- checks webpage to be accessible. web page address is an environment variable coming from constant object
2- creates message to kafka topic
"""
import time,sys
from datetime import datetime
from config.Constants import CONSTANT_OBJ
from config.Utils import wait
from config.Regex import SearchingList;
import config.API
from config.Connection import create_producer
from config.log import log

if __name__ == "__main__":
    producer = None
    try:
        producer = create_producer(CONSTANT_OBJ.KafkaHost, CONSTANT_OBJ.KafkaPort)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.msg(f"Error in creating producer obj in line no {exc_tb.tb_lineno} \n {e}")
        exit(1)
    starttime = time.time()
    log.msg (f"started at {str(starttime)}")
    period = int(CONSTANT_OBJ.CheckPeriod) # this is interval in seconds that program checks webpage
    nexttime = starttime + period
    while True: # infinitive loop
        checktime = str(datetime.now()) # time program to check webpage availability
        try:
            response = config.API.Response(CONSTANT_OBJ.APIAddress, SearchingList)
            tempdict = {
                'CheckTime': checktime,
                'Returncode': response.Returncode,
                'ReturnTime': response.Returntime,
                'RegexResult': response.RegexResult,
                'APIAddress': CONSTANT_OBJ.APIAddress
            }
            log.msg(f"sent message at {str(checktime)}")
            producer.send(f"{CONSTANT_OBJ.KafkaTopic}", tempdict)
            producer.flush();
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            log.msg(f"Error in creating response obj or sending result in line no {exc_tb.tb_lineno} \n {e}")
            exit(1)
        nexttime += period
        wait(nexttime)
