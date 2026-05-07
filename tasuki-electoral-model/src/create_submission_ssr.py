#!/usr/bin/env python3
"""Generate Social Science Research (SSR) submission documents.

SSR = Elsevier, IF 3.5, double-blind, quantitative social science focus.
Transfer from Electoral Studies (both Elsevier).

Documents:
  1. Cover letter (mentioning transfer + quantitative framing)
  2. Title page (separate for double-blind)
  3. Highlights (3-5 items, ≤85 chars each)
  4. Declarations (COI, CRediT, Data Availability, Ethics)
"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from datetime import date

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'submission_ssr')
os.makedirs(OUT_DIR, exist_ok=True)


# ══════════════════════════════════════════════
# 1. Cover Letter
# ══════════════════════════════════════════════
def create_cover_letter():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.15

    today = date.today().strftime('%B %d, %Y')

    p = doc.add_paragraph(today)
    p.paragraph_format.space_after = Pt(12)

    lines = [
        'The Editors',
        'Social Science Research',
    ]
    for line in lines:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph('')

    p = doc.add_paragraph('Dear Editors,')
    p.paragraph_format.space_after = Pt(12)

    paragraphs = [
        'We are pleased to submit our manuscript entitled "Trust-Adjusted Transparent Scoring '
        'with Unified Knowledge Integration (TATSUKI): An Agent-Based Model of Accountability-Driven '
        'Electoral Reform with Empirical Calibration" for consideration for publication in '
        'Social Science Research. This manuscript was previously submitted to Electoral Studies '
        '(Manuscript No. [to be filled]) and is being transferred via the Elsevier transfer service '
        'at the suggestion of the Editorial Office.',

        'This paper introduces a novel quantitative framework for studying electoral accountability. '
        'TATSUKI formalizes the informal retrospective voting mechanism into an institutional design '
        'in which candidates\u2019 pre-declared policy pledges are systematically evaluated post-term, '
        'yielding a continuous trust coefficient that modulates effective electoral support. '
        'Using an agent-based model (ABM) compliant with the ODD protocol, we simulate '
        'multi-generational electoral dynamics under this mechanism, examining equilibrium outcomes, '
        'evolutionary candidate-type selection, and adversarial robustness.',

        # ── Why this paper is needed now ──
        'We believe this paper addresses a timely gap in the literature. A fundamental structural '
        'limitation of contemporary representative democracy is that citizens can express their '
        'political will only at the moment of voting\u2014typically once every four to five years. '
        'Between elections, voters possess no institutional mechanism to ensure that the promises '
        'motivating their choice are honored. This temporal mismatch between intermittent democratic '
        'feedback and continuous governance is arguably the central structural weakness of modern '
        'representative democracy, and existing reform proposals do not fully resolve it: quadratic '
        'voting enriches preference expression at election time but provides no post-election '
        'accountability; liquid democracy enables continuous re-delegation but does not evaluate '
        'whether delegated decisions align with voters\u2019 preferences; futarchy operates continuously '
        'via prediction markets but replaces democratic decision-making with market-based selection.',

        'Three converging trends now make it possible to address this gap. '
        'First, public trust in democratic '
        'institutions has declined to historic lows across established democracies (OECD, 2022; '
        'Edelman Trust Barometer, 2024), creating urgent demand for institutional mechanisms that '
        'demonstrably link electoral promises to consequences. Second, the empirical infrastructure '
        'for systematic pledge tracking has matured: the Polimeter project now covers multiple '
        'countries and parliamentary terms, and the Comparative Party Pledges Database (Thomson '
        'et al., 2017) spans 20,000+ pledges across 12 countries\u2014making an accountability '
        'mechanism grounded in measured fulfillment technically feasible at scale for the first '
        'time. Third, computational social science methods\u2014particularly agent-based modeling '
        'and adversarial testing\u2014now provide the tools to evaluate institutional reforms '
        'before deployment, a capacity that was unavailable when classical accountability models '
        'were formulated.',

        # ── Comparative positioning ──
        'The manuscript positions TATSUKI explicitly within this landscape. '
        'A structured comparison (Table 1 in the '
        'manuscript) shows that existing proposals\u2014quadratic voting, liquid democracy, futarchy, '
        'and computational democratic mechanism design\u2014address different democratic deficits '
        'but none institutionalizes the retrospective accountability relationship '
        'between pre-election pledges and post-election performance, and none transforms the '
        'voter\u2019s one-time electoral choice into a continuous institutional commitment. '
        'TATSUKI is designed to '
        'fill precisely this gap, and is the only proposal that combines OPOV-compatible design, '
        'empirical calibration with large-scale pledge data, and adversarial robustness testing.',

        'We believe this work is particularly well-suited for Social Science Research for three reasons. '
        'First, the paper demonstrates a quantitative method\u2014agent-based simulation with genetic '
        'algorithm adversarial testing\u2014that cuts across political science, economics, and '
        'computational social science, directly aligning with SSR\u2019s cross-disciplinary mission. '
        'Second, the ABM is calibrated with two large-scale empirical datasets: the Polimeter '
        'pledge-tracking project (1,050 coded promises, three Canadian parliamentary terms, 2015\u20132025) '
        'and the Comparative Party Pledges Database (Thomson et al., 2017; 20,000+ pledges, 12 countries, '
        '57 elections). This grounds the simulation in observable political behavior and enables '
        'counterfactual analysis using real-world data. Third, the methodology\u2014combining mechanism '
        'design, evolutionary ABM, and adversarial analysis\u2014provides a reusable quantitative '
        'toolkit that researchers can adapt to evaluate other institutional reform proposals.',

        'Key contributions include: (i) a formal specification of the TATSUKI mechanism with a family '
        'of influence functions; (ii) an ODD-protocol compliant ABM demonstrating TATSUKI\u2019s effects '
        'on accountability and candidate-type evolution; (iii) adversarial robustness analysis using '
        'genetic algorithm search; (iv) empirical calibration with counterfactual trust trajectory '
        'analysis for a real-world minority government; and (v) a systematic comparative analysis '
        'positioning TATSUKI within the broader landscape of electoral reform proposals.',

        'The manuscript has not been published elsewhere and is not under consideration by any '
        'other journal. All authors have approved the manuscript and agree with its submission '
        'to Social Science Research. The authors declare no competing interests.',

        'We confirm that this submission complies with the journal\u2019s double-anonymized review '
        'policy: the manuscript contains no author-identifying information. Author details are '
        'provided in the separate title page.',

        'Thank you for considering our submission. We look forward to receiving your decision.',
    ]

    for text in paragraphs:
        p = doc.add_paragraph(text)
        p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph('')

    closing_lines = [
        'Sincerely,',
        '',
        '[Corresponding Author Name]',
        '[Affiliation]',
        '[Email Address]',
        '[ORCID]',
    ]
    for line in closing_lines:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)

    out = os.path.join(OUT_DIR, 'Cover_Letter_SSR.docx')
    doc.save(out)
    print(f'Cover letter saved to {out}')


# ══════════════════════════════════════════════
# 2. Title Page (separate for double-blind)
# ══════════════════════════════════════════════
def create_title_page():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5

    p = doc.add_paragraph()
    run = p.add_run(
        'Trust-Adjusted Transparent Scoring with Unified Knowledge Integration (TATSUKI):\n'
        'An Agent-Based Model of Accountability-Driven Electoral Reform\n'
        'with Empirical Calibration'
    )
    run.bold = True
    run.font.size = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(24)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('[Author 1 Name]')
    run.font.size = Pt(12)
    run = p.add_run('a')
    run.font.superscript = True
    run = p.add_run('*')
    run.font.superscript = True
    p.paragraph_format.space_after = Pt(12)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('a')
    run.font.superscript = True
    run = p.add_run(' [Affiliation, City, Country]')
    run.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(24)

    p = doc.add_paragraph()
    run = p.add_run('* Corresponding author:')
    run.bold = True
    p.paragraph_format.space_after = Pt(3)

    info = [
        'Email: [email@example.com]',
        'Address: [Full postal address]',
        'ORCID: [0000-0000-0000-0000]',
    ]
    for line in info:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(1.0)

    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Word count: ')
    run.bold = True
    p.add_run('approximately 9,500 words (excluding references and figure captions)')
    p.paragraph_format.space_after = Pt(3)

    p = doc.add_paragraph()
    run = p.add_run('Number of figures: ')
    run.bold = True
    p.add_run('7')
    p.paragraph_format.space_after = Pt(3)

    p = doc.add_paragraph()
    run = p.add_run('Number of tables: ')
    run.bold = True
    p.add_run('1')
    p.paragraph_format.space_after = Pt(12)

    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Acknowledgments')
    run.bold = True
    p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph(
        '[Add acknowledgments here. Note: acknowledgments are placed on the title page '
        'to maintain double-anonymized review of the main manuscript.]'
    )

    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Funding')
    run.bold = True
    p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph(
        '[Specify funding sources, if any. If none, state: '
        '"This research did not receive any specific grant from funding agencies '
        'in the public, commercial, or not-for-profit sectors."]'
    )

    out = os.path.join(OUT_DIR, 'Title_Page_SSR.docx')
    doc.save(out)
    print(f'Title page saved to {out}')


# ══════════════════════════════════════════════
# 3. Highlights (3-5 items, ≤85 chars each)
# ══════════════════════════════════════════════
def create_highlights():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5

    p = doc.add_paragraph()
    run = p.add_run('Highlights')
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_after = Pt(18)

    highlights = [
        'TATSUKI links candidate trust coefficients to measured pledge fulfillment.',
        'Agent-based model shows TATSUKI raises accountability and resists gaming.',
        'Concave and sigmoid influence functions optimally balance incentives.',
        'Model calibrated with 1,050 real pledges from Polimeter and Thomson data.',
        'Counterfactual analysis confirms stable trust trajectories for Trudeau.',
    ]

    for h in highlights:
        p = doc.add_paragraph(h, style='List Bullet')
        p.paragraph_format.space_after = Pt(6)
        if len(h) > 85:
            print(f'  WARNING: Highlight exceeds 85 chars ({len(h)}): {h[:50]}...')

    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Note: ')
    run.italic = True
    p.add_run(
        'Each highlight must be no more than 85 characters including spaces. '
        'These are entered separately during the Editorial Manager submission process.'
    ).italic = True

    out = os.path.join(OUT_DIR, 'Highlights_SSR.docx')
    doc.save(out)
    print(f'Highlights saved to {out}')


# ══════════════════════════════════════════════
# 4. Declarations
# ══════════════════════════════════════════════
def create_declarations():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5

    # Declaration of Competing Interest
    p = doc.add_paragraph()
    run = p.add_run('Declaration of Competing Interest')
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_after = Pt(12)

    doc.add_paragraph(
        'The authors declare that they have no known competing financial interests or personal '
        'relationships that could have appeared to influence the work reported in this paper.'
    )

    doc.add_paragraph('')

    # CRediT Author Statement
    p = doc.add_paragraph()
    run = p.add_run('CRediT Author Statement')
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_after = Pt(12)

    doc.add_paragraph(
        '[Author 1]: Conceptualization, Methodology, Software, Formal analysis, '
        'Investigation, Data curation, Writing \u2013 Original Draft, Writing \u2013 Review & Editing, '
        'Visualization.'
    )

    doc.add_paragraph('')

    # Data Availability Statement
    p = doc.add_paragraph()
    run = p.add_run('Data Availability Statement')
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_after = Pt(12)

    doc.add_paragraph(
        'The Polimeter data used for empirical calibration are publicly available at '
        'https://polimeter.org. The Thomson et al. (2017) cross-national pledge fulfillment '
        'data are available in the published article (American Journal of Political Science, '
        '61(3), 527\u2013542). The simulation code and calibration scripts will be made available '
        'in a public repository upon acceptance.'
    )

    doc.add_paragraph('')

    # Ethics Statement
    p = doc.add_paragraph()
    run = p.add_run('Ethics Statement')
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_after = Pt(12)

    doc.add_paragraph(
        'This study uses only publicly available aggregate data (Polimeter pledge tracking data '
        'and published cross-national statistics). No human subjects were involved in data '
        'collection. Ethical approval was not required for this research.'
    )

    out = os.path.join(OUT_DIR, 'Declarations_SSR.docx')
    doc.save(out)
    print(f'Declarations saved to {out}')


# ══════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════
if __name__ == '__main__':
    create_cover_letter()
    create_title_page()
    create_highlights()
    create_declarations()
    print('\nAll SSR submission documents created successfully!')
    print(f'Output directory: {OUT_DIR}')
