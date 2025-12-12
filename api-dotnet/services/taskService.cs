using api_dotnet.Models;

namespace api_dotnet.Services
{
    public class TaskService
    {
        private readonly List<TaskItem> _tasks = new();
        private int _nextId = 1;

        public IEnumerable<TaskItem> GetAll() => _tasks;

        public TaskItem? GetById(int id) =>
            _tasks.FirstOrDefault(t => t.Id == id);

        public TaskItem Create(string title, string? description)
        {
            var task = new TaskItem
            {
                Id = _nextId++,
                Title = title,
                Description = description
            };

            _tasks.Add(task);
            return task;
        }

        public TaskItem? UpdateCompleted(int id, bool completed)
        {
            var task = GetById(id);
            if (task == null) return null;

            task.Completed = completed;
            return task;
        }

        public bool Delete(int id)
        {
            var task = GetById(id);
            if (task == null) return false;

            return _tasks.Remove(task);
        }
    }
}