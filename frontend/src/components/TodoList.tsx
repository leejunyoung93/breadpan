import React, {FC, useEffect, useState} from "react";
import { todoData } from "modules/todo";

interface Props {
    todoList : todoData;
    getTodos: () => any;
}

const TodoList: FC<Props> = props => {
    const [todoList, setTodoList] = useState([]);

    useEffect(() => {
        const getTodos = props.getTodos;
        getTodos();
    }, [props.getTodos]);

    useEffect(() => {
        const todoObj = props.todoList;
        const arr = [];

        Object.keys(todoObj).forEach(el=>{
            arr.push(todoObj[el])
        });

        setTodoList(arr);

    },[props.todoList]);


    return (
        <div className="todo-contents"> Todo List
            {}
        </div>

    );
};

export default TodoList;