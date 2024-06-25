#!/usr/bin/yarn dev

// Import necessary functions from the 'redis' package
import { createClient, print } from 'redis';

// Create a new Redis client
const client = createClient();

// Event listener for Redis connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Function to update a field in a Redis hash
const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

// Function to print all fields and values of a Redis hash
const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

// Main function to demonstrate Redis hash operations
function main() {
  // Object containing field-value pairs for the hash
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  // Iterate over the object and update the Redis hash
  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }

  // Print the entire hash
  printHash('HolbertonSchools');
}

// Event listener for successful Redis connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
  // Execute the main function once connected
  main();
});
