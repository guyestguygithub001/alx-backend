#!/usr/bin/yarn dev

// Import the createQueue function from the 'kue' package
// Kue is a priority job queue backed by Redis
import { createQueue } from 'kue';

// Create a new queue with default configuration
const queue = createQueue();

// Define a function to simulate sending a notification
// This function logs the phone number and message to the console
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

// Set up a process to handle jobs of type 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
  // Extract phoneNumber and message from the job data
  // Call the sendNotification function with these parameters
  sendNotification(job.data.phoneNumber, job.data.message);
  
  // Call the done function to indicate that the job is completed
  // This is important for Kue to know the job has been processed
  done();
});
