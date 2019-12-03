import {call, put, takeLatest} from "redux-saga/effects";
import service from "service";


//todoActionTypes
const GET_TODOS = "GET_TODOS";
const GET_TODOS_SUCCESS = "GET_TODOS_SUCCESS";
const GET_TODOS_FAILURE = "GET_TODOS_FAILURE";


//todoParamsTypes
interface todoState {
    todoList: todoData
}

export interface todoData {
    todo1: {
        task: string;
    },
    todo2: {
        task: string;
    },
    todo3: {
        task: string;
    },
}

//todoActions
export const actions = {
    getTodos: () => ({
        type: GET_TODOS
    }),
    getTodosSuccess: ( payload : todoData) => ({
        type: GET_TODOS_SUCCESS,
        payload
    }),
    getTodosFailure: () => ({
        type: GET_TODOS_FAILURE
    }),

};


//todoReducer
export function todoReducer(
    state: todoState = {
        todoList: {
            todo1: {
                task: ""
            },
            todo2: {
                task: ""
            },
            todo3: {
                task: ""
            }
        }
    },
    action
): todoState {
    switch (action.type) {
        case GET_TODOS:
            return {
                ...state,
            };
        case GET_TODOS_SUCCESS:
            const { todoData : todoList } = action;
            return {
                ...state,
                todoList
            };
        case GET_TODOS_FAILURE:
            return {
                ...state,
            };
        default:
            return state;
    }
};

//todoAPI
export const api = {
    getTodos: async () => {
        return await service.get(`/todos`);
    },
};

//todoFunc
function* todoFunc() {
    try {
        const res = yield call(api.getTodos);
        if (res) {
            yield put({type: GET_TODOS_SUCCESS, todoData: res});
        }
    } catch (e) {
        yield put({type: GET_TODOS_FAILURE});
    }
};

export function* todoSaga() {
    yield takeLatest(GET_TODOS, todoFunc);
};