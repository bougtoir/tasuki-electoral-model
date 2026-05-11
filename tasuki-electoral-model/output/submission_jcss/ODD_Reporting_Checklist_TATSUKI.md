# ODD Protocol Reporting Checklist for TATSUKI Paper

**Guideline**: ODD (Overview, Design concepts, Details) Protocol, Version 2020
**Reference**: Grimm, V. et al. (2020) "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism." *Journal of Artificial Societies and Social Simulation*, 23(2), 7. https://doi.org/10.18564/jasss.4259

**Note**: JCSS does not mandate a specific reporting checklist for ABM papers, but the ODD protocol is the *de facto* standard for describing agent-based models. This checklist follows the ODD 2020 version (Grimm et al., 2020) and is applied to the TATSUKI manuscript.

---

## Element 1: Purpose and Patterns

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 1.1 | Purpose of the model clearly stated | Sect. 4.1 | [x] |
| 1.2 | Key questions or hypotheses the model addresses | Sect. 4.1 (i)-(iv) | [x] |
| 1.3 | Patterns used as criteria for evaluating model's purpose | Sect. 4.1 ("gradual accountability improvement") | [x] |
| 1.4 | Rationale for why ABM is appropriate methodology | Sect. 1 (Introduction) + Sect. 6.2 | [x] |

## Element 2: Entities, State Variables, and Scales

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 2.1 | All entity types listed (agents, spatial units, environment, etc.) | Sect. 4.2 | [x] |
| 2.2 | State variables for each entity type described | Sect. 4.2 (candidates: type, pledge portfolio, accountability score, trust coefficient; voters: preferences, location) | [x] |
| 2.3 | Temporal scales (time step, simulation duration) | Sect. 4.2 (30 electoral cycles) | [x] |
| 2.4 | Spatial scales (if applicable) | N/A (non-spatial model) | [x] |
| 2.5 | Units of state variables specified | Sect. 4.2 + Sect. 3.4 | [x] |

## Element 3: Process Overview and Scheduling

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 3.1 | All processes (actions) listed | Sect. 4.3 (6-phase cycle) | [x] |
| 3.2 | Order of execution specified | Sect. 4.3 (pledge declaration → election → term → evaluation → scoring → trust update) | [x] |
| 3.3 | Scheduling (synchronous vs. asynchronous) described | Sect. 4.3 | [x] |

## Element 4: Design Concepts

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 4.1 | **Basic principles**: Underlying theories or hypotheses | Sect. 3 (TATSUKI Model) + Sect. 2.1 (retrospective voting) | [x] |
| 4.2 | **Emergence**: Which model results emerge vs. are imposed | Sect. 4.4 (accountability improvement, candidate type evolution are emergent) | [x] |
| 4.3 | **Adaptation**: How agents change behavior in response to environment | Sect. 4.4 (strategic candidates adapt pledges; evolutionary selection of types) | [x] |
| 4.4 | **Objectives**: If agents have objectives, what are they and how measured | Sect. 4.4 (candidates: maximize re-election probability; voters: maximize welfare) | [x] |
| 4.5 | **Learning**: Whether and how agents learn | Sect. 4.4 | [ ] |
| 4.6 | **Prediction**: How agents predict future conditions | Sect. 4.4 | [ ] |
| 4.7 | **Sensing**: What information agents have access to | Sect. 4.4 (voters observe trust coefficients; candidates observe election outcomes) | [x] |
| 4.8 | **Interaction**: How agents interact (direct/indirect) | Sect. 4.4 (indirect via elections; trust coefficients as public information) | [x] |
| 4.9 | **Stochasticity**: Role of randomness in the model | Sect. 4.4 (fulfillment scores drawn from Beta distributions; voter noise) | [x] |
| 4.10 | **Collectives**: Whether agents form groups | Sect. 4.4 | [ ] |
| 4.11 | **Observation**: How data are collected from the ABM | Sect. 4.4 + Sect. 5.1 (50 replications, random seeds) | [x] |

## Element 5: Initialization

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 5.1 | Initial conditions described | Sect. 4.5 | [x] |
| 5.2 | Initial values of state variables specified | Sect. 4.5 (equal proportions of 3 candidate types; τ₀ = 1.0) | [x] |
| 5.3 | Rationale for initial conditions | Sect. 4.5 | [x] |

## Element 6: Input Data

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 6.1 | External data used as input described | Sect. 5.5 (Polimeter data, Thomson et al.) | [x] |
| 6.2 | Source and accessibility of input data stated | Sect. 5.5.1 + Data Availability Statement | [x] |

## Element 7: Submodels

| # | Item | Manuscript Section | Status |
|---|------|-------------------|--------|
| 7.1 | Each submodel described in detail | Sect. 4.6-4.7 + Sect. 3.2-3.7 | [x] |
| 7.2 | Parameter values and their sources specified | Sect. 4.6 + Sect. 5.5.2 | [x] |
| 7.3 | Rationale for submodel design choices | Throughout Sect. 3-4 | [x] |

---

## Additional JCSS/Springer Requirements

| # | Item | Section | Status |
|---|------|---------|--------|
| A.1 | Abstract: 150-250 words, no undefined abbreviations, no unspecified references | Abstract (189 words) | [x] |
| A.2 | Keywords: 4-6 items | Keywords (6 items) | [x] |
| A.3 | Decimal headings (max 3 levels) | Throughout | [x] |
| A.4 | All figures cited in text in consecutive order before appearance | Fig. 1-7 | [x] |
| A.5 | Figure captions: "**Fig. N**" in bold, no trailing punctuation | All captions | [x] |
| A.6 | References: numbered [1]-[30] in order of first appearance | References | [x] |
| A.7 | References: APA format with DOIs as full URLs | References | [x] |
| A.8 | Statements and Declarations (Competing Interests) | Statements and Declarations | [x] |
| A.9 | Data Availability Statement | Data Availability Statement | [x] |
| A.10 | Acknowledgments on title page | Title Page | [x] |
| A.11 | Author ORCID and Google Scholar URL | Title Page + Manuscript | [x] |
| A.12 | Footnotes instead of endnotes | N/A (no footnotes used) | [x] |

---

## Simulation Experiment Documentation (ODD Supplement S7)

| # | Item | Section | Status |
|---|------|---------|--------|
| S.1 | Experimental design clearly described | Sect. 5.1 | [x] |
| S.2 | Number of replications stated | Sect. 5.1 (50 replications) | [x] |
| S.3 | Random seed handling described | Sect. 5.1 (different random seeds) | [x] |
| S.4 | Parameter ranges for sensitivity analysis specified | Sect. 5.3 (τ_min, τ_max parameter space) | [x] |
| S.5 | Output variables and metrics defined | Sect. 5.1-5.4 | [x] |
| S.6 | Validation against empirical data | Sect. 5.5 (Polimeter + Thomson et al.) | [x] |

---

## Summary

- **Total items**: 38
- **Addressed**: 35
- **Not explicitly addressed**: 3 (Learning 4.5, Prediction 4.6, Collectives 4.10)
- **Note**: Items 4.5, 4.6, 4.10 are marked as not explicitly addressed. Per ODD guidelines, if a design concept does not apply to the model, the description should state "N/A" or briefly explain why it is not relevant. Consider adding a brief note in Sect. 4.4 to address these.
