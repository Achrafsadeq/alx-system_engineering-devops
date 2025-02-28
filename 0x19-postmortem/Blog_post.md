## Postmortem: Attack Bot Disrupts Website Availability
![cyber security control room with a hacker surrounded by high-tech screens](Attack.png)

## Issue Summary

Duration: February 27, 2025, 14:00 UTC – February 27, 2025, 18:30 UTC (4 hours 30 minutes)

Impact: The website became inaccessible to users, returning 503 Service Unavailable errors. Approximately 90% of users were affected, experiencing slow load times or complete downtime. Internal services relying on the API were also impacted.

Root Cause: A bot-driven attack overwhelmed our web server with an excessive number of requests, exhausting server resources and causing an outage.

## Timeline

- 13:50 UTC  Initial signs of slow website performance noticed but assumed to be minor traffic fluctuations.
- 14:00 UTC  Monitoring alerts triggered due to a spike in server CPU and memory usage.
- 14:10 UTC  Users began reporting 503 Service Unavailable errors.
- 14:30 UTC  Engineering team started investigating logs and server metrics.
- 15:00 UTC  Initial assumption: potential database overload; database queries optimized, but issue persisted.
- 15:30 UTC  Discovered a high volume of suspicious requests originating from multiple IPs.
- 16:00 UTC  Incident escalated to the security team for deeper analysis.
- 16:30 UTC  Identified bot-driven DDoS (Distributed Denial of Service) attack targeting key endpoints.
- 17:00 UTC  Implemented rate limiting and IP banning via firewall rules; partial recovery observed.
- 17:30 UTC  Deployed Cloudflare protection to filter out bot traffic; website stability improved.
- 18:30 UTC  Full recovery; website fully operational.


## Root Cause and Resolution

### Root Cause:

- An automated attack bot exploited unprotected API endpoints and overwhelmed the server with an unusually high number of requests.
- The sudden spike in traffic exhausted available resources, leading to downtime.
- The lack of rate limiting and bot detection mechanisms exacerbated the issue.

### Resolution:

- Identified attack patterns and blocked malicious IPs.
- Configured Web Application Firewall (WAF) rules to filter bot traffic.
- Implemented rate limiting on API requests.
- Enabled Cloudflare’s DDoS protection and bot mitigation features.
- Monitored system performance to ensure recovery.


## Corrective and Preventative Measures

### Improvements:

- Enhance monitoring alerts to detect bot-driven traffic spikes earlier.
- Strengthen server security and firewall configurations.
- Optimize API endpoints to prevent excessive load from automated attacks.

### TODO List:

-  Implement CAPTCHA for high-risk endpoints.
-  Deploy rate limiting for API requests.
-  Enable bot detection mechanisms via Cloudflare.
-  Improve logging and monitoring for unusual traffic patterns.
-  Set up automated alerts for traffic anomalies.
-  Conduct security audits to identify potential vulnerabilities.
-  Educate the team on DDoS mitigation best practices.


### Final Thoughts

In the battle of humans vs. bots, we might have lost a few hours, but we won the war. Lesson learned: always expect the unexpected, and never underestimate a rogue script’s ability to bring your site to its knees. But hey, at least our monitoring worked.


