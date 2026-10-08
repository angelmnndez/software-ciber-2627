from dataclasses import dataclass
from typing import Optional


@dataclass
class Incident:
    incident_id: str
    alert_id: str
    event_type: str
    severity: str
    source_ip: Optional[str]
    status: str
    created_at: str
    resolved_at: Optional[str] = None
