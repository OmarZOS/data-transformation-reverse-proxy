# Scalable graph computing

## Scalable graph computing using graphX library




### Description:
This repository holds the necessary code to initiate a reverse proxy that is meant to route data throughout transformtaions before storage. The transformer serviecs can use Scala scripts for scalable graph computing over spark clusters. You can also implement services that use Spark REST API and add the listener class to inform about the end of the job.

#### Job listener:

- I implemented a low level java listener that sends the state to wanted components. (similar to those used by spark dashboard)
- Make sure to set the *SPARK_JOB_LISTENER_HOST* and *SPARK_JOB_LISTENER_PORT* environment variables.


### Packaging:
Please follow these instructions:
    
    # Enter the target directory (make sure to have __init__.py file if it was python scripts)
    zip -r packageName.zip

