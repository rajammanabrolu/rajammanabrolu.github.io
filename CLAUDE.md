# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Jekyll-based personal academic website hosted on GitHub Pages using the minimal-mistakes remote theme. The site features an automated bibliography workflow that converts BibTeX files to YAML data files for dynamic publication display.

## Development Commands

### Local Development
```bash
# Install dependencies
bundle install

# Serve the site locally (with live reload)
bundle exec jekyll serve

# Build the site
bundle exec jekyll build
```

The local server runs at `http://localhost:4000` by default.

### Bibliography Workflow

The site uses a custom Python-based pipeline to convert BibTeX files to YAML:

```bash
# Run the complete bibliography workflow manually
bash bib2yaml.sh <input.bib> <output.yml>

# For automated workflow (used by GitHub Actions)
bash bib2yaml_workflow.sh
```

**Workflow Steps:**
1. `bib2yml.py` - Converts BibTeX to initial YAML using pybtex
2. `fix.py` - Cleans up YAML formatting, removes special characters, reformats entry IDs
3. `fold.py` - Embeds original BibTeX entries back into YAML as `bibtex` fields
4. Final output moved to `_data/pubs.yml`

**Important:** The workflow generates temporary files (`temp1.yml`, `temp2.yml`) during processing.

## Architecture

### Content Structure

- **Markdown Pages** (`*.md`): Main content pages (bio, publications, projects, teaching, etc.)
- **`_data/` Directory**: YAML files that drive dynamic content
  - `pubs.yml` - Auto-generated publication database from `lab.bib`
  - `projects.yml` - Research project descriptions with linked publications
  - `phds.yaml`, `masters.yaml`, `undergrads.yaml` - Student/mentee information
  - `navigation.yml` - Site navigation menu structure
  - `years.yml` - List of years for publication timeline
- **`_posts/`**: Blog posts following Jekyll naming convention `YYYY-MM-DD-title.markdown`
- **`assets/images/`**: Static image assets

### Theme Configuration

The site uses the `minimal-mistakes` remote theme with custom skin "game". Key configuration in `_config.yml`:
- `remote_theme: "rajammanabrolu/minimal-mistakes"`
- `minimal_mistakes_skin: "game"`
- Custom defaults for post layouts and reading time

### Publication Display System

Publications are rendered on `publications.md` through a multi-step template:
1. Iterates through years from `_data/years.yml`
2. For each year, displays matching publications from `_data/pubs.yml`
3. Dynamically generates badges (Conference, Workshop, Journal, Preprint, etc.)
4. Includes collapsible BibTeX citations via `toggle.js`
5. Inline CSS styles define badge colors and formatting

**Key Fields in `pubs.yml`:**
- `id` - Unique identifier (matches BibTeX key)
- `author` - List of author objects with first/middle/last names
- `title`, `booktitle`, `journal`, `year`, `volume`
- `url`, `website`, `code`, `blog`, `media`, `talk` - External links
- `bibtex` - Original BibTeX entry (embedded by `fold.py`)

### Projects System

Projects in `_data/projects.yml` link research themes to publications:
- Each project has a `name`, `description`, and list of `pubs`
- Publications reference `pubs.yml` entries by `id`
- Each pub includes a `context` field explaining its relevance to the project

## GitHub Actions

**Workflow:** `.github/workflows/bib2yaml.yml`
- **Trigger:** Pushes to `raj.bib`
- **Actions:**
  1. Installs pybtex
  2. Runs `bib2yaml_workflow.sh`
  3. Auto-commits updated `_data/pubs.yml` with message "Rebuilt from bibtex"

**Note:** The workflow uses `lab.bib` as the source file, not `raj.bib`. There's a mismatch in the workflow trigger path.

## Key Dependencies

- **Jekyll** (~> 4.2.0 via github-pages gem)
- **Python packages:** pybtex (for BibTeX parsing)
- **Jekyll plugins:**
  - jekyll-feed
  - jekyll-include-cache
  - jekyll-seo-tag

## Common Workflows

### Adding a New Publication
1. Add entry to `lab.bib` (or `raj.bib`)
2. Run `bash bib2yaml_workflow.sh` to regenerate `_data/pubs.yml`
3. If automated: Push `raj.bib` to trigger GitHub Actions
4. Optionally: Add to relevant project in `_data/projects.yml`

### Updating Site Content
- **Personal info:** Edit `index.md` and `_config.yml`
- **Navigation menu:** Edit `_data/navigation.yml`
- **Research projects:** Edit `_data/projects.yml`
- **Student listings:** Edit `_data/{phds,masters,undergrads}.yaml`

### Modifying Publication Display
- **Styling:** Edit inline CSS in `publications.md`
- **Layout:** Modify Liquid template logic in `publications.md`
- **Toggle behavior:** Edit `toggle.js`

## Notes

- The site requires server restart when `_config.yml` changes (not hot-reloaded)
- BibTeX entries should avoid special characters; `fix.py` strips `{}^\`, `\'`
- The `fold.py` script excludes certain BibTeX fields: code, website, blog, media, talk
- Site credits: Based on eilab.gatech.edu and mark_riedl's site architecture
