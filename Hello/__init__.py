# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from datetime import datetime

def main(name: str) -> str:
    now = datetime.now()
    msg = f'hello {name} time: {now.strftime("%d/%m/%Y %H:%M:%S")} ==========='
    logging.info(msg)
    return msg
