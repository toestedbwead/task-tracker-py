# Task CLI

A simple command-line task tracker that stores tasks in a JSON file.

project url: https://roadmap.sh/projects/task-tracker

## Usage

```bash
python task_cli.py <command> [arguments]
Commands
add "task description" - Add new task

list - Show all tasks

list <status> - Filter tasks by status (todo, in progress, done)

update <id> "new description" - Update task description

mark <id> <status> - Change task status

delete <id> - Remove task