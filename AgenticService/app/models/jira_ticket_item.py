from dataclasses import dataclass, field


@dataclass
class JiraTicketItem:
    type: str
    description: str
