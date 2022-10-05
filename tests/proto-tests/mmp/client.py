# import the generated classes
import datetime
import time

import grpc
from music_server.grpc import mmp_pb2_grpc, mmp_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:5005')
client = mmp_pb2_grpc.MusicPlayerStub(channel)

sr = mmp_pb2.MMPStatusRequest()

# make the call
response = client.RegisterMMPNotify(sr)
begin_time = time.time()
for status in response:
    duration = time.time() - begin_time
    print("[{} - {:.2f} sec.] {}".format(datetime.datetime.now().strftime('%H:%M:%S'), duration, status.state))
    begin_time = time.time()
