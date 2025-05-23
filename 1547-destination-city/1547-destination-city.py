class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        st = set()
        for path in paths:
            st.add(path[0])
        for path in paths:
            if path[1] not in st:
                return path[1]
            else:
                st.remove(path[1])