import React, { FC, useEffect } from "react";
import { todoData } from "modules/todo";

interface Props {
    todoList : todoData;
    getTodos: () => any;
}

const TodoList: FC<Props> = props => {
    useEffect(() => {
        props.getTodos();
    }, []);

    return (
        <div className="todo-contents"> Todo List</div>
    );
};

export default TodoList;