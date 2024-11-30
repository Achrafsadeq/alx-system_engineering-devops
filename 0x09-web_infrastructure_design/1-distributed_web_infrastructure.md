# 1. Distributed Web Infrastructure

## Task Overview

### Scenario
Evolve the web infrastructure for `www.foobar.com` by introducing distributed components to improve reliability and performance.

## Infrastructure Components

| Component | Quantity | Purpose | Key Improvement |
|-----------|----------|---------|-----------------|
| Servers | 3 Total (2 New) | Distribute workload | Increased redundancy |
| Web Server (Nginx) | 1 | Handle web requests | Improved request handling |
| Application Server | 1 | Process application logic | Dedicated processing |
| Load Balancer (HAproxy) | 1 | Distribute network traffic | Enhanced availability |
| Database (MySQL) | 1 (Primary-Replica) | Data management | Improved data reliability |
| Application Files | 1 Set | Website core functionality | Consistent deployment |

## Architectural Enhancements

### Load Balancing Strategy
- Distributes incoming traffic across multiple servers
- Prevents single server overload
- Improves website responsiveness and reliability

#### Load Balancing Algorithms
1. Round Robin
   - Requests distributed sequentially
   - Equal load across servers
   - Simple, predictable distribution

2. Least Connections
   - Routes to server with fewest active connections
   - Dynamically adapts to server load
   - Optimal for varied workload scenarios

### Active-Active vs Active-Passive Setup

#### Active-Active Load Balancing
- All servers actively handle requests
- Maximum resource utilization
- Immediate failover capabilities
- Higher performance potential

#### Active-Passive Load Balancing
- One server actively handles requests
- Standby server remains inactive
- Provides backup/failover mechanism
- Lower resource utilization

### Database Primary-Replica Cluster

#### Primary (Master) Node
- Handles write operations
- Source of truth for data modifications
- Synchronizes changes to replica nodes
- Critical for data consistency

#### Replica (Slave) Node
- Handles read operations
- Creates redundant data copies
- Provides read scalability
- Serves as backup for primary node

## Infrastructure Workflow
1. User requests `www.foobar.com`
2. DNS resolves to load balancer
3. Load balancer distributes request
4. Chosen server processes request
5. Application server executes logic
6. Database provides/updates data
7. Response sent back to user

## Infrastructure Limitations

### Single Points of Failure (SPOF)
- Load balancer dependency
- Single database server for writes
- Potential network infrastructure vulnerabilities

### Security Concerns
- No firewall protection
- Lack of HTTPS encryption
- Exposed server configurations
- Potential unauthorized access risks

### Monitoring Gaps
- No system performance tracking
- Limited visibility into server health
- Cannot detect potential issues proactively

## Improvement Recommendations
- Implement firewall rules
- Add SSL/HTTPS encryption
- Introduce comprehensive monitoring
- Create multi-master database configuration
- Implement advanced load balancing techniques
- Add automatic failover mechanisms

## Learning Objectives
- Understand distributed system design
- Explore load balancing strategies
- Recognize infrastructure complexity
- Develop scalable architecture skills

## Submission Requirements
- Whiteboard comprehensive infrastructure design
- Capture detailed screenshot
- Explain component interactions
- Discuss potential improvements

## Mission Director
ALX System Engineering DevOps Program

## Repository
[alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)

## Additional Insights
- Distributed infrastructure requires careful design
- Balance between complexity and maintainability
- Continuous optimization is key to robust systems
