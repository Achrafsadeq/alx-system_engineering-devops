# 0. Simple Web Stack

## Task Overview

### Scenario
A user wants to access the website `www.foobar.com` using a simple, single-server web infrastructure.

## Infrastructure Components

| Component | Description | Purpose |
|-----------|-------------|---------|
| Server | Physical/virtual machine | Host all web infrastructure components |
| Web Server (Nginx) | HTTP server | Handle incoming web requests, serve static content |
| Application Server | Runtime environment | Process dynamic content, execute application logic |
| Application Files | Codebase | Contain website's core functionality and logic |
| Database (MySQL) | Data storage system | Store and manage website's persistent data |
| Domain Name (foobar.com) | Website address | Provide human-readable web address |

## Architectural Workflow
1. User enters `www.foobar.com` in browser
2. DNS resolves domain to server IP (8.8.8.8)
3. Request reaches Nginx web server
4. Web server forwards request to application server
5. Application server processes request
6. Database provides necessary data
7. Response travels back to user's browser

## Detailed Component Explanations

### Server
- A computer that provides services to other computers
- Hosts all web infrastructure components
- Processes and responds to network requests
- Runs necessary software for website functionality

### Domain Name
- Human-readable website address
- Translates to IP address via DNS
- Allows easy, memorable website access
- Provides brand identity and recognition

### DNS Record (www)
- Type: CNAME (Canonical Name) or A (Address) record
- Maps `www.foobar.com` to specific IP address
- Enables users to access website using www prefix

### Web Server (Nginx)
- Handles HTTP/HTTPS requests
- Serves static content (HTML, CSS, images)
- Routes dynamic request to application server
- Manages web traffic and connection protocols

### Application Server
- Executes server-side application logic
- Processes dynamic content generation
- Interacts with database to retrieve/store data
- Implements business logic and application workflows

### Database (MySQL)
- Persistent data storage system
- Stores website's structured data
- Manages data relationships
- Provides data retrieval and manipulation capabilities

### Communication Protocol
- Uses HTTP/HTTPS protocols
- TCP/IP network communication
- Client-server request-response model

## Infrastructure Limitations

### Single Point of Failure (SPOF)
- Entire website depends on single server
- Hardware failure causes complete service outage
- No redundancy or backup mechanisms

### Maintenance Challenges
- Deploying new code requires web server restart
- Causes temporary website unavailability
- Limited zero-downtime deployment options

### Scalability Constraints
- Fixed server resources
- Cannot handle sudden traffic spikes
- Limited horizontal scaling capabilities

## Improvement Recommendations
- Implement multiple servers
- Add load balancing
- Create redundant infrastructure
- Use cloud or distributed computing
- Develop auto-scaling mechanisms

## Learning Objectives
- Understand basic web infrastructure components
- Explore server-side architecture
- Recognize infrastructure limitations
- Develop critical design thinking

## Submission Requirements
- Whiteboard infrastructure design
- Take clear screenshot
- Explain each component thoroughly
- Discuss potential improvements

## Mission Director
ALX System Engineering DevOps Program

## Repository
[alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
