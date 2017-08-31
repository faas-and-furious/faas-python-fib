# faas-python-fib
An [OpenFaaS](https://www.openfaas.com/) function to generate the first N fibonacci numbers


## Install it

```
$ faas-cli -action build -f ./stack.yml
$ faas-cli -action deploy -f ./stack.yml
```

## Run it

You can execute the function like this:

```
$ curl http://localhost:8080/function/fib -d "10"
```

(or use the FaaS UI to send the URL)

![](https://pbs.twimg.com/media/C9oep7KUMAAb_eZ.jpg:large)
