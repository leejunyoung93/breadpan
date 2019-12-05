import { call, put, takeLatest } from "redux-saga/effects";
import service from "service";

//todoListActionTypes
const GET_TODOS = "GET_TODOS";
const GET_TODOS_SUCCESS = "GET_TODOS_SUCCESS";
const GET_TODOS_FAILURE = "GET_TODOS_FAILURE";

//todoListParamsTypes
interface todoState {
  todoList: todoListData;
}

export interface todoListData {
  [key: string]: {
    [key: string]: string;
  };
}

//todoListActions
export const actions = {
  getTodos: () => ({
    type: GET_TODOS
  }),
  getTodosSuccess: (payload: todoListData) => ({
    type: GET_TODOS_SUCCESS,
    payload
  }),
  getTodosFailure: () => ({
    type: GET_TODOS_FAILURE
  })
};

//todoListReducer
export function todoReducer(
  state: todoState = {
    todoList: {}
  },
  action
): todoState {
  switch (action.type) {
    case GET_TODOS:
      return {
        ...state
      };
    case GET_TODOS_SUCCESS:
      const { todoListData: todoList } = action;
      return {
        ...state,
        todoList
      };
    case GET_TODOS_FAILURE:
      return {
        ...state
      };
    default:
      return state;
  }
}

//todoListAPI
export const api = {
  getTodos: async () => {
    return await service.get(`/todos`);
  }
};

//todoListFunc
function* todoFunc() {
  try {
    const res: todoListData = yield call(api.getTodos);
    if (res) {
      yield put({ type: GET_TODOS_SUCCESS, todoListData: res });
    }
  } catch (e) {
    yield put({ type: GET_TODOS_FAILURE });
  }
}

export function* todoSaga() {
  yield takeLatest(GET_TODOS, todoFunc);
}
