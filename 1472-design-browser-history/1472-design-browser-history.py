# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self._history, self._future = [], []
#         # 'homepage' is the first visited URL.
#         self._current = homepage

#     def visit(self, url: str) -> None:
#         # Push 'current' in 'history' stack and mark 'url' as 'current'.
#         self._history.append(self._current)
#         self._current = url
#         # We need to delete all entries from 'future' stack.
#         self._future = []

#     def back(self, steps: int) -> str:
#         # Pop elements from 'history' stack, and push elements in 'future' stack.
#         while steps > 0 and self._history:
#             self._future.append(self._current)
#             self._current = self._history.pop()
#             steps -= 1
#         return self._current

#     def forward(self, steps: int) -> str:
#         # Pop elements from 'future' stack, and push elements in 'history' stack.
#         while steps > 0 and self._future:
#             self._history.append(self._current)
#             self._current = self._future.pop()
#             steps -= 1
#         return self._current
class DLLNode:
    def __init__(self, url: str):
        self.data = url
        self.prev, self.next = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        # 'homepage' is the first visited URL.
        self.linked_list_head = DLLNode(homepage)
        self.current = self.linked_list_head

    def visit(self, url: str) -> None:
        # Insert new node 'url' in the right of current node.
        new_node = DLLNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        # Make this new node as current node now.
        self.current = new_node

    def back(self, steps: int) -> str:
        # Move 'current' pointer in left direction.
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        # Move 'current' pointer in right direction.
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)