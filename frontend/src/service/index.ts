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

const link = window.location.origin + "/";
// const link = "http://localhost:6553/";
const host = `${link}api/v1`;

const service = new ResourceService(host);

export default service;
