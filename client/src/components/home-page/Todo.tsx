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
  mutation TodoDeleteMutation($todoId: GlobalID!) {
    deleteTodo(todoId: $todoId)
  }
`;

type Props = {
  todo: TodoFragment$key;
};

export default function Todo({ todo }: Props) {
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
              commitMutation({ variables: { todoId: data.id } });
            }}
          >
            <Icons.trash className="h-4 w-4" />
          </Button>
        </div>
      </CardHeader>
      <CardFooter>
        <p>{data.createdAt}</p>
      </CardFooter>
    </Card>
  );
}
