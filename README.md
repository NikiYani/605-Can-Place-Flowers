# 605-Can-Place-Flowers

You have a long flowerbed in which some of the plots are planted, </br>
and some are not. However, flowers cannot be planted in adjacent plots.</br>

Given an integer array flowerbed containing 0's and 1's, </br>
where 0 means empty and 1 means not empty, and an integer n, </br>
return true if n new flowers can be planted in the flowerbed without violating </br>
the no-adjacent-flowers rule and false otherwise. </br>

## Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1 </br>
Output: true </br> 

## Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2 </br>
Output: false </br>

## Constraints:

1 <= flowerbed.length <= 2 * 104 </br>
flowerbed[i] is 0 or 1. </br>
There are no two adjacent flowers in flowerbed. </br>
0 <= n <= flowerbed.length </br>
