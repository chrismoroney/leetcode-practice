import java.util.HashMap;

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        return isRowValid(board) && isColumnValid(board);
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

    private boolean isColumnValid(char[][] board) {

        for (int column = 0; column < board.length; column++) {
            char[] columnVals = new char[9];
            for (int row = 0; row < board.length; row++) {
                columnVals[row] = board[row][column];
            }

            HashMap<Character, Integer> map = new HashMap<>();
            for (char element : columnVals){
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
