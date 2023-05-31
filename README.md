# MyTasks

This project is basead on [Taskbook](https://github.com/klaudiosinani/taskbook.git). Using the Taskbook the need arose to create sub-tasks, so I remodeled the project to use a tree structure, thus allowing to group tasks.

### Description
MyTasks allows you to simply and efficiently manage your tasks and notes from your terminal. You can also organize your tasks into subtasks (boards). All this using a simple and minimal syntax.

### Structure
MyTasks uses a tree structure, where the leaf nodes are the tasks and notes, and the branches are the boards.

<div align="center">
  <img alt="structure" width="50%" src="structure.svg"/>
</div>

## Install

  Clone this repository.
  ```
  git clone https://github.com/fanhenrique/my-tasks.git
  ```

## Usage


### Tree View

### Timeline View

### Help

  Use option `--help` for help.
  
  ```
  python main.py --help
  ```

### Create Board

  To create a new board use the `--board`/`-b` option with your description following right after.
    
  ```
  python main.py --board my-board
  ```

### Create Task

  To create a new task use the `--task`/`-t` option with your description following right after.
  
  ```
  python main.py --task write document
  ```

### Create Note

  To create a new note use the `--note`/`-t` option with your description following right after.
    
  ```
  python main.py --note caution with orthography at the document
  ```

### Delete Node

  To delete some node use the `--delete`/`-d` option followed by the list of ids of the nodes.
  
  ```
  python main.py --delete 3 4 7 9
  ```

### Edit Node

  To edit some node use the `--edit`/`-e` option followed by the list of ids of the nodes. In this case it is necessary to indicate the id of the node
  
  ```
  python main.py 3 --edit new name node
  ```

### Starred Node

  To mark a node as starred, use the `--star`/`-x` option followed by the list of ids of the tasks.
    
  ```
  python main.py --star 2 3 5
  ```

### Checked Task

  To mark a task as complete/incomplete, use the `--check`/`-c` option followed by the list of ids of the tasks.
    
  ```
  python main.py --check 2 3 5
  ```

### Started Task

  To mark a task as started/not started, use the `--started`/`-s` option followed by the list of ids of the tasks.
  
  ```
  python main.py --started 2 3 5
  ```

### Change priority level Task

  To change the priority level of a task, use the `--priority <level>`/`-p <level>` option. In this case it is necessary to indicate the id of the task

  - 0 - Default priority 
  - 1 - Low priority 
  - 2 - High priority 

  ```
  python main.py 4 --priority 1
  ```
  
## Contact
<div>
  <p><strong>Henrique Fan</strong></p>
  <a href = "fanhenrique@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank" > </a>
  <a href="https://www.linkedin.com/in/fanhenrique/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>
