import {
  Sidebar,
  SidebarContent,
  SidebarHeader,
} from "@/components/ui/sidebar";
import { House, Table } from "lucide-react";
import { SidebarLogo } from "./logo";
import { NavItems } from "./items";

const tabs = [
  {
    title: "Dashboard",
    url: "/",
    icon: House,
  },
  {
    title: "Tables",
    url: "/tables",
    icon: Table,
  },
];

export function AppSidebar() {
  return (
    <Sidebar collapsible="icon">
      <SidebarHeader>
        <SidebarLogo />
      </SidebarHeader>

      <SidebarContent>
        <NavItems items={tabs} />
      </SidebarContent>
    </Sidebar>
  );
}
