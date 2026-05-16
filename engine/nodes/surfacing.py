"""SurfacingOption — R1 detached module, default-OFF (charter §1 / 03 R1).

Must NOT be coupled to the primary engine (purpose-pollution guard). Returns a
detached spec only; never auto-invoked.
"""

from __future__ import annotations


def SurfacingOption(enabled: bool = False) -> dict:
    return {
        "enabled": enabled,
        "separation_guard": "MUST NOT couple to primary audit engine",
        "exit_path": "if scale needed -> IDEA-20-01 surfacing variant (separate round)",
        "default": "OFF",
        "active": False if not enabled else True,
    }
