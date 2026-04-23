# Systems Performance — ad hoc checklist method (2.5.4) (ad-hoc-checklist-method-2-5-4) (PDF pages 78–84)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-methodology-2-5-scout-p78-84.md

---

2.5.4     Ad Hoc Checklist Method
Stepping through a canned checklist is a common methodology used by support professionals
when asked to check and tune a system, often in a short time frame. A typical scenario involves
the deployment of a new server or application in production, and a support professional spending
half a day checking for common issues now that the system is under real load. These checklists
are ad hoc and are built from recent experience and issues for that system type.

Here is an example checklist entry:

    Run iostat –x 1 and check the r_await column. If this is consistently over 10 (ms)
    during load, then either disk reads are slow or the disk is overloaded.

A checklist may be composed of a dozen or so such checks.

While these checklists can provide the most value in the shortest time frame, they are point-in-
time recommendations (see Section 2.3, Concepts) and need to be frequently refreshed to stay
current. They also tend to focus on issues for which there are known fixes that can be easily
documented, such as the setting of tunable parameters, but not custom fixes to the source code
or environment.
44   Chapter 2 Methodologies


     If you are managing a team of support professionals, an ad hoc checklist can be an effective way
     to ensure that everyone knows how to check for common issues. A checklist can be written to be
     clear and prescriptive, showing how to identify each issue and what the fix is. But bear in mind
     that this list must be constantly updated.
