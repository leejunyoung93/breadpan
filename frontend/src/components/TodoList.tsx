import React, { FC, useEffect, useState } from "react";
import { todoListData } from "modules/todo";

interface Props {
  todoList: todoListData;
  getTodos: () => any;
}

const TodoList: FC<Props> = props => {
  const [todoList, setTodoList] = useState([]);
  const [toggle, setToggle] = useState(false);
  const [task, setTask] = useState("");
  useEffect(() => {
    const getTodos = props.getTodos;
    getTodos();
  }, [props.getTodos]);

  useEffect(() => {
    const todoObj = props.todoList;
    const arr = [];

    Object.keys(todoObj).forEach((el, key) => {
      arr.push({ task: todoObj[el].task, id: key, done: false });
    });
    setTodoList(arr);
  }, [props.todoList]);

  const onChange = e => {
    const { value } = e.target;
    setTask(value);
  };

  const onClickAdd = () => {
    const newObj = {
      task
    };
    setTodoList(todoList.concat(newObj));
    setTask("");
    setToggle(false);
  };

  const onClickToggle = () => {
    setToggle(!toggle);
  };

  const onClickDelete = (id, task) => {
    const filterArr = todoList.filter(el => {
      return task !== el.task;
    });
    const newTodoList = filterArr.concat({
      id,
      done: true,
      task
    });
    setTodoList(newTodoList);
  };

  return (
    <div className="todo-contents">
      {" "}
      Todo List
      <ul>
        {todoList.map((el, key) => {
          return (
            <li
              key={key}
              style={{
                color: el.done ? "red" : "black"
              }}
            >
              {el.task}
              {!el.done && (
                <button onClick={() => onClickDelete(key, el.task)}>
                  Delete
                </button>
              )}
            </li>
          );
        })}
        {toggle && <input type="text" onChange={onChange} value={task}></input>}
        {toggle && <button onClick={onClickAdd}>Add</button>}
        <button onClick={onClickToggle}>Create</button>
      </ul>
    </div>
  );
};

export default TodoList;
