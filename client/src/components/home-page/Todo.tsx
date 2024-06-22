import { useMutation } from "react-relay";
import { graphql } from "relay-runtime";
import { Icons } from "../icons";
import { Button } from "../ui/button";
import { Card, CardFooter, CardHeader, CardTitle } from "../ui/card";

const deleteTodoMutation = graphql`
  mutation TodoDeleteMutation($noteId: String!) {
    deleteNote(noteId: $noteId) {
      id
    }
  }
`;

export default function Todo({ todo }: { todo: any }) {
  // TODO: update todo list cache after mutation
  const [commitMutation, isMutationInFlight] = useMutation(deleteTodoMutation);

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
            disabled={isMutationInFlight}
            onClick={() => {
              commitMutation({ variables: { noteId: todo.id } });
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
