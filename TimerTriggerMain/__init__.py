import datetime
import logging

import azure.functions as func
import azure.durable_functions as df


async def main(mytimer: func.TimerRequest, starter: str) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    # if mytimer.past_due:
    client = df.DurableOrchestrationClient(starter)
    logging.info('The timer is past due!')
    instance_id = await client.start_new(
        'DurableFunctionsOrchestrator1',
        None,
        None
    )
    logging.info(f"started orchestration with ID = '{instance_id}' at '{utc_timestamp}'")
    
    logging.info('Python timer trigger function ran at %s DurableOrchestrationContext', utc_timestamp)
