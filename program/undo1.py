from domain import *
class UndoController:
    def __init__(self):
        self._history = []
        self._index = 0
        self._duringUndo = False

    def recordOperation(self, operation):
        """
        Record the operation for undo/redo
        :param operation: an Operation instance
        :return:
        """
        if self._duringUndo == True:
            return
        self._history.append(operation)
        self._index += 1

    def undo(self):
        if self._index == 0:
            raise ValueError("No more undos")
        self._duringUndo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndo = False

    def redo(self):
        if self._index == len(self._history):
            raise ValueError("No more redos")
        self._duringUndo =True
        self._history[self._index].redo()
        self._index += 1
        self._duringUndo = False

# undo and redo are both functions

class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._params = parameters

    def call(self):
        self._function(*self._params)

class Operation:
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()

class CascadeOperation:
    def __init__(self, operation):
        self._operation = operation

    def undo(self):
        for op in self._operation:
            op.undo()

    def redo(self):
        for op in self._operation:
            op.redo()

