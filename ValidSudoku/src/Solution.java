import java.util.HashMap;

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        return isRowValid(board) && isColumnValid(board) && isSquaresValid(board);
    }

    private boolean isRowValid(char[][] board) {

        for (char[] row : board) {
            if (!checkInvalid(row)){
                return false;
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

            if (!checkInvalid(columnVals)){
                return false;
            }

        }

        return true;
    }

    private boolean isSquaresValid(char[][] board) {
        for (int squareRow = 0; squareRow < 3; squareRow++) {
            for (int squareCol = 0; squareCol < 3; squareCol++) {

                char[] squareVals = new char[9];
                int index = 0;
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        squareVals[index++] = board[squareRow * 3 + i][squareCol * 3 + j];
                    }
                }

                if (!checkInvalid(squareVals)){
                    return false;
                }

            }
        }
        return true;
    }

    private boolean checkInvalid(char[] arr){

        HashMap<Character, Integer> map = new HashMap<>();
        for (char element : arr){
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
        return true;
    }
}
