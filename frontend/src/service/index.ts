import Ajax from "./ajax";
// import { getToken } from "others/token";

class ResourceService extends Ajax {
  public constructor(host: string) {
    super({
      headerAuthorization: () => {
        // if (getToken()) {
        //   return `Bearer ${getToken()}`;
        // }
        return "";
      },
      headers: {
        accept: "application/json",
        "Content-Type": "application/json"
      },
      baseURL: host
    });
  }
}

const link = "http://127.0.0.1:5000/";

const host = `${link}`;
const service = new ResourceService(host);
export default service;
