# BankingSystem

To generate grpc server and client stub files:
```
python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/service.proto
```


