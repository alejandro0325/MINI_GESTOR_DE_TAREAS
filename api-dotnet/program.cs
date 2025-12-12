using api_dotnet.Models;
using api_dotnet.Services;

var builder = WebApplication.CreateBuilder(args);

// servicios
builder.Services.AddSingleton<TaskService>();

//cors para angular
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAngular", policy =>
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader());
});

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

//activar cors
app.UseCors("AllowAngular");

app.UseSwagger();
app.UseSwaggerUI();

//obtener tareas
app.MapGet("/tasks", (TaskService service) =>
{
    return Results.Ok(service.GetAll());
});

//crear tarea
app.MapPost("/tasks", (TaskService service, TaskCreateDto dto) =>
{
    if (string.IsNullOrWhiteSpace(dto.Title))
        return Results.BadRequest(new { error = "el titulo es obligatorio" });

    var created = service.Create(dto.Title, dto.Description);
    created.Completed = dto.Completed;
    return Results.Created($"/tasks/{created.Id}", created);
});

//actualizar tarea
app.MapPut("/tasks/{id}", (TaskService service, int id, TaskCreateDto dto) =>
{
    var task = service.GetById(id);
    if (task == null)
        return Results.NotFound(new { error = "tarea no encontrada" });

    if (!string.IsNullOrWhiteSpace(dto.Title))
        task.Title = dto.Title;

    if (dto.Description != null)
        task.Description = dto.Description;

    task.Completed = dto.Completed;

    return Results.Ok(task);
});

//eliminar tarea
app.MapDelete("/tasks/{id}", (TaskService service, int id) =>
{
    var deleted = service.Delete(id);
    if (!deleted)
        return Results.NotFound(new { error = "tarea no encontrada" });

    return Results.NoContent();
});

app.Run();