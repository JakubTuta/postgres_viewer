import { useTablesStore } from "@/stores/tables";

export default function Home() {
  const tables = useTablesStore((state) => state.tables);
  const isLoading = useTablesStore((state) => state.isLoading);
  const error = useTablesStore((state) => state.error);

  return (
    <section className="space-y-4 p-6">
      <h1 className="text-2xl font-semibold">Tables</h1>

      {isLoading && <p>Loading tables...</p>}

      {error && <p role="alert">Could not load tables: {error}</p>}

      {!isLoading && !error && tables.length === 0 && <p>No tables found.</p>}

      {tables.length > 0 && (
        <ul className="list-inside list-disc space-y-2">
          {tables.map((table) => (
            <li key={table}>{table}</li>
          ))}
        </ul>
      )}
    </section>
  );
}
