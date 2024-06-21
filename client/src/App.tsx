import TodoController from "./components/todo-controller";
import TodoList from "./components/todo-list";

function App() {
  return (
    <div className="mx-auto max-w-lg flex flex-col w-full h-full justify-center gap-8">
      <TodoController />
      <TodoList />
    </div>
  );
}

export default App;
