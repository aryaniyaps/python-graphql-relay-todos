import { useMutation } from "react-relay";
import { graphql } from "relay-runtime";
import { Icons } from "../icons";
import { Button } from "../ui/button";
import { Card, CardFooter, CardHeader, CardTitle } from "../ui/card";

export const TodoFragment = graphql`
  fragment TodoFragment on Todo {
    id
    content
    createdAt
    updatedAt
  }
`;

const deleteTodoMutation = graphql`
  mutation TodoDeleteMutation($todoId: GlobalID!) {
    deleteTodo(todoId: $todoId)
  }
`;

type Props = {
  todo: {
    id: string;
    content: string;
    createdAt: string;
    updatedAt: string;
  };
};

export default function Todo({ todo }: Props) {
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
              commitMutation({ variables: { todoId: todo.id } });
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
