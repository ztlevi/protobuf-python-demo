## Protocol Buffer Basics: Python

https://developers.google.com/protocol-buffers/docs/pythontutorial

## Compile protobuf file to python classes
``` sh
protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto
```
