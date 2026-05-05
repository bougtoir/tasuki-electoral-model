#!/usr/bin/env python3
"""Generate submission documents for SSR, SSH Open, and JCSS (cover letters, title page, highlights, declarations)."""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from datetime import date

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'submission')
os.makedirs(OUT_DIR, exist_ok=True)

TITLE = (
    'Trust-Adjusted Transparent Scoring with Unified Knowledge Integration (TATSUKI):\n'
    'An Agent-Based Computational Model of Accountability-Driven Electoral Reform\n'
    'with Empirical Calibration'
)


def _make_doc():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.15
    return doc


# ══════════════════════════════════════════════
# 1. SSR Cover Letter
# ══════════════════════════════════════════════
def create_cover_letter_ssr():
    doc = _make_doc()
    today = date.today().strftime('%B %d, %Y')

    p = doc.add_paragraph(today)
    p.paragraph_format.space_after = Pt(12)

    for line in ['The Editor', 'Social Science Research', 'Elsevier']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph('')

    p = doc.add_paragraph('Dear Editor,')
    p.paragraph_format.space_after = Pt(12)

    paragraphs = [
        'We are pleased to submit our manuscript entitled "Trust-Adjusted Transparent Scoring '
        'with Unified Knowledge Integration (TATSUKI): An Agent-Based Computational Model of '
        'Accountability-Driven Electoral Reform with Empirical Calibration" for consideration '
        'for publication in Social Science Research.',

        'This paper introduces TATSUKI, a novel electoral mechanism that links candidate trust '
        'coefficients to measured policy fulfillment through influence functions, creating '
        'continuous accountability incentives within representative democracy. Using an agent-based '
        'model compliant with the ODD protocol, we simulate multi-generational electoral dynamics '
        'and demonstrate that TATSUKI raises accountability levels, selects for sincere candidates, '
        'and exhibits robustness to adversarial exploitation discovered via genetic algorithm search.',

        'We believe this work is well-suited for Social Science Research for three reasons. '
        'First, the paper combines formal theoretical modeling with empirical calibration using '
        'real-world data\u2014the Polimeter project (1,050 coded promises from the Trudeau government '
        'across three Canadian parliamentary terms, 2015\u20132025) and cross-national benchmarks from '
        'Thomson et al. (2017; 20,000+ pledges across 12 countries). This integration of '
        'computational methods with empirical social science data aligns with SSR\u2019s emphasis on '
        'rigorous quantitative social science research. Second, the counterfactual analysis applying '
        'TATSUKI to real-world data demonstrates the mechanism\u2019s empirical plausibility. Third, '
        'the topic of electoral accountability and institutional design is of broad interest to SSR\u2019s '
        'interdisciplinary readership.',

        'Key contributions include: (i) a formal specification of the TATSUKI mechanism with a family '
        'of influence functions; (ii) an ODD-compliant agent-based model demonstrating effects on '
        'accountability, candidate-type evolution, and voter welfare; (iii) adversarial robustness '
        'analysis using genetic algorithms; and (iv) empirical calibration with counterfactual '
        'trust trajectory analysis.',

        'The manuscript has not been published elsewhere and is not under consideration by any '
        'other journal. All authors have approved the manuscript and agree with its submission '
        'to Social Science Research. The authors declare no competing interests.',

        'We confirm that this submission complies with the journal\u2019s double-blind review '
        'policy: the manuscript contains no author-identifying information.',

        'Thank you for considering our submission. We look forward to receiving your decision.',
    ]

    for text in paragraphs:
        p = doc.add_paragraph(text)
        p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph('')
    for line in ['Sincerely,', '', '[Corresponding Author Name]', '[Affiliation]',
                 '[Email Address]', '[ORCID]']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)

    out = os.path.join(OUT_DIR, 'Cover_Letter_SSR.docx')
    doc.save(out)
    print(f'SSR cover letter saved to {out}')


# ══════════════════════════════════════════════
# 2. SSH Open Cover Letter
# ══════════════════════════════════════════════
def create_cover_letter_ssh_open():
    doc = _make_doc()
    today = date.today().strftime('%B %d, %Y')

    p = doc.add_paragraph(today)
    p.paragraph_format.space_after = Pt(12)

    for line in ['The Editor', 'Social Sciences & Humanities Open', 'Elsevier']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph('')

    p = doc.add_paragraph('Dear Editor,')
    p.paragraph_format.space_after = Pt(12)

    paragraphs = [
        'We are pleased to submit our manuscript entitled "Trust-Adjusted Transparent Scoring '
        'with Unified Knowledge Integration (TATSUKI): An Agent-Based Computational Model of '
        'Accountability-Driven Electoral Reform with Empirical Calibration" for consideration '
        'for publication in Social Sciences & Humanities Open.',

        'This paper introduces TATSUKI, a novel electoral mechanism bridging political science, '
        'computational social science, and mechanism design. Candidates pre-declare weighted policy '
        'pledges, an independent body evaluates fulfillment at term end, and the resulting '
        'accountability score modulates a candidate-level trust coefficient that influences '
        'subsequent elections. Using an ODD-compliant agent-based model calibrated with empirical '
        'pledge fulfillment data (Polimeter project, 1,050 promises; Thomson et al., 20,000+ '
        'cross-national pledges), we demonstrate that TATSUKI significantly improves accountability '
        'and selects for sincere candidates.',

        'We believe this work is particularly well-suited for Social Sciences & Humanities Open '
        'for three reasons. First, the paper is genuinely interdisciplinary, integrating '
        'computational modeling, political science theory, mechanism design, and empirical data '
        'analysis\u2014exactly the kind of cross-disciplinary work that SSH Open welcomes. Second, '
        'the methodology combines agent-based simulation with real-world calibration and '
        'counterfactual analysis, demonstrating methodological innovation. Third, the topic '
        'addresses fundamental questions about democratic governance that span the social sciences '
        'and humanities.',

        'The manuscript has not been published elsewhere and is not under consideration by any '
        'other journal. All authors have approved the manuscript. The authors declare no competing '
        'interests.',

        'We confirm compliance with the journal\u2019s double-blind review policy.',

        'Thank you for considering our submission.',
    ]

    for text in paragraphs:
        p = doc.add_paragraph(text)
        p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph('')
    for line in ['Sincerely,', '', '[Corresponding Author Name]', '[Affiliation]',
                 '[Email Address]', '[ORCID]']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)

    out = os.path.join(OUT_DIR, 'Cover_Letter_SSH_Open.docx')
    doc.save(out)
    print(f'SSH Open cover letter saved to {out}')


# ══════════════════════════════════════════════
# 3. JCSS Cover Letter (single-blind)
# ══════════════════════════════════════════════
def create_cover_letter_jcss():
    doc = _make_doc()
    today = date.today().strftime('%B %d, %Y')

    p = doc.add_paragraph(today)
    p.paragraph_format.space_after = Pt(12)

    for line in ['The Editor', 'Journal of Computational Social Science', 'Springer']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph('')

    p = doc.add_paragraph('Dear Editor,')
    p.paragraph_format.space_after = Pt(12)

    paragraphs = [
        'We are pleased to submit our manuscript entitled "Trust-Adjusted Transparent Scoring '
        'with Unified Knowledge Integration (TATSUKI): An Agent-Based Computational Model of '
        'Accountability-Driven Electoral Reform with Empirical Calibration" for consideration '
        'for publication in the Journal of Computational Social Science.',

        'This paper makes a contribution to computational social science by introducing TATSUKI, '
        'a novel electoral mechanism, and analyzing its properties through agent-based modeling '
        'and genetic algorithm-based adversarial analysis. The computational contributions include: '
        '(i) an ODD-protocol compliant agent-based model simulating multi-generational electoral '
        'dynamics with heterogeneous candidate types; (ii) systematic parameter space exploration '
        'across a family of influence functions; (iii) adversarial robustness testing using genetic '
        'algorithm search to discover exploitation strategies; and (iv) empirical calibration using '
        'real-world pledge fulfillment data from the Polimeter project (1,050 promises across three '
        'Canadian parliamentary terms) and the Thomson et al. cross-national database (20,000+ '
        'pledges, 12 countries).',

        'We believe this work aligns well with JCSS\u2019s scope and evaluation criteria. The paper '
        'presents new empirical results derived from computational simulations, introduces a novel '
        'theoretical and methodological framework for computational analysis of electoral systems, '
        'and contributes reusable simulation software. The agent-based model produces emergent '
        'dynamics\u2014including evolutionary selection pressure favoring sincere candidates and '
        'robustness patterns across influence function families\u2014that would be difficult to derive '
        'analytically, demonstrating the value of computational approaches to social science questions.',

        'The counterfactual analysis applying TATSUKI retrospectively to empirical Canadian data '
        'demonstrates that computational models can generate interpretable, policy-relevant insights '
        'when calibrated with real-world data.',

        'The manuscript has not been published elsewhere and is not under consideration by any '
        'other journal. All authors have approved the manuscript. The authors declare no competing '
        'interests.',

        'The simulation code and calibration scripts will be made available in a public repository '
        'upon acceptance.',

        'Thank you for considering our submission. We look forward to receiving your decision.',
    ]

    for text in paragraphs:
        p = doc.add_paragraph(text)
        p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph('')
    for line in ['Sincerely,', '', '[Corresponding Author Name]', '[Affiliation]',
                 '[Email Address]', '[ORCID]']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)

    out = os.path.join(OUT_DIR, 'Cover_Letter_JCSS.docx')
    doc.save(out)
    print(f'JCSS cover letter saved to {out}')


# ══════════════════════════════════════════════
# 4. Title Page (shared across journals; anonymized for double-blind)
# ══════════════════════════════════════════════
def create_title_page():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5

    p = doc.add_paragraph()
    run = p.add_run(TITLE)
    run.bold = True
    run.font.size = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(24)

    # Authors
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('[Author 1 Name]')
    run.font.size = Pt(12)
    run = p.add_run('a')
    run.font.superscript = True
    run = p.add_run('*')
    run.font.superscript = True
    p.paragraph_format.space_after = Pt(12)

    # Affiliations
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('a')
    run.font.superscript = True
    run = p.add_run(' [Affiliation, City, Country]')
    run.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(24)

    # Corresponding author
    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('* Corresponding author:')
    run.bold = True
    p.paragraph_format.space_after = Pt(3)

    for line in ['Email: [email@example.com]', 'Address: [Full postal address]',
                 'ORCID: [0000-0000-0000-0000]']:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(1.0)

    # Word count
    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Word count: ')
    run.bold = True
    p.add_run('approximately 9,500 words (excluding references and figure captions)')

    p = doc.add_paragraph()
    run = p.add_run('Number of figures: ')
    run.bold = True
    p.add_run('7')

    p = doc.add_paragraph()
    run = p.add_run('Number of tables: ')
    run.bold = True
    p.add_run('0')
    p.paragraph_format.space_after = Pt(12)

    # Acknowledgments
    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Acknowledgments')
    run.bold = True
    p.paragraph_format.space_after = Pt(6)
    doc.add_paragraph(
        '[Add acknowledgments here. Note: acknowledgments are placed on the title page '
        'to maintain double-anonymized review of the main manuscript.]')

    # Funding
    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Funding')
    run.bold = True
    p.paragraph_format.space_after = Pt(6)
    doc.add_paragraph(
        'This research did not receive any specific grant from funding agencies '
        'in the public, commercial, or not-for-profit sectors.')

    out = os.path.join(OUT_DIR, 'Title_Page.docx')
    doc.save(out)
    print(f'Title page saved to {out}')


# ══════════════════════════════════════════════
# 5. Highlights (SSR requires; SSH Open optional)
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

    # 3-5 bullet points, max 85 characters each (SSR requirement)
    highlights = [
        'TATSUKI links candidate trust to measured pledge fulfillment scores.',       # 68 chars
        'Agent-based model shows TATSUKI raises accountability, resists gaming.',     # 70 chars
        'Concave and sigmoid influence functions optimally balance incentives.',       # 69 chars
        'Model calibrated with 1,050 real pledges from Polimeter project data.',      # 70 chars
        'Counterfactual analysis confirms stable trust trajectories empirically.',     # 71 chars
    ]

    for h in highlights:
        p = doc.add_paragraph(h, style='List Bullet')
        p.paragraph_format.space_after = Pt(6)
        if len(h) > 85:
            print(f'  WARNING: Highlight exceeds 85 chars ({len(h)}): {h[:50]}...')
        else:
            print(f'  OK ({len(h)} chars): {h}')

    doc.add_paragraph('')
    p = doc.add_paragraph()
    run = p.add_run('Note: ')
    run.italic = True
    p.add_run('Each highlight must be no more than 85 characters including spaces. '
              'Entered separately during the Editorial Manager submission process.').italic = True

    out = os.path.join(OUT_DIR, 'Highlights.docx')
    doc.save(out)
    print(f'Highlights saved to {out}')


# ══════════════════════════════════════════════
# 6. Declarations
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
        'relationships that could have appeared to influence the work reported in this paper.')

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
        'Visualization.')

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
        'in a public repository upon acceptance.')

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
        'collection. Ethical approval was not required for this research.')

    out = os.path.join(OUT_DIR, 'Declarations.docx')
    doc.save(out)
    print(f'Declarations saved to {out}')


# ══════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════
if __name__ == '__main__':
    create_cover_letter_ssr()
    create_cover_letter_ssh_open()
    create_cover_letter_jcss()
    create_title_page()
    create_highlights()
    create_declarations()
    print('\nAll submission documents created successfully!')
    print(f'Output directory: {OUT_DIR}')
