namespace api_dotnet.Models
{
    public class TaskCreateDto
    {
        public string? Title { get; set; }
        public string? Description { get; set; }
        public bool Completed { get; set; }
    }
}