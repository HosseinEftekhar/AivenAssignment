"""
this module format output message to json format to be compatible for log readers like Kibana
"""
from datetime import datetime
import structlog
"""
reference : https://www.structlog.org/en/stable/getting-started.html
"""
### function to add time stamp to event_dict ( prepared for log )
def timestamper(_, __, event_dict):
    event_dict["time"] = datetime.now().isoformat()
    return event_dict
structlog.configure(processors=[timestamper, structlog.processors.JSONRenderer()])
log = structlog.get_logger()