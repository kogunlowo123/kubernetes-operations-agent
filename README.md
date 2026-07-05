# Kubernetes Operations Agent

[![CI](https://github.com/kogunlowo123/kubernetes-operations-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/kubernetes-operations-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Kubernetes cluster operations agent that monitors cluster health, auto-remediates pod failures, manages deployments and rollbacks, optimizes resource allocation, and provides natural language cluster administration through kubectl integration.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `get_cluster_status` | Get comprehensive cluster health status |
| `diagnose_pod_failure` | Diagnose why a pod is in CrashLoopBackOff or Pending state |
| `rollback_deployment` | Rollback a deployment to a previous revision |
| `scale_workload` | Scale a deployment, statefulset, or HPA |
| `optimize_resources` | Recommend resource requests/limits based on actual usage |
| `execute_kubectl` | Execute a kubectl command from natural language description |
| `drain_node` | Safely drain a node for maintenance |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/clusters/{cluster}/status` | Get cluster health status |
| `POST` | `/api/v1/clusters/{cluster}/diagnose` | Diagnose pod/node issues |
| `POST` | `/api/v1/clusters/{cluster}/deployments/{name}/rollback` | Rollback deployment |
| `POST` | `/api/v1/clusters/{cluster}/scale` | Scale workload |
| `POST` | `/api/v1/clusters/{cluster}/optimize` | Get resource optimization recommendations |
| `POST` | `/api/v1/kubectl` | Natural language kubectl execution |
| `POST` | `/api/v1/clusters/{cluster}/nodes/{node}/drain` | Drain node |

## Features

- Cluster Monitoring
- Pod Remediation
- Deployment Management
- Resource Optimization
- Kubectl Nl

## Integrations

- Kubernetes Api
- Prometheus
- Grafana
- Pagerduty

## Architecture

```
kubernetes-operations-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── kubernetes_operations_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 7 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 7 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Kubernetes API + LLM**

---

Built as part of the Enterprise AI Agent Platform.
