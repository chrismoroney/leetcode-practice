# Problem: Flood Fill (DFS)
# You are given a 2D array (matrix) representing an image, where each value represents a color. 
# You are also given a starting pixel (row, col) and a new color. 
# Perform a "flood fill" on the image, meaning that you should change the starting pixel and all connected pixels with the same color to the new color.

# Connected pixels are those that have the same color and are directly connected either horizontally or vertically.

def flood_fill(image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    original_color = image[sr][sc]

    if original_color == new_color:
        return image
    
    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
            return
        
        image[r][c] = new_color
    
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    dfs(sr, sc)
    return image

if __name__ == "__main__":
    image = [
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0]
    ]

    sr = 2 
    sc = 2  
    new_color = 3  

    print(flood_fill(image, sr, sc, new_color))