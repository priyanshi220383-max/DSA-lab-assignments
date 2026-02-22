#  Data Structures experiments – Viva Questions 

This document contains short and clear answers for viva questions based on all 6 experiment.

---

## Experiment 1: Stack & ADT

**1. What is an ADT?**  
ADT (Abstract Data Type) defines what operations are performed, not about how they are implemented.  
Example: Stack ADT defines push, pop, peek.

**2. Why push/pop can be O(1)?**  
 both push and pop can be 0(1) Because both operations work only on the top element and do not require looping.

**3. One real-world use of stack**  
Undo and Redo operation in text editors.

---

##  Experiment 2: Time Complexity

**1. Big-O vs Big-Theta difference?**  
Big-O gives upper bound (worst case), Big-Theta gives exact growth rate.

**2. What does worst-case represent?**  
 it represents maximum time taken for the most difficult input.

**3. Why complexity matters in real systems?**  
It helps choose efficient algorithms and saves time and memory.

---

##  Experiment 3: Recursion

**1. What is recursion depth?**  
Number of recursive calls present in the call stack at a time.

**2. Why recursion uses stack memory?**  
Each function call is stored in the call stack until it returns.

**3. When iteration is better than recursion?**  
When memory usage must be low and performance is critical.

---

##  Experiment 4: Fibonacci & Memoization

**1. Why naive Fibonacci is slow?**  
 Fibonacci is slow because it recalculates the same values repeatedly (exponential time).

**2. Memoization relates to DP?**  
Yes, memoization is a technique used in Dynamic Programming to store results.

**3. Space impact of memoization**  
It uses extra memory to store previously computed values.

---

##  Experiment 5: Tower of Hanoi

**1. Why moves are 2ⁿ − 1?**  
Each disk movement depends on moving smaller disks first, forming a recurrence relation.

**2. What is recursion tree idea?**  
A tree representation of recursive calls showing how problems split.

**3. Practical risk of exponential algorithms**  
They become very slow for large inputs and consume more resources.

---

## Experiment 6: Binary Search

**1. Why sorted data is required?**  
Because binary search divides data into halves based on order.

**2. Best/avg/worst case?**  
Best: O(1), Average: O(log n), Worst: O(log n)

**3. Divide & Conquer meaning**  
Break a problem into smaller parts, solve them, and combine results.

---
