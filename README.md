# Data transforming services

## data-transformation-reverse-proxy

### Description:
This repository holds the necessary code to initiate a reverse proxy that is meant to route data throughout transformations before/after storage. The transformer services can variate in any way the framework user wants.

### Setup using docker-compose:

    docker-compose up -d

### Progress:

 - [ ] REST server. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
   - [x] Simple server.
   - [ ] Third party service subscription.
   - [ ] Service identifying.
 - [x] Listening to a canal. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
   - [x] Simple client.
   - [ ] Dynamic listening.
 - [x] Data sending. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/80)
 - [x] Containerisation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)

>---
>**NOTES:**
>- This component's internal flow is dependent on the existence of a container running rabbit-mq broker.
>---
