import TodoController from "./components/todo-controller";
import TodoList from "./components/todo-list";

function App() {
  return (
    <div className="mx-auto max-w-lg flex items-center w-full h-full justify-center">
      <div className="flex flex-col items-center w-full h-full justify-center gap-8 py-8">
        <TodoController />
        <TodoList />
      </div>
    </div>
  );
}

export default App;
