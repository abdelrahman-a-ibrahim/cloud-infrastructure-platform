"""Proposed application boundary for Terraform & Terragrunt Platform Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class InfrastructureReview:
    def summarize_plan(self, plan: dict) -> dict:
        """Classify destructive changes and identify unreviewed drift."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def validate_inventory(self, resources: list) -> list:
        """Find resources lacking ownership, environment or expiration labels."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

