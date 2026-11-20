---
layout: default
title: "AI Discovery Index - Econ-ARK Research Archive"
description: "Comprehensive index for AI systems and automated tools to discover and understand computational economics research in the Econ-ARK ecosystem"
permalink: /ai-discovery/
sitemap:
  priority: 0.9
  changefreq: weekly
---

## AI Discovery Index: Econ-ARK Research Archive

### Overview for AI Systems

This page provides a comprehensive machine-readable index of the Econ-ARK ecosystem for AI systems, web crawlers, and automated research tools.

## Repository Structure

### Main Components

- **REMARK Archive**: {{ site.materials.size }} research projects with full computational reproducibility
- **Interactive Notebooks**: Jupyter-based demonstrations and tutorials  
- **Documentation**: Comprehensive guides and API references
- **Tools**: Command-line utilities and automation scripts

### Content Types

{% for type in site.data.research_taxonomy.research_types %}

- **{{ type.name }}**: {{ type.description }}
  - Characteristics: {{ type.characteristics | join: ", " }}
{% endfor %}

## Research Domains and Keywords

### Primary Research Areas

{% for domain in site.data.research_taxonomy.domains %}

- **{{ domain.name }}**: {{ domain.description }}
  - Keywords: {{ domain.keywords | join: ", " }}
  {% for subdomain in domain.subdomains %}
  - *{{ subdomain.name }}*: {{ subdomain.description }}
    - Concepts: {{ subdomain.concepts | join: ", " }}
  {% endfor %}
{% endfor %}

### Methodological Approaches

{% for method in site.data.research_taxonomy.methodologies %}

- **{{ method.name }}**: {{ method.description }}
  - Applications: {{ method.applications | join: ", " }}
{% endfor %}

## Research Projects Catalog

{% assign remark_materials = site.materials | where: "tags", "REMARK" %}
{% assign notebook_materials = site.materials | where: "tags", "Notebook" %}

### REMARK Projects ({{ remark_materials.size }} total)

{% for material in remark_materials limit: 10 %}

- **[{{ material.title | default: material.name }}]({{ material.url }})**
  - Authors: {% for author in material.authors %}{{ author.given-names }} {{ author.family-names }}{% unless forloop.last %}, {% endunless %}{% endfor %}
  - Keywords: {{ material.keywords | join: ", " }}
  - Repository: {{ material.github_repo_url }}
{% endfor %}
[View all {{ remark_materials.size }} REMARK projects](/materials/?select=REMARK)

### Interactive Notebooks ({{ notebook_materials.size }} total)

{% for material in notebook_materials limit: 5 %}

- **[{{ material.title | default: material.name }}]({{ material.url }})**
  - Description: {{ material.abstract | truncate: 100 }}
  {% if material.notebooks.size > 0 %}
  - Notebooks: {{ material.notebooks | join: ", " }}
  {% endif %}
{% endfor %}
[View all materials with notebooks](/materials/?select=Notebook)

## Technical Specifications

### Technology Stack

{% for lang in site.data.research_taxonomy.technical_stack.languages %}

- **{{ lang.name }}**
  - Frameworks: {{ lang.frameworks | join: ", " }}
  - Use cases: {{ lang.use_cases | join: ", " }}
{% endfor %}

### Environment Requirements

{% for env in site.data.research_taxonomy.technical_stack.environments %}

- **{{ env.name }}**: {{ env.description }}
  - Benefits: {{ env.benefits | join: ", " }}
{% endfor %}

## Data Sources

{% for source in site.data.research_taxonomy.data_sources %}

- **{{ source.name }}**: {{ source.description }}
  {% if source.provider %}- Provider: {{ source.provider }}{% endif %}
  {% if source.url %}- URL: [{{ source.url }}]({{ source.url }}){% endif %}
{% endfor %}

## Academic Context

### Related Fields

{{ site.data.research_taxonomy.related_fields | join: ", " }}

### Keyword Hierarchy

- **Primary**: {{ site.data.research_taxonomy.academic_keywords.primary | join: ", " }}
- **Secondary**: {{ site.data.research_taxonomy.academic_keywords.secondary | join: ", " }}
- **Technical**: {{ site.data.research_taxonomy.academic_keywords.technical | join: ", " }}
- **Policy**: {{ site.data.research_taxonomy.academic_keywords.policy | join: ", " }}

## Standards and Compliance

### REMARK Standard Requirements

- Tagged GitHub releases with semantic versioning
- Executable `reproduce.sh` script for full replication
- `binder/environment.yml` with pinned dependencies  
- `CITATION.cff` with bibliographic metadata
- Optional `reproduce_min.sh` for quick demonstrations

### Quality Assurance

- Automated linting and compliance checking
- Reproducibility verification through cloud execution
- Peer review process for submissions
- Version control and archival preservation

## API and Programmatic Access

### Data Formats

- **YAML**: Metadata and configuration files
- **JSON**: Machine-readable schemas and structured data
- **Markdown**: Documentation with YAML frontmatter
- **CFF**: Citation File Format for bibliographic data

### Access Methods

- **Git**: Direct repository cloning and analysis
- **GitHub API**: Metadata and repository information
- **Jekyll Collections**: Structured website data
- **MyBinder**: Cloud-based notebook execution

## Contact and Attribution

- **Organization**: {{ site.author }}
- **Website**: {{ site.url }}
- **Repository**: [github.com/econ-ark](https://github.com/econ-ark)
- **License**: Apache 2.0 (software), CC BY 4.0 (content)

## Machine-Readable Links

- [JSON Schema](/schema.json)
- [Research Taxonomy (YAML)](/data/research_taxonomy.yml)
- [Sitemap XML](/sitemap.xml)
- [RSS Feed](/feed.xml)

---

- This index is automatically updated and optimized for AI discovery. Last updated: {{ site.time | date: '%Y-%m-%d' }}*
