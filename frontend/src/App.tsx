import React, {FC} from 'react';
import { Provider } from "react-redux";
import {store} from "./store";
import './App.css';

import TodoList from "./pages/TodoList";


const App: FC = () => {
  return (
      <Provider store={store}>
          <TodoList/>
      </Provider>
  );
}

export default App;
