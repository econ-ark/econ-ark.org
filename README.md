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

## Local Build Instructions

1. Install Ruby 3.0.4
2. Run the following commands:
```
gem install bundler  # installs bundler gem
git clone ...        # clone repo
cd path/to/repo      # navigate to repo top level
bundle config set --local path 'vendor/bundle'  # set bundler output directory
bundle install       # bundle your jekyll application
bundle exec jekyll serve  # begin serving your site locally
```

