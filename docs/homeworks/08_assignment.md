# Assignment 8 (8 p.)

In this assignment will be asked to practice working with IO formats.

1. (4 p.) (_Protobuf_, _Magic methods_) Let the data in the binary file be stored as a set of records. The record has the following format:
   * The first 8 bytes contain a number N;
   * The next N bytes contain a message in the _protobuf_ format (the message scheme is the same for all records).
   Implement a class `ProtoList` in module `proto_list.py` that allows you to work with a file as a list of _protobuf_ messages (without loading all messages in memory). Class `ProtoList` must open access to data in context manager, and close file on exit from context.
2. (4 p.) (_HDF_, _ZIP_) Implement script for conversion binary data from CAEN multy channel ADC to HDF5 file. Example of data located by [link](https://drive.google.com/drive/folders/1i3-2b_kpVFNYf8p9Y0_em3bG7PZCg9tq?usp=sharing), in archive `wave.data.zip`. Don't extract data from archive: use `ZipFiles` for direct reading. In archive contains several files, each file is data from one channel of ADC. Every file contains set of entries. Entries in different files is synchronized (first entry in one file corresponds first entry in another file). Each entry contain 24-bytes header and 1024 float32 values. Convert ADC data to HDF5 Tables: index of row corresponds to number of event , index of column corresponds to number of channel. Item of table is 1024-sized array corresponds values from entry without header.