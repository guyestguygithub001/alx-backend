#!/usr/bin/yarn dev

// Import the createQueue function from the 'kue' package
// Kue is a priority job queue backed by Redis
import { createQueue } from 'kue';

// Create a new queue named 'push_notification_code'
// This queue will handle jobs related to push notifications
const queue = createQueue({name: 'push_notification_code'});

// Create a new job in the queue
// The job type is 'push_notification_code'
// The job data includes a phoneNumber and a message
const job = queue.create('push_notification_code', {
  phoneNumber: '07045679939',
  message: 'Account registered',
});

// Set up event listeners for the job
job
  // Event listener for when the job is added to the queue
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  // Event listener for when the job is completed successfully
  .on('complete', () => {
    console.log('Notification job completed');
  })
  // Event listener for when the job fails
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });

// Save the job to the queue
// This actually adds the job to the queue and makes it available for processing
job.save();
