import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track the job progress to 0 out of 100
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error message
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  // Track the job progress to 50%
  job.progress(50, 100);

  // Log the notification message
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Create a queue
const queue = kue.createQueue();

// Process jobs from the queue 'push_notification_code_2'
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Event listeners for logging
queue.on('job complete', (id) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job ${job.id} completed`);
    job.remove((err) => {
      if (err) throw err;
      console.log(`Removed completed job ${job.id}`);
    });
  });
});

queue.on('job failed', (id, errorMessage) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });
});

queue.on('job progress', (id, progress) => {
  console.log(`Notification job ${id} ${progress}% complete`);
});
