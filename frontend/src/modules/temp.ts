import { call, put, takeEvery } from "redux-saga/effects";
import service from "service";


//tempActionTypes
const TEMP = "TEMP";
const TEMP_SUCCESS = "TEMP_SUCCESS";
const TEMP_FAILURE = "TEMP_FAILURE";


//tempParamsTypes
interface tempState {
    //
}

export interface tempData {
    //
}

//tempActions
export const actions = {
    temp: () => ({
        type: TEMP
    }),
    tempSuccess: () => ({
        type: TEMP_SUCCESS
    }),
    tempFailure: () => ({
        type: TEMP_FAILURE
    }),

};

//tempReducer
export function tempReducer(
    state: tempState = {},
    action
): tempState {
    switch (action.type) {
        case TEMP:
            return {
                ...state,
            };
        case TEMP_SUCCESS:
            return {
                ...state,
            };
        case TEMP_FAILURE:
            return {
                ...state,
            };
        default:
            return state;
    }
};

//tempAPI
export const api = {
    temp: async () => {
        return await service.get(`/temp`);
    },
};

//tempFunc
function* tempFunc() {
    try {
        const res = yield call(api.temp);
        if (res) {
            yield put({type: TEMP_SUCCESS});
        }
    }
    catch (e) {
        yield put({type: TEMP_FAILURE});
    }
};

export function* tempSaga() {
    yield takeEvery(TEMP, tempFunc);
};