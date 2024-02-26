
## Infrastructure Specifics:

### Additional Elements and Their Purpose:

- **2 Servers:** Redundancy and fault tolerance to avoid a Single Point of Failure (SPOF).
  
- **Web Server (Nginx):** Efficient handling of HTTP requests, managing static content, and distributing requests to the application server.

- **Application Server:** Executes application logic, processes dynamic content, and handles server-side operations.

- **Load Balancer (HAproxy):** Distributes incoming web traffic across multiple servers to ensure optimal resource utilization and prevent overload on a single server.

- **Set of Application Files (Your Code Base):** Contains the application code and files necessary for the web server and application server to function.

- **Database (MySQL):** Stores and manages application data, chosen for reliability and scalability.

### Load Balancer Configuration:

- **Distribution Algorithm:** Configured with a Round Robin distribution algorithm. It routes each new request to the next server in line, distributing the load evenly among available servers.

- **Active-Active or Active-Passive Setup:** Configured with an Active-Active setup, where all servers actively handle requests. This configuration improves resource utilization and provides better performance.

### Database Primary-Replica (Master-Slave) Cluster:

- **How it Works:** The database is set up as a Primary-Replica (Master-Slave) cluster. The Primary node (Master) handles both read and write operations, while the Replica nodes (Slaves) replicate data from the Primary node. This setup provides redundancy, fault tolerance, and scalability.

### Difference between Primary and Replica Nodes in Regards to the Application:

- **Primary Node:** Responsible for handling write operations, serving as the authoritative source for data. It actively updates and manages the dataset.

- **Replica Node:** Serves read operations and acts as a backup for data. Replicates data from the Primary node, providing fault tolerance and improving read performance.

## Issues with the Infrastructure:

### Single Point of Failure (SPOF):

- The Load Balancer (HAproxy) serves as a potential SPOF. If it fails, it can disrupt the distribution of traffic to servers, leading to potential service interruptions.

### Security Issues:

- **No Firewall:** The absence of a firewall exposes the infrastructure to potential security threats. Implementing a firewall is essential for controlling incoming and outgoing traffic, protecting against unauthorized access, and enhancing overall security.

- **No HTTPS:** Lack of HTTPS leaves the communication between users and servers unencrypted, posing a security risk. Implementing HTTPS with SSL/TLS certificates is crucial to secure data transmission and protect user privacy.

### No Monitoring:

- The absence of monitoring tools means there is no proactive oversight of the infrastructure. Monitoring solutions are essential for detecting issues, performance bottlenecks, and security threats in real-time, allowing for timely intervention and optimization.
