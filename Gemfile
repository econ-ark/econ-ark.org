source 'https://rubygems.org'

# Jekyll core
gem 'jekyll', '~> 4.3.0'

# Theme and styling
gem 'minima', '~> 2.5'

# Development dependencies
group :jekyll_plugins do
  gem 'jekyll-seo-tag', '~> 2.8'      # Automatic SEO meta tags
  gem 'jekyll-sitemap', '~> 1.4'      # XML sitemap generation  
  gem 'jekyll-feed', '~> 0.17'        # RSS/Atom feed generation
  gem 'jekyll-redirect-from', '~> 0.16'  # URL redirection
end

# Windows and JRuby compatibility
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem 'tzinfo', '>= 1', '< 3'
  gem 'tzinfo-data'
end

# Performance booster for watching directories on Windows
gem 'wdm', '~> 0.1.1', :platforms => [:mingw, :x64_mingw, :mswin]

# Lock JRuby to 2.5 branch
gem 'http_parser.rb', '~> 0.6.0', :platforms => [:jruby]

# gem 'github-pages', group: :jekyll_plugins # Removed - incompatible with Jekyll 4.x, site uses GitHub Actions not GitHub Pages Jekyll

gem 'webrick' # needed to build locally

