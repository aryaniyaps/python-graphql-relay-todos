import { gql, useQuery } from "@apollo/client";

const GET_TODOS = gql`
  query GetTodos {
    allNotes {
      id
      content
      createdAt
      updatedAt
    }
  }
`;

export default function TodoList() {
  const { loading, error, data } = useQuery(GET_TODOS);

  if (loading) return "Loading...";
  if (error) return `Error! ${error.message}`;

  return (
    <div>
      {data.allNotes.map((note) => {
        <div key={note.id}>{note.content}</div>;
      })}
    </div>
  );
}
