// tslint:disable-next-line
import { combineReducers } from "redux";
import { todoReducer as todo } from "modules/todo";

const createRootReducer = () =>
    combineReducers({
        // router: connectRouter(_history),
        todo
    });

const rootReducer = createRootReducer();

export default rootReducer;
