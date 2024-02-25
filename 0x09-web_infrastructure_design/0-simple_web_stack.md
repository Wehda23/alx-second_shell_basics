# Infrastructure Questions and Answers (Task 0)

## What is a server?

A server is a computer or system that is dedicated to managing network resources and providing services to other computers, known as clients. Servers can serve various purposes, such as hosting websites, managing email communication, storing files, and more.

## What is the role of the domain name?

A domain name serves as a human-readable label that represents an IP address on the internet. It is used to identify specific web pages and resources. The domain name system (DNS) translates human-readable domain names into IP addresses, allowing users to access websites using easily memorable names.

## What type of DNS record is www in www.foobar.com?

The DNS record for "www" in www.foobar.com is typically a CNAME (Canonical Name) record. It is an alias that points to the domain's main or canonical record, allowing the website to be accessed through the "www" subdomain.

## What is the role of the web server?

A web server is responsible for handling HTTP requests from clients (usually web browsers) and delivering web content in the form of HTML pages, images, or other resources. It processes requests, interacts with the application server (if needed), and returns the appropriate response to the user's browser.

## What is the role of the application server?

An application server is responsible for executing application logic and processing dynamic content. It works in conjunction with the web server to handle more complex tasks, such as running server-side scripts, processing database queries, and generating dynamic web pages.

## What is the role of the database?

The database stores and manages structured data, which can include user information, content, and other relevant data for an application. It is accessed by the application server to retrieve and store information, providing a persistent and organized data storage solution.

## What is the server using to communicate with the computer of the user requesting the website?

The server communicates with the user's computer using the HTTP (Hypertext Transfer Protocol) or its secure counterpart, HTTPS. These protocols define how data is formatted and transmitted between the server and the client, ensuring the proper exchange of information for website rendering.

# Infrastructure Issues

## SPOF (Single Point of Failure)

A Single Point of Failure occurs when there is a component in the infrastructure that, if it fails, can bring down the entire system. This vulnerability can lead to service disruptions and downtime if not mitigated through redundancy and fault-tolerant measures.

## Downtime when maintenance needed (like deploying new code; web server needs to be restarted)

During maintenance, deploying new code, or restarting the web server, there is potential downtime where the website may be inaccessible to users. Proper planning and deployment strategies, such as rolling updates or redundant server setups, can minimize downtime during maintenance activities.

## Cannot scale if too much incoming traffic

The inability to scale in response to high incoming traffic is a scalability issue. If the infrastructure is not designed to handle increased demand, it may result in slow performance or even downtime during traffic spikes. Implementing load balancing, caching, and scalable architectures can address this challenge and ensure optimal performance under varying workloads.
