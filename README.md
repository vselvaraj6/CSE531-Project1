# BankingSystem

To generate interface file:

``` bash
protoc protos/service.proto --python_out . --proto_path generated=.
```

To generate grpc file:
```
python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. protos/service.proto
```


