from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json,sys
from .log import log
"""
this module defines two functions to create producer and consumer for topics declared in env variables
"""

def create_producer(KafkaHost, KafkaPort):
    try:
        producer = KafkaProducer(bootstrap_servers=[f'{KafkaHost}:{KafkaPort}']
                             , value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info();
        log.msg(f"Error in connection to kafka in line no {exc_tb.tb_lineno} \n {e}");
        exit(1)

def create_consumer(KafkaTopic, KafkaHost, KafkaPort, KafkaGroupID, KafkaPartitionID):
    try:
        if KafkaGroupID:
            consumer = KafkaConsumer(KafkaTopic, bootstrap_servers=[f'{KafkaHost}:{KafkaPort}'], group_id=KafkaGroupID,value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        else:
            consumer = KafkaConsumer(KafkaTopic, bootstrap_servers=[f'{KafkaHost}:{KafkaPort}'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        if KafkaPartitionID:
            consumer.assign([TopicPartition(KafkaTopic, int(KafkaPartitionID))])
        return consumer
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info();
        log.msg(f"Error in connection to kafka in line no {exc_tb.tb_lineno} \n {e}");
        exit(1)
