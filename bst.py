import random
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class BSTNode:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError(f"Cannot create a BSTNode with {type(value)}")

        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f"BSTNode(value={self.value})"

    def __eq__(self, other):
        if isinstance(other, BSTNode):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            raise ValueError(f"Cannot compare types {type(self)} with {type(other)}")

    def __le__(self, other):
        if isinstance(other, BSTNode):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        else:
            raise ValueError(f"Cannot compare types {type(self)} with {type(other)}")

    def __lt__(self, other):
        if isinstance(other, BSTNode):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            raise ValueError(f"Cannot compare types {type(self)} with {type(other)}")

    def __ge__(self, other):
        if isinstance(other, BSTNode):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        else:
            raise ValueError(f"Cannot compare types {type(self)} with {type(other)}")

    def __gt__(self, other):
        if isinstance(other, BSTNode):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        else:
            raise ValueError(f"Cannot compare types {type(self)} with {type(other)}")


class BST:
    def __init__(self, val=None):
        self.root = BSTNode(val) if val else None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        elif val < node:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        balance = self._balance(node)

        if balance > 1:
            if self._balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
        elif balance < -1:
            if self._balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node
        elif val < node:
            node.left = self._delete(node.left, val)
        elif val > node:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                temp = node.right
                return temp

            elif node.right is None:
                temp = node.left
                return temp

            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance(node)

        if balance > 1 and self._balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self._balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self._balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node:
            return False
        elif node == val:
            return True
        elif val < node:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if not node:
            return []
        return self._inorder_traversal(node.left) + [node.value] + self._inorder_traversal(node.right)

    def height(self):
        return self._height(self.root)

    @staticmethod
    def _height(node):
        if not node:
            return 0
        return node.height

    def balance(self):
        return self._balance(self.root)

    def _balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def get_min_value_node(self):
        return self._get_min_value_node(self.root)

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def pretty_print(self):
        self._pretty_print(self.root, "", True)

    def _pretty_print(self, node, prefix, is_left):
        if not node:
            return

        self._pretty_print(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        self._pretty_print(node.left, prefix + ("    " if is_left else "│   "), True)


def generator(n, low, high):
    for _ in range(n):
        yield random.randrange(low, high)


def run_experiment(n, worst_case=False, ops=10_000):
    available_ops = ["insert", "search", "delete"]
    low = 0
    high = n

    t = BST()

    start_time = time.time_ns()

    if not worst_case:
        for _ in range(n):
            t.insert(random.randrange(low, high))

    else:
        for i in range(n):
            t.insert(i)

    preparation_time_ms = (time.time_ns() - start_time) / 1_000_000

    insert_ops_time = []
    search_ops_time = []
    delete_ops_time = []

    for _ in range(ops):
        op = random.choice(available_ops)
        val = random.randrange(low, high)

        if op == "insert":
            start_time = time.time_ns()
            t.insert(val)
            elapsed_time_ms = (time.time_ns() - start_time) / 1_000_000
            insert_ops_time.append(elapsed_time_ms)

        elif op == "search":
            start_time = time.time_ns()
            t.search(val)
            elapsed_time_ms = (time.time_ns() - start_time) / 1_000_000
            search_ops_time.append(elapsed_time_ms)

        else:
            while not t.search(val):
                val = random.randrange(low, high)
            start_time = time.time_ns()
            t.delete(val)
            elapsed_time_ms = (time.time_ns() - start_time) / 1_000_000
            delete_ops_time.append(elapsed_time_ms)

    return {
        "worst_case": worst_case, "n": n,
        "possible_lowest": low, "possible_highest": high,
        "prep_time": preparation_time_ms,
        "avg_insert": sum(insert_ops_time) / len(insert_ops_time),
        "max_insert": max(insert_ops_time),
        "min_insert": min(insert_ops_time),
        "avg_search": sum(search_ops_time) / len(search_ops_time),
        "max_search": max(search_ops_time),
        "min_search": min(search_ops_time),
        "avg_delete": sum(delete_ops_time) / len(delete_ops_time),
        "max_delete": max(delete_ops_time),
        "min_delete": min(delete_ops_time),
    }


def run_experiments(total_experiments, start_n, worst_case=False):
    avg_insert_time = []
    avg_delete_time = []
    avg_search_time = []
    prep_time = []
    total_n = []

    for i in range(total_experiments):
        print(f"\rRunning experiment {i + 1} out of {total_experiments}...", end="")
        n = start_n * (i + 1)
        result = run_experiment(n, worst_case=worst_case)

        total_n.append(n)
        avg_insert_time.append(result["avg_insert"])
        avg_delete_time.append(result["avg_delete"])
        avg_search_time.append(result["avg_search"])
        prep_time.append(result["prep_time"])

    print(f"\rFinished running all {total_experiments} experiments...")

    sns.set_theme(style="whitegrid")
    df = pd.DataFrame({
        "num": np.array(total_n),
        "avg_insert": np.array(avg_insert_time),
        "avg_delete": np.array(avg_delete_time),
        "avg_search": np.array(avg_search_time),
        # "prep_time": np.array(prep_time),
    })

    # sns.lineplot(data=df, x="num", y="prep_time")

    sns.lineplot(data=pd.melt(df, ["num"]), x="num", y="value", hue="variable", legend=False)
    plt.title(f"BST operations time comparison{' (worst case)' if worst_case else ''}")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (ms)")
    plt.legend(
        title="Operations",
        loc="upper left",
        labels=["Avg insert time (ms)", "Avg delete time (ms)", "Avg search time (ms)"]
    )
    plt.show()


if __name__ == "__main__":
    run_experiments(100, 1_000)
    # t = BST()
    #
    # for _ in range(15):
    #     val = random.randrange(100)
    #     t.insert(val)
    #     print(val, end=" ")
    #
    # print()
    # t.pretty_print()
    # print(t.balance())
    # print(t.height())
