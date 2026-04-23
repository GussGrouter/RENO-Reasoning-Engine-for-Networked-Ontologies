# Systems Performance — time-based patterns (2.9.1) (time-based-patterns-2-9-1) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.9.1     Time-Based Patterns
Examples of time-based patterns are shown in Figures 2.24, 2.25, and 2.26, which plot file sys-
tem reads from a cloud computing server over different time intervals.
78   Chapter 2 Methodologies




     Figure 2.24 Monitoring activity: one day




     Figure 2.25 Monitoring activity: five days




     Figure 2.26 Monitoring activity: 30 days

     These graphs show a daily pattern that begins to ramp up around 8 a.m., dips a little in the after-
     noon, and then decays during the night. The longer-scale charts show that activity is lower on
     the weekend days. A couple of short spikes are also visible in the 30-day chart.

     Various cycles of behavior including those shown in the figures can commonly be seen in his-
     toric data, including:

         ■   Hourly: Activity may occur every hour from the application environment, such as
             monitoring and reporting tasks. It’s also common for these to execute with a 5- or 10-
             minute cycle.
         ■   Daily: There may be a daily pattern of usage that coincides with work hours (9 a.m. to
             5 p.m.), which may be stretched if the server is for multiple time zones. For Internet
             servers, the pattern may follow when worldwide users are active. Other daily activity
             may include nightly log rotation and backups.
                                                                                            2.10 Visualizations      79


    ■   Weekly: As well as a daily pattern, there may be a weekly pattern present based on work-
        days and weekends.
    ■   Quarterly: Financial reports are done on a quarterly schedule.
    ■   Yearly: Yearly patterns of load may be due to school schedules and vacations.

Irregular increases in load may occur with other activities, such as releasing new content on a
website, and sales (Black Friday/Cyber Monday in the US). Irregular decreases in load can occur
due to external activities, such as widespread power or internet outages, and sports finals (where
everyone watches the game instead of using your product).6
