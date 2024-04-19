FROM python:3.11

ADD greeter_server.py .

ADD greeter_client.py .

ADD helloworld.proto .

RUN pip install grpcio

RUN pip install grpcio-tools

RUN python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. helloworld.proto

CMD ["python", "greeter_server.py"]