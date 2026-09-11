# Contributing to Econ-ARK Website

## Overview

The Econ-ARK website serves as the public discovery interface for computational economics research. Contributions help improve accessibility, discoverability, and functionality for researchers, students, and AI systems worldwide.

## Types of Contributions

### 1. Content and Documentation
- **Research Material Enhancement**: Improve metadata, descriptions, and categorization
- **Documentation**: Enhance guides, tutorials, and technical documentation  
- **AI/SEO Optimization**: Improve structured data and search engine optimization
- **Accessibility**: Enhance usability for diverse users and assistive technologies

### 2. Technical Improvements
- **Template Enhancement**: Improve Jekyll layouts and includes
- **Search Functionality**: Enhance filtering and discovery features
- **Performance**: Optimize build times and page loading
- **API Development**: Expand programmatic access capabilities

### 3. Design and User Experience
- **Visual Design**: Improve styling and layout
- **Navigation**: Enhance site structure and user flows
- **Mobile Experience**: Optimize responsive design
- **Interactive Features**: Add dynamic functionality

## Getting Started

### Prerequisites
- **Ruby**: 3.0.4 or higher
- **Git**: For version control
- **Text Editor**: VS Code, Atom, or similar
- **Basic Knowledge**: HTML, CSS, Markdown, YAML

### Development Setup

```bash
# 1. Fork and clone repository
export WEBSITE_REPO_PATH="${WEBSITE_REPO_PATH:-./econ-ark-website}"
git clone https://github.com/your-username/econ-ark.org "$WEBSITE_REPO_PATH"
cd "$WEBSITE_REPO_PATH"

# 2. Install dependencies
gem install bundler
bundle config set --local path 'vendor/bundle'
bundle install

# 3. Run content generation (optional)
python scripts/populate_remarks.py

# 4. Start development server
bundle exec jekyll serve
# Site available at http://localhost:4000

# 5. Create feature branch
git checkout -b feature/your-improvement
```

### Repository Structure Understanding

```
econ-ark.org/
├── _materials/          # Auto-generated research project pages
├── _team/              # Team member profiles (manual)
├── _layouts/           # Jekyll page templates
├── _includes/          # Reusable template components
├── _data/              # YAML data files (taxonomy, configuration)
├── assets/             # CSS, JavaScript, images
├── pages/              # Static content pages
├── scripts/            # Build and maintenance scripts
└── .github/workflows/  # Automation and deployment
```

## Contribution Guidelines

### 1. Content Contributions

#### Research Material Enhancements
**What You Can Improve**:
- Material descriptions and abstracts
- Keyword assignments and categorization
- Cross-references between related projects
- Educational context and learning objectives

**Process**:
```bash
# Materials are auto-generated, so improvements go to source repositories
# For website-specific enhancements:

1. Identify the source repository (shown on material page)
2. Create REMARK.md or enhance existing one
3. Submit PR to source repository
4. Changes will sync automatically within 24 hours
```

**Template for REMARK.md**:
```yaml
---
# Website-specific metadata
jupyter_notebooks:
  - path: "notebooks/main_analysis.ipynb"
    description: "Interactive demonstration of key results"
    
learning_objectives:
  - "Understand buffer stock theory foundations"
  - "Apply numerical methods to consumption models"
  
prerequisites:
  - "Basic microeconomics"
  - "Introductory Python programming"
  
related_materials:
  - "BufferStockTheory"
  - "ConsumptionSaving"
---

# Additional content for website display
This material demonstrates...
```

#### Documentation Improvements
**Files You Can Edit**:
- `README.md`: Repository overview and setup
- `ARCHITECTURE.md`: Technical architecture documentation
- `API-GUIDE.md`: Programmatic access documentation
- `pages/*.md`: Static content pages

**Style Guidelines**:
- Use clear, concise language
- Include code examples where appropriate
- Maintain consistent formatting
- Add cross-references to related documentation

### 2. Technical Contributions

#### Template Development
**Key Files**:
- `_layouts/material.html`: Individual research project pages
- `_layouts/materials.html`: Searchable catalog interface
- `_includes/structured-data.html`: Schema.org markup

**Best Practices**:
```html
<!-- Use semantic HTML -->
<article class="research-project">
  <header>
    <h1>{{ page.title }}</h1>
    <div class="metadata">
      <!-- Structured author information -->
    </div>
  </header>
  
  <!-- Include accessibility attributes -->
  <nav aria-label="Research project navigation">
    <!-- Navigation elements -->
  </nav>
</article>
```

#### Search and Filter Enhancement
**Current Implementation**: `assets/js/main.js`
**Enhancement Areas**:
- Advanced filtering options
- Search result ranking
- Faceted search interface
- Search analytics

**Example Enhancement**:
```javascript
// Add new filter category
function addTopicFilter() {
  const materials = window.materialsData;
  const topics = [...new Set(materials.flatMap(m => m.topics || []))];
  
  // Create filter UI
  const filterContainer = document.getElementById('filters');
  const topicFilter = createFilterElement('topic', topics);
  filterContainer.appendChild(topicFilter);
}
```

#### Performance Optimization
**Areas for Improvement**:
- Jekyll build time optimization
- Image optimization and lazy loading
- CSS/JavaScript minification
- Caching strategies

### 3. Data and Taxonomy Improvements

#### Research Taxonomy (`_data/research_taxonomy.yml`)
**Enhancement Areas**:
- Add new research domains
- Expand keyword hierarchies
- Include technical methodology details
- Add cross-disciplinary connections

**Example Addition**:
```yaml
domains:
  - name: "Behavioral Economics"
    description: "Integration of psychological insights into economic models"
    keywords: ["behavioral economics", "psychology", "decision making"]
    subdomains:
      - name: "Prospect Theory"
        description: "Decision making under uncertainty with psychological biases"
        concepts:
          - "Loss Aversion"
          - "Probability Weighting"
          - "Reference Dependence"
```

#### Structured Data Enhancement
**File**: `_includes/structured-data.html`
**Improvement Areas**:
- Add additional Schema.org types
- Include more detailed technical specifications
- Enhance author and organization markup
- Add course/educational content schemas

## Testing and Quality Assurance

### Local Testing
```bash
# Test site build
bundle exec jekyll build

# Test with draft content
bundle exec jekyll serve --drafts

# Test different configurations
bundle exec jekyll serve --config _config.yml,_config_dev.yml
```

### Content Validation
```bash
# Validate YAML frontmatter
python -c "import yaml; yaml.safe_load(open('_materials/example.md').read().split('---')[1])"

# Check internal links
bundle exec jekyll build && bundle exec htmlproofer ./_site --disable-external

# Validate structured data
# Use Google's Structured Data Testing Tool
```

### Accessibility Testing
- **Screen Reader**: Test with NVDA or VoiceOver
- **Keyboard Navigation**: Ensure all functionality accessible via keyboard
- **Color Contrast**: Use tools like WebAIM Color Contrast Checker
- **HTML Validation**: Use W3C Markup Validator

## Submission Process

### Pull Request Guidelines

1. **Branch Naming**: Use descriptive names
   - `feature/enhanced-search-filters`
   - `docs/api-guide-improvements`
   - `fix/mobile-navigation-issue`

2. **Commit Messages**: Follow conventional format
   ```
   feat: add advanced search filtering options
   
   - Implement topic-based filtering
   - Add author search functionality
   - Improve mobile search interface
   
   Closes #123
   ```

3. **PR Description Template**:
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement
   
   ## Testing
   - [ ] Local testing completed
   - [ ] Cross-browser testing (if applicable)
   - [ ] Accessibility testing (if applicable)
   
   ## Screenshots (if applicable)
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   ```

### Review Process

1. **Automated Checks**: GitHub Actions run build and validation tests
2. **Code Review**: Maintainers review technical implementation
3. **Content Review**: Subject matter experts review content accuracy
4. **Testing**: Deployment to staging environment for final testing
5. **Merge**: Integration into main branch and deployment

### Review Criteria
- **Functionality**: Does the change work as intended?
- **Performance**: Does it maintain or improve site performance? 
- **Accessibility**: Is it usable by people with disabilities?
- **SEO**: Does it maintain or improve search engine optimization?
- **Maintainability**: Is the code clean and well-documented?

## Special Considerations

### Content Generation Integration
**Important**: The `_materials/` directory is auto-generated
- Don't edit files in `_materials/` directly
- Improvements should go to source repositories or generation scripts
- Test content generation process when modifying `scripts/populate_remarks.py`

### SEO and AI Optimization
When making changes that affect discoverability:
- Update structured data markup as needed
- Maintain or improve keyword density
- Ensure machine-readable formats remain valid
- Test with Google's Rich Results Test

### Cross-Repository Coordination
Some improvements require coordination across repositories:
- **REMARK Standards**: Changes may affect the REMARK repository
- **Individual Projects**: Content improvements may need source repository updates
- **Automation**: Workflow changes may affect multiple repositories

## Getting Help

### Documentation
- **Architecture**: Read `ARCHITECTURE.md` for technical details
- **API Access**: See `API-GUIDE.md` for programmatic interfaces
- **Jekyll**: Official Jekyll documentation at jekyllrb.com

### Community Support
- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions and share ideas
- **Email**: Contact maintainers for sensitive issues

### Development Environment Issues
Common setup problems and solutions:

```bash
# Ruby version issues
rbenv install 3.0.4
rbenv local 3.0.4

# Bundle installation problems
bundle config set --local path 'vendor/bundle'
bundle install --retry=3

# Jekyll build errors
bundle exec jekyll doctor
bundle exec jekyll build --verbose
```

## Recognition

Contributors are recognized through:
- **GitHub**: Automatic contribution tracking
- **Website**: Contributor acknowledgments (when appropriate)
- **Academic**: Citation in research outputs using the infrastructure

Thank you for contributing to the advancement of computational economics research accessibility and reproducibility! 