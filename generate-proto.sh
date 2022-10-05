#!/bin/bash
echo "Generating proto grpc files..."
python -m grpc_tools.protoc -I=proto --python_out=mappsmusicplayer/grpc --grpc_python_out=mappsmusicplayer/grpc proto/mmp.proto
echo "DONE"
