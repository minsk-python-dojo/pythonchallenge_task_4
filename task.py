from task_solver import TaskSolver


if __name__ == '__main__':
    solver: TaskSolver = TaskSolver()
    solver.solve()
    print(solver.result)