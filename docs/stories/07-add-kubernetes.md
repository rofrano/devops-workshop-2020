# Add Kubernetes support

**As a:** Service Provider  
**I need:** the ability to deploy my service on Kubernetes  
**So that:** I can easily scale it out horizontally as needed  

**Assumptions:**

- Need to create Kubernetes manifests
- Need a to deploy a Redis database in Kubernetes

**Tasks:**

- [ ] Create a `deployment.yaml` file for service
- [ ] Create a `service.yaml` file for the service
- [ ] Create a `redis.yaml` file to deploy Redis as a `StatefulService`

**Acceptance Criteria:**

```gherkin
Given I have my service in Kubernetes
When I ask Kubernetes to scale to 5 instance
Then I should have 5 instances of my service running
```
