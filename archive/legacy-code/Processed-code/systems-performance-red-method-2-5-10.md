# Systems Performance — RED method (2.5.10) (red-method-2-5-10) (PDF pages 86–96)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-use-red-scout-p86-96.md

---

2.5.10      The RED Method
The focus of this methodology is services, typically cloud services in a microservice architecture.
It identifies three metrics for monitoring health from a user perspective and can be summarized
as [Wilkie 18]:

    For every service, check the request rate, errors, and duration.

The metrics are:
   ■   Request rate: The number of service requests per second
   ■   Errors: The number of requests that failed
   ■   Duration: The time for requests to complete (consider distribution statistics such as per-
       centiles in addition to the average: see Section 2.8, Statistics)

Your task is to draw a diagram of your microservice architecture and ensure that these three
metrics are monitored for each service. (Distributed tracing tools may provide such diagrams for
you.) The advantages are similar to the USE method: the RED method is fast and easy to follow,
and comprehensive.

The RED method was created by Tom Wilkie, who has also developed implementations of the
USE and RED method metrics for Prometheus with dashboards using Grafana [Wilkie 18]. These
methodologies are complementary: the USE method for machine health, and the RED method
for user health.

The inclusion of the request rate provides an important early clue in an investigation: whether a
performance problem is one of load versus architecture (see Section 2.3.8, Load vs. Architecture).
If the request rate has been steady but the request duration has increased, it points to a problem
with the architecture: the service itself. If both the request rate and duration have increased,
then the problem may be one of the load applied. This can be further investigated using work-
load characterization.
54   Chapter 2 Methodologies
