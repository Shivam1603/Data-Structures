'''
This is a template containing a general purpose segment tree. Important note - it doesn't include lazy prop implementation.

Both query and update should be treated as a 0 based indexing processes.

Update the following parts based on your use-case:
1. The operator function, it can be a simple function like sum, max, min, xor. It can also be a complicated function catering to a specific problem.
2. ans_first variable: initial value at each position within your tree array. For sum, xor, max it should be 0. However, for min() it should be +INF
3. seg_default array: Almost always this should be your initial given array

Implementation below is a range sum segment tree which supports point updates.
'''

class SegTree():
    def __init__(self, n, default_values, seg_op, ans_init):
        """
        Initialize the segment tree.
        n: Number of elements in the array managed by the tree.
        default_values: Initial values for initializing the segment tree.
        seg_op: Operation to perform on the segment tree.
        ans_init: Initial value for the answer.
        self.size: The smallest power of 2 greater than or equal to n.
        """
        self.size = 1
        self.op = seg_op
        self.ans_init = ans_init
        while self.size < n:
            self.size *= 2
        self.tree = [ans_init] * (self.size * 2)
        # Set initial values at the leaves.
        for i in range(n):
            self.tree[self.size + i] = default_values[i]
        # Build the segment tree.
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.op(self.tree[i * 2], self.tree[i * 2 + 1])
        # print(self.tree)

    def update(self, pos, x):
        """
        Replace the value at position pos in the segment tree with x.
        Then update towards the root of the segment tree.
        """
        pos += self.size
        self.tree[pos] = x
        while pos >= 2:
            pos >>= 1
            self.tree[pos] = self.op(self.tree[pos * 2], self.tree[pos * 2 + 1])

    def query(self, l, r):
        """
        Get the result for the semi-open interval [l, r).
        If a node is included in the interval [l, r) and the parent node's interval extends to the left,
        the node is on the right side (odd).
        Conversely, if the parent node extends to the right, the node is on the left side (even).
        Traverse the tree from bottom to top, performing the operation on the left if the parent's interval extends,
        and shift the index one to the right. For the right side, perform the operation on the right if the parent's interval extends,
        and shift the index one to the left.
        However, for the right side, check if it's odd because it's a semi-open interval.
        """
        l += self.size
        r += self.size

        lres, rres = self.ans_init, self.ans_init
        while l < r:
            # If l is odd, l's parent extends to the left.
            if l & 1:
                lres = self.op(lres, self.tree[l])
                l += 1
            # For the semi-open interval, if r is odd, the parent of r-1 extends to the right.
            if r & 1:
                r -= 1
                rres = self.op(rres, self.tree[r])

            l >>= 1
            r >>= 1
        res = self.op(lres, rres)
        return res

# Update this operator function as per the problem
def op(x, y):
    return x + y

# Update this initial answer variable as per the problem
ans_first = 0


# Driver code below:
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Update this default array as per the problem (often times it's your input array)
seg_default = A.copy()
segtree = SegTree(N, seg_default, op, ans_first)
for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        # It updates (b - 1)th index to value 'c'
        segtree.update(b - 1, c)
    else:
        # It queries [b-1, c) segment
        result = segtree.query(b - 1, c)
        print(result)

'''
Input:
8 4
3 2 4 5 1 1 5 3
2 1 4
2 5 6
1 3 1
2 1 4

Output:
14
2
11
'''