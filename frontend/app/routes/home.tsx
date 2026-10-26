import { Welcome } from "../welcome/welcome";
import { useApiStore } from "~/stores/api";

export default function Home() {
  const { call } = useApiStore();
  return (
    <div>
      <button onClick={() => call("/api/tables")}>CALL</button>
    </div>
  );
  // return <Welcome />;
}
