FROM ruby:3.0

WORKDIR /site

# Install bundler and Jekyll
RUN gem install bundler jekyll

# Copy the Gemfile first for better caching
COPY Gemfile* ./

# Install dependencies
RUN bundle install

# Copy the rest of the site
COPY . .

# Expose port 4000
EXPOSE 4000

# Start Jekyll server
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "4000", "--livereload"] 