# BankingSystem

To generate grpc server and client stub files:
```
python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/service.proto
```


To run server:
```bash
python3 server.py input.json
```

To run client:
```bash
python3 client.py input.json
```