#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    // Filter tasks for completed ones
    const completedTasks = tasks.filter(task => task.completed);

    // Count completed tasks for each user
    const completedTasksByUser = completedTasks.reduce((acc, task) => {
      if (acc[task.userId]) {
        acc[task.userId]++;
      } else {
        acc[task.userId] = 1;
      }
      return acc;
    }, {});

    console.log(completedTasksByUser);
  }
});
