<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.4.7 Static Performance Tuning
Static performance tuning focuses on issues of the configured environment. For application
performance, examine the following aspects of the static configuration:
■

What version of the application is running, and what are its dependencies? Are there
newer versions? Do their release notes mention performance improvements?

■

Are there known performance issues? Is there a bug database that lists them?

■

How is the application configured?

■

If it was configured or tuned differently from the defaults, what was the reason? (Was it
based on measurements and analysis, or guesswork?)

■

Does the application employ a cache of objects? How is it sized?

■

Does the application run concurrently? How is that configured (e.g., thread pool sizing)?

■

Is the application running in a special mode? (For example, debug mode may have been
enabled and be reducing performance, or the application may be a debug build instead of
a release build.)

■

What system libraries does the application use? What versions are they?

■

What memory allocator does the application use?

■

Is the application configured to use large pages for its heap?

■

Is the application compiled? What version of the compiler? What compiler options and
optimizations? 64-bit?


5.5 Observability Tools

■

■

■

Does the native code include advanced instructions? (Should it?) (For example,
SIMD/vector instructions including Intel SSE.)
Has the application encountered an error, and is it now in a degraded mode? Or is it
misconfigured and always running in a degraded mode?
Are there system-imposed limits or resource controls for CPU, memory, file system, disk,
or network usage? (These are common with cloud computing.)

Answering these questions may reveal configuration choices that have been overlooked.
