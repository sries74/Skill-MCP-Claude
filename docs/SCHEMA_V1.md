# `_meta.json` Schema — v1 (Current Implicit Schema)

> **Generated**: 2025-03-05  
> **Method**: Exhaustive scan of every `skills/*/_meta.json` file (94 files)  
> **Purpose**: Baseline documentation of the schema as it exists today, prior to any normalization

---

## 1. Corpus Summary

| Metric | Value |
|--------|-------|
| Total `_meta.json` files | 94 |
| Parse errors | 0 |
| Skills with non-empty `sub_skills` | 4 |
| Total `sub_skill` entries across all files | 17 |
| Unique `source` values | 7 |
| Unique `tags` values | 48 |

---

## 2. Top-Level Field Reference

### 2.1 `name`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Present in** | 94 / 94 (100%) |
| **Required?** | **Yes** — present in every file |
| **Description** | Skill identifier. Always matches the directory name. |

**Examples:**
- `"3d-building-advanced"`
- `"audio-analysis"`
- `"forms"`

---

### 2.2 `description`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Present in** | 94 / 94 (100%) |
| **Required?** | **Yes** — present in every file |
| **Description** | Free-text description of the skill's purpose. Varies wildly in length (4–378 chars). Often contains the opening lines of `SKILL.md`. |

**Examples:**
- `"Test"` (4 chars — `my-new-skill`)
- `"Audio analysis with Tone.js and Web Audio API including FFT, frequency data extraction, amplitude measurement, and wa..."` (truncated — `audio-analysis`)
- `"Frontend development guidelines for React/TypeScript applications. Modern patterns including Suspense, lazy loading..."` (378 chars — `frontend-dev-guidelines`)

**Observation:** Some descriptions appear to be auto-extracted opening lines from `SKILL.md` rather than curated summaries. Many include markdown syntax, code snippets, or import statements.

---

### 2.3 `tags`

| Property | Value |
|----------|-------|
| **Type** | `array` of `string` |
| **Present in** | 93 / 94 (99%) |
| **Required?** | **Effectively yes** — missing only from `source-skill` |
| **Description** | List of keyword tags for categorization and search. |

**Examples:**
- `[]` (empty — 50 skills)
- `["react", "api", "typescript", "ui", "components", "ux", "validation", "form", "user"]` (`form-validation`)
- `["rust", "multiplayer", "three.js", "caching", "sync", "optimization", "performance", "javascript", "networking", "validation"]` (`3d-building-advanced`)

**Tag array length distribution:**

| Length | Count |
|--------|-------|
| 0 (empty) | 50 |
| 1 | 1 |
| 2 | 1 |
| 4 | 1 |
| 5 | 1 |
| 6 | 2 |
| 7 | 6 |
| 8 | 10 |
| 9 | 20 |
| 10 | 1 |

**Top 20 tags by frequency:**

| Tag | Usage count |
|-----|-------------|
| `ui` | 34 |
| `user` | 20 |
| `forms` | 18 |
| `javascript` | 15 |
| `validation` | 15 |
| `react` | 15 |
| `html` | 12 |
| `typescript` | 12 |
| `documentation` | 11 |
| `api` | 11 |
| `examples` | 10 |
| `accessibility` | 10 |
| `ux` | 9 |
| `python` | 8 |
| `game` | 8 |
| `components` | 8 |
| `design` | 6 |
| `css` | 6 |
| `public` | 6 |
| `multiplayer` | 5 |

**Observation:** Over half of skills (50/94) have an empty tags array. Tags are not standardized — e.g., `"forms"` vs `"form"` both appear. Tag semantics are mixed (technology names, domain concepts, audience markers like `"user"` and `"public"`).

---

### 2.4 `sub_skills`

| Property | Value |
|----------|-------|
| **Type** | `array` of `object` |
| **Present in** | 92 / 94 (98%) |
| **Required?** | **Effectively yes** — missing only from `imported-skill` and `source-skill` |
| **Description** | References to sub-skill markdown files with trigger keywords. Almost always empty. |

**Population breakdown:**

| State | Count |
|-------|-------|
| Empty array `[]` | 88 |
| Non-empty | 4 |
| Missing entirely | 2 |

**Skills with populated `sub_skills`:**

| Skill | Sub-skill count |
|-------|-----------------|
| `forms` | 7 |
| `building` | 4 |
| `3d-building-advanced` | 3 |
| `dashboard` | 3 |

See [Section 3](#3-sub_skills-entry-schema) for the sub-object schema.

---

### 2.5 `source`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Present in** | 88 / 94 (94%) |
| **Required?** | **No** — missing from 6 skills |
| **Description** | Provenance marker indicating how the skill was created or imported. |

**Value distribution:**

| Value | Count | Description |
|-------|-------|-------------|
| `claude-user` | 59 | User-created via Claude |
| `claude-examples` | 10 | From example/template library |
| `claude-public` | 6 | From public skill repository |
| `json-upload` | 6 | Imported via JSON upload |
| `imported` | 3 | Imported from another source |
| `created` | 3 | Created via skill creation flow |
| `obra/superpowers` | 1 | From the obra/superpowers repository |

**Missing from:** `3d-building-advanced`, `building`, `dashboard`, `forms`, `imported-skill`, `source-skill`

**Observation:** The 4 skills with populated `sub_skills` (`3d-building-advanced`, `building`, `dashboard`, `forms`) are all missing `source`. These appear to be a distinct structural pattern — composite/router-style skills that may predate the `source` field or were created through a different pathway.

---

## 3. `sub_skills` Entry Schema

Each entry in the `sub_skills` array is an object with 3 fields. All 17 observed entries have identical structure.

### 3.1 `name`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Present in** | 17 / 17 entries (100%) |
| **Required?** | **Yes** |
| **Description** | Identifier for the sub-skill. |

**Examples:**
- `"multiplayer-networking"`
- `"charts"`
- `"accessibility"`

---

### 3.2 `file`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Present in** | 17 / 17 entries (100%) |
| **Required?** | **Yes** |
| **Description** | Relative path to the sub-skill markdown file (relative to the skill directory). Always follows the pattern `references/<name>.md`. |

**Examples:**
- `"references/multiplayer-networking.md"`
- `"references/charts.md"`
- `"references/accessibility.md"`

---

### 3.3 `triggers`

| Property | Value |
|----------|-------|
| **Type** | `array` of `string` |
| **Present in** | 17 / 17 entries (100%) |
| **Required?** | **Yes** |
| **Description** | Keywords that trigger loading this sub-skill. Array length ranges from 4 to 10 items. |

**Examples:**
- `["WCAG", "ARIA", "screen reader", "a11y"]` (4 items)
- `["chart", "graph", "D3", "recharts", "visualization"]` (5 items)
- `["localPiece", "tempId", "Delta Compression", "multiplayer-networking", "The Networking Challenge", "BuildingPermissionSystem", "UpdateBatcher", "Authority Models", "updatePredictions", "pending"]` (10 items)

---

## 4. Structural Variants

Three distinct file shapes emerge from the data:

### Variant A: Full skill (88 files)
```json
{
  "name": "string",
  "description": "string",
  "tags": ["string"],
  "sub_skills": [],
  "source": "string"
}
```

### Variant B: Composite skill with sub-skills (4 files)
Missing `source`. Has populated `sub_skills`.
```json
{
  "name": "string",
  "description": "string",
  "tags": ["string"],
  "sub_skills": [
    {
      "name": "string",
      "file": "references/<name>.md",
      "triggers": ["string"]
    }
  ]
}
```

**Instances:** `3d-building-advanced`, `building`, `dashboard`, `forms`

### Variant C: Minimal/legacy (2 files)
Missing `sub_skills` and/or `tags` and `source`.
```json
{
  "name": "string",
  "description": "string"
}
```

**Instances:** `source-skill` (name + description only), `imported-skill` (name + description + tags)

---

## 5. Inconsistencies & Observations

### 5.1 Missing Fields

| Field | Missing from | Notes |
|-------|-------------|-------|
| `tags` | `source-skill` (1 file) | Only file without any tags |
| `sub_skills` | `imported-skill`, `source-skill` (2 files) | Legacy/minimal structure |
| `source` | `3d-building-advanced`, `building`, `dashboard`, `forms`, `imported-skill`, `source-skill` (6 files) | Composite skills + legacy files |

### 5.2 Type Consistency

All fields have consistent types across all files where they appear. No field appears as different types in different files. This is good — no type coercion issues exist.

### 5.3 Description Quality

Descriptions range from 4 to 378 characters with a median of ~175. Several contain:
- Raw markdown syntax (headers, bold, lists)
- Code snippets and import statements (`import { z } from 'zod';`)
- Truncated fragments from `SKILL.md` opening lines

These are currently stored as raw strings with no length constraint or format validation.

### 5.4 Tag Taxonomy Issues

- **53% of skills have empty tags** — tags are not reliably populated
- **No controlled vocabulary** — tags are free-form strings
- **Duplicate concepts** — `"forms"` (18 uses) vs `"form"` (appears in some skills)
- **Mixed semantics** — technology (`react`, `python`), domain (`game`, `forms`), audience (`user`, `public`), quality (`examples`)
- **Over-tagging** — Many skills with tags have 8–9 tags, diluting specificity

### 5.5 Source Provenance Gap

Six skills lack `source`. The four composite skills (`3d-building-advanced`, `building`, `dashboard`, `forms`) may have been created before the field was introduced. The two minimal files (`imported-skill`, `source-skill`) appear to be test/legacy artifacts.

### 5.6 Sub-skills Underutilization

Only 4 of 94 skills (4.3%) use `sub_skills`. The remaining 88 carry an empty array. Several skills that function as routers (e.g., `forms-router`, `particles-router`, `shader-router`, `r3f-router`) have empty `sub_skills` despite conceptually routing to child skills — their routing logic lives entirely in `SKILL.md` instead.

---

## 6. Canonical JSON Schema (Descriptive)

This JSON Schema describes the structure as it currently exists, including optional fields:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "_meta.json",
  "description": "Skill metadata file — v1 implicit schema",
  "type": "object",
  "required": ["name", "description"],
  "properties": {
    "name": {
      "type": "string",
      "description": "Skill identifier, matches directory name"
    },
    "description": {
      "type": "string",
      "description": "Free-text skill description (4–378 chars observed)"
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "default": [],
      "description": "Keyword tags for categorization (often empty)"
    },
    "sub_skills": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "file", "triggers"],
        "properties": {
          "name": {
            "type": "string",
            "description": "Sub-skill identifier"
          },
          "file": {
            "type": "string",
            "description": "Relative path to sub-skill markdown (references/<name>.md)"
          },
          "triggers": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Keywords that trigger this sub-skill (4–10 items observed)"
          }
        }
      },
      "default": [],
      "description": "Sub-skill references with trigger keywords (usually empty)"
    },
    "source": {
      "type": "string",
      "enum": [
        "claude-user",
        "claude-examples",
        "claude-public",
        "json-upload",
        "imported",
        "created",
        "obra/superpowers"
      ],
      "description": "Provenance marker — how the skill was created or imported"
    }
  }
}
```

---

## 7. Field Inventory (Quick Reference)

| # | Field | Type | Present | Required | Default |
|---|-------|------|---------|----------|---------|
| 1 | `name` | `string` | 94/94 (100%) | Yes | — |
| 2 | `description` | `string` | 94/94 (100%) | Yes | — |
| 3 | `tags` | `array<string>` | 93/94 (99%) | Effectively | `[]` |
| 4 | `sub_skills` | `array<SubSkill>` | 92/94 (98%) | Effectively | `[]` |
| 5 | `source` | `string` | 88/94 (94%) | No | — |

| # | SubSkill Field | Type | Present | Required |
|---|----------------|------|---------|----------|
| 1 | `name` | `string` | 17/17 (100%) | Yes |
| 2 | `file` | `string` | 17/17 (100%) | Yes |
| 3 | `triggers` | `array<string>` | 17/17 (100%) | Yes |
