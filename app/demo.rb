require 'httpx'
require 'uri'
require 'json'

# Flush stdout immediately for real-time output
$stdout.sync = true

model_service_url = URI('http://model:80/embed')

# Get the text to embed from the CLI arguments
text_value = ARGV[0]

loop do
  # Send a request to the model service
  response = HTTPX.post(model_service_url, json: { text: text_value })
  
  # Handle the response
  if response.status >= 200 && response.status < 300
    vector = JSON.parse(response.body)
    puts "Received a vector of length #{vector.length}"
  else
    puts "Error: #{response.status}"
  end
  
  # Wait before sending the next request
  sleep 30
end
