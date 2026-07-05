#!/bin/bash
set -euo pipefail
echo "Setting up Kubernetes Operations Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
