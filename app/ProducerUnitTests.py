import unittest
from config.API import Response
from config.Connection import create_producer,create_consumer
from config.Constants import CONSTANT_OBJ
from config.log import log
class MyTestCase(unittest.TestCase):
    def test_constants(self):
        log.msg("###### Checking if constants variables are created correctly #######")
        self.assertEqual(CONSTANT_OBJ.KafkaTopic,"webmonitor")
    def test_API(self):
        log.msg("###### Checking Response class in API.py #######")
        r = Response("http://www.google.com",["google"])
        self.assertEqual(r.Returncode, 200)
    def test_connection(self):
        log.msg("###### Checking create_producer and create_consumer in Connection.py #######")
        p = create_producer(CONSTANT_OBJ.KafkaHost, CONSTANT_OBJ.KafkaPort)
        c = create_consumer("TestTopic", CONSTANT_OBJ.KafkaHost, CONSTANT_OBJ.KafkaPort, "TestGroup",0)
        tempdict = {
            'teststring': "string1"
        }
        p.send(f"TestTopic", tempdict);
        p.flush()
        for rec in c:
            self.assertEqual(rec.value['teststring'],"string1")
            break



if __name__ == '__main__':
    unittest.main()
