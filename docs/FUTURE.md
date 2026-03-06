# Future Work

Post-MVP improvements identified during the migration. None of these are blockers.

## SDLC Gap Skills

Three SDLC phases have zero skill coverage:

| Phase | Suggested Skills |
|-------|-----------------|
| cicd | `github-actions`, `ci-pipeline-builder` |
| monitoring | `observability-setup`, `error-tracking` |
| feedback | `retrospective-facilitator` |

Two phases have fragile single-skill coverage:

| Phase | Suggested Skills |
|-------|-----------------|
| deployment | `docker-deployment`, `vercel-deployment` |
| testing | `e2e-testing`, `api-testing` |

## Router Architecture Rethink

With `depends_on` in schema, the server could auto-compose skill chains without routers. Evaluate whether `type: "router"` should trigger server-side auto-loading of dependencies, making explicit routers optional.

## Tag Autocomplete API

Expose the controlled tag vocabulary as an API endpoint for skill creation UIs.

## Search Ranking Overhaul

With type, structured tags, and dependency data, search could rank by: tag match > type match > dependency proximity > text match.

## Sub-skills Deprecation or Expansion

Only router skills actively use `sub_skills`. Evaluate whether `sub_skills` should be removed (replaced by `depends_on`) or expanded.

## Description Quality Pass

Rewrite auto-extracted descriptions into curated 1-2 sentence summaries.

## Test Parallelization

Refactor fixtures to use isolated state for `pytest-xdist` parallelization.

## Composition Presets

Create first-class "preset" objects from the COMPOSITION_MAP's typical compositions (e.g., "Audio Visualizer" = 7 specific skills).
