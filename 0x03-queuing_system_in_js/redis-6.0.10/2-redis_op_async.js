#!/usr/bin/yarn dev

// Import necessary functions from 'util' and 'redis' packages
import { promisify } from 'util';
import { createClient, print } from 'redis';

// Create a new Redis client
const client = createClient();

// Event listener for Redis connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Function to set a new key-value pair in Redis
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Async function to retrieve and display a value from Redis
const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

// Main function to demonstrate Redis operations
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Event listener for successful Redis connection
client.on('connect', async () => {
  console.log('Redis client connected to the server');
  // Execute the main function once connected
  await main();
});
