import { create } from "zustand";
import type { Table } from "@/types/table";
import { useApiStore } from "./api";

interface TablesState {
  tables: Table[];
  isLoading: boolean;
  error: string | null;
  fetchTables: () => Promise<void>;
}

export const useTablesStore = create<TablesState>((set, get) => ({
  tables: [],
  isLoading: false,
  error: null,

  fetchTables: async () => {
    if (get().isLoading) return;

    set({ isLoading: true, error: null });

    try {
      const { call } = useApiStore.getState();
      const response = await call("/api/tables");
      set({ tables: response.data });
    } catch (error) {
      set({
        error:
          error instanceof Error ? error.message : "Failed to fetch tables.",
      });
    } finally {
      set({ isLoading: false });
    }
  },
}));
