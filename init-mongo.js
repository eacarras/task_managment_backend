db = db.getSiblingDB('taskdb');  // Conectar a la base de datos 'taskdb'

// Crear la colección 'users' si no existe
db.createCollection('users');

// Crear la colección 'tasks' si no existe
db.createCollection('tasks');

// Agregar algunos datos iniciales a las colecciones (opcional)
db.users.insertOne({
  username: "admin",
  password: "admin123",
  email: "admin@example.com",
  role: "admin"
});

db.tasks.insertOne({
  title: "Sample Task",
  description: "This is a sample task.",
  status: "in-progress",
  user_id: "admin"
});
