 # Quiz

 

## Welcome Message

 

Welcome to this coding test. For enhanced readability, please copy the contents of this documentation into a file using Markdown's extension `.md`.

 

The coding test is not homework; rather, it's an opportunity for you to showcase your:

 

- Coding style

- Coding skills

- Design patterns

- Clear thinking

 

## How to Submit

 

Please create a public Repository on Github and share us with the `URL link to your repository`. _Please don't share the code with Email_.

 

## Code Tests Folder Structure

 

Please create a folder structure like the following:

 

```

.

|-- webapp        <-- This folder contains the FastAPI application

|   |-- main.py   <-- This is the main entry point of the application

|-- quiz.py       <-- This file contains the quiz.

|-- review.py     <-- This file contains your code review tasks.

|--

```

 

#### 1 Quiz.py

 

Your `quiz.py` should have the following content.

 

```python

 

def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions

 

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """

    pass

 

def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    pass

```

 

### 2 Webapp

 

Build a basic real-time chat application using FastAPI Framework and WebSockets. The application should have the following requirements:

 

- Allow multiple clients to connect to the server and broadcast messages to all connected clients in real time

 

  - When a message is received from a client, broadcast this message to all connected clients.

 

- Each client should be able to send and receive messages

  - Each client should send its username upon connection

  - The server should prepend the username to each message before broadcasting it to other clients.

 

#### Example

 

- When Client A connects, it sends its username "ClientA"

- When Client B connects, it sends its username "ClientB"

- When ClientA sends a message "Hello, everyone!", the server broadcasts "CLientA: Hello, everyone!" to all connected clients

- When ClientB sends a message "Hi, ClientA!", the server broadcasts "ClientB: Hi, ClientA!" to all connected clients

- Disconnection

  - Handle client disconnections gracefully and remove their WebSocket connections from the active connections list

 

The following is an example code for your `main.py` file, it gives you the basic code structure. You can change it by your design.

 

```python

 

app = FastAPI()

 

class ConnectionManager:

    def __init__(self):

        pass

 

    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        pass

 

    def disconnect(self, websocket: WebSocket):

        pass

 

    async def broadcast(self, message: str):

        for connection in self.active_connections:

            pass

 

manager = ConnectionManager()

 

@app.websocket("/ws/{username}")

async def websocket_endpoint(websocket: WebSocket, username: str):

    pass

 

```

 

### 3 Code Review

 

In this part, you need to conduct the `Code Reviewing` tasks. Please review the following code by:

 

- Detecting if is there anything wrong with the code?

- If there’s, show where and show how to fix.

 

The following is the content of `review.py`.

 

```python

 

# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

 

# Review 2

def format_greeting(name, age):

    return "Hello, my name is {name} and I am {age} years old."

 

# Review 3

class Counter:

    count = 0

 

    def __init__(self):

        self.count += 1

 

    def get_count(self):

        return self.count

 

# Review 4

import threading

 

class SafeCounter:

    def __init__(self):

        self.count = 0

 

    def increment(self):

        self.count += 1

 

def worker(counter):

    for _ in range(1000):

        counter.increment()

 

counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

 

for t in threads:

    t.join()

 

# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts

 

```