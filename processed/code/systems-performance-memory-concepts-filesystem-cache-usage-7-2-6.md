7.2.6 File System Cache Usage
It is normal for memory usage to grow after system boot as the operating system uses available
memory to cache the file system, improving performance. The principle is: If there is spare
main memory, use it for something useful. This can distress naïve users who see the available
free memory shrink to near zero sometime after boot. But it does not pose a problem for applications, as the kernel should be able to quickly free memory from the file system cache when
applications need it.
For more about the various file system caches that can consume main memory, see Chapter 8,
File Systems.
