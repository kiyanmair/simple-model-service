FROM ruby:3-slim

# Set the working directory inside the container
WORKDIR /app

# Install the requirements
COPY Gemfile .
RUN bundle install

# Copy the rest of the files
COPY . .
