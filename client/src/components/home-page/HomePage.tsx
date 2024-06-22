import TodoController from "./TodoController";
import TodoList from "./TodoList";

export default function HomePage() {
  return (
    <div className="flex flex-col items-center w-full h-full justify-center gap-8 py-8">
      <TodoController />
      <TodoList />
    </div>
  );
}
