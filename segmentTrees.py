'''Author: Shivam Kumar Singh'''
'''Segment Tree Implementation using Python List'''
class buildSegmentTree:
    '''Constructor to create a segment tree with the passed array'''
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = [0]*(4*self.length+1)
        self.start = 0
        self.end = self.length-1
        self.mid = int((self.start + self.end)/2)
        self.data = arr
        def build(self, arr, tree, start, end, mid, treeNode):
            #Base Case:
            if(start==end):
                tree[treeNode] = arr[start]
                return;

            build(self, arr, tree, start, mid, int((start+mid)/2), 2*treeNode)
            build(self, arr, tree, mid+1, end, int((end + mid+1) / 2), 2*treeNode + 1)
            tree[treeNode] = tree[2*treeNode] + tree[2*treeNode + 1]
        
        #function call:
        build(self, arr, self.tree, self.start, self.end, self.mid, 1)
    
    #create a function to print the tree in array format
    def print_tree(self): 
        print(self.tree)
        
    #function to process the given query
    def query(self, start, end):
        return self._query(start, end, self.start, self.end, 1)
    
    #Recursive function to facilitate query function
    def _query(self, qs, qe, s, e, treeIndex):
        #Case 1: No overlap
        if(qe<s or e<qs):
            return 0
        #Case 2: Complete Overlap
        elif(s>=qs and e<=qe):
            return self.tree[treeIndex]
        #Case 3: Partial Overlap
        else:
            mid = int((s+e)/2)
            leftAns = self._query(qs, qe, s, mid, 2*treeIndex)
            rightAns = self._query(qs, qe, mid + 1, e, 2*treeIndex + 1)

            return leftAns + rightAns
    
    #function to modify/update the tree
    def update(self, index, element):
        val = element - self.data[index]
        return self._update(index, val, self.start, self.end, 1)
    
    #Recursive function to facilitate update function
    def _update(self, ind, val, s, e, treeIndex):
        if(ind<s or ind>e):
            return
        if(ind==s and s==e):
            self.tree[treeIndex] += val
            return
        self.tree[treeIndex] += val
        mid = int((s+e)/2)
        self._update(ind, val, s, mid, 2*treeIndex)
        self._update(ind, val, mid + 1, e, 2*treeIndex + 1)
        return


tree = buildSegmentTree([1,2,3,4,5,6])
print(tree.query(0,2)) #prints 6
tree.update(2,9)
print(tree.query(0,2)) #prints 12
