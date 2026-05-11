#!/usr/bin/env python3
"""Generate Journal of Computational Social Science (JCSS) submission documents.

JCSS = Springer Nature, IF 2.3, single-blind peer review.
Transfer from SSR (Elsevier) / Electoral Studies (Elsevier).

Documents:
  1. Cover letter (mentioning transfer + computational social science framing)
  2. Title page (author info, acknowledgments, abstract, keywords)
"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from datetime import date

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'submission_jcss')
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
        'Prof. Takashi Kamihigashi',
        'Editor-in-Chief',
        'Journal of Computational Social Science',
        'Springer Nature',
    ]
    for line in lines:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph('')

    p = doc.add_paragraph('Dear Prof. Kamihigashi,')
    p.paragraph_format.space_after = Pt(12)

    paragraphs = [
        'We are pleased to submit our manuscript entitled "Trust-Adjusted Transparent Scoring '
        'with Unified Knowledge Integration (TATSUKI): An Agent-Based Computational Model of '
        'Accountability-Driven Electoral Reform with Empirical Calibration" for consideration '
        'for publication in the Journal of Computational Social Science.',

        'This paper introduces a novel computational framework for evaluating electoral '
        'accountability mechanisms. TATSUKI formalizes the informal retrospective voting '
        'mechanism into an institutional design in which candidates\u2019 pre-declared policy '
        'pledges are systematically evaluated post-term, yielding a continuous trust coefficient '
        'that modulates effective electoral support. Using an agent-based model (ABM) compliant '
        'with the ODD protocol, we simulate multi-generational electoral dynamics under this '
        'mechanism, examining equilibrium outcomes, evolutionary candidate-type selection, and '
        'adversarial robustness via genetic-algorithm search. The model is calibrated against '
        'empirical pledge-fulfillment data from two large-scale databases, bridging computational '
        'modeling with real-world political data.',

        'We believe this manuscript is particularly well-suited for JCSS for four reasons. '
        'First, the core methodology\u2014agent-based modeling with evolutionary dynamics and '
        'adversarial robustness testing via genetic algorithms\u2014represents a distinctly '
        'computational approach to institutional design evaluation that aligns with the '
        'journal\u2019s interdisciplinary scope. Second, the empirical calibration using '
        'large-scale pledge-fulfillment databases (the Polimeter project with 1,050 coded '
        'promises and the Thomson et al. Comparative Party Pledges Database with 20,000+ '
        'pledges across 12 countries) demonstrates the integration of computational modeling '
        'with real-world data that characterizes leading work in computational social science. '
        'Third, the paper addresses a fundamental structural problem in democratic '
        'governance\u2014the temporal mismatch between intermittent electoral feedback and '
        'continuous governance\u2014through a computational lens that invites both theoretical '
        'analysis and empirical validation. Fourth, the computational methodology '
        'itself\u2014combining ABM, empirical calibration, and algorithmic adversarial '
        'testing\u2014offers a replicable template for evaluating institutional design '
        'proposals, which we believe will be of broad interest to the JCSS readership.'

        'The paper makes six specific contributions: (i) the formal specification of the TATSUKI '
        'mechanism and its family of influence functions; (ii) theoretical analysis of incentive '
        'compatibility and manipulation resistance; (iii) an ODD-compliant ABM demonstrating '
        'evolutionary selection for sincere candidates; (iv) adversarial robustness analysis using '
        'genetic algorithms; (v) systematic comparison with existing reform proposals (quadratic '
        'voting, liquid democracy, futarchy, Democratic AI); and (vi) empirical calibration and '
        'counterfactual analysis using real-world pledge fulfillment data.',

        'The manuscript has not been published previously and is not under consideration for '
        'publication elsewhere. All authors have read and approved the submitted manuscript.',

        'We look forward to your editorial decision.',
    ]

    for para in paragraphs:
        p = doc.add_paragraph(para)
        p.paragraph_format.space_after = Pt(12)

    # Closing
    p = doc.add_paragraph('Sincerely,')
    p.paragraph_format.space_after = Pt(24)

    p = doc.add_paragraph('[Author Name]')
    p.paragraph_format.space_after = Pt(0)
    p = doc.add_paragraph('[Institutional Affiliation]')
    p.paragraph_format.space_after = Pt(0)
    p = doc.add_paragraph('[Email Address]')
    p.paragraph_format.space_after = Pt(0)

    path = os.path.join(OUT_DIR, 'Cover_Letter_JCSS.docx')
    doc.save(path)
    print(f'Cover letter saved to {path}')


# ══════════════════════════════════════════════
# 2. Title Page (JCSS requires separate title page with author info)
# ══════════════════════════════════════════════
def create_title_page():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5

    # Title
    p = doc.add_paragraph()
    run = p.add_run(
        'Trust-Adjusted Transparent Scoring with Unified Knowledge Integration (TATSUKI):\n'
        'An Agent-Based Computational Model of Accountability-Driven Electoral Reform\n'
        'with Empirical Calibration'
    )
    run.bold = True
    run.font.size = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(24)

    # Author info
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('[Author Name]')
    run.font.size = Pt(12)
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('[Institutional Affiliation, City, Country]')
    run.font.size = Pt(11)
    run.italic = True
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('Email: [email@example.com]')
    run.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('ORCID: [0000-0000-0000-0000]')
    run.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('Google Scholar: [URL]')
    run.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(24)

    # Corresponding author
    p = doc.add_paragraph()
    run = p.add_run('Corresponding author: ')
    run.bold = True
    p.add_run('[Author Name], [email@example.com]')
    p.paragraph_format.space_after = Pt(18)

    # Word count and figures/tables
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
    p.add_run('0')
    p.paragraph_format.space_after = Pt(18)

    # Acknowledgments (JCSS: on title page)
    p = doc.add_paragraph()
    run = p.add_run('Acknowledgments')
    run.bold = True
    run.font.size = Pt(13)
    p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph(
        'The author gratefully acknowledges the Polimeter project team at Universit\u00e9 Laval '
        'for making their pledge fulfillment data publicly available, which enabled the empirical '
        'calibration component of this study.'
    )

    path = os.path.join(OUT_DIR, 'Title_Page_JCSS.docx')
    doc.save(path)
    print(f'Title page saved to {path}')


# ══════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════
if __name__ == '__main__':
    create_cover_letter()
    create_title_page()
    print('All JCSS submission documents generated.')
