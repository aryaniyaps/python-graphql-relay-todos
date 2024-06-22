import { Skeleton } from "../ui/skeleton";

function TodoSkeleton() {
  return <Skeleton className="h-[125px] w-full rounded-xl" />;
}

export default function TodoListSkeleton() {
  return (
    <div className="flex flex-col gap-2">
      {[...Array(3)].map((_, i) => (
        <TodoSkeleton key={i} />
      ))}
    </div>
  );
}
