"""Kubernetes Operations Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_get_cluster_status():
    """Test Get comprehensive cluster health status."""
    tools = AgentTools()
    result = await tools.get_cluster_status(cluster="test", include_metrics=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_diagnose_pod_failure():
    """Test Diagnose why a pod is in CrashLoopBackOff or Pending state."""
    tools = AgentTools()
    result = await tools.diagnose_pod_failure(namespace="test", pod_name="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_rollback_deployment():
    """Test Rollback a deployment to a previous revision."""
    tools = AgentTools()
    result = await tools.rollback_deployment(namespace="test", deployment="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_scale_workload():
    """Test Scale a deployment, statefulset, or HPA."""
    tools = AgentTools()
    result = await tools.scale_workload(namespace="test", resource_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.kubernetes_operations_agent_agent import KubernetesOperationsAgentAgent
    agent = KubernetesOperationsAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
