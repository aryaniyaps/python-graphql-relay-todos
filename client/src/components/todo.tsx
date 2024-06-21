import { gql, useMutation } from "@apollo/client";
import { Icons } from "./icons";
import { Button } from "./ui/button";
import { Card, CardFooter, CardHeader, CardTitle } from "./ui/card";

const DELETE_TODO = gql`
  mutation DeleteTodo($noteId: String!) {
    deleteNote(noteId: $noteId) {
      id
    }
  }
`;

export default function Todo({ todo }: { todo: any }) {
  // TODO: update todo list cache after mutation
  const [deleteTodo, { loading }] = useMutation(DELETE_TODO);

  return (
    <Card>
      <CardHeader>
        <div className="flex justify-between">
          <div className="flex flex-col">
            <CardTitle>{todo.content}</CardTitle>
          </div>
          <Button
            size={"icon"}
            variant={"ghost"}
            disabled={loading}
            onClick={async () => {
              await deleteTodo({ variables: { noteId: todo.id } });
            }}
          >
            <Icons.trash className="h-4 w-4" />
          </Button>
        </div>
      </CardHeader>
      <CardFooter>
        <p>{todo.createdAt}</p>
      </CardFooter>
    </Card>
  );
}
