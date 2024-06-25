#!/usr/bin/yarn dev

// Import the createQueue function from the 'kue' package
import { createQueue } from 'kue';

// Define an array of job data, each containing a phoneNumber and a message
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  // ... (other job data objects)
];

// Create a new queue named 'push_notification_code_2'
const queue = createQueue({ name: 'push_notification_code_2' });

// Iterate over each job in the jobs array
for (const jobInfo of jobs) {
  // Create a new job in the queue with type 'push_notification_code_2' and the current job data
  const job = queue.create('push_notification_code_2', jobInfo);

  // Set up event listeners for the job
  job
    // When the job is added to the queue
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    // When the job is completed successfully
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    })
    // When the job fails
    .on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());
    })
    // When the job reports progress
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });

  // Save the job to the queue
  job.save();
}
