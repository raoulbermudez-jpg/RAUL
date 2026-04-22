"""Phase 2 migration helper: update residual backslash paths in copied files.

Scope: fix references to old repo/workspace paths in the new /RAUL/ tree,
EXCLUDING files that must preserve historical paths (MIGRATION-PLAN, DECISIONS,
CLAUDE-CODE-RULES, task-log, Python scripts).

Uses regular Python strings with escaped backslashes for file-content matching.
"""
from pathlib import Path

DST = Path(r"C:\RAUL")

FILES_TO_FIX = [
    DST / "04-system/01-config/CLAUDE.md",
    DST / "04-system/01-config/CONTEXT.md",
    DST / "04-system/02-agents/content-supply-chain/RUNBOOK_Raul_Global.md",
    DST / "04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md",
    DST / "04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md",
    DST / "04-system/02-agents/content-supply-chain/AGENTS_Content-Supply-Chain.md",
    DST / "04-system/02-agents/conceptual/celeste.md",
    DST / "04-system/02-agents/conceptual/oz.md",
    DST / "04-system/02-agents/conceptual/renzo.md",
    DST / "04-system/02-agents/conceptual/_roster.md",
    DST / ".claude/agents/celeste/AGENT.md",
    DST / ".claude/agents/oz/AGENT.md",
    DST / ".claude/agents/renzo/AGENT.md",
]

# Regular strings: '\\' = one literal backslash
REPLACEMENTS = [
    ("c:\\WorkspaceIA\\PROJECTS\\Claude code\\", "C:\\RAUL\\"),
    ("C:\\WorkspaceIA\\PROJECTS\\Claude code\\", "C:\\RAUL\\"),
    ("Knowledge Base\\Technical\\", "02-knowledge-base\\02-domains\\01-genteca\\specs\\"),
    ("Knowledge Base\\Market\\", "02-knowledge-base\\02-domains\\01-genteca\\wiki\\market\\"),
    ("Assets\\Products\\", "02-knowledge-base\\02-domains\\01-genteca\\assets\\products\\"),
    ("Assets\\Packaging\\", "02-knowledge-base\\02-domains\\01-genteca\\assets\\packaging\\"),
    ("Assets\\Diagrams\\", "02-knowledge-base\\02-domains\\01-genteca\\assets\\diagrams\\"),
    ("Assets\\Uncoded\\", "02-knowledge-base\\02-domains\\01-genteca\\assets\\uncoded\\"),
    ("\\Owner Inbox\\", "\\01-inbox\\02-deliverables-to-owner\\"),
    ("\\Team inbox\\", "\\01-inbox\\01-owner-to-raul\\"),
]

def main():
    total_edits = 0
    for f in FILES_TO_FIX:
        if not f.exists():
            print(f"SKIP (missing): {f}")
            continue
        content = f.read_text(encoding="utf-8")
        original = content
        file_edits = 0
        for old, new in REPLACEMENTS:
            occurrences = content.count(old)
            if occurrences:
                content = content.replace(old, new)
                file_edits += occurrences
        if content != original:
            f.write_text(content, encoding="utf-8")
            print(f"{f.relative_to(DST)}: {file_edits} replacements")
            total_edits += file_edits
        else:
            print(f"{f.relative_to(DST)}: no changes")
    print(f"\nTotal edits: {total_edits}")

if __name__ == "__main__":
    main()
