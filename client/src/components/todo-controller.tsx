import { gql, useMutation } from "@apollo/client";
import { SubmitHandler, useForm } from "react-hook-form";

const CREATE_TODO = gql`
  mutation CreateTodo($content: String!) {
    createNote(content: $content) {
      id
      content
      createdAt
      updatedAt
    }
  }
`;

type CreateTodoInput = {
  content: string;
};

export default function TodoController() {
  // TODO: update todo list cache after mutation
  const [createTodo, { loading, error }] = useMutation(CREATE_TODO);

  const { register, handleSubmit } = useForm<CreateTodoInput>();

  const onSubmit: SubmitHandler<CreateTodoInput> = async (data) => {
    await createTodo({ variables: { content: data.content } });
  };

  if (loading) return "Submitting...";
  if (error) return `Submission error! ${error.message}`;

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input {...register("content", { required: true })} />
        <button type="submit">Create Todo</button>
      </form>
    </div>
  );
}
