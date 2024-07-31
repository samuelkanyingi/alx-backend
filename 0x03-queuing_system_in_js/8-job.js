import kue from 'kue';

/**
 * Creates push notification jobs.
 * 
 * @param {Array} jobs - Array of job objects.
 * @param {Object} queue - Kue queue instance.
 * 
 * @throws Will throw an error if jobs is not an array.
 */
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Loop through each job in the jobs array
  jobs.forEach((jobData) => {
    // Create a job in the queue push_notification_code_3
    const job = queue.create('push_notification_code_3', jobData);

    // Event listener for job creation
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Event listener for job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Event listener for job failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Event listener for job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save((err) => {
      if (err) {
        console.log(`Failed to save job ${job.id}: ${err}`);
      }
    });
  });
}

export default createPushNotificationsJobs;
