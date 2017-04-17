# faas-python-fib
A [FaaS](http://get-faas.com) function to generate the first N fib numbers

You can execute the function like this:

`curl http://localhost:8080/function/func_fib -d "https://www.docker.com/sites/default/files/social/docker-facebook-share.png"`

(or use the FaaS UI to send the URL)

## Installation

You can either install `faas-python-fib` via your FaaS compose file or you can add it via the UI.

### Compose file

Add this to `docker-compose.yml` and then redeploy the stack

```Dockerfile
ascii:
    image: developius/faas-python-fib:latest
    labels:
        function: "true"
    depends_on:
        - gateway
    networks:
        - functions
    environment:
        no_proxy: "gateway"
        https_proxy: $https_proxy
```

`docker stack deploy -c docker-compose.yml func`

### UI

Hit the `CREATE NEW FUNCTION` button and add these details:

- Image: `developius/faas-python-fib:latest`
- Service name: `ascii`
- fProcess: `node /app/index.js`
- Network: `func_functions`

Hit create!
