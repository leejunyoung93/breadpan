import { connect } from "react-redux";
import { Dispatch, Action } from "redux";
import { actions as todosActions } from "../modules/todo";
import TodoList from "../components/TodoList";

const mapStateToProps = state => ({
    todoList : state.todoList
});

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
    getTodos: () => dispatch(todosActions.getTodos()),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(TodoList);
