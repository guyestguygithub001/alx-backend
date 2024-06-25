#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs from an array of job information.
 * @param {Job[]} jobs - Array of job information objects
 * @param {Queue} queue - Kue queue instance
 * @throws {Error} If jobs is not an array
 */
export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  
  for (const jobInfo of jobs) {
    // Create a new job in the queue
    const job = queue.create('push_notification_code_3', jobInfo);
    
    // Set up event listeners for the job
    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });
    
    // Save the job to the queue
    job.save();
  }
};

export default createPushNotificationsJobs;
