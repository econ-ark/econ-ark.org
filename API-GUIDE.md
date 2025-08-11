# Econ-ARK Website API Guide

## Overview

The Econ-ARK website provides multiple programmatic access methods for researchers, developers, and AI systems to interact with the computational economics research catalog. This guide covers all available APIs, data formats, and integration patterns.

## Access Methods

### 1. Jekyll Collections API

#### Materials Collection
**Endpoint Pattern**: `/materials/{project-name}/`
**Data Format**: JSON-LD embedded in HTML + structured HTML

**Example Request**:
```bash
curl -H "Accept: application/ld+json" \
     https://econ-ark.org/materials/bufferstocktheory/
```

**Response Structure**:
```json
{
  "@context": "https://schema.org",
  "@type": "ResearchProject",
  "name": "Buffer Stock Theory",
  "description": "Theoretical foundations of buffer stock saving behavior",
  "author": [
    {
      "@type": "Person",
      "name": "Christopher Carroll",
      "affiliation": "Johns Hopkins University"
    }
  ],
  "programmingLanguage": "Python",
  "codeRepository": "https://github.com/econ-ark/BufferStockTheory",
  "keywords": ["consumption", "saving", "buffer stock theory"],
  "abstract": "Full research abstract...",
  "datePublished": "2023-01-15",
  "version": "1.2.0"
}
```

#### Catalog Endpoint
**URL**: `/materials/`
**Format**: HTML with embedded structured data for all projects

**Programmatic Access**:
```python
import requests
from bs4 import BeautifulSoup
import json

# Fetch catalog page
response = requests.get('https://econ-ark.org/materials/')
soup = BeautifulSoup(response.content, 'html.parser')

# Extract JSON-LD data
scripts = soup.find_all('script', type='application/ld+json')
projects = [json.loads(script.string) for script in scripts]
```

### 2. Data Files API

#### Research Taxonomy
**URL**: `https://econ-ark.org/_data/research_taxonomy.yml`
**Format**: YAML
**Content**: Structured topic hierarchy, keywords, methodologies

**Usage Example**:
```python
import requests
import yaml

# Fetch taxonomy data
response = requests.get('https://econ-ark.org/_data/research_taxonomy.yml')
taxonomy = yaml.safe_load(response.text)

# Access domain information
for domain in taxonomy['domains']:
    print(f"Domain: {domain['name']}")
    for subdomain in domain['subdomains']:
        print(f"  - {subdomain['name']}: {subdomain['concepts']}")
```

#### Site Configuration
**URL**: `https://econ-ark.org/_config.yml`
**Format**: YAML
**Content**: Site metadata, keywords, plugin configuration

### 3. Feed APIs

#### RSS Feed
**URL**: `/feed.xml`
**Format**: RSS 2.0
**Content**: Recent site updates and new materials

**Consumption**:
```python
import feedparser

feed = feedparser.parse('https://econ-ark.org/feed.xml')
for entry in feed.entries:
    print(f"{entry.title}: {entry.published}")
```

#### Sitemap
**URL**: `/sitemap.xml`
**Format**: XML Sitemap Protocol
**Content**: All pages with priority and update frequency

### 4. Search and Filter API

#### Client-Side Filtering
**Implementation**: JavaScript-based search on materials page
**Parameters**: 
- `select`: Filter by type (REMARK, Notebook, etc.)
- Text search: Real-time filtering by keywords

**URL Examples**:
```
/materials/?select=REMARK
/materials/?select=Notebook
/materials/ (with search terms in interface)
```

**Programmatic Interface**:
```javascript
// Access search functionality
const materials = window.materialsData; // Embedded JSON data
const filtered = materials.filter(m => 
  m.tags.includes('REMARK') && 
  m.keywords.some(k => k.includes('consumption'))
);
```

## Data Extraction Patterns

### 1. Comprehensive Catalog Scraping

```python
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

class EconArkScraper:
    def __init__(self, base_url='https://econ-ark.org'):
        self.base_url = base_url
        
    def get_all_materials(self):
        """Extract all material metadata from catalog page"""
        response = requests.get(f'{self.base_url}/materials/')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract JSON-LD structured data
        materials = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string)
                if data.get('@type') == 'ResearchProject':
                    materials.append(data)
            except json.JSONDecodeError:
                continue
                
        return materials
    
    def get_material_detail(self, material_name):
        """Get detailed information for specific material"""
        url = f'{self.base_url}/materials/{material_name}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract structured data
        script = soup.find('script', type='application/ld+json')
        if script:
            return json.loads(script.string)
        return None
    
    def get_taxonomy(self):
        """Fetch research taxonomy structure"""
        response = requests.get(f'{self.base_url}/_data/research_taxonomy.yml')
        import yaml
        return yaml.safe_load(response.text)

# Usage
scraper = EconArkScraper()
all_materials = scraper.get_all_materials()
taxonomy = scraper.get_taxonomy()
```

### 2. Repository Integration

```python
import git
from pathlib import Path
import yaml

class EconArkIntegrator:
    def __init__(self, local_path=None, repo_url=None):
        self.local_path = Path(local_path or './econ-ark-data')
        self.repo_url = repo_url or 'https://github.com/econ-ark/econ-ark.org'
        
    def clone_website_repo(self):
        """Clone website repository for local analysis"""
        if not self.local_path.exists():
            repo = git.Repo.clone_from(self.repo_url, self.local_path)
        return git.Repo(self.local_path)
    
    def extract_materials_metadata(self):
        """Extract metadata from all material files"""
        materials_dir = self.local_path / '_materials'
        materials = {}
        
        for md_file in materials_dir.glob('*.md'):
            with open(md_file, 'r') as f:
                content = f.read()
                
            # Parse YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    materials[md_file.stem] = {
                        'metadata': metadata,
                        'content': parts[2].strip()
                    }
                    
        return materials
    
    def sync_with_source_repos(self, materials_metadata):
        """Clone source repositories for deeper analysis"""
        repos = {}
        for name, data in materials_metadata.items():
            repo_url = data['metadata'].get('repository-code')
            if repo_url:
                local_repo_path = self.local_path / 'repos' / name
                if not local_repo_path.exists():
                    repo = git.Repo.clone_from(repo_url, local_repo_path)
                    repos[name] = repo
                    
        return repos
```

### 3. Content Analysis and Mining

```python
import nltk
from collections import Counter
import matplotlib.pyplot as plt

class EconArkAnalyzer:
    def __init__(self, materials_data):
        self.materials = materials_data
        
    def keyword_analysis(self):
        """Analyze keyword distribution across materials"""
        all_keywords = []
        for material in self.materials:
            if 'keywords' in material:
                all_keywords.extend(material['keywords'])
                
        return Counter(all_keywords)
    
    def author_network(self):
        """Build author collaboration network"""
        from collections import defaultdict
        
        author_projects = defaultdict(list)
        collaborations = defaultdict(int)
        
        for material in self.materials:
            authors = material.get('author', [])
            material_name = material.get('name', '')
            
            # Track author projects
            for author in authors:
                author_name = author.get('name', '')
                if author_name:
                    author_projects[author_name].append(material_name)
            
            # Track collaborations
            for i, author1 in enumerate(authors):
                for author2 in authors[i+1:]:
                    name1 = author1.get('name', '')
                    name2 = author2.get('name', '')
                    if name1 and name2:
                        pair = tuple(sorted([name1, name2]))
                        collaborations[pair] += 1
                        
        return dict(author_projects), dict(collaborations)
    
    def topic_evolution(self):
        """Analyze research topic trends over time"""
        import pandas as pd
        from datetime import datetime
        
        data = []
        for material in self.materials:
            date_str = material.get('datePublished', '')
            keywords = material.get('keywords', [])
            
            if date_str and keywords:
                try:
                    date = datetime.fromisoformat(date_str)
                    for keyword in keywords:
                        data.append({
                            'date': date,
                            'keyword': keyword,
                            'project': material.get('name', '')
                        })
                except ValueError:
                    continue
                    
        df = pd.DataFrame(data)
        return df.groupby(['date', 'keyword']).size().unstack(fill_value=0)
```

## Integration Examples

### 1. Bibliography Generator

```python
def generate_bibtex(material_data):
    """Generate BibTeX entry from material metadata"""
    authors = ', '.join([
        f"{a.get('name', '')}" for a in material_data.get('author', [])
    ])
    
    bibtex = f"""@misc{% raw %}{{{material_data.get('name', '').lower()},
    title={% raw %}{{{material_data.get('name', '')}}}{% endraw %},
    author={% raw %}{{{authors}}}{% endraw %},
    year={% raw %}{{{material_data.get('datePublished', '')[:4]}}}{% endraw %},
    url={% raw %}{{{material_data.get('codeRepository', '')}}}{% endraw %},
    note={{Computational Economics Research Archive}}
}}"""
    return bibtex
```

### 2. Research Discovery Tool

```python
def find_related_research(query_keywords, materials_data, threshold=0.3):
    """Find materials related to query keywords"""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    
    # Prepare text corpus
    corpus = []
    for material in materials_data:
        text = ' '.join([
            material.get('name', ''),
            material.get('abstract', ''),
            ' '.join(material.get('keywords', []))
        ])
        corpus.append(text)
    
    # Add query
    query_text = ' '.join(query_keywords)
    corpus.append(query_text)
    
    # Calculate similarities
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]).flatten()
    
    # Return relevant materials
    relevant_indices = [i for i, sim in enumerate(similarities) if sim > threshold]
    return [(materials_data[i], similarities[i]) for i in relevant_indices]
```

### 3. Educational Content Aggregator

```python
def create_learning_path(topic, materials_data):
    """Create ordered learning path for specific topic"""
    
    # Filter materials by topic
    topic_materials = []
    for material in materials_data:
        keywords = [k.lower() for k in material.get('keywords', [])]
        if topic.lower() in keywords or topic.lower() in material.get('abstract', '').lower():
            topic_materials.append(material)
    
    # Sort by complexity (simple heuristic: notebook vs full research)
    def complexity_score(material):
        tags = material.get('tags', [])
        if 'Notebook' in tags:
            return 1  # Educational notebooks first
        elif 'Exploration' in material.get('tags', []):
            return 2  # Demonstrations second
        elif 'Replication' in tags:
            return 3  # Replications third
        else:
            return 4  # Original research last
    
    topic_materials.sort(key=complexity_score)
    
    return [{
        'title': material.get('name', ''),
        'url': f"https://econ-ark.org/materials/{material.get('name', '').lower()}/",
        'description': material.get('abstract', '')[:200] + '...',
        'complexity': complexity_score(material)
    } for material in topic_materials]
```

## Rate Limiting and Best Practices

### Responsible Usage
- **Rate Limiting**: Maximum 60 requests per minute per IP
- **Caching**: Cache responses locally to minimize repeated requests
- **User Agent**: Identify your application in HTTP headers
- **Error Handling**: Implement exponential backoff for failed requests

### Example Implementation
```python
import time
import requests
from functools import wraps

def rate_limited(max_calls_per_minute=60):
    min_interval = 60.0 / max_calls_per_minute
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.time()
            return ret
        return wrapper
    return decorator

@rate_limited(max_calls_per_minute=30)
def fetch_material(material_name):
    response = requests.get(
        f'https://econ-ark.org/materials/{material_name}/',
        headers={'User-Agent': 'Research-Analysis-Tool/1.0'}
    )
    return response
```

## Support and Contributing

### API Issues
- **Bug Reports**: GitHub issues on econ-ark.org repository
- **Feature Requests**: Discuss needs with development team
- **Documentation**: Contribute improvements to this guide

### Data Quality
- **Error Reporting**: Report inconsistent or missing data
- **Metadata Enhancement**: Suggest additional structured data fields
- **Search Improvements**: Recommend better categorization schemes

This API guide enables comprehensive programmatic access to the Econ-ARK research ecosystem while ensuring sustainable usage patterns and data quality. 