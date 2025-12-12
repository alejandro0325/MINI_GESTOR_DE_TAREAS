import { Component, OnInit } from '@angular/core';
import { Task, TaskService } from '../../services/task.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  tasks: Task[] = [];
  newTaskTitle: string = '';
  editingId: number | null = null;

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks() {
    this.taskService.getTasks().subscribe(res => {
      this.tasks = res;
    });
  }

  addTask() {
    if (!this.newTaskTitle.trim()) return;

    const task: Task = {
      title: this.newTaskTitle,
      completed: false
    };

    this.taskService.addTask(task).subscribe(() => {
      this.newTaskTitle = '';
      this.loadTasks();
    });
  }

  startEdit(task: Task) {
    this.editingId = task.id!;
    this.newTaskTitle = task.title;
  }

  saveEdit() {
    if (this.editingId === null) return;

    const updated: Task = {
      title: this.newTaskTitle,
      completed: false
    };

    this.taskService.updateTask(this.editingId, updated).subscribe(() => {
      this.editingId = null;
      this.newTaskTitle = '';
      this.loadTasks();
    });
  }

  deleteTask(id: number) {
    this.taskService.deleteTask(id).subscribe(() => {
      this.loadTasks();
    });
  }
}

