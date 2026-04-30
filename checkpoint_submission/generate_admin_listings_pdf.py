import os
import sys
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'draftscout.settings')

import django

django.setup()

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

from scouting.models import Player, ScoutingReport, SkillGrade, Team

output_file = 'checkpoint_submission/admin_record_listings.pdf'
doc = SimpleDocTemplate(output_file, pagesize=letter)
styles = getSampleStyleSheet()

story = []

story.append(Paragraph('2026 NBA Draft Scouting Database', styles['Title']))
story.append(Paragraph('Django Admin Record Listings (Mock Data)', styles['Heading2']))
story.append(Paragraph(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', styles['Normal']))
story.append(Spacer(1, 18))


def listing_page(title, headers, rows):
    story.append(Paragraph(f'Admin Listing: {title}', styles['Heading1']))
    story.append(Spacer(1, 8))

    data = [headers] + rows
    table = Table(data, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0f172a')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]
        )
    )
    story.append(table)
    story.append(PageBreak())


team_rows = [[str(t.id), t.name, t.conference, t.country] for t in Team.objects.all()]
listing_page('Teams', ['ID', 'Name', 'Conference', 'Country'], team_rows)

player_rows = [
    [str(p.id), f'{p.first_name} {p.last_name}', p.position, p.team.name, str(p.projected_pick), str(p.age)]
    for p in Player.objects.select_related('team').all()
]
listing_page('Players', ['ID', 'Name', 'Position', 'Team', 'Projected Pick', 'Age'], player_rows)

report_rows = [
    [str(r.id), str(r.player), r.nba_comparison, r.updated_at.strftime('%Y-%m-%d')]
    for r in ScoutingReport.objects.select_related('player').all()
]
listing_page('Scouting Reports', ['ID', 'Player', 'NBA Comparison', 'Updated'], report_rows)

grade_rows = [
    [
        str(g.id),
        str(g.report.player),
        str(g.shooting),
        str(g.defense),
        str(g.athleticism),
        str(g.overall_grade),
    ]
    for g in SkillGrade.objects.select_related('report__player').all()
]
listing_page('Skill Grades', ['ID', 'Player', 'Shooting', 'Defense', 'Athleticism', 'Overall'], grade_rows)

if story and isinstance(story[-1], PageBreak):
    story.pop()

doc.build(story)
print(f'Generated {output_file}')
