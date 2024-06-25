#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

// Create a new Redis client
const client = createClient();

// Event listener for Redis connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Event listener for successful Redis connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Function to set a new key-value pair in Redis
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Function to retrieve and display a value from Redis
const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

// Example usage: Display the value for 'Holberton'
displaySchoolValue('Holberton');

// Example usage: Set a new key-value pair
setNewSchool('HolbertonSanFrancisco', '100');

// Example usage: Display the value for 'HolbertonSanFrancisco'
displaySchoolValue('HolbertonSanFrancisco');
