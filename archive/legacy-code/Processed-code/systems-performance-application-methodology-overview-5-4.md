<!-- pdftotext -f 182 -l 230 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.4 Methodology
This section describes methodologies for application analysis and tuning. The tools used for
analysis are either introduced here or are referenced from other chapters. The methodologies are
summarized in Table 5.2.

Table 5.2

Application performance methodologies

Section

Methodology

Type

5.4.1

CPU profiling

Observational analysis

5.4.2

Off-CPU profiling

Observational analysis

5.4.3

Syscall analysis

Observational analysis

5.4.4

USE method

Observational analysis

5.4.5

Thread state analysis

Observational analysis

5.4.6

Lock analysis

Observational analysis

5.4.7

Static performance tuning

Observational analysis, tuning

5.4.8

Distributed tracing

Observational analysis

See Chapter 2, Methodologies, for the introduction to some of these, and also additional general
methodologies: for applications, in particular consider CPU profiling, workload characterization, and drill-down analysis. Also see the chapters that follow for the analysis of system
resources and virtualization.
These methodologies may be followed individually or used in combination. My suggestion is to
try them in the order listed in the table.

8

There has been much work on techniques to reduce GC time or application interrupts from GC. One example uses
system and application metrics to determine when best to call GC [Schwartz 18].

5.4 Methodology

In addition to these, look for custom analysis techniques for the specific application and the
programming language in which it is developed. These may consider logical behavior of
the application, including known issues, and lead to some quick performance wins.

