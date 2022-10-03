Greed
http://en.wikipedia.org/wiki/Greed_%28dice_game%29

# Greed (Dice Game):

* Write a class Greed with a score() method that accepts an array of die values (up to 6).
* Scoring rules can be combined to deliver the highest total result.

### Scoring rules are as follows:
* [ ] A single one (100)
* [ ] A single five (50)
* [ ] Triple ones [1,1,1] -> (1000)
* [ ] Triple twos [2,2,2] -> (200)
* [ ] Triple threes [3,3,3] -> (300)
* [ ] Triple fours [4,4,4] -> (400)
* [ ] Triple fives [5,5,5] -> (500)
* [ ] Triple sixes [6,6,6] -> (600)


* [ ] Four-of-a-kind (Multiply Triple Score by 2)
* [ ] Five-of-a-kind (Multiply Triple Score by 4)
* [ ] Six-of-a-kind (Multiply Triple Score by 8)
* [ ] Three Pairs [2,2,3,3,4,4] -> (800)
* [ ] Straight [1,2,3,4,5,6] -> (1200)
* [ ] No scoring dice -> (0)


### Example testcases:
* [0, 0, 0, 0, 0, 0, 0] -> Exception
* [0, 0, 0, 0, 0, 0] -> 0
* [] -> Exception
* [1] -> 100
* [5] -> 50
* [1, 5] -> 150
* [1, 1] -> 200
* [5, 5] -> 100
* [1, 1, 1] -> 1000
* [2, 2, 2] -> 200
* [3, 3, 3] -> 300
* [4, 4, 4] -> 400
* [5, 5, 5] -> 500
* [6, 6, 6] -> 600
* [6, 6, 6, 1, 5, 2] -> 750
* [2, 2, 2, 3, 3, 3] -> 500
* [1, 1, 1, 1] -> 2000
* [2, 2, 2, 2] -> 400
* [3, 3, 3, 3] -> 600
* [1, 1, 1, 1, 1] -> 4000
* [4, 4, 4, 4, 4] -> 1600
* [5, 5, 5, 5, 5] -> 2000
* [1, 1, 1, 1, 1, 1] -> 8000
* [2, 2, 2, 2, 2, 2] -> 1600
* [6, 6, 6, 6, 6, 6] -> 4800
* [2, 2, 3, 3, 6, 6] -> 800
* [1, 1, 4, 4, 5, 5] -> 800
* [1, 2, 3, 4, 5, 6] -> 1200
* [2, 2, 3, 4, 4, 6] -> 0
