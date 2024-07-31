import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Create job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test message',
};

// Create a job in the queue named 'push_notification_code'
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error(`Notification job failed: ${err}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Log job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Log job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
