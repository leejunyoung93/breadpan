// tslint:disable-next-line
import { combineReducers } from "react-redux";
import { tempReducer as temp } from "modules/temp";

const createRootReducer = () =>
    combineReducers({
        // router: connectRouter(_history),
        temp
    });

const rootReducer = createRootReducer();

export default rootReducer;
