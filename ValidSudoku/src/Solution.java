import java.util.HashMap;

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        return isRowValid(board);
    }

    private boolean isRowValid(char[][] board) {
        for (char[] row : board) {
            HashMap<Character, Integer> map = new HashMap<>();
            for (char element : row){
                if (map.containsKey(element)){
                    int count = map.get(element);
                    map.put(element, count + 1);
                } else {
                    map.put(element, 1);
                }
            }
            for (Character key : map.keySet()) {
                Integer value = map.get(key);
                if (key != '.' && value > 1){
                    return false;
                }
            }
        }
        return true;
          
    }
}
