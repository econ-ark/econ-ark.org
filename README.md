# The Econ-ARK Website
 
This site uses Markdown along with Jekyll site generator to compile a static site.

The site code is hosted here on GitHub, the compiled site is hosted on Netlify, and DNS configured with AWS Route53.

Any edits to any of the markdown files will be recompiled and pushed live upon commit to `master` branch. Changes should be visible <10 minutes.

So, to trigger a recompile (for example, in case some external source material has changed), edit this README.md

You can also browse directly to the site's info for a particular resource with a command like:

https://econ-ark.org/materials/bufferstocktheory

or 

https://econ-ark.org/materials/distributionofwealthmpc

(note that our convention is that the name of the "material" should be all lower case)

- Updated SolvingMicroDSOPs.md to point to llorracc/SolvingMicroDSOPS/SolvingMicroDSOPS.ipynb
- Fixed path in REMARKs/DurableConsumerType.md
- 2023-03-14: Updated LucasAssetPrice.md on DemARK

## Local Development

### Option 1: Docker (Recommended)

The easiest way to run the site locally is using Docker:

```bash
# Build and start the Jekyll server
docker-compose up --build

# Or run in detached mode (background)
docker-compose up --build -d

# View logs
docker-compose logs jekyll

# Stop the server
docker-compose down
```

The site will be available at http://localhost:4000 with live reload enabled.

### Option 2: Native Ruby Setup

If you prefer to run Jekyll natively:

**Prerequisites:**
- Ruby 3.0.4+ (recommended to use rbenv for version management)
- Bundler gem

**Setup:**
```bash
# Install rbenv (if not already installed)
brew install rbenv ruby-build

# Install and set Ruby version
rbenv install 3.1.2
rbenv local 3.1.2

# Install bundler
gem install bundler

# Install Jekyll dependencies
bundle config set --local path 'vendor/bundle'
bundle install

# Start the Jekyll server
bundle exec jekyll serve --livereload
```

The site will be available at http://localhost:4000

## Development Notes

- **Live Reload**: Both Docker and native setups include live reload functionality
- **Port**: The site runs on port 4000 by default
- **Content Changes**: Markdown files will auto-regenerate when saved
- **Configuration Changes**: Restart the server after modifying `_config.yml`

## Troubleshooting

### Ruby Version Issues
If you encounter Ruby version conflicts, use the Docker setup which ensures a consistent environment.

### Permission Errors
On macOS, if you get permission errors with native Ruby, use rbenv instead of system Ruby.

### Port Conflicts
If port 4000 is already in use:
```bash
# For Docker
docker-compose down

# For native Jekyll
bundle exec jekyll serve --port 4001
```

