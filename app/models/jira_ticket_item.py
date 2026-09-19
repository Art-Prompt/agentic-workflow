from dataclasses import dataclass, field


@dataclass
class JiraTicketItem:
    name: str
    paragraphs: list[str] = field(default_factory=list)
