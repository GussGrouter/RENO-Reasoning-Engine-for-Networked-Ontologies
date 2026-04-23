# Systems Performance — streetlight anti-method (2.5.1) (streetlight-anti-method-2-5-1) (PDF pages 78–84)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-methodology-2-5-scout-p78-84.md

---

2.5.1 Streetlight Anti-Method
     This method is actually the absence of a deliberate methodology. The user analyzes performance
     by choosing observability tools that are familiar, found on the Internet, or just at random to see if
     anything obvious shows up. This approach is hit or miss and can overlook many types of issues.

     Tuning performance may be attempted in a similar trial-and-error fashion, setting whatever
     tunable parameters are known and familiar to different values to see if that helps.

     Even when this method reveals an issue, it can be slow as tools or tunings unrelated to the issue
     are found and tried, just because they’re familiar. This methodology is therefore named after an
     observational bias called the streetlight effect, illustrated by this parable:

         One night a police officer sees a drunk searching the ground beneath a streetlight and
         asks what he is looking for. The drunk says he has lost his keys. The police officer can’t
         find them either and asks: “Are you sure you lost them here, under the streetlight?” The
         drunk replies: “No, but this is where the light is best.”

     The performance equivalent would be looking at top(1), not because it makes sense, but because
     the user doesn’t know how to read other tools.

     An issue that this methodology does find may be an issue but not the issue. Other methodolo-
     gies quantify findings, so that false positives can be ruled out more quickly, and bigger issues
     prioritized.
