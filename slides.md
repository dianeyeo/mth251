---
theme: seriph
title: "MTH251"
background: https://raw.githubusercontent.com/fastzhong/mth251/main/images/cover.webp
highlighter: shiki
lineNumbers: true
colorSchema: "light"
---

# MTH251

Data Structures and Algorithms I

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Zhong Lun
  </span>
</div>

---

# About Me

<br/>

<i class="fab fa-linkedin"></i> [https://www.linkedin.com/in/zhonglun/](https://www.linkedin.com/in/zhonglun/)  
<i class="far fa-envelope"></i> [zhonglun@gmail.com](zhonglun@gmail.com)  
<i class="fas fa-mobile-alt"></i> 9647 7009

<br/>

<img src="/images/linkedin.png" style="border-radius: 8px; width:50%"/>

---

# Course Structure

<br/>

<div grid="~ cols-2 gap-4">
<div>
6 weeks (Jan ~ Mar)/6 seminars/6 labs:

<p class="norm">
1. Jan 24: Python, Complexity & Big O<br/>
2. Feb 07: Array, Stack, Queue, Recursion<br/>
3. Feb 14: Linked List, Lineary Search, Binary Search<br/> 
4. Feb 21: Tree<br/> 
5. Feb 28: Algorithm Design & Pattern<br/> 
6. Mar 07: Review
</p>
<p>Mar 07: Resit Online Session</p>
</div>
<div>
3 assignments & open book exam:
<p class="norm">
<img src="/images/assessment.png" style="width:80%"/>
</p>
</div>
</div>

---

# Learning Objectives

1. python
2. algorithm time & space complexity
3. basic data structure: <span class="hl-bg">array</span>&nbsp;&nbsp;<span class="hl-bg">stacks</span>&nbsp;&nbsp;<span class="hl-bg">queues</span>&nbsp;&nbsp;<span class="hl-bg">list</span>&nbsp;&nbsp;<span class="hl-bg">tree</span>
4. recursion algorithm

---

# Slides & Notebooks

<br/>

slides online: [https://mth251.fastzhong.com/](https://mth251.fastzhong.com/)

pdf: [<logos-github-octocat /> https://github.com/fastzhong/mth251/blob/main/mth251.pdf](https://github.com/fastzhong/mth251/blob/main/mth251.pdf)

labs: [<logos-github-octocat /> https://github.com/fastzhong/mth251/tree/main/notebooks](https://github.com/fastzhong/mth251/tree/main/notebooks)

---

# Learning Resource

[📚 books](https://github.com/fastzhong/mth251/tree/main/resources)

<div grid="~ cols-4 gap-4">
  <div><img src="/images/study_guide.png" style="width: 140px; height: 180px"/></div>
  <div><img src="/images/study_book.png" style="width: 140px; height: 180px"/></div>
  <div><img src="/images/common-sense.jpg" style="width: 140px; height: 180px"/></div>
  <div><img src="/images/grokking.jpg" style="width: 140px; height: 180px"/></div>
  <div><img src="/images/algorithms.png" style="width: 140px; height: 180px"/></div>
  <div><img src="/images/intro_algorithms.png" style="width: 140px; height: 180px"/></div>
</div>

---

# Learning Resource

[<mdi-file-code /> Leetcode](https://leetcode.com/)

<img src="/images/leetcode.png" style="border-radius: 8px; width: 70%"/>

---

# Why Python

> _The TIOBE Programming Community index is an indicator of the popularity of programming languages._

<br/>

<img src="/images/tiobe.png" style="border-radius: 8px; width: 70%"/>

---

# Why Python

<br/>

<p class="norm">
✔ Easy To Learn<br/> 
✔ Human Readable<br/>
✔ Productivity<br/>
✔ Cross Platform
</p>

<br/>

> **The Zen of Python, by Tim Peters**  
> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> There should be one-- and preferably only one --obvious way to do it.  
> If the implementation is hard to explain, it's a bad idea.

---

# Python Jobs

<br/>

<p class="norm">
✔ backend: <strong>Python</strong> vs. Java, C++, Go, Php<br/> 
✔ devops: <strong>Python</strong> vs. Go, Ruby, Shell<br/>
✔ test automation: <strong>Python</strong> vs. Groovy, shell<br/>
✔ data engineering: <strong>Python</strong> vs. Java, C++<br/>  
✔ data analytics & visualization: <strong>Python</strong> vs. R, Java, C++<br/>  
✔ data science & machine learning: <strong>Python</strong> vs. R, Julia, C++<br/>
</p>

---

# Python 101

<br/>

<div grid="~ cols-3 gap-8">
  <div>
    <uo><li>Compiled vs. Interpreted</li></uo><br/>
    <img src="/images/compiled_interpreted.png" style="width: 250px;"/>
  </div>
  <div>
    <uo><li>CPython bytecode</li></uo><br/>
    <img src="/images/cpython.png" style="width: 250px;"/>
  </div>
  <div>
    <uo><li>Python implementations</li></uo><br/>
    <img src="/images/python-implementations.png" style="width: 250px;"/>
  </div>
</div>

---

# Python Data Type & Operators

<logos-jupyter />

-   numbers: <kbd>int</kbd> <kbd>float</kbd> <kbd>complex</kbd>

    -   arithmetic operator: <kbd>+</kbd> <kbd>-</kbd> <kbd>\*</kbd> <kbd>/</kbd> <kbd>//</kbd> <kbd>%</kbd> <kbd>\*\*</kbd>
    -   bitwise operator: <kbd>&</kbd> <kbd>|</kbd> <kbd>^</kbd> <kbd>>></kbd> <kbd><<</kbd> <kbd>~</kbd>
    -   <kbd>range()</kbd>: a list of integers

-   strings: <kbd>''</kbd> <kbd>""</kbd> <kbd>\'</kbd> <kbd>\"</kbd> <kbd>\t</kbd> <kbd>\n</kbd> <kbd>\r</kbd> <kbd>\\\\</kbd> <span class="norm">etc.</span>

    -   <kbd>join()</kbd> <kbd>split()</kbd> <kbd>ljust()</kbd> <kbd>rjust()</kbd> <kbd>lower()</kbd> <kbd>upper()</kbd> <kbd>lstrip()</kbd> <kbd>rstrip()</kbd> <kbd>strip()</kbd> <span class="norm">etc.</span>

-   boolean: <kbd>True</kbd> <kbd>False</kbd>

    -   True: <span class="norm">non-zero number, non-empty string, non-empty list </span>
    -   False: <span class="norm">0, 0.0, "", [], None</span>

---

# Python Data Type & Operators

<logos-jupyter />

-   boolean: <kbd>True</kbd> <kbd>False</kbd>

    -   logic operator: <kbd>and</kbd> <kbd>or</kbd> <kbd>not</kbd>
    -   comparison operator: <kbd>></kbd> <kbd><</kbd> <kbd>>=</kbd> <kbd><=</kbd> <kbd>==</kbd> <kbd>！=</kbd>
    -   identity operator: <kbd>is</kbd> <kbd>is not</kbd>

-   None

-   type conversion/casting: <kbd>int()</kbd> <kbd>float()</kbd> <kbd>str()</kbd> <kbd>bool()</kbd> <kbd>hex()</kbd> <kbd>ord()</kbd>

---

# Python Collections

<logos-jupyter />

-   collections: <kbd>list</kbd> <kbd>tuple</kbd> <kbd>set</kbd> <kbd>dictionary</kbd>

    -   membership operator: <kbd>in</kbd> <kbd>not in</kbd>

-   list []: a collection of items, usually the items all have the same type

    -   sequence type, sortable, grow and shrink as needed, most widely used

-   tuple (): a collection which is ordered and unchangeable

-   set {}: a collection which is unordered and unindexed

-   dictionary: a set of <kbd>key: value</kbd> pairs, unordered, changeable and indexed

---

# Python Program Structure

<logos-jupyter />

-   variable

-   statement & comments

    -   Python uses new lines to complete a command, as opposed to other programming languages often use <kbd>;</kbd> or <kbd>()</kbd>；relies on indentation (<span class="uline">whitespace sensitive</span>), to define scope, such as the scope of loops, functions and classes, as opossed to other programming languages often use <kbd>{}</kbd>

-   control flow

    -   <kbd>if ... elif ... else</kbd>
    -   <kbd>while</kbd> <kbd>for</kbd> <kbd>break</kbd> <kbd>continue</kbd>

---

# Python Program Structure

<logos-jupyter />

-   function

    -   <kbd>def</kbd> <kbd>return</kbd>
    -   <kbd>_main_</kbd>
    -   advanced:
        -   lambda
        -   decorator
        -   closure

-   error/exception

    -   handling exception: <kbd>try ... except ... else ... finally</kbd>
    -   raise execption: <kbd>raise</kbd>

---

# Python OO & Class

<logos-jupyter />

-   <kbd>Procedural</kbd> <span class="norm">vs.</span> <kbd>OOP</kbd> <span class="norm">vs.</span> <kbd>FP</kbd>

-   OO Principal

    -   <kbd>Inherience</kbd>
    -   <kbd>Encapsulation</kbd>
    -   <kbd>Polymorphism</kbd>

-   class, instance, attributes, properties, method

-   <kbd>override</kbd> <span class="norm">vs.</span> <kbd>overload</kbd> <span class="norm">vs.</span> <kbd>overwrite</kbd>

<!--
There are 3 programming paradigms. In early days, there was only procedural programming - program is written in a step by step manner, no magic, no fancy stuff. While it is very naive approach ans still used nowadays, it has some shotcomings: hard to read, hard to reuse (copy and paste).

OO is invented to simulate how the real world works. We put logic and data together inside the object.

FP as the name suggested, we describe the logic using function and attach function to the data, data-driven instead of process-driven. Function has no state, just logic, consistent input and output. Unlike OO, when putting different objects together, deveopers have to take the responsible to debug, reuse, and maintain the whole software. Software built with FP is relatively testable and reliable.
-->

---

# Misc.

<logos-jupyter />

-   modular programming: <kbd>function</kbd> → <kbd>class</kbd> → <kbd>module</kbd> → <kbd>package</kbd>

-   Modules: Python module (default main module), C module, Build-in module

-   Packages:

![pkg](/images/pkg.png)

-   Standard Lib: <kbd>math</kbd> <kbd>random</kbd> <kbd>re</kbd> <kbd>os</kbd> <kbd>itertools</kbd> <kbd>collections</kbd>

---

# Misc.

<logos-jupyter />

-   Namespaces & Scopes: <kbd>LEGB</kbd> rule

<img src="/images/LEGB.png" style="height:25%"/>

-   memory, copy vs. deepcopy

-   help

Cheatsheet:  
 🧾&nbsp;&nbsp;[Python Crash Course - Cheat Sheets](https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf)  
 🧾&nbsp;&nbsp;[Comprehensive Python Cheatsheet](https://github.com/gto76/python-cheatsheet)

<!--

Names are identifiers, we use names to track objects - everything in Python is object, class, methods/functions, modules, and so on. Namespace is the naming hierarchy to name things in a way without any ambiguity. Namespaces are implemented as dictionaries in Python.

Scope is the boundary of the namespace which the particular objects are accessible by others.

Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by Python when you run a program or script.

Global (or module) scope is the top-most scope in a Python program, script, or module. This Python scope contains all of the names that you define at the top level of a program or a module. Names in this Python scope are visible from everywhere in your code.

Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope contains the names that you define in the enclosing function. The names in the enclosing scope are visible from the code of the inner and enclosing functions.

Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function. It’s created at function call, not at function definition, so you’ll have as many different local scopes as function calls. This is true even if you call the same function multiple times, or recursively. Each call will result in a new local scope being created.

LEGB rule — a rule that defines the order of scopes following which a Python interpreter resolves the names (e.g., variables, functions) for any given operations (e.g., accessing attributes, calling functions).

-->

---

# Python Tutorials

<br/>

<span class="hl-color">Programming with Mosh</span>

<logos-youtube-icon />&nbsp;&nbsp;[Python Tutorial - Python for Beginners 2020](https://www.youtube.com/watch?v=kqtD5dpn9C8)

<span class="hl-color">freeCodeCamp</span>

<logos-youtube-icon />&nbsp;&nbsp;[Learn Python - Full Course for Beginners Tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw)  
<logos-youtube-icon />&nbsp;&nbsp;[Python for Everybody - Full University Python Course](https://www.youtube.com/watch?v=8DvywoWv6fI)  
<logos-youtube-icon />&nbsp;&nbsp;[Intermediate Python Programming Course](https://www.youtube.com/watch?v=HGOBQPFzWKo)

<span class="hl-color">Tech With Tim</span>

<logos-youtube-icon />&nbsp;&nbsp;[Learn Python - Full Course for Beginners Tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw)

<span class="hl-color">[The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)</span>

<style>
p {
  font-size: 0.9rem;
}
</style>

---

# Data Structure & Algorithms (DSA)

<br/>

A data structure is a way of organizing information so that it can be used effectively <span class="uline">by computer</span>

Algorithms provides computer step by step instructions to process the information and solve a problem

<p class="hl-strong">Program = Data Structure + Algorithm </p>

<br/>

<pre class="norm">
    -   Input
    -   Output
    -   Definiteness
    -   Effectiveness
    -   Finiteness

</pre>

<!--
A data structure is a data organization, managment, and storage format that enables efficient access and modification. More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.

An algorithm is a sequence of instructions, typically to solve a class of problems or perform a computation. Algorithms are unambiguous specifications for performing calculation, data processing, automated reasoing and other tasks.

algorithm:
  - precise input & output
  - clear and unambigurous steps
  - no unnecessary and redundant steps
  - must stop eventually and give expected output
DSA is by computer, for computer
-->

---

# Data Structure & Algorithms

Example: keyword searching

<div grid="~ cols-2 gap-8">
  <div>
    <p><span class="hl-strong">Data Structure</span>: index</p>
    <p><span class="hl-strong">Algorithm</span>: looking up the page no.</p>
  </div>
  <div>
    <img src="/images/book_index.png" style="width: 70%;"/>
  </div> 
</div>

---

# Data Structure & Algorithms

Example: adding two vectors

<div grid="~ cols-2 gap-8">
  <div>
    <p><span class="hl-strong">Data Structure</span>: complex number</p>
    <p><span class="hl-strong">Algorithm</span>: adding two complex numbers</p>
    <pre class="norm">
      a + b = (x + yi) + (u + vi) = (x + u) + (y + v)i
    </pre>
  </div>
  <div>
    <img src="/images/vector_add.png" style="width: 70%;"/>
  </div> 
</div>

---

# Data Structure & Algorithms

Data Structure

-   Linear
    -   Array, String, Linked List
    -   Stack, Queue, Deque, Set, Map/Hash, etc.
-   Non-Linear
    -   Tree, Graph
    -   Binary Search Tree, Red-Black Tree, AVL, Heap, Disjoin Set, Trie, etc.
-   Others
    -   Bitwise, BloomFilter, LRU Cache

---

# Algorithms & Data Structure

Algorithms

-   branching: if-else, switch
-   iteration: for, while loop
-   recursion: divide & conquer, backtrace
    <br/>
-   searching: binary search, depth first, breath first, A\*, etc.
-   sorting: quick sort, bubble sort, merge sort, etc.
-   dynamic programming
-   greedy
-   ...

---

# Algorithms & Data Structure

<br/>

<span class="hl-color">Why</span>

<p class="norm">
✓ deeper understanding of computer system  <br/>
✓ improve coding skill  <br/>
✓ coding interview  <br/>
✓ building powerful framework and library  
</p>

<span class="hl-color">How</span>

<p class="norm">
🏃‍♂️ learning by doing, implementing from scratch  <br/>
🙇🏻‍♂️ problem solving 
</p>
---

# Algorithm Complexity Analysis

<logos-jupyter />

How to measure Performance/Efficiency ?

-   cpu, memory, io, networking, etc.
-   no. of lines
-   worst case vs. best case
-   code slows as data grows
-   ...

---

# Algorithm Complexity Analysis

<br/>

<span class="hl-strong">Time Complexity</span> : by giving the size of the data set as integer N, consider the number of operations that need to be conducted by computer before the algorithm can finish

<span class="hl-strong">Space Complexity</span> : by giving the size of the data set as integer N, consider the size of extra space that need to be allocated by computer before the algorithm can finish

Good code:

✔ readability  
✔ speed  
✔ memory

👉 When: Accessing, Searching, Inserting, Deleting, .....

<!--
Algorithm is a step by step pragmatic instruction to computer to solve problem

To design and implement a algorithm usually we sacrifice space to achieve fast performance, in another word time is more important than space. But in reality we still need to take care of memory usage or storage otherwise computer may hang or hitting out of memory error.

Data structure is our building blocks for algorithm, so when using these data structure we need to consider the performance of those most common operations, namely Accessing, Searching, Inserting, Deleting of data
-->

---

# Big-O

<logos-jupyter />

<p class="hl">
Lef f(n) and g(n) be functions from positive integers to positive integers to positive  
reals <br/>
f = O(g) if there is a constant c > 0 such that f(n) ≦ c·g(n) for large n
</p>

<p class="norm"><i class="far fa-comment-dots"></i> f(n) <span class="uline">grows no faster</span> than g(n) </p>

<span class="norm">e.g.</span>  
$f(n) = O(4n^2 + 8n + 16) → O(n^2) → g(n) = n^2$  
$O(4n^2 + 8n + 16) = O(n^2)$

> _Big-O describes the trend of algorithm performance when the data size increases_

---

# Big-O

|                |              |
| -------------: | :----------- |
|        $O(1)$: | constant     |
| $O(\log_* n)$: | logarithmic  |
|        $O(n)$: | linear       |
|  $O(nlog_*n)$: | linearithmic |
|      $O(n^2)$: | polynomial   |
|      $O(2^n)$: | exponential  |
|       $O(n!)$: | factorial    |

<!--
Big-O indicating the complexity level not the exact number of operations or the exact size of space

How to Determine Complexities

-->

---

# Big-O

<br/>

👉 [Master theorem (analysis of algorithms)](<https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)>)

$O(f) = f$  
$O(c·f) = O(f)$  
$O(f+g) = O(max(f, g))$  
$O(f)·O(g) = O(f·g)$  
$O(f·g) \leq O(f·h)$ <span class="norm">if & only if</span> $O(g) \leq O(h)$  
$O(x^a) \leq O(x^b)$ <span class="norm">if & only if</span> $a \leq b$  
$O(a^x) \lt O(b^x)$ <span class="norm">if & only if </span> $a \lt b$  
$O(x^c) \lt O(d^x)$ <span class="norm">if & only if </span> $d \gt 1$ (assuming $c \geq 1$ and $d \geq 1$)  
$O(log_* x) \lt O(x^c)$ <span class="norm">if & only if</span> $c \gt 0$

<!--
O(logN) = O(log2N)
-->

---

# Big-O

<br/>

😊 $O(1) < O(\log_* n) < O(n) < O(n\log_* n) < O(n^2) < O(2^n) < O(n!)$ 🥵

<img src="/images/bigo-chart.jpeg" style="width:50%"/>

<span class="norm"><mdi-file-code /> [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)</span>

---

# Array

<br/>

To store a list of similar things, example:

<pre class="norm">
    A list of names: [“Alex”, “Bob”, “Charles”, “David”]
    A list of numbers: [1, 2, 3, 4]
</pre>

Each item in the array referred as “<span class="hl">element</span>”

---

# Array

<br/>

-   Element Type: same type (array is structured data)

-   Element Size: fixed

```java
# java
String[] cars = {“BMW”, “Toyota”, “Tesla”} // declare & init

Integer[] scores = new Integer[10] // declare
// init
scores[0] = 90
scores[1] = 80
```

-   Element Index: 0, 1, ..., length - 1

---

# Array 2-D

<br/>

<pre class="norm">
students = [  
    [“Alex”,  “M”, “S1111111A”],  
    [“Bob”,   “M”, “S2222222B”],  
    [“James”, “M”, “S3333333C”],  
]  

students[2]      → [“James”, “M”, “S3333333C”]  
Students[1][2] → “S2222222B”
</pre>

<br/>

| **Index** | **0** | **1** | **2**     |
| :-------: | :---- | :---: | :-------- |
|   **0**   | Alex  |   M   | S1111111A |
|   **1**   | Bob   |   M   | S2222222B |
|   **2**   | James |   M   | S3333333C |

---

# Array Address

<pre class="norm">
str = "HELLO" = ['H', 'E', 'L', 'L', 'O']
</pre>

<img src="/images/array_address.png" style="width: 60%" />

<pre class="norm">
data type: char  
data type size: 2 byte (1 byte = 8 bits, 0000 0000 ~ 1111 1111)  
</pre>

<br/>

<span class="hl-strong">total_size = array_size \* data_type_size</span>

<span class="hl-strong">array[i].address = base_address + i \* data_type_size</span>

👉 **O(1)**

<!--
Array is very simple but fundamental data structure because it represents the basic structure how we allocate and use memory.

Memory is like a big building and it contains many rooms, the room can store data, each room has a unique room number which is the address, the room size is same and in computer the size unit is byte and one byte equals to 8 bit, 0~255. one byte can store 8 0s to 8 1s, for unsigned integer, it means from 0 to 255.

By definition array should contain a numbers of element with same data type. String can be considered as an array of chars. We can use the index to identify the element.

Why the starting index is 0?

Memory is a limited resource in programing and memory allocation is quite complicated because we dont do memory allocation randomly and manually. A background process - Garbage collector (GC) will reclaim memory from programs smartly without our intervention.

-->

---

# Dynamic Array

<logos-jupyter />

<!--
-->

<div grid="~ cols-2 gap-4">
  <div>
    <p class="norm">- what is the good space size for an array?</p>
    <p class="norm">- when is the good time to expand/shrink the array? </p>
    
  </div>  
  <div align="center">
    <img src="/images/dynamic_array.png" style="width: 90%"/>
  </div> 
</div>

<br/>

Growth Pattern:

-   Python $0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...$
-   Java $((size * 3) / 2) + 1$
-   C# $size * 2$

<br/>

<p class="norm">
👉 memory management is one of the biggest programming challenges. 
</p>

<!--
You may wonder how to implement a dynamic array, in fact it can be implemented by a normal array.

When we append, insert & delete, we touch not just a single element.

Memory is still a limited resource, the actual implementation of dynamic array has to take it into consideration. And memory management is a very complicated problem.

This over-allocates proportional to the list size, making room for additional growth. The over-allocation is mild but is enough to give linear-time amortized behavior over a long sequence of appends() in the presence of a poorly-performing system realloc().

Note: new_allocated won't overflow because the largest possible value is PY_SSIZE_T_MAX * (9 / 8) + 6 which always fits in a size_t.

Objects/listobject.c:
new_allocated = (size_t)newsize + (newsize >> 3) + (newsize < 9 ? 3 : 6);


-->

---

# Array Complexity

<div style="width: 70%">
  <table class="ops">
    <thead>
      <tr>
        <th id="">Operation</th>
        <th id="">Array</th>
        <th id="">Dynamic Array</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Accessing</th>
        <td>O(1)</td>
        <td>O(1)</td>
      </tr>
      <tr class="even">
        <th>Searching</th>
        <td>O(n)</td>
        <td>O(n)</td>
      </tr>
      <tr class="odd">
        <th>Inserting</th>
        <td>-</td>
        <td>O(n)</td>
      </tr>
      <tr class="even">
        <th>Deleting</th>
        <td>-</td>
        <td>O(n)</td>
      </tr>
    </tbody>
  </table>
</div>

---

# Python Collection Complexity

<div style="width: 100%">
  <table class="ops">
    <thead>
      <tr>
        <th id="" colspan="2">List [a, b, c, ...]</th>
        <th id="" colspan="2">Dicts {k:v, ...}</th>
        <th id="" colspan="2">Set {a, b, c,}</th>
      </tr>
    </thead>
    <tbody>
      <tr class="even">
        <th>mylist.append(val)</th>
        <td>O(1)</td>
        <th>mydict[key] = val</th>
        <td>O(1)</td>
        <th>myset.add(val)</th>
        <td>O(1)</td>
      </tr>
      <tr class="even">
        <th>mylist[i]</th>
        <td>O(1)</td>
        <th>mydict[key]</th>
        <td>O(1)</td>
        <th></th>
        <td></td>
      </tr>
      <tr class="odd">
        <th>val in mylist</th>
        <td>O(N)</td>
        <th>key in mydict</th>
        <td>O(1)</td>
        <th>val in myset</th>
        <td>O(1)</td>
      </tr>
      <tr class="even">
        <th>for val in mylist:</th>
        <td>O(N)</td>
        <th>for key in mydict:</th>
        <td>O(N)</td>
        <th>for val in myset:</th>
        <td>O(N)</td>
      </tr>
      <tr class="even">
        <th>mylist.sort()</th>
        <td>O(NlogN)</td>
        <th></th>
        <td></td>
        <th></th>
        <td></td>
      </tr>
    </tbody>
  </table>
</div>

<style>
    td:nth-child(1) {
        width: 25%;
    }
    td:nth-child(2) {
        width: 6%;
    }
    td:nth-child(3) {
        width: 25%;
    }
    td:nth-child(4) {
        width: 6%;
    }
    td:nth-child(5) {
        width: 25%;
    }
    td:nth-child(6) {
        width: 6%;
    }
</style>

---

# Trade-offs

<br/>

```python
# .. make a list ..
if thing in my_list: # O(N)

# ✅ Good
# .. make a set ..
if thing in my_set:  # O(1)

# ❌ Bad
# .. make a list ..
my_set = set(my_list) # O(N)
if thing in my_set:   # O(1)

# ✅ Good
# .. make a list ..
my_set = set(my_list) # O(N)
for many_times: 
  if thing in my_set:   # O(1)

```

---


# ADT vs. Data Structure

<br/>

An <span class="hl-bg">abstract data type</span> (ADT) is an abstraction of a <span class="hl-bg">data structure</span> which provides only the interface to which a data structure must adhere to. The interface does not give any specific details about how something should be implemented.

Programming language provides different <span class="hl-bg">data types</span> to implement/represent different data structure.

i.e. Array

-   a linear abstract data type
-   a java data type

<!--
When studying algorithm, we use data structure such as Array, Dynamic Array, Linked List, as the solution or algorithm is programming language independent.

When coding or implementing the algorithm in a specific programming language like Python, we use data type like int, string, list which are supported by the language. Different programming language provides different builtin data types. Java has a few of linear data type: Array, ArrayList, AttributeList, LinkedList, Stack, and so on. We can implement more advanced data structure by using the builtin date types.

List could mean a dynamic array as a data structure but it is one Python collection data type. The name is same but it is used in different context and has different meaning.
-->

---

# Stack

<br/>

-   Sequential Access vs Random Access (such as Array)

-   <span class="hl-strong">LIFO</span> (Last In First Out) sequential collection

<br/>

<img src="/images/stack.jpg" style="width: 30%"/>

<!--
As we have known, any element in Array we can access directly by calling upon the index location, but unlike Array, for some linear data structure, the element can be accessed only in a particular order, Stack is one of them.

By definition, stack is a linear data structure that stores data in such a way that the last piece of data stored, is the first one retrieved also called last-in, first-out or first-in, last-out.
-->

---

# Stack: Operations

<br/>

-   <span class="hl-strong">push</span>() − pushing (storing) an element on the stack
-   <span class="hl-strong">pop</span>() − removing (accessing) an element from the stack
-   top()/peek() − get the top data element of the stack, without removing it
-   size(), isEmpty(), isFull()

<br/>

<div grid="~ cols-2 gap-10">
  <div><img src="/images/stack_push.png" style="width: 70%"/></div>
  <div><img src="/images/stack_pop.png"  style="width: 70%"/></div>
</div>

<!--
Push & Pop are the 2 most important operations for stack. Push is to store an element to the top and stack size will increase 1. Be careful if the stack is full, pop will throw overflown exception. The opposite is Pop, pop is to remove the top element and the size will decrease 1. And if stack is empty, it will throw underflow exception.
-->

---

# Stack Complexity

<div style="width: 50%">
  <table class="ops">
      <thead>
        <tr>
          <th id="">Operation</th>
          <th id="">Stack</th>
        </tr>
      </thead>
      <tbody>
        <tr class="odd">
          <td>Accessing</td>
          <td>O(n)</td>
        </tr>
        <tr class="even">
          <td>Searching</td>
          <td>O(n)</td>
        </tr>
        <tr class="odd">
          <td>Inserting</td>
          <td>O(1)(push)</td>
        </tr>
        <tr class="even">
          <td>Deleting</td>
          <td>O(1)(pop)</td>
        </tr>
      </tbody>
  </table>
</div>

<!--
To access the bottom element of the stack, we have to remove all the elements above it, so the time complexity is O(n). This is the weakness when we apply stack to solve problem.

Search is similar to accessing.

As stack is LIFO we cannot insert and delete random element.

-->

---

# Queue

<br/>

-   <span class="hl-strong">FIFO</span> (First In First Out) sequential collection

<br/>

<img src="/images/queue.png" style="width: 30%"/>

---

# Queue: Operations

<br/>

-   <span class="hl-strong">enqueue</span>() − adding (storing) an element to the queue
-   <span class="hl-strong">dequeue</span>() − removing (accessing) an element from the queue
-   fist()/peek() − get the first element of the queue, without removing it
-   size(), isEmpty(), isFull()

<br/>

<div grid="~ cols-2 gap-10">
  <div><img src="/images/queue_enqueue.png" style="width: 70%"/></div>
  <div><img src="/images/queue_dequeue.png" style="width: 70%"/></div>
</div>

<!--
-->

---

# Queue Complexity

<div style="width: 50%">
  <table class="ops">
    <thead>
      <tr>
        <th id="">Operation</th>
        <th id="">Queue</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Accessing</th>
        <td>O(n)</td>
      </tr>
      <tr class="even">
        <th>Searching</th>
        <td>O(n)</td>
      </tr>
      <tr class="odd">
        <th>Inserting</th>
        <td>O(1)(enqueue)</td>
      </tr>
      <tr class="even">
        <th>Deleting</th>
        <td>O(1)(dequeue)</td>
      </tr>
    </tbody>
  </table>
</div>

<!--
-->

---

# Linked List

<br/>

-   dynamic linear data structure

-   data stored in a “Node” class

-   data & pointer

<div grid="~ cols-2 gap-10">
  <div><img src="/images/ll_singly.png" style="width: 60%"/></div>
  <div>code here</div>
</div>

<!--
In previous class, we introduce 4 linear data structure and 3 of them are dynamic – dynamic array, stack and queue. As we know, they can be actually implemented by array and rely on resize() function to increase or decrease the memory size when we add/remove element.

Today we will introduce a new data structure - Linked List, which is truly dynamic data structure. Similar to Array, it is basic but very important data structure and it is widely used.

In Linked List, each a single node in the linked list has two parts, one is to store the actual data and  the other is a pointer or ref which points to the next node.
-->

---

# Linked List Operations

<div style="width: 70%">
  <table class="ops">
    <thead>
      <tr>
        <th id="">Operation</th>
        <th id="">Linked List</th>
        <th id="">Dynamic Array</th>
        </tr>
      </thead>
      <tbody>
        <tr class="odd">
          <th>Accessing</th>
          <td>O(n)</td>
          <td>O(1)</td>
        </tr>
        <tr class="even">
          <th>Searching</th>
          <td>O(n)</td>
          <td>O(n)</td>
        </tr>
        <tr class="odd">
          <th>Inserting</th>
          <td>O(1)</td>
          <td>O(n)</td>
        </tr>
        <tr class="even">
          <th>Deleting</th>
          <td>O(1)</td>
          <td>O(n)</td>
        </tr>
      </tbody>
  </table>
</div>

<!--
For inserting, just need to create the new node and update the pre node

For deleting, just need to update the pre node and next node

Comparing Array, the accessing is slower but the update is much faster.
-->

---

# Linked List

<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div align="right">Singly Linked List</div>
  <div><img src="/images/ll_singly.png" style="width: 50%"/></div>
  <div align="right">Doubly Linked List</div>
  <div><img src="/images/ll_doubly.png" style="width: 50%"/></div>
  <div align="right">Circular Linked List</div>
  <div><img src="/images/ll_circular.png" style="width: 50%"/></div>
  <div align="right">Positional Linked List</div>
  <div><img src="/images/ll_positional.png" style="width: 50%"/></div>
</div>

<!--
Besides Single Linked List, we have some other forms of linked list.

For Circular Linked List, the last element points back to the first element, instead of null

For Double Linked List, we have two pointers, one points to the previous node, the other points to the next.

To speed up the accessing, we can create the position class, each node is associated with a position object. We don’t use indexing as position as indexing can be changed as we remove/add the nodes. The actual position logic is up to the implementation.
-->

---

# Linked List vs. Array

<br/>

<pre class="norm">
✔ dynamic, no need to deal with fixed memory size 
✖ accessing speed    
</pre>

<br/>
<br/>

<div class="inline-grid grid-cols-[1fr,3fr] gap-8">
  <div align="right">Array:</div>
  <div><img src="/images/array_address.png" style="width: 70%"/></div>
  <div align="right">Linked List:</div>
  <div><img src="/images/ll_address.png" style="width: 70%"/></div>
</div>

<!--
Both array and linked list are very foundation data structure, because they represent how we store data into memory.  For array we require consecutive memory units, imaging after certain time, the memory becomes fragment. If we want to store a big chunk of data, for example the data needs 100 memory units, we may not able to find 100 unites together, but linked list can solve that problem as the node is stored randomly in the memory.

Linked list is more flexible than Array but why Array is still important and useful.
-->

---

# Linked List vs. Array

<br/>

<div align="center">
  <img src="/images/storage_speed.png" style="width:70%"/>
</div>

<!--
Let us look at this picture, data in our computer can be stored in different place, especially on runtime, data is accessible not just in memory but also in cpu cache. Giving one example, if we have one integer array which contains 4 integer 1,2,3,4, if 1 is being processed by cpu, it will be loaded into cpu cache. As 2, 3, 4 are close to 1, and very likely to be processed next, So modern cpu is so smart that it will preload 2,3,4 into cpu cache together with 1. This optimization operation is available for array data structure but not linked list.
-->

---

# Recursion

Recursion by definition is a function that calls itself.

-   base case
-   recursive case

<br/>
<br/>

<div grid="~ cols-2 gap-8">
  <div class="norm">
    <p>Example: </p>
    <p>Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, …  </p>
    <ul>
      <li>when n = 1, fib(1) = 0</li>
      <li>when n = 2, fib(2) = 1</li>
      <li>when n > 2, fib(n) = fib(n-1) + fib(n-2)</li>
    </ul>
  </div>
  <div>
    <p> </p>
    <img src="/images/fib_recursive.png" style="width: 400px;"/>
  </div>
</div>

<!--
Recursion pattern: recursion includes 2 cases the base and the recursive case

Base case: the exist condition
Recursive case: reduce the original problem to a smaller version

Every single recursion function must have at least 1 base case and 1 recursive case.

To understand complicated concept like Recursion, its always good to start with example.

Big(O) of Fibonacci - iterative vs. recursive

-->

---

# Recursion vs. Iterative

<br/>

> _Anything with a recursion can be done iteratively (loop)_

<br/>
<br/>

<div grid="~ cols-2 gap-8">
  <div>
    <h4>🤗 Intuitive/DRY, code readability</h4>
  </div>
  <div>
    <img src="/images/fib_recursive.png" style="width: 350px;"/>
  </div>
  <div>
    <h4>🤔 Optimization, call stack </h4>
  </div>
  <div>
    <img src="/images/fib_iterative.png" style="width: 350px;"/>
  </div>  
</div>

<!--
It is ALWAYS possible to convert a recursion implementation into iterative/loop implementation.
-->

---

# Recursive Call

<br/>
<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-12">
  <div align="right">
    <h4>Call Stack: </h4>
  </div>
  <div>
    <img src="/images/recursive_callstack.png" style="width: 350px;"/>
  </div>
  <div align="right">
    <h4>fib_recursive(5): </h4>
  </div>
  <div>
    <img src="/images/fib_callstack.png" style="width: 350px;"/>
  </div>  
</div>

<!--
It is ALWAYS possible to convert a recursion implementation into iterative/loop implementation.
-->

---

# Recursive Call

<br/>
<br/>

-   Max call stack size (stack overflow error)

-   Tail Call Optimization

-   Memorization

---

# Recursive Call

<br/>
<br/>

Fundamental technique to solve problem:

-   Identifying the base case

-   Identifying the recursion formula/equation to transform the problem to smaller version

    -   Problem requires back-tracking
    -   Problem has tree structure

<!--
Recursion is applied widely in many algorithms, so it is very important to master this technique.

Hopefully after the class, recursion is no more magic to you and you can understand how to resolve problem with recursion.
-->

---

# Linear Search

<br/>

-   Input: array, target element
-   Output: position (-1 if not existing)

---

# Binary Search

<br/>

-   Input: array, target element
-   Output: position (-1 if not existing)

---

# Tree

<br/>

<div grid="~ cols-2 gap-8">
  <div align="center">
    <img src="/images/tree_example1.png" style="width: 80%"/>
  </div>  
  <div align="center">
    <img src="/images/tree_example2.png" style="width: 80%"/>
  </div> 
</div>

---

# Tree Terminology

<br/>

<div class="inline-grid grid-cols-[1fr,3fr] gap-8">
  <div align="left" class="norm">
    <ul>
      <li>Node: Root, leaf, Internal Node</li>
      <li>Paren, Children, Sibling</li> 
      <li>Edge, Degree</li>
      <li>SubTree</li>
      <li>Path </li>
      <li>Level</li>     
    </ul>
  </div>  
  <div align="left">
    <img src="/images/tree_terminology1.png" style="width: 80%"/>
  </div> 
</div>

<!--
Tree is collection of data in hierarchical structure. Each element in the tree is called node but unlike Linked list, tree node can have multiple links to the others, the link is called edge.

We have different nodes in a tree, first node is root, no parent, only one root in a tree.

The degree of a node is the total numbers of links or total numbers of child nodes.

SubTree: child node forms a tree recursively.

Path: sequence of nodes and edges from one node to the other, A -> B -> D -> E
-->

---

# Tree Terminology

<br/>

<div class="inline-grid grid-cols-[1fr,3fr] gap-8">
  <div align="left" class="norm">
    <ul>
      <li>Level vs. Depth vs. Height</li>   
    </ul>
  </div>  
  <div align="left">
    <img src="/images/tree_terminology2.png" style="width: 80%"/>
  </div> 
</div>

<!--
Level: edges in path from root to the node
Depth: edges in path from the node to the root
Height: edges in longest path from the node to the leaf
-->

---

# Binary Tree

<br/>

-   One root

-   Max 2 child nodes

-   One and only one path from root to each node

-   Max nodes on level: $2^l$

-   Max nodes total: $2^{h+1} - 1$

---

# Binary Tree

<br/>

<div grid="~ cols-2 gap-8">
  <div>
    <ul>
      <li>Array</li> 
    </ul>
    <img src="/images/bt_array1.png" style="width: 60%"/>
    <br/>
    <img src="/images/bt_array2.png" style="width: 60%"/>
  </div>  
  <div>
    <ul>
      <li>Left/Right Linked List</li> 
    </ul>
    <img src="/images/bt_ll1.png" style="width: 60%"/>
    <br/>
    <img src="/images/bt_ll2.png" style="width: 60%"/>
  </div> 
</div>

<!--
-->

---

# Binary Tree Traverse (DFS): pre-order

<br/>
<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div class="norm">
    ROOT → Left → Right:  
    <ol>
      <li>Visit the root</li> 
      <li>Traverse the left subtree</li> 
      <li>Traverse the right subtree</li> 
    </ol>
    <p class="hl-color">A B D H I E J C F G K</p>
  </div>  
  <div align="center">
    <img src="/images/bt_traverse.png" style="width: 60%"/>
  </div> 
</div>

<!--
-->

---

# Binary Tree Traverse (DFS): in-order

<br/>
<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div class="norm">
    Left → Root → Right:  
    <ol>
      <li>Traverse the left subtree</li> 
      <li>Visit the root</li>   
      <li>Traverse the right subtree</li> 
    </ol>
    <p class="hl-color">H D I B J E A F C K G</p>
  </div>  
  <div align="center">
    <img src="/images/bt_traverse.png" style="width: 60%"/>
  </div> 
</div>

<!--
-->

---

# Binary Tree Traverse (DFS): post-order

<br/>
<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div class="norm">
    Left → Right → Root:  
    <ol>
      <li>Traverse the left subtree</li> 
      <li>Traverse the right subtree</li> 
      <li>Visit the root</li>   
    </ol>
    <p class="hl-color">H I D J E B F K G C A</p>
  </div>  
  <div align="center">
    <img src="/images/bt_traverse.png" style="width: 60%"/>
  </div> 
</div>

<!--
-->

---

# Binary Tree Traverse (BFS): level order

<br/>
<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div class="norm">
    <ol>
      <li>Visit the root</li>  
      <li>Visit the left node</li> 
      <li>Visit the right node</li> 
      <li>Go to next level</li> 
    </ol>
    <p class="hl-color">A B C D E F G H I J K</p>
  </div>  
  <div align="center">
    <img src="/images/bt_traverse.png" style="width: 60%"/>
  </div> 
</div>

<!--
-->

---

# Binary Tree

<br/>

<div grid="~ cols-2 gap-8">
  <div align="left" class="norm">
    <ul>
      <li>Complete Tree: every level is completely filled except the last (leaf) and all nodes are as far left as possible</li> 
      <br/>
      <li>Full Binary Tree: every node has two child nodes except leaf</li> 
      <br/>
      <li>Perfect Binary Tree: every node has two child nodes except leaf and all leaves on same level</li>   
    </ul>
  </div>  
  <div align="left">
    <img src="/images/binary_tree.png" style="width: 90%"/>
  </div> 
</div>

<!--
-->

---

# Trees

<br/>

<img src="/images/tree.png" style="height: 80%" />

---
layout: center
---

# Summary

---

# Array

<div style="width: 100%">
  <table class="flashcard">
    <thead>
      <tr>
        <th id=""></th>
        <th id=""></th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Concept</th>
        <td>
          <ul>
            <li>consecutive memory space: arr[i].address = base_address + i * data_type_size</li>
            <li>same data type → same size for each element </li>
            <li>fixed length </li>  
          </ul>
        </td>
      </tr>
      <tr class="even">
        <th>Complexity</th>
        <td><span class="hl-strong">Accessing O(1)</span>, Searching O(n)</td>
      </tr>
      <tr class="odd">
        <th>Notes</th>
        <td>
          <ul>
            <li>not memory friendly</li>
            <li>cpu cacheable </li>
            <li>index from 0</li>
            <li>fundamental data structure to implement others such as stack, queue, heap</li>
            <li>data type (programming language) vs. data structure </li>
          </ul>
        </td>
      </tr>
      <tr class="even">
        <th>Hands-on</th>
        <td>dynamic array, stack/queue, binary search, etc. </td>
      </tr>
    </tbody>
  </table>
</div>

---

# Stack

<div style="width: 100%">
  <table class="flashcard">
    <thead>
      <tr>
        <th id=""></th>
        <th id=""></th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Concept</th>
        <td><span class="hl-strong">LIFO/FILO</span></td>
      </tr>
      <tr class="even">
        <th>Complexity</th>
        <td>Accessing O(n), Searching O(n), Inserting/push O(1), Deleting/pop O(1)</td>
      </tr>
      <tr class="odd">
        <th>Notes</th>
        <td>Stack implementation by dynamic array or linked list</td>
      </tr>
      <tr class="even">
        <th>Hands-on</th>
        <td>function call stack, expression matching, etc. </td>
      </tr>
    </tbody>
  </table>
</div>

---

# Queue

<div style="width: 100%">
  <table class="flashcard">
    <thead>
      <tr>
        <th id=""></th>
        <th id=""></th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Concept</th>
        <td><span class="hl-strong">FIFO/LILO</span></td>
      </tr>
      <tr class="even">
        <th>Complexity</th>
        <td>Accessing O(n), Searching O(n), Inserting/enqueue O(1), Deleting/dequeue O(1)</td>
      </tr>
      <tr class="odd">
        <th>Notes</th>
        <td>Queue implementation by dynamic array or linked list</td>
      </tr>
      <tr class="even">
        <th>Hands-on</th>
        <td>priority queue, circular queue, job queue, resource pool, etc. </td>
      </tr>
    </tbody>
  </table>
</div>

---

# Linked List

<div style="width: 100%">
  <table class="flashcard">
    <thead>
      <tr>
        <th id=""></th>
        <th id=""></th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Concept</th>
        <td>
          <ul>
            <li>nonconsecutive memory space</li>
            <li>node: data + pointer</li>
            <li>Single Linked List, Doubly Linked List, Circular Linked List, Positional Linked List </li>  
          </ul>
        </td>
      </tr>
      <tr class="even">
        <th>Complexity</th>
        <td>Accessing O(n), Searching O(n), <span class="hl-strong">Inserting O(1)</span>, <span class="hl-strong">Deleting O(1)</span></td>
      </tr>
      <tr class="odd">
        <th>Notes</th>
        <td>
          <ul>
            <li>accessing slower than array</li>
            <li>with/without head/tail node (which don’t store any data)   </li>
            <li>fundamental data structure to implement others such as skip list, hash table, etc.</li>
          </ul>
        </td>
      </tr>
      <tr class="even">
        <th>Hands-on</th>
        <td>stack, queue, traverse/reverse/update/merge, etc. </td>
      </tr>
    </tbody>
  </table>
</div>

---

# Binary Tree

<div style="width: 100%">
  <table class="flashcard">
    <thead>
      <tr>
        <th id=""></th>
        <th id=""></th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <th>Concept</th>
        <td>
          <ul>
            <li>one root</li>
            <li>max 2 child nodes</li>
            <li>height & depth</li>
            <li>4 traversal (DFS/BFS): in-order(left-root-right), pre-order(root-left-right), post-order(left-right-root), level-order</li> 
            <li>proper, perfect, full, complete binary tree</li> 
          </ul>
        </td>
      </tr>
      <tr class="even">
        <th>Complexity</th>
        <td>
          <ul>
            <li>DFS: time O(n), space O(h) </li>
            <li>BFS: time O(n), space O(n)</li>
          </ul>
        </td>
      </tr>
      <tr class="odd">
        <th>Notes</th>
        <td>stored in array or linked nodes</td>
      </tr>
      <tr class="even">
        <th>Hands-on</th>
        <td>4 traversal</td>
      </tr>
    </tbody>
  </table>
</div>

---

<div id="labs">
</div>

<style>

#labs {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  background: url('/images/lab.jpg');
  background-repeat: no-repeat;
  background-size: cover;
}

</style>

---

# Lab 1

<br/>

<mdi-clipboard-list-outline />

-   download and install Anaconda
-   create and Activate your Anaconda Python env
-   (Optional) install and setup VS Code
-   familiar yourself with Python and do exercise 📝 [lab1.ipynb](https://github.com/fastzhong/mth251/blob/main/notebooks/lab1.ipynb)

---

# Lab 1

#### Download and install Anaconda

<br/>

> <i class="fas fa-external-link-alt"></i> [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

<img src="/images/lab/anaconda_install.png" style="height: 50%"/>

---

# Lab 1

#### Create and Activate your Anaconda Python env

<div class="inline-grid grid-cols-[3fr,4fr] gap-4">
  <div>
    <p class="norm">
      <ol>
        <li>Launch Conda Navigator</li>
        <li>Environments → +Create to create a new env (<strong>mth251</strong>)</li>
        <li>Switch to your Python env <strong>mth251</strong> from “Application on”</li>
        <li>Install Jupyter Notebook</li>
        <li>After that, Launch Jupyter Notebook</li>
      </ol>
    </p> 
  </div>
  <div>
    <p>
        <img src="/images/lab/anaconda_env.png" style="width:60%"/><br/>
        <img src="/images/lab/anaconda_jupyter.png" style="width:60%"/>
    </p>
  </div>  
</div>

---

# Lab 1

#### Create and Activate your Anaconda Python env

<br/>

<pre class="norm">
<i class="far fa-comment-dots"></i> Also possible to perform via command line:
</pre>

```cmd
> # create the env
> conda create -n mth251 python=3.8
> # activate the env
> conda activate mth251
> # install jupyter
> conda install -c conda-forge notebook
> # multipledispatch for lab1
> conda install -c anaconda multipledispatch
> # start jupyter notebook
> jupyter notebook
```

<div grid="~ cols-2 gap-8">
  <div class="norm">
    <ul>
      <li>copy & paste the Jupyter link in the prompt to your browser</li>
      <li>Control-C to stop Jupyter from the command line</li>  
    </ul>
  </div>  
  <div>
    <img src="/images/lab/anaconda_cmd.png" style="height:80%"/>
  </div> 
</div>

---

# Lab 1

#### Create and Activate your Anaconda Python env

<div class="inline-grid grid-cols-[1fr,2fr] gap-4">
  <div>
    <p class="norm">
      <ol start="6">
        <li>Now you are ready to create, edit and run Jupyter notebooks (lab1.ipynb): </li>
      </ol>
    </p>
  </div>
  <div>
    <p><img src="/images/lab/anaconda_notebook.png" style="width:50%"/></p>
  </div>
</div>

---

# Lab 1

#### <logos-visual-studio-code/> VS Code

<br/>

> VS Code now fully integrated with Jupyter notebook, refer to this link:  
> <i class="fas fa-external-link-alt"></i> [Jupyter Notebooks in VS Code](https://www.youtube.com/watch?v=Ozq24uAshXo)

<br/>
<br/>

#### <simple-icons-googlecolab /> Google Colab

<br/>

> Google provides online Jupyter env:  
> <i class="fas fa-external-link-alt"></i> [https://colab.research.google.com/](https://colab.research.google.com/)

notebooks: [https://github.com/fastzhong/mth251/tree/main/notebooks](https://github.com/fastzhong/mth251/tree/main/notebooks)

---

# Lab 1

<br/>

<span class="hl">lab1.ipynb</span>

-   Python

    1. Data Type & Operators
    2. Collections
    3. Program Structure
    4. OO & Class

-   Big O

---

# Lab 2

<br/>

<mdi-clipboard-list-outline />

-   review Array, Stack, Queue, Recursion
-   exercise 📝 [lab2.ipynb](https://github.com/fastzhong/mth251/blob/main/notebooks/lab2.ipynb)
-   priority queue
-   circular queue

---

# Lab 2

#### Exercise: two sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1  
Input: _nums = [2,7,11,15], target = 9_  
Output: _[0,1]_  
Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2  
Input: _nums = [3,2,4], target = 6_  
Output: _[1,2]_

Example 3  
Input: _nums = [3,3], target = 6_  
Output: _[0,1]_

<style>
p {
    font-family: 'Open Sans';
    font-size: 0.8rem;
    line-height: 1.5em;
}
</style>

---

# Lab 2

#### Exercise: valid parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

-   Open brackets must be closed by the same type of brackets.
-   Open brackets must be closed in the correct order.

Example 1  
Input: s = "()[]{}" Output: true  
Example 2  
Input: s = "(]" Output: false  
Example 3  
Input: s = "([)]" Output: false  
Example 4  
Input: s = "{[]}" Output: true

<style>
p {
    font-family: 'Open Sans';
    font-size: 0.8rem;
    line-height: 1.5em;
}
</style>

---

# Lab 2

<br/>

<span class="hl-bg">Priority Queue</span> is similar to queue but the element with higher priority can be moved forward to the front. Use exiting Queue class to implement a priority queue (element with lower value has higher priority).

<pre class="norm">
<i class="far fa-sticky-note"></i> Priority Queue can be used in Printer Jobs or Schedule Tasks.
</pre>

---

# Lab 2

<br/>

<span class="hl-bg">Circular Queue</span> is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

Design your implementation of circular queue.

---

# Lab 2

#### Circular Queue

<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div class="norm">1. init</div>
  <div><img src="/images/lab/cq1_init.png" style="height: 90px"/></div>
  <div class="norm">2. enqueue D1</div>
  <div><img src="/images/lab/cq2.png" style="height: 90px"/></div>  
  <div class="norm">3. enqueue D2, D3, D4 and dequeue D1</div>
  <div><img src="/images/lab/cq3.png" style="height: 90px"/></div>
</div>

---

# Lab 2

#### Circular Queue

<br/>

<div class="inline-grid grid-cols-[1fr,2fr] gap-8">
  <div class="norm">4. enqueue D5, D6, D7, D8</div>
  <div><img src="/images/lab/cq4.png" style="height: 90px"/></div>
  <div class="norm">5. dequeue D2, D3, D4, D5 and enqueue D9, D10</div>
  <div><img src="/images/lab/cq5.png" style="height: 90px"/></div> 
</div>

---

# Lab 2

#### Circular Queue

<br/>

<div class="norm">
<i class="far fa-sticky-note"></i> One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue (and it does not prevent the program accidentally creates a large queue or stack and use up the memory).
</div>

Implementation of CircularQueue class:

<div class="norm">
  <ul>
    <li><strong>enqueue</strong>(): insert the element</li>
    <li><strong>dequeue</strong>(): delete the element</li>
    <li><strong>front</strong>(): return the first element in the queue, if queue is empty, return None</li>
    <li><strong>rear</strong>(): return the last element in the queue, if queue is empty, return None</li>
    <li><strong>is_empty</strong>(): return true if queue is empty</li>
    <li><strong>is_full</strong>(): return true if queue is full</li>
  </ul>
</div>

---

# Lab 3

<br/>

<mdi-clipboard-list-outline />

-   Python (lab1)  
    5. misc.  
    6. PEP8
-   review Singly Linked List, Doubly Linked List
-   review linear search, binary search
-   exercise 📝 [lab3.ipynb](https://github.com/fastzhong/mth251/blob/main/notebooks/lab3.ipynb)

---

# Lab 3

### lineary search & binary search

<br/>

<span class="norm">

1. Go to [https://www.cs.usfca.edu/~galles/visualization/Search.html]([https://www.cs.usfca.edu/~galles/visualization/Search.html]) to understand how Linear Search & Binary Search is working

2. Implement Linear Search & Binary Search in Python by yourself:

-   familiar with Python coding style
-   understand the input, output, steps and ending condition
-   learn and compare different approaches (time & space complexity)
-   test code reliability with different cases

</span>

---

# Lab 3

<br/>

-   implement Stack by linked list
-   implement Queue by linked list
-   reverse a linked list
    -   recursive implementation
    -   iterative implementation

---

# Lab 3

#### Exercise: palindrome

Implement a Python function to determines if a string is a palindrome, for example, ‘racecar’ and ‘level’ are palindromes

<style>
p {
    font-family: 'Open Sans';
    font-size: 0.8rem;
    line-height: 1.5em;
}
</style>

---

# Lab 4

<br/>

<mdi-clipboard-list-outline />

-   review Binary Tree and 4 traverse methods
-   exercise 📝 [lab4.ipynb](https://github.com/fastzhong/mth251/blob/main/notebooks/lab4.ipynb)

---

# Lab 4

#### Exercise: get maximum depth of binary tree

<p class="norm">
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
</p>

<div grid="~ cols-2 gap-8">
  <div class="norm">
    <p><i>For example: the maximum depth is 3</i></p>
    <img src="/images/lab/tree_depth.png" style="width:50%"/>
  </div>  
  <div class="norm">

</div> 
</div>

---

# Lab 4

#### Exercise: check a balanced binary tree

<p class="norm">
A binary tree in which the left and right subtrees of every node differ in height by no more than 1.
</p>

<div grid="~ cols-2 gap-8">
  <div class="norm">
    <p><i>balanced = true:</i></p>
    <img src="/images/lab/tree_balance_true.png" style="width:50%"/>
  </div>  
  <div class="norm">
    <p><i>balanced = false:</i></p>
    <img src="/images/lab/tree_balance_false.png" style="width:50%"/>
  </div> 
</div>

---

# Lab 4

#### Exercise: check a complete binary tree

<p class="norm">
In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
</p>

<div grid="~ cols-2 gap-8">
  <div class="norm">
    <p><i>complete = true:</i></p>
    <img src="/images/lab/tree_complete_true.png" style="width:50%"/>
  </div>  
  <div class="norm">
    <p><i>complete = false:</i></p>
    <img src="/images/lab/tree_complete_false.png" style="width:50%"/>
  </div> 
</div>

---

# Lab 5

<br/>

<mdi-clipboard-list-outline />

-   let us do some leetcode exercises 📝 [lab5.ipynb](https://github.com/fastzhong/mth251/blob/main/notebooks/lab5.ipynb)

---

# Lab 5

#### Exercise: remove duplicate numbers

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1  
Input: _nums = [1,1,2]_  
Output: _2, nums = [1,2]_  
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Example 2  
Input: _nums = [0,0,1,1,1,2,2,3,3,4]_  
Output: _5, nums = [0,1,2,3,4]_  
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.

<style>
p {
    font-family: 'Open Sans';
    font-size: 0.8rem;
    line-height: 1.5em;
}
</style>

---

# Lab 6

<br/>

<mdi-clipboard-list-outline />

-   📝 [lab6.ipynb](https://github.com/fastzhong/mth251/blob/main/notebooks/lab6.ipynb)
