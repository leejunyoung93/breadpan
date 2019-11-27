import { all, fork } from "redux-saga/effects";

import { tempSaga } from "modules/temp";

export default function* rootSaga() {
    yield all([
        fork(tempSaga),
    ]);
}





