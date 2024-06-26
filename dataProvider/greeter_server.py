# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.dataProvider server."""

from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import random


class dataProvider(helloworld_pb2_grpc.dataProviderServicer):
    # def SayHello(self, request, context):
    #     return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)
    
    # def SayHelloAgain(self, request, context):
    #     return helloworld_pb2.HelloReply(message=f"Hello Again, {request.name}!")
    
    def serverConnection(self, request, context):
        return helloworld_pb2.Data(data_id=request.project_id, data_elements=[str(random.randint(1, 100)) for i in range(10)])


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_dataProviderServicer_to_server(dataProvider(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
