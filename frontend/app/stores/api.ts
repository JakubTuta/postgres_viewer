import { create } from "zustand";
import axios, { type AxiosRequestConfig } from "axios";

export const useApiStore = create(() => ({
  call: async (
    url: string,
    method: "GET" | "POST" | "DELETE" | "PATCH" | "PUT" = "GET",
    data: object | null = null,
    headers: object | null = null,
  ) => {
    const config: AxiosRequestConfig = {
      url,
      baseURL: "http://localhost:8000",
      method,
    };

    if (data) config.data = data;
    if (headers) config.headers = headers;

    const response = await axios.request(config);
    console.log(response);
  },
}));
