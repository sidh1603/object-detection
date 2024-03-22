from objectdetection.logger import logging
from objectdetection.exception import objectException
import sys

#logging.info("Welcome to the Project")

try: 
    a= 7 / '9'

except  Exception as e:
    raise objectException(e, sys) from e