"""Phase 2 — second pass: parent-workspace paths and Drive mirror paths."""
from pathlib import Path

DST = Path(r"C:\RAUL")

FILES_TO_FIX = [
    DST / "04-system/01-config/CLAUDE.md",
    DST / "04-system/01-config/CONTEXT.md",
    DST / "04-system/02-agents/content-supply-chain/RUNBOOK_Raul_Global.md",
    DST / "04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md",
    DST / "04-system/02-agents/conceptual/celeste.md",
    DST / "04-system/02-agents/conceptual/oz.md",
    DST / "04-system/02-agents/conceptual/renzo.md",
    DST / "04-system/02-agents/conceptual/_roster.md",
    DST / ".claude/agents/celeste/AGENT.md",
    DST / ".claude/agents/oz/AGENT.md",
    DST / ".claude/agents/renzo/AGENT.md",
]

# Longer specific patterns first (match before the shorter prefix)
REPLACEMENTS = [
    # Google Drive mirror
    ("G:\\Mi unidad\\WorkspaceIA\\Team Inbox\\", "G:\\Mi unidad\\RAUL\\01-inbox\\01-owner-to-raul\\"),
    ("G:\\Mi unidad\\WorkspaceIA\\Owner Inbox\\", "G:\\Mi unidad\\RAUL\\01-inbox\\02-deliverables-to-owner\\"),
    ("G:\\Mi unidad\\WorkspaceIA\\RAG_SOURCES\\", "G:\\Mi unidad\\RAUL\\01-inbox\\03-raw-sources\\"),
    ("G:\\Mi unidad\\WorkspaceIA\\Staging\\", "G:\\Mi unidad\\RAUL\\01-inbox\\03-raw-sources\\"),
    ("G:\\Mi unidad\\WorkspaceIA\\Knowledge Base\\", "G:\\Mi unidad\\RAUL\\02-knowledge-base\\"),
    ("G:\\Mi unidad\\WorkspaceIA\\Assets\\", "G:\\Mi unidad\\RAUL\\02-knowledge-base\\02-domains\\01-genteca\\assets\\"),
    ("G:\\Mi unidad\\WorkspaceIA\\", "G:\\Mi unidad\\RAUL\\"),
    # Parent workspace local (c:\WorkspaceIA\)
    ("c:\\WorkspaceIA\\Team Inbox\\", "C:\\RAUL\\01-inbox\\01-owner-to-raul\\"),
    ("c:\\WorkspaceIA\\Owner Inbox\\", "C:\\RAUL\\01-inbox\\02-deliverables-to-owner\\"),
    ("c:\\WorkspaceIA\\RAG_SOURCES\\", "C:\\RAUL\\01-inbox\\03-raw-sources\\"),
    ("c:\\WorkspaceIA\\Staging\\", "C:\\RAUL\\01-inbox\\03-raw-sources\\"),
    ("c:\\WorkspaceIA\\TEMP\\", "C:\\RAUL\\01-inbox\\03-raw-sources\\"),
    ("c:\\WorkspaceIA\\TRIGGERS\\", "C:\\RAUL\\04-system\\04-tools-and-scripts\\"),
    ("c:\\WorkspaceIA\\_ARCHIVE\\", "C:\\RAUL\\05-archive\\"),
    ("C:\\WorkspaceIA\\Team Inbox\\", "C:\\RAUL\\01-inbox\\01-owner-to-raul\\"),
    ("C:\\WorkspaceIA\\Owner Inbox\\", "C:\\RAUL\\01-inbox\\02-deliverables-to-owner\\"),
    ("C:\\WorkspaceIA\\RAG_SOURCES\\", "C:\\RAUL\\01-inbox\\03-raw-sources\\"),
    ("C:\\WorkspaceIA\\Staging\\", "C:\\RAUL\\01-inbox\\03-raw-sources\\"),
]

def main():
    total = 0
    for f in FILES_TO_FIX:
        if not f.exists():
            print(f"SKIP: {f}")
            continue
        content = f.read_text(encoding="utf-8")
        edits = 0
        for old, new in REPLACEMENTS:
            occ = content.count(old)
            if occ:
                content = content.replace(old, new)
                edits += occ
        if edits:
            f.write_text(content, encoding="utf-8")
            print(f"{f.relative_to(DST)}: {edits}")
            total += edits
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
