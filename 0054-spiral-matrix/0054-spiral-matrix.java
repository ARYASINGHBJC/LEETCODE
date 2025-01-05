class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int rowStart = 0;
        int rowEnd = n -1;
        int colStart = 0;
        int colEnd = m-1;
        ArrayList<Integer> res = new ArrayList<>();
        while(rowStart <= rowEnd && colStart <= colEnd){
            for(int i= colStart; i <= colEnd; i++){
                res.add(matrix[rowStart][i]);
            }
            rowStart++;
            for(int i = rowStart; i <= rowEnd; i++){
                res.add(matrix[i][colEnd]);
            }
            colEnd--;
            if(rowStart <= rowEnd){
                for(int i = colEnd; i >= colStart; i--){
                    res.add(matrix[rowEnd][i]);
                }
                rowEnd--;
            }
            if(colStart <= colEnd){
                for(int i = rowEnd; i >= rowStart; i--){
                    res.add(matrix[i][colStart]);
                }
                colStart++;
            }
        }
        return res;
    }
}