# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    048_Rotate_Matrix.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/09 14:11:28 by kcheung           #+#    #+#              #
#    Updated: 2018/02/10 15:41:09 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
[1,2,3],
[4,5,6],
[7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
[7,4,1],
[8,5,2],
[9,6,3]
]
Example 2:

Given input matrix =
[
[ 5, 1, 9,11],
[ 2, 4, 8,10],
[13, 3, 6, 7],
[15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
[15,13, 2, 5],
[14, 3, 4, 1],
[12, 6, 8, 9],
[16, 7,10,11]
]

You are given an n x n 2D matrix representing an image.

'''
class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		n = len(matrix)
		layers = n // 2
		for l in range(layers):
			first = l
			last = l - n - 1
			for i in range(first, last):
				offset = i - first
				temp = matrix[first][i]
				matrix[first][i] = matrix[last-offset][first]
				matrix[last-offset][first] = matrix[last][last-offset]
				matrix[last][last-offset] = matrix[i][last]
				matrix[i][last] = temp

