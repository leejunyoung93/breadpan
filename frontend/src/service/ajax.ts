import axios, {
  AxiosInstance,
  AxiosRequestConfig,
  AxiosPromise,
  AxiosResponse,
  AxiosError
} from "axios";

export interface AjaxOptions {
  baseURL: string;
  headers?: object;
  headerAuthorization?: string | (() => string);
}

export default class Ajax {
  private options: AjaxOptions;

  public constructor(options?: AjaxOptions) {
    this.options = options;
  }

  private static buildOptions(options: AjaxOptions): AxiosRequestConfig {
    const config: AxiosRequestConfig = {};
    if (options.baseURL) {
      config.baseURL = options.baseURL;
    }
    if (options.headerAuthorization) {
      if (!config.headers) {
        config.headers = {};
      }
      const authorization =
        typeof options.headerAuthorization === "string"
          ? options.headerAuthorization
          : options.headerAuthorization();
      config.headers["Authorization"] = authorization;
    }
    if (options.headers) {
      if (!config.headers) {
        config.headers = {};
      }

      for (const key of Object.keys(options.headers)) {
        config.headers[key] = options.headers[key];
      }
    }
    return config;
  }

  private static instance(options?: AjaxOptions): AxiosInstance {
    const result: AxiosInstance = options
      ? axios.create(Ajax.buildOptions(options))
      : axios.create();
    result.interceptors.response.use(
      (response: AxiosResponse) => response.data,
      (error: AxiosError) => Promise.reject(error.response)
    );
    return result;
  }
  public instance = (): AxiosInstance => Ajax.instance(this.options);

  public get = (url: string): AxiosPromise => {
    return this.instance().get(url) as AxiosPromise;
  };
  public post = (url: string, data: any): AxiosPromise => {
    return this.instance().post(url, data);
  };
  public delete = (url: string): AxiosPromise => {
    return this.instance().delete(url);
  };
  public put = (url: string, data: any): AxiosPromise => {
    return this.instance().put(url, data);
  };
  public patch = (url: string, data: any): AxiosPromise => {
    return this.instance().patch(url, data);
  };
}
