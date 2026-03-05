# Composition Map

> Interdependency analysis of all skills: explicit dependencies, enhancement relationships, SDLC phase mapping, gap analysis, and composition clusters.

## Methodology

- **Depends on**: Skills explicitly referenced, linked to, or required by this skill's SKILL.md content.
- **Enhances**: Skills this one could layer onto to improve output quality, based on domain overlap.
- **Phase**: Which SDLC phase(s) the skill primarily serves.
- **Type**: `creative-engine` | `discipline` | `router` | `template` (from content-based classification).

---

## Skill Composition Table

### Creative Engines

| Skill | Type | Phase(s) | Depends On | Enhances |
|-------|------|----------|------------|----------|
| algorithmic-art | creative-engine | implementation | — | particles-gpu, shader-fundamentals, shader-noise, canvas-design |
| canvas-design | creative-engine | implementation | — | pptx, pdf, brand-guidelines, slack-gif-creator |
| frontend-design | creative-engine | implementation | — | component-library, form-react, form-vue, form-vanilla, web-artifacts-builder, d3js-visualization |

### Disciplines

| Skill | Type | Phase(s) | Depends On | Enhances |
|-------|------|----------|------------|----------|
| backend-dev-guidelines | discipline | implementation, review | — | aws-skills, mcp-builder, multiplayer-building |
| brainstorming | discipline | requirements, architecture | using-git-worktrees, writing-plans | writing-plans, doc-coauthoring |
| doc-coauthoring | discipline | requirements | — | scientific-documentation, internal-comms, pptx, docx |
| frontend-dev-guidelines | discipline | implementation, review | — | component-library, form-react, web-artifacts-builder, d3js-visualization, r3f-fundamentals |
| software-architecture | discipline | architecture, review | — | mcp-builder, aws-skills, component-library, multiplayer-building |
| subagent-driven-development | discipline | implementation | writing-plans | writing-plans, test-driven-development |
| systematic-debugging | discipline | testing, review | — | all implementation skills |
| test-driven-development | discipline | testing, implementation | — | all implementation skills |
| writing-plans | discipline | architecture | subagent-driven-development | subagent-driven-development, brainstorming |

### Routers

| Skill | Type | Phase(s) | Depends On | Enhances |
|-------|------|----------|------------|----------|
| audio-router | router | implementation | audio-playback, audio-analysis, audio-reactive | postfx-bloom, postfx-effects, particles-gpu, gsap-sequencing, r3f-fundamentals, shader-effects |
| building | router | implementation | performance-at-scale, structural-physics, multiplayer-building, terrain-integration | — |
| building-router | router | implementation, architecture | performance-at-scale, structural-physics, multiplayer-building, terrain-integration, decay-upkeep, builder-ux, platform-building, case-studies-reference | — |
| dashboard | router | implementation | _(internal sub-skills: charts, real-time, filtering)_ | d3js-visualization |
| forms | router | implementation, review | form-accessibility, form-validation, form-security, form-react, form-vue, form-vanilla, form-ux-patterns | — |
| forms-router | router | implementation, review | form-accessibility, form-validation, form-security, form-react, form-vue, form-vanilla, form-ux-patterns | — |
| gsap-router | router | implementation | gsap-fundamentals, gsap-sequencing, gsap-scrolltrigger, gsap-react | r3f-fundamentals, postfx-composer, audio-playback, particles-gpu |
| immersive-visuals-router | router | implementation | r3f-router, shader-router, particles-router, postfx-router, gsap-router, audio-router | — |
| particles-router | router | implementation | particles-gpu, particles-physics, particles-lifecycle | shader-noise, shader-effects |
| postfx-router | router | implementation | postfx-composer, postfx-bloom, postfx-effects | r3f-fundamentals, shader-fundamentals, particles-gpu, audio-analysis |
| r3f-router | router | implementation | r3f-fundamentals, r3f-geometry, r3f-materials, r3f-performance, r3f-drei | — |
| shader-router | router | implementation | shader-fundamentals, shader-noise, shader-sdf, shader-effects | — |

### Templates

| Skill | Type | Phase(s) | Depends On | Enhances |
|-------|------|----------|------------|----------|
| 3d-building-advanced | template | implementation | r3f-fundamentals | structural-physics, terrain-integration |
| audio-analysis | template | implementation | — | audio-reactive, particles-gpu, postfx-bloom |
| audio-playback | template | implementation | — | audio-reactive, audio-analysis |
| audio-reactive | template | implementation | audio-analysis, audio-playback | particles-gpu, postfx-bloom, gsap-sequencing, shader-effects |
| aws-skills | template | environment, deployment | — | mcp-builder |
| brand-guidelines | template | requirements | — | pptx, docx, frontend-design, component-library, theme-factory, web-artifacts-builder, slack-gif-creator |
| builder-ux | template | implementation | — | 3d-building-advanced, structural-physics, multiplayer-building |
| case-studies-reference | template | architecture | — | 3d-building-advanced, structural-physics, multiplayer-building |
| component-library | template | implementation | — | form-react, web-artifacts-builder, d3js-visualization |
| d3js-visualization | template | implementation | — | dashboard |
| decay-upkeep | template | implementation | — | structural-physics, multiplayer-building |
| docx | template | implementation | — | scientific-documentation, internal-comms |
| form-accessibility | template | implementation, review | — | form-react, form-vue, form-vanilla |
| form-react | template | implementation | — | form-ux-patterns |
| form-security | template | implementation, review | — | form-react, form-vue, form-vanilla |
| form-ux-patterns | template | implementation | — | form-react, form-vue, form-vanilla |
| form-validation | template | implementation | — | form-react, form-vue, form-vanilla |
| form-vanilla | template | implementation | — | — |
| form-vue | template | implementation | — | — |
| gsap-fundamentals | template | implementation | — | gsap-react, gsap-sequencing, gsap-scrolltrigger |
| gsap-react | template | implementation | gsap-fundamentals | — |
| gsap-scrolltrigger | template | implementation | gsap-fundamentals | — |
| gsap-sequencing | template | implementation | gsap-fundamentals | — |
| internal-comms | template | implementation | — | doc-coauthoring |
| mcp-builder | template | architecture, implementation | — | — |
| multiplayer-building | template | implementation | — | performance-at-scale, structural-physics |
| particles-gpu | template | implementation | — | particles-physics, particles-lifecycle |
| particles-lifecycle | template | implementation | particles-gpu | — |
| particles-physics | template | implementation | particles-gpu | — |
| pdf | template | implementation | — | scientific-documentation |
| performance-at-scale | template | implementation | — | multiplayer-building, structural-physics, 3d-building-advanced |
| platform-building | template | implementation | — | multiplayer-building, builder-ux |
| postfx-bloom | template | implementation | postfx-composer | r3f-fundamentals, particles-gpu, audio-reactive |
| postfx-composer | template | implementation | — | postfx-bloom, postfx-effects |
| postfx-effects | template | implementation | postfx-composer | r3f-fundamentals, particles-gpu |
| pptx | template | implementation | — | internal-comms, scientific-documentation |
| product-self-knowledge | template | requirements | — | internal-comms, doc-coauthoring |
| r3f-drei | template | implementation | r3f-fundamentals | — |
| r3f-fundamentals | template | implementation | — | r3f-geometry, r3f-materials, r3f-drei, r3f-performance |
| r3f-geometry | template | implementation | r3f-fundamentals | r3f-performance |
| r3f-materials | template | implementation | r3f-fundamentals | r3f-performance |
| r3f-performance | template | implementation | r3f-fundamentals | — |
| router-template | template | environment | — | skill-creator |
| scientific-documentation | template | implementation | — | doc-coauthoring |
| shader-effects | template | implementation | shader-fundamentals | postfx-effects, particles-gpu |
| shader-fundamentals | template | implementation | — | shader-noise, shader-sdf, shader-effects |
| shader-noise | template | implementation | shader-fundamentals | particles-physics, terrain-integration |
| shader-sdf | template | implementation | shader-fundamentals | — |
| skill-creator | template | environment | — | router-template |
| slack-gif-creator | template | implementation | — | internal-comms |
| structural-physics | template | implementation | — | 3d-building-advanced, decay-upkeep |
| terrain-integration | template | implementation | — | 3d-building-advanced, structural-physics |
| theme-factory | template | implementation | — | pptx, docx, pdf, web-artifacts-builder, scientific-documentation, internal-comms |
| using-git-worktrees | template | environment | — | subagent-driven-development, writing-plans |
| web-artifacts-builder | template | environment, implementation | — | frontend-design, component-library |
| xlsx | template | implementation | — | d3js-visualization, scientific-documentation |

### Stubs & Missing SKILL.md

These skills have no meaningful content or lack a SKILL.md file entirely. They are excluded from dependency and phase analysis.

| Skill | Status | Notes |
|-------|--------|-------|
| binary-import | no SKILL.md | — |
| binary-skill | no SKILL.md | — |
| import-me | stub | Single line: `# Imported` |
| imported-skill | stub | Single line: `# Imported Skill` |
| integration-test | stub | Minimal test content |
| json-import | stub | Single line: `# JSON Imported` |
| json-skill | stub | Single line: `# JSON Skill` |
| my-new-skill | stub | Empty body, frontmatter only |
| new-skill | stub | Minimal: `Content here` |
| no-skill-md | stub | Minimal: `Imported skill` |
| renamed-skill | stub | Single line: `# Test` |
| safe | no SKILL.md | — |
| source-skill | stub | Two lines: `# Imported / From folder.` |
| traversal-test | no SKILL.md | — |

---

## Gap Analysis

### Phase Coverage Summary

| Phase | Skill Count | Skills |
|-------|-------------|--------|
| **requirements** | 4 | brainstorming, doc-coauthoring, product-self-knowledge, brand-guidelines |
| **architecture** | 5 | brainstorming, writing-plans, software-architecture, mcp-builder, case-studies-reference |
| **environment** | 5 | using-git-worktrees, web-artifacts-builder, aws-skills, skill-creator, router-template |
| **implementation** | ~60 | _(majority of all skills — see table above)_ |
| **testing** | 3 | test-driven-development, systematic-debugging, integration-test (stub) |
| **review** | 6 | backend-dev-guidelines, frontend-dev-guidelines, software-architecture, systematic-debugging, form-accessibility, form-security |
| **cicd** | 0 | _(none)_ |
| **deployment** | 1 | aws-skills |
| **monitoring** | 0 | _(none)_ |
| **feedback** | 0 | _(none)_ |

### Critical Gaps

**Zero-coverage phases:**

| Phase | Gap Description | Suggested Skills |
|-------|-----------------|------------------|
| **cicd** | No skills for CI/CD pipelines, build automation, or release management. | `github-actions`, `ci-pipeline-builder`, `release-management` |
| **monitoring** | No skills for observability, error tracking, logging, or alerting. | `observability-setup`, `error-tracking`, `logging-patterns` |
| **feedback** | No skills for user feedback loops, A/B testing, retrospectives, or iteration patterns. | `retrospective-facilitator`, `user-feedback-analyzer` |

**Single-coverage phases (fragile):**

| Phase | Gap Description | Suggested Skills |
|-------|-----------------|------------------|
| **deployment** | Only `aws-skills` covers deployment, and only for AWS. No general deployment, Docker, or multi-cloud support. | `docker-deployment`, `deployment-checklist`, `infrastructure-as-code` |
| **testing** | Only `test-driven-development` provides real testing guidance. `systematic-debugging` is partially testing. `integration-test` is a stub. No E2E, load, or security testing skills. | `e2e-testing`, `api-testing`, `load-testing`, `security-testing` |

### Phase Distribution Imbalance

```
requirements    ████ 4
architecture    █████ 5
environment     █████ 5
implementation  ████████████████████████████████████████████████████████████ ~60
testing         ███ 3
review          ██████ 6
cicd            0
deployment      █ 1
monitoring      0
feedback        0
```

The skill library is heavily concentrated in the **implementation** phase (~70% of all skills). The "right side" of the SDLC (cicd → deployment → monitoring → feedback) has almost no coverage.

---

## Composition Clusters

### 1. Immersive Visuals Pipeline

The largest interconnected cluster. A master router dispatches to 6 domain routers covering 25+ implementation skills.

```
immersive-visuals-router
├── r3f-router ─────── r3f-fundamentals, r3f-geometry, r3f-materials, r3f-performance, r3f-drei
├── shader-router ──── shader-fundamentals, shader-noise, shader-sdf, shader-effects
├── particles-router ─ particles-gpu, particles-physics, particles-lifecycle
├── postfx-router ──── postfx-composer, postfx-bloom, postfx-effects
├── gsap-router ────── gsap-fundamentals, gsap-sequencing, gsap-scrolltrigger, gsap-react
└── audio-router ───── audio-playback, audio-analysis, audio-reactive
```

**Cross-domain links** (skills that bridge domains):
- `audio-reactive` → drives `postfx-bloom`, `particles-gpu`, `shader-effects`, `gsap-sequencing`
- `shader-noise` ← used by `particles-physics`, `terrain-integration`
- `postfx-bloom` ← used by `r3f-fundamentals`, `particles-gpu`, `audio-reactive`
- `gsap-sequencing` ← used with `audio-playback` for beat-synced timelines

**Typical project compositions:**

| Project Type | Skills Combined |
|--------------|----------------|
| Audio Visualizer | audio-playback + audio-analysis + audio-reactive + r3f-fundamentals + shader-effects + particles-gpu + postfx-bloom |
| Landing Page Hero | r3f-fundamentals + r3f-drei + gsap-fundamentals + gsap-scrolltrigger + postfx-bloom |
| Creative Coding | shader-fundamentals + shader-noise + r3f-fundamentals + postfx-composer |
| Cinematic 3D Scene | r3f-fundamentals + r3f-materials + shader-fundamentals + postfx-composer + postfx-bloom + postfx-effects + gsap-sequencing |
| Particle-Heavy Effect | particles-gpu + particles-physics + particles-lifecycle + r3f-fundamentals + postfx-bloom + shader-noise |

---

### 2. Building Game Stack

8 specialized skills for 3D building game mechanics, dispatched by `building-router`.

```
building-router
├── Tier 1: Core Mechanics
│   ├── performance-at-scale (spatial indexing, collision)
│   ├── structural-physics (stability, damage, collapse)
│   └── multiplayer-building (networking, prediction)
├── Tier 2: Enhanced Features
│   ├── terrain-integration (slopes, foundations)
│   ├── decay-upkeep (timer decay, tool cupboard)
│   └── builder-ux (blueprints, undo/redo)
└── Tier 3: Platform & Reference
    ├── platform-building (touch, VR, accessibility)
    └── case-studies-reference (design analysis)
```

**Typical compositions:**

| Game Type | Skills Combined |
|-----------|----------------|
| Full Survival (Rust-style) | performance-at-scale + structural-physics + multiplayer-building + terrain-integration + decay-upkeep + builder-ux |
| Battle Royale Building | performance-at-scale + multiplayer-building |
| Single-Player Builder | structural-physics + terrain-integration + builder-ux |
| Persistent Server | multiplayer-building + structural-physics + decay-upkeep + performance-at-scale |

---

### 3. Forms Stack

7 specialized skills for web form development, dispatched by `forms-router`.

```
forms-router
├── Tier 1: Core (always include)
│   ├── form-accessibility (WCAG, ARIA)
│   ├── form-validation (Zod schemas)
│   └── form-security (CSRF, XSS, autocomplete)
├── Tier 2: Framework
│   ├── form-react (React Hook Form / TanStack)
│   ├── form-vue (VeeValidate / Vuelidate)
│   └── form-vanilla (Constraint Validation API)
└── Tier 3: Enhanced UX
    └── form-ux-patterns (wizards, chunking)
```

**Typical compositions:**

| Form Type | Skills Combined |
|-----------|----------------|
| Standard Production Form | form-accessibility + form-validation + form-security + form-react |
| Secure Auth Form | form-security + form-accessibility + form-validation + form-react |
| Multi-Step Wizard | form-ux-patterns + form-validation + form-accessibility + form-react |
| Framework-Free Form | form-vanilla + form-accessibility + form-security |

---

### 4. Development Process Chain

A linear workflow chain connecting 5 discipline/template skills from ideation to execution.

```
brainstorming
  │  "Design before code"
  │  Outputs: design document in docs/plans/
  ▼
writing-plans
  │  "Write plans clear enough for a junior engineer"
  │  Outputs: step-by-step plan in docs/plans/
  ▼
using-git-worktrees
  │  "Isolate feature work. Keep main clean."
  │  Outputs: isolated worktree with dependencies installed
  ▼
subagent-driven-development
  │  "Fresh context per task. Review between tasks."
  │  Executes plan task-by-task with review checkpoints
  ▼
test-driven-development
  │  "Red → Green → Refactor"
  │  Each task follows TDD within subagent execution
```

**Explicit references:**
- `brainstorming` → explicitly names `using-git-worktrees` and `writing-plans` as next steps
- `writing-plans` → explicitly names `subagent-driven-development` for execution
- `subagent-driven-development` → loads plans from `docs/plans/` (produced by `writing-plans`)

**Enhancement layer:** `systematic-debugging` can be applied at any point when issues arise.

---

### 5. Document Production Cluster

8 skills that combine for comprehensive document creation and styling.

```
                  brand-guidelines ──────┐
                  product-self-knowledge ─┤
                                         ▼
               ┌── docx ◄── theme-factory
               ├── pptx ◄── theme-factory
doc-coauthoring ┤── pdf  ◄── theme-factory
               ├── xlsx
               ├── scientific-documentation
               └── internal-comms
```

**Key relationships:**
- `theme-factory` layers onto `docx`, `pptx`, `pdf`, and `web-artifacts-builder` to provide consistent styling (10 preset themes)
- `brand-guidelines` provides brand identity that informs `theme-factory`, `frontend-design`, and all document skills
- `doc-coauthoring` provides the structured writing workflow used alongside any document format skill
- `product-self-knowledge` provides reference knowledge used by `internal-comms` and `doc-coauthoring`

**Typical compositions:**

| Document Type | Skills Combined |
|---------------|----------------|
| Branded Slide Deck | pptx + theme-factory + brand-guidelines |
| Technical Spec | docx + doc-coauthoring + scientific-documentation |
| Internal Memo | internal-comms + product-self-knowledge |
| Financial Report | xlsx + pdf + theme-factory |
| Research Paper | scientific-documentation + pdf + doc-coauthoring |

---

### 6. Creative Art Cluster

3 independent creative engines that resist templating but share aesthetic philosophy.

```
algorithmic-art ──── p5.js generative art, seeded randomness
canvas-design ────── static visual art (.png/.pdf), design philosophy
frontend-design ──── distinctive web UI, anti-"AI slop" aesthetics
```

**Shared principles:** All three explicitly resist generic output and emphasize original, non-repeatable creative work. They share no explicit dependencies but operate in overlapping aesthetic territory.

**Cross-cluster connections:**
- `algorithmic-art` techniques (noise, particles, flow fields) overlap with the Immersive Visuals Pipeline
- `canvas-design` output formats overlap with the Document Production Cluster
- `frontend-design` directly enhances any web-facing template skill

---

### 7. Meta/Tooling Cluster

Skills for creating and managing other skills.

```
skill-creator ────── guides new skill creation (init_skill.py)
router-template ──── boilerplate for creating new routers
mcp-builder ──────── guides MCP server development
web-artifacts-builder ── React artifact scaffolding for Claude.ai
```

These are "skills about skills" — they produce the infrastructure that other skills run on.

---

## Cross-Cluster Bridges

Skills that connect multiple clusters:

| Bridge Skill | Clusters Connected |
|--------------|--------------------|
| audio-reactive | Immersive Visuals ↔ Audio (drives visuals from audio data) |
| shader-noise | Immersive Visuals ↔ Building Game (terrain generation) |
| frontend-design | Creative Art ↔ Forms ↔ Document Production (visual quality layer) |
| theme-factory | Document Production ↔ Web (styling for both domains) |
| brainstorming | Development Process ↔ all clusters (entry point for any project) |
| systematic-debugging | Development Process ↔ all implementation skills (debugging layer) |
| test-driven-development | Development Process ↔ all implementation skills (testing layer) |
| case-studies-reference | Building Game ↔ Architecture phase (design analysis) |
| software-architecture | Development Process ↔ all implementation skills (design principles) |

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total skill directories | 94 |
| Skills with SKILL.md | 90 |
| Skills without SKILL.md | 4 |
| Stub/test skills | 10 |
| **Functional skills** | **76** |
| — Creative engines | 3 |
| — Disciplines | 9 |
| — Routers | 12 |
| — Templates | 52 |
| Composition clusters | 7 |
| SDLC phases with zero coverage | 3 (cicd, monitoring, feedback) |
| SDLC phases with ≤1 skill | 5 (+ deployment, testing) |
