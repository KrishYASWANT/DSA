''' Given a n*m grid of char board and a string word .return true if word exists in the grid

The word can be constructed from letters of sequential adjacent cells where adjacent cells are horizontal or vertical neighboring.
The same letter cell may not be used more than once   ''' 
from typing import List
class solution:
	def exist(self,board:List[List[str]],word:str)->bool:
		ROWS,COLS = len(board),len(board[0])
		path = set()

		def dfs(r,c,i):
			if i==len(word):
				return True
			if(r<0 or c<0 or
				r>=ROWS or c>=COLS or
				word[i]!=board[r][c] or
				(r,c) in path):
				return False
			path.add((r,c))
			#print(path)
			res=(dfs(r+1,c,i+1) or
				dfs(r-1,c,i+1) or
				dfs(r,c+1,i+1) or
				dfs(r,c-1,i+1))
			path.remove((r,c))
			return res
		for r in range(ROWS):
			for c in range(COLS):
				if dfs(r,c,0):
					return True
		return False

board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

word="ABCCED"
a=solution()
print(a.exist(board,word))