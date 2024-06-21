import TodoController from "./components/todo-controller";
import TodoList from "./components/todo-list";

function App() {
  return (
    <div className="flex flex-col w-full h-full">
      <TodoController />
      <TodoList />
    </div>
  );
}

export default App;
