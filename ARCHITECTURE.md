# Econ-ARK Website Architecture

## System Overview

The Econ-ARK website is a Jekyll-based static site that serves as the discovery and access portal for a distributed ecosystem of computational economics research. The architecture emphasizes automation, reproducibility, and seamless integration across multiple repositories.

## Component Architecture

### 1. Content Generation Layer

#### Primary Script: `populate_remarks.py`
**Purpose**: Automated content synchronization from distributed research repositories

**Process Flow**:
```python
1. Repository Discovery
   - Clone REMARK repository
   - Parse catalog files (REMARKs/*.yml)
   - Extract repository URLs and versions

2. Concurrent Content Fetching  
   - Multi-threaded cloning of research repositories
   - Sparse checkout for performance (metadata files only)
   - Error handling for unreachable repositories

3. Metadata Extraction and Merging
   - Parse CITATION.cff (bibliographic data)
   - Parse REMARK.md (website-specific content)
   - Merge with catalog metadata
   - Validate required fields

4. Jekyll Content Generation
   - Create _materials/{name}.md files
   - Format YAML frontmatter + Markdown content
   - Preserve existing manual overrides
```

**Technical Implementation**:
- **Concurrency**: ThreadPoolExecutor for parallel repository operations
- **Git Operations**: Sparse checkout with `--filter=tree:0` for efficiency
- **Error Resilience**: Continues processing if individual repositories fail
- **Memory Management**: Uses temporary directories, automatic cleanup

#### Workflow Automation (`.github/workflows/site-preprocess.yml`)
**Triggers**: 
- Daily scheduled runs (content freshness)
- Manual dispatch for immediate updates
- Repository webhook triggers (future enhancement)

**Process**:
```yaml
1. Environment Setup
   - Python 3.9+ with dependencies
   - Git configuration for repository access
   
2. Content Generation
   - Execute populate_remarks.py
   - Validate generated content structure
   - Commit changes if content updated

3. Site Rebuild Trigger
   - Netlify automatically detects repository changes
   - Jekyll build process initiates
   - Site deployment within minutes
```

### 2. Jekyll Static Site Layer

#### Configuration (`_config.yml`)
**Core Settings**:
- **Collections**: Materials (auto-generated), Team (manual)
- **Plugins**: SEO optimization, sitemap generation, RSS feeds
- **Permalinks**: SEO-friendly URL structure (`/materials/{name}/`)
- **Metadata**: Comprehensive keywords and descriptions for search engines

**SEO and Discoverability**:
```yaml
keywords: computational economics, reproducible research, 
          economic modeling, heterogeneous agents, 
          dynamic programming, macroeconomics, 
          consumption theory, portfolio choice, 
          wealth distribution, Python, Jupyter notebooks
```

#### Template Architecture

**Layout Hierarchy**:
```
_layouts/
├── default.html          # Base template with SEO headers
├── material.html         # Individual research project pages  
├── materials.html        # Searchable catalog interface
└── home.html            # Landing page with featured content
```

**Key Features**:
- **Responsive Design**: Mobile-first approach with progressive enhancement
- **Structured Data**: Schema.org markup for research projects
- **Search Integration**: Client-side filtering and categorization
- **Navigation**: Dynamic breadcrumbs and cross-references

#### Content Collections

**Materials Collection** (`_materials/`):
- **Source**: Auto-generated from research repositories
- **Structure**: YAML frontmatter + Markdown content
- **Metadata**: Authors, abstracts, keywords, repository links, execution requirements
- **Processing**: Jekyll automatically creates individual pages and catalog entries

**Team Collection** (`_team/`):
- **Source**: Manually curated profiles
- **Structure**: Biographical information, research interests, contact details
- **Integration**: Cross-referenced with material authorship

### 3. Data and Taxonomy Layer

#### Research Taxonomy (`_data/research_taxonomy.yml`)
**Purpose**: Structured categorization for AI systems and search engines

**Structure**:
```yaml
domains:              # Primary research areas
  - name: "Computational Economics"
    subdomains:       # Specialized topics
      - name: "Consumption Theory"
        concepts:     # Specific techniques/theories

methodologies:        # Technical approaches
technical_stack:      # Tools and environments
academic_keywords:    # Search optimization terms
```

**Usage**:
- **AI Discovery**: Powers machine-readable topic index
- **Search Enhancement**: Provides keyword expansion for queries
- **Content Classification**: Automatic tagging and categorization

#### Structured Data Integration
**Schema.org Implementation** (`_includes/structured-data.html`):
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ResearchProject",
  "name": "{{ page.title }}",
  "description": "{{ page.abstract }}",
  "author": [/* author array */],
  "programmingLanguage": "Python",
  "operatingSystem": "Platform Independent"
}
</script>
```

## Integration Points

### 1. Repository Synchronization

**Metadata Sources Priority**:
1. **CITATION.cff**: Authoritative bibliographic data
2. **REMARK.md**: Website-specific presentation
3. **REMARKs/{name}.yml**: Catalog entry and versioning
4. **Generated**: URLs, tags, collection assignments

**Conflict Resolution**:
- Repository metadata overrides catalog entries
- REMARK.md supplements but doesn't replace CITATION.cff
- Manual overrides in website repository take precedence

### 2. Content Validation

**Automated Checks**:
- Required metadata fields presence
- Repository accessibility verification  
- YAML syntax validation
- Link integrity testing

**Quality Assurance**:
- Preview builds for pull requests
- Staging environment testing
- Error logging and monitoring

### 3. Search and Discovery

**Multiple Access Patterns**:
```
1. Browsing: /materials/ → Filterable catalog
2. Direct Access: /materials/{name}/ → Individual projects  
3. Search: Client-side filtering by keywords, authors, topics
4. API Access: JSON-LD data embedded in HTML
5. Machine Reading: /ai-discovery/ → Comprehensive index
```

## Performance and Scalability

### Build Performance
**Optimization Strategies**:
- **Sparse Git Operations**: Only fetch necessary files
- **Concurrent Processing**: Parallel repository operations
- **Incremental Builds**: Jekyll processes only changed content
- **CDN Delivery**: Netlify global distribution

**Current Metrics**:
- **Content Generation**: ~2-3 minutes for full catalog
- **Jekyll Build**: ~30-60 seconds for typical updates
- **Total Update Cycle**: <5 minutes from trigger to live site

### Scalability Considerations
**Current Capacity**: Handles ~50-100 repositories efficiently
**Scaling Bottlenecks**: 
- Git clone operations (network bandwidth)
- Jekyll build time (grows with content size)
- Repository metadata parsing (CPU bound)

**Future Enhancements**:
- Incremental updates (only changed repositories)
- Caching layer for repository metadata
- Microservice architecture for content generation

## Monitoring and Maintenance

### Health Checks
**Automated Monitoring**:
- Daily content generation success/failure
- Repository accessibility verification
- Website uptime and performance monitoring
- Search functionality validation

**Error Handling**:
- Graceful degradation for unreachable repositories
- Detailed logging for debugging
- Automatic retry mechanisms
- Manual intervention alerts

### Content Quality
**Validation Pipeline**:
- Metadata completeness verification
- Link integrity checking
- Content duplication detection
- SEO optimization scoring

**Manual Review Process**:
- New repository addition approval
- Quality assurance for featured content
- Periodic content audits and cleanup

## Security and Compliance

### Repository Access
**Security Model**:
- Read-only access to public repositories
- No authentication required for content generation
- Sandboxed execution environment
- Input validation and sanitization

### Data Privacy
**Compliance Measures**:
- No personal data collection beyond public repository metadata
- GDPR-compliant contact and author information handling
- Transparent data usage policies
- User control over profile visibility

## Development and Deployment

### Local Development Setup
```bash
# Environment Setup
ruby --version  # Requires 3.0.4+
gem install bundler

# Repository Setup (adjust URL/path as needed)
git clone https://github.com/econ-ark/econ-ark.org ./website-repo
cd ./website-repo
bundle config set --local path 'vendor/bundle'
bundle install

# Content Generation (optional, requires REMARK repository access)
# Set REMARK_REPO_PATH if REMARK repository is in non-standard location
python scripts/populate_remarks.py

# Local Development Server
bundle exec jekyll serve
# → http://localhost:4000
```

### Deployment Pipeline
**Production Deployment**:
1. **Source Control**: GitHub repository (master branch)
2. **Build System**: Netlify automatic deployment
3. **CDN**: Global content distribution
4. **DNS**: AWS Route53 configuration
5. **SSL**: Automatic certificate management

**Staging Environment**:
- Branch-based preview deployments
- Pull request integration testing
- Content validation before merge

This architecture enables reliable, automated operation while maintaining flexibility for future enhancements and scaling to accommodate the growing ecosystem of computational economics research. 