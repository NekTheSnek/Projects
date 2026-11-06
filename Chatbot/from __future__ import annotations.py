from __future__ import annotations
from datetime import datetime
from textwrap import fill

# ===================== ΑΛΛΑΖΕΙΣ ΕΔΩ =====================
FROM_NAME = "Nektaria"
GUILD_NAME = "Guild Wars Friends"

COMMANDER = {
    "name": "Commander",
    "role": "Squad Commander",
    "summary": "Leads with calm clarity and keeps runs organized without ego.",
    "traits": [
        "Clear direction without pressure",
        "Steady and reliable",
        "Protects the squad vibe",
        "Makes new players feel capable",
    ],
    "strengths": [
        "Coordination & positioning",
        "Keeping focus under stress",
        "Reading fights quickly",
    ],
    "impact": [
        "Runs feel safe and structured",
        "People follow calls with trust",
        "The guild feels like a real team",
    ],
    "achievements": [
        ("TAG UP, CALM ON", "When the tag appears, chaos becomes a plan."),
        ("NO ONE LEFT BEHIND", "You make sure everyone stays included."),
        ("MORALE ANCHOR", "You keep the vibe stable—even on wipes."),
    ],
}

QUIET_HERO = {
    "name": "Quiet Hero",
    "role": "The Kind One",
    "summary": "Peaceful, kind, and genuinely likable—helps without needing credit.",
    "traits": [
        "Kindness without showing off",
        "Calm and respectful energy",
        "Supportive by nature",
        "Trusted by everyone",
    ],
    "strengths": [
        "Helping without being asked",
        "Keeping the group comfortable",
        "Consistency and reliability",
    ],
    "impact": [
        "Makes the guild feel like home",
        "Turns random runs into friendly moments",
        "Quietly raises the group’s quality",
    ],
    "achievements": [
        ("QUIET MVP", "Impact without spotlight."),
        ("INSTANT TRUST", "People relax because you’re there."),
        ("SUPPORT AURA", "Small help—big difference."),
    ],
}

SHARED_POINTS = [
    "Different roles, same respect.",
    "One leads the direction — the other protects the atmosphere.",
    "Together you make runs organized and human at the same time.",
]

PERSONAL_NOTE = (
    "Thank you for being the kind of people that make online spaces feel safe and real.\n"
    "This is a small coded gift — a reminder that your presence matters."
)

OUTPUT_FILE = "GW2_Character_Dossier.txt"   # ή .md αν θες
# ========================================================


WIDTH = 74


def line(char="="):
    return char * WIDTH


def title_block(text: str):
    text = text.upper()
    pad = (WIDTH - len(text) - 2)
    left = pad // 2
    right = pad - left
    return f"{' ' * left} {text} {' ' * right}"


def bullet_list(items):
    return "\n".join(f"  • {x}" for x in items)


def achievements(items):
    out = []
    for name, desc in items:
        out.append(f"  ▸ {name}\n    {fill(desc, width=WIDTH-4, subsequent_indent='    ')}")
    return "\n".join(out)


def profile_section(p: dict):
    parts = []
    parts.append(line("="))
    parts.append(title_block(p["name"]))
    parts.append(line("="))
    parts.append(f"ROLE: {p['role']}\n")
    parts.append("SUMMARY:")
    parts.append(fill(p["summary"], width=WIDTH, subsequent_indent=""))
    parts.append("")
    parts.append("TRAITS:")
    parts.append(bullet_list(p["traits"]))
    parts.append("")
    parts.append("STRENGTHS:")
    parts.append(bullet_list(p["strengths"]))
    parts.append("")
    parts.append("IMPACT ON THE GUILD:")
    parts.append(bullet_list(p["impact"]))
    parts.append("")
    parts.append("ACHIEVEMENTS UNLOCKED:")
    parts.append(achievements(p["achievements"]))
    parts.append("")
    return "\n".join(parts)


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    header = [
        line("="),
        title_block("GUILD WARS 2 - CHARACTER DOSSIER"),
        line("="),
        f"GUILD: {GUILD_NAME}",
        f"CREATED: {now}",
        f"FROM: {FROM_NAME}",
        line("-"),
        "PURPOSE:",
        fill(
            "A recognition file describing who they are inside the guild ecosystem: "
            "role, traits, strengths, impact, and earned respect — without dialogues.",
            width=WIDTH,
        ),
        "",
    ]

    shared = [
        line("-"),
        "SHARED IMPACT:",
        bullet_list(SHARED_POINTS),
        "",
        "PERSONAL NOTE:",
        PERSONAL_NOTE,
        "",
        line("="),
    ]

    text = "\n".join(header) + "\n"
    text += profile_section(COMMANDER)
    text += profile_section(QUIET_HERO)
    text += "\n".join(shared)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Έτοιμο! Δημιουργήθηκε το αρχείο: {OUTPUT_FILE}")
    print("➡️ Άνοιξέ το και στείλ’ το σαν δώρο.")


if __name__ == "__main__":
    main()
