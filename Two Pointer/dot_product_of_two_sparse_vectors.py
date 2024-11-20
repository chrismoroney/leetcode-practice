# Dot Product of Two Sparse Vectors

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, 
# you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.non_zeros = []
        for idx, val in enumerate(nums):
            if val != 0:
                self.non_zeros.append((idx, val))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        ans = 0
        i = 0
        j = 0

        while i < len(self.non_zeros) and j < len(vec.non_zeros):
            if self.non_zeros[i][0] == vec.non_zeros[j][0]:
                ans += self.non_zeros[i][1] * vec.non_zeros[j][1]
                i += 1
                j += 1
            elif self.non_zeros[i][0] < vec.non_zeros[j][0]:
                i += 1
            else:
                j += 1

        return ans

if __name__ == "__main__":
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)