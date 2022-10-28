# BankingSystem

To generate interface file:

``` bash
protoc proto/service.proto --grpc_python_out=./generated --python_out=./generated --proto_path=./proto
```

To generate grpc file:
```
python3 -m grpc_tools.protoc -I proto --python_out=./generated --grpc_python_out=./generated proto/service.proto
```


