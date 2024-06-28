import { dtf } from "@/lib/intl";
import { useFragment, useMutation } from "react-relay";
import { graphql } from "relay-runtime";
import { Icons } from "../icons";
import { Button } from "../ui/button";
import { Card, CardFooter, CardHeader, CardTitle } from "../ui/card";
import { TodoFragment$key } from "./__generated__/TodoFragment.graphql";

export const TodoFragment = graphql`
  fragment TodoFragment on Todo {
    id
    content
    createdAt
    updatedAt
  }
`;

const deleteTodoMutation = graphql`
  mutation TodoDeleteMutation($todoId: ID!, $connections: [ID!]!) {
    deleteTodo(todoId: $todoId) {
      deletedTodoId @deleteEdge(connections: $connections)
    }
  }
`;

type Props = {
  todo: TodoFragment$key;
  connectionId: string;
};

export default function Todo({ todo, connectionId }: Props) {
  // TODO: update todo list cache after mutation
  const [commitMutation, isMutationInFlight] = useMutation(deleteTodoMutation);
  const data = useFragment(TodoFragment, todo);

  return (
    <Card className="mb-4">
      <CardHeader>
        <div className="flex justify-between">
          <div className="flex flex-col">
            <CardTitle>{data.content}</CardTitle>
          </div>
          <Button
            size={"icon"}
            variant={"ghost"}
            disabled={isMutationInFlight}
            onClick={() => {
              commitMutation({
                variables: { todoId: data.id, connections: [connectionId] },
              });
            }}
          >
            <Icons.trash className="h-4 w-4" />
          </Button>
        </div>
      </CardHeader>
      <CardFooter>
        <p>created at {dtf.format(new Date(data.createdAt))}</p>
      </CardFooter>
    </Card>
  );
}
