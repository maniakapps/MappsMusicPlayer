import datetime
import time
from concurrent import futures

import grpc
# import generated classes
from music_server.grpc import mmp_pb2
from music_server.grpc import mmp_pb2_grpc


class MMPService(mmp_pb2_grpc.MusicPlayerServicer):

    def RetrieveAlbumList(self, request, context):
        print("retrieve list")
        alist = mmp_pb2.AlbumList()
        print(type(alist.album_list))
        alist.album_list.extend([mmp_pb2.Album(title="Test")])
        # alist.album_list.append(mmp_pb2.Album(title="Test1"))
        # alist.album_list.append(mmp_pb2.Album(title="Test2"))
        # alist.album_list.append(mmp_pb2.Album(title="Test3"))
        return alist

    def RetrieveSongList(self, request, context):
        return super().RetrieveSongList(request, context)

    def Play(self, request, context):
        return super().Play(request, context)

    def ChangeVolume(self, request, context):
        return super().ChangeVolume(request, context)

    def ChangePosition(self, request, context):
        return super().ChangePosition(request, context)

    def Previous(self, request, context):
        return super().Previous(request, context)

    def Next(self, request, context):
        return super().Next(request, context)

    def RetrieveMMPStatus(self, request, context):
        return super().RetrieveMMPStatus(request, context)

    def AddNext(self, request, context):
        return super().AddNext(request, context)

    def AddToQueue(self, request, context):
        return super().AddToQueue(request, context)

    def RegisterMMPNotify(self, request, context):
        print("Client registered")
        delay = 40
        while True:
            print("[{}] sending status".format(datetime.datetime.now().strftime('%H:%M:%S')))
            yield mmp_pb2.MMPStatus()
            print("delay is: %s" % delay)
            time.sleep(delay)
            delay += delay


# create a gRPC music_server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

mmp_pb2_grpc.add_MusicPlayerServicer_to_server(MMPService(), server)

print('Starting music_server. Listening...')
server.add_insecure_port('[::]:5005')
server.start()

# since music_server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
