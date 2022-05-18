# Producer/Consumer
Simple incremental numbers producer/consumer with Mutex sync. Implemented in Python.

In this code we propose two classes, one is a producer and another is a consumer. We use a global `UUID` and `BUFFER` to simulate what a simple OS/Program/Whatever might do to number something with a unique id.

So, we have a number of threads for each object. And the way it works is that, when available, producers produce till full, consumers consume one at a time.

Hope it helps, and if it did, don't forget to star it :)