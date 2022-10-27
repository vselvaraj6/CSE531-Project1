# BankingSystem

To generate service files:

``` bash
python3 -m grpc_tools.protoc \
        -I . \
        --proto_path=. \
        --python_out=. \
        --grpc_python_out=. \
        ./service.proto
```


