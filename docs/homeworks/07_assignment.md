# Assignment 7 (8 p.)

In this assignment you have to implement Dataforge Envelope --- format for transmission messages contain meta-data and binary data.

1. Implement next methods for class `Envelope`:
   1. (3 p.) `read(input: BufferedReader) -> "Envelope"`
   2. (3 p.) `write_to(self, output: RawIOBase):`
   3. (1 p.) `from_bytes(buffer: bytes) -> "Envelope":`
   4. (1 p.) `to_bytes(self) -> bytes`

Use next shortly description of DataForge Envelope:

* 