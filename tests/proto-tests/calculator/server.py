import time
from concurrent import futures

import grpc

import calculator
# import generated classes
import calculator_pb2
import calculator_pb2_grpc


# create a class to define the music_server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        print(response.value)
        return response


# create a gRPC music_server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the music_server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
    CalculatorServicer(), server)

# listen on port 50051
print('Starting music_server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since music_server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
