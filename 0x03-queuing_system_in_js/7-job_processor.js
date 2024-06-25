#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

// Array of phone numbers that are not allowed to receive notifications
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];

// Create a new Kue queue
const queue = createQueue();

/**
 * Sends a push notification to a user.
 * @param {String} phoneNumber - The recipient's phone number
 * @param {String} message - The notification message
 * @param {Job} job - The Kue job object
 * @param {Function} done - Callback to be called when job is complete
 */
const sendNotification = (phoneNumber, message, job, done) => {
  let total = 2, pending = 2;
  let sendInterval = setInterval(() => {
    // Update job progress
    if (total - pending <= total / 2) {
      job.progress(total - pending, total);
    }
    
    // Check if phone number is blacklisted
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    
    // Log notification details when starting to send
    if (total === pending) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }
    
    // Decrement pending count and check if job is complete
    --pending || done();
    pending || clearInterval(sendInterval);
  }, 1000);
};

// Process jobs of type 'push_notification_code_2' with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
