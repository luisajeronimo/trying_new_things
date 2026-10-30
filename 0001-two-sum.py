# LeetCode 1 - Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        numeros = {}

        for indice, valor in enumerate(nums):
            falta = target - valor

            if falta in numeros:
                return [numeros[falta], indice]

            numeros[valor] = indice