document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    // Load existing tasks
    fetchTasks();

    taskForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const task = taskInput.value.trim();
        if (task) {
            await createTask(task);
            taskInput.value = '';
            fetchTasks();
        }
    });

    async function fetchTasks() {
        const response = await fetch('/tasks');
        const tasks = await response.json();
        taskList.innerHTML = '';
        tasks.forEach(task => {
            const li = document.createElement('li');
            li.innerHTML = `
                <span>${task.task}</span>
                <div>
                    <button class="edit-btn" onclick="editTask(${task.id})">Edit</button>
                    <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
                </div>
            `;
            taskList.appendChild(li);
        });
    }

    async function createTask(task) {
        await fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task })
        });
    }

    window.editTask = async function(id) {
        const newTask = prompt('Edit task:');
        if (newTask) {
            await fetch(`/tasks/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task: newTask })
            });
            fetchTasks();
        }
    }

    window.deleteTask = async function(id) {
        if (confirm('Are you sure you want to delete this task?')) {
            await fetch(`/tasks/${id}`, {
                method: 'DELETE'
            });
            fetchTasks();
        }
    }
});
