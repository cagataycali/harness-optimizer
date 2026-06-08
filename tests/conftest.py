"""Shared test fixtures for strands_harness_optimizer tests."""

import pytest


@pytest.fixture
def sample_context():
    """A minimal agent context dict for testing formulas."""
    return {
        "system_prompt": "You are a helpful assistant.",
        "messages": [],
    }
