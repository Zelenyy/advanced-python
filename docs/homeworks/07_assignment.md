# Assignment 7 (10 p.)

In this assignment you have to implement Dataforge Envelope --- format for transmission messages contain meta-data and binary data.

1. (2 p.) In module `envelope.py` implement the method `default(self, obj: Meta) -> Any:` of the class `MetaEncoder(JSONEncoder)`. Class `MetaEncoder` must allow to serialize `Meta object` to JSON format as encoder for module `json`.
2. In module `envelope.py` implement the class `Envelope` - format for transferring data via byte stream. Description of format see below. If data size less than `Envelope._MAX_SIZE` store data in the memory, otherwise on disk using memory mapping. Implement next methods for class `Envelope`:
   1. (3 p.) **staticmetod** `read(input: BufferedReader) -> "Envelope"` --- create `Envelope` instance from stream.
   2. (3 p.) `write_to(self, output: RawIOBase):` --- write `Envelope` instance to stream.
   3. (1 p.) **staticmetod** `from_bytes(buffer: bytes) -> "Envelope":` create `Envelope` instance from binary string.
   4. (1 p.) `to_bytes(self) -> bytes` --- convert `Envelope` instance to binary string.
   Note: Use module `struct` for work with binary values.


Use next description of DataForge Envelope:

* **Tag** .First 20 bytes of file or stream is reserved for envelope properties binary representation:
  * `#~` - two ASCII symbols, beginning of binary string.
  * 4 bytes - properties `type` field: envelope format type and version. For default format the string `DF02` is used, but in principle other envelope types could use the same format.
  * 2 bytes - properties `metaType` field: metadata encoding type.
  * 4 bytes - properties `metaLength` field: metadata length in bytes including new lines and other separators.
  * 4 bytes - properties `dataLength` field: the data length in bytes.
  * `~#` - two ASCII symbols, end of binary string.
  * `\r\n` - two bytes, new line.
The values are read as binary and transformed into 4-byte unsigned tag codes (Big endian).
* **Metadata block**. Metadata in any accepted format which length equal to `metaLength` properties. In our implementation we will consider only JSON format.
* **Data block**. Any other binary data which length equal to `dataLength` properties.