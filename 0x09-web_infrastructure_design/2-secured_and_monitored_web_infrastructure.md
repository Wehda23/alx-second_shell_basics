
## Infrastructure Specifics:

### Additional Elements and Their Purpose:

- **3 Firewalls:** Added for security purposes to control incoming and outgoing traffic, preventing unauthorized access and providing an additional layer of defense.

- **SSL Certificate:** Utilized to serve www.foobar.com over HTTPS, ensuring encrypted communication between the client and the web server for improved security.

- **3 Monitoring Clients:** Deployed to collect data for monitoring services (e.g., Sumologic). These clients collect information about the infrastructure's performance, security, and availability.

### Why These Elements are Added:

- **Firewalls:** Provide a security barrier between the servers and the internet. They control and monitor incoming and outgoing network traffic, acting as a protective shield against potential threats.

- **SSL Certificate:** Enables HTTPS to secure data transmission between clients and the web server. It encrypts sensitive information, protecting it from eavesdropping and ensuring data integrity.

- **Monitoring Clients:** Essential for real-time observation of the infrastructure's health, performance, and security. Monitoring helps identify issues proactively and allows for timely intervention and optimization.

### Specific Explanations:

- **Terminating SSL at the Load Balancer Level:** Terminating SSL at the load balancer level may expose decrypted data within the internal network. To mitigate this, end-to-end encryption is preferred, ensuring encrypted communication between the load balancer and the application server.

- **Single MySQL Server Accepting Writes:** This poses a single point of failure (SPOF) for write operations. Implementing a Primary-Replica (Master-Slave) cluster allows for redundancy and fault tolerance.

- **Servers with Identical Components:** Homogeneous servers may lead to uniform vulnerabilities. Diversifying components helps reduce the risk of systemic failures and enhances overall resilience.

## Issues with the Infrastructure:

### Terminating SSL at the Load Balancer Level:

- **Issue:** Decrypting SSL at the load balancer exposes data within the internal network.
- **Mitigation:** Implement end-to-end encryption to secure communication between the load balancer and the application server.

### Single MySQL Server Accepting Writes:

- **Issue:** A single MySQL server accepting writes creates a potential SPOF for write operations.
- **Mitigation:** Implement a Primary-Replica (Master-Slave) cluster for redundancy and fault tolerance in write operations.

### Servers with Identical Components:

- **Issue:** Identical server components increase the risk of systemic vulnerabilities.
- **Mitigation:** Diversify components across servers to reduce the risk of uniform failures and enhance overall resilience.
