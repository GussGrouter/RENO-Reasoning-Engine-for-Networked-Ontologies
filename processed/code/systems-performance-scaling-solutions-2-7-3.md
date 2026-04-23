# Systems Performance — scaling solutions (2.7.3) (scaling-solutions-2-7-3) (PDF pages 108–116)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-capacity-planning-scout-p108-116.md

---

2.7.3     Scaling Solutions
     Meeting higher performance demands has often meant larger systems, a strategy called vertical
     scaling. Spreading load across numerous systems, usually fronted by systems called load balancers
     that make them all appear as one, is called horizontal scaling.

     Cloud computing takes horizontal scaling further, by building upon smaller virtualized systems
     rather than entire systems. This provides finer granularity when purchasing compute to process
     the required load and allows scaling in small, efficient increments. Since no initial large pur-
     chase is required, as with enterprise mainframes (including a support contract commitment),
     there is less need for rigorous capacity planning in the early stages of a project.

     There are technologies to automate cloud scaling based on a performance metric. The AWS tech-
     nology for this is called an auto scaling group (ASG). A custom scaling policy can be created
     to increase and decrease the number of instances based on a usage metric. This is pictured in
     Figure 2.21.




     Figure 2.21 Auto scaling group

     Netflix commonly uses ASGs that target a CPU utilization of 60%, and will scale up and down
     with the load to maintain that target.
                                                                                     2.8 Statistics     73


Container orchestration systems may also provide support for automatic scaling. For example,
Kubernetes provides horizontal pod autoscalers (HPAs) that can scale the number of Pods (con-
tainers) based on CPU utilization or another custom metric [Kubernetes 20a].

For databases, a common scaling strategy is sharding, where data is split into logical components,
each managed by its own database (or redundant group of databases). For example, a customer
database may be split into parts by splitting the customer names into alphabetical ranges.
Picking an effective sharding key is crucial to evenly spread the load across the databases.
