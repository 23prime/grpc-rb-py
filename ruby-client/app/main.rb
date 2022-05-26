require "securerandom"

require_relative "lib/helloworld_pb"
require_relative "lib/helloworld_services_pb"

def main
  puts "Start Ruby gRPC client..."
  stub = Helloworld::Greeter::Stub.new("localhost:50051", :this_channel_is_insecure)
  puts "Done."

  10.times do
    user = SecureRandom.hex(4)
    age = rand(99)
    puts "user: #{user}, age: #{age}"

    message = stub.say_hello(Helloworld::HelloRequest.new(name: user, age: age)).message
    puts "Greeting: #{message}"
  end
end

main
