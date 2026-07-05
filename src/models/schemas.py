"""Kubernetes Operations Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class ClusterStatus(BaseModel):
    """ClusterStatus for Kubernetes Operations Agent."""
    cluster: str
    nodes_ready: int
    nodes_total: int
    pods_running: int
    pods_failing: int
    resource_utilization: dict


class PodDiagnosis(BaseModel):
    """PodDiagnosis for Kubernetes Operations Agent."""
    pod_name: str
    namespace: str
    status: str
    root_cause: str
    events: list[dict]
    recommendation: str


class ResourceRecommendation(BaseModel):
    """ResourceRecommendation for Kubernetes Operations Agent."""
    namespace: str
    workload: str
    current_cpu: str
    recommended_cpu: str
    current_memory: str
    recommended_memory: str
    savings_percent: float

