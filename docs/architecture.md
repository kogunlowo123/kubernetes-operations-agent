# Kubernetes Operations Agent Architecture

Kubernetes cluster operations agent that monitors cluster health, auto-remediates pod failures, manages deployments and rollbacks, optimizes resource allocation, and provides natural language cluster administration through kubectl integration.

## Domain Tools

- **get_cluster_status**: Get comprehensive cluster health status
- **diagnose_pod_failure**: Diagnose why a pod is in CrashLoopBackOff or Pending state
- **rollback_deployment**: Rollback a deployment to a previous revision
- **scale_workload**: Scale a deployment, statefulset, or HPA
- **optimize_resources**: Recommend resource requests/limits based on actual usage
- **execute_kubectl**: Execute a kubectl command from natural language description
- **drain_node**: Safely drain a node for maintenance