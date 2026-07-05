"""Test configuration for Kubernetes Operations Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "kubernetes-operations-agent", "category": "DevOps & Platform Engineering"}
