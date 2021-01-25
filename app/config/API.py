import requests, re
import sys
from .Constants import CONSTANT_OBJ
from .log import log
from .Utils import lineno
"""
Refrerence:
https://rapidapi.com/blog/how-to-use-an-api-with-python/
"""

"""
The website checker should perform the checks periodically and collects the
HTTP response time, error code returned, as well as optionally checking the
returned page contents for a regexp pattern that is expected to be found on the
page.
"""


class Response:
    RegexResult = {}  # dictionary for checking regex experissions in website context
    Returntime = None # time elapsed to return from website
    Returncode = None # return code of get request
    Returntext = None # content of return message

    def __init__(self,apiaddress=CONSTANT_OBJ.APIAddress, searchlist=[]):
        # search list is list of keywords for regex experistions
        if CONSTANT_OBJ.run_state=="DEV":
            log.msg("Starting Response API.py at line no : " + lineno())
        try:
            response = requests.get(apiaddress);
            """
            return code can be in following list
            200 – OK. The request was successful. The answer itself depends on the method used (GET, POST, etc.) and the API specification.
            204 – No Content. The server successfully processed the request and did not return any content.
            301 – Moved Permanently. The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.
            400 – Bad Request. The server cannot process the request because the client-side errors (incorrect request format).
            401 – Unauthorized. Occurs when authentication was failed, due to incorrect credentials or even their absence.
            403 – Forbidden. Access to the specified resource is denied.
            404 – Not Found. The requested resource was not found on the server.
            500 – Internal Server Error. Occurs when an unknown error has occurred on the server."""
            self.Returntime = response.elapsed.total_seconds()
            self.Returncode = response.status_code
            self.Returntext = response.text
            for i in searchlist:
                if re.search(".*"+str(i)+".*",self.Returntext):
                    self.RegexResult[i] = "Yes"
                else:
                    self.RegexResult[i] = "No"
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info();
            log.msg(f"Error in connection to {apiaddress} in line no {exc_tb.tb_lineno} \n {e}");
            exit(1)

