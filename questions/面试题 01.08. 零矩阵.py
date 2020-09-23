class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ks = []
        _ks = []
        for _k, _v in enumerate(matrix):
            for k,v in enumerate(_v):
                if v == 0:
                    ks.append(_k)
                    _ks.append(k)

        for _k, _v in enumerate(matrix):
            if _k in ks:
                _v[:] = [0]*len(_v)
                continue
            for _ in _ks:
                _v[_]=0