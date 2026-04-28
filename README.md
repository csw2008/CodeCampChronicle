# 🏆 CodeCampChronicle

> An ongoing collection of algorithm implementations for LeetCode/NowCoder, dedicated to grad school summer camps and interview prep.

## Acknowledgments

This repository was created as I follow along with the data structures and algorithms tutorial by **Teacher Zuo** (左程云). 

- 📺 **Video Tutorial:** [Bilibili Link](https://www.bilibili.com/video/BV13g41157hK/) *(in Chinese)*
- 👨‍💻 **Teacher Zuo's GitHub:** [@algorithmzuo](https://github.com/algorithmzuo)

---

## 🗂️ Sorting

| Platform | Problem | Problem Style | Solution | Solution Description |
| :--- | :--- | :--- | :--- | :--- |
| LeetCode <br> [Sorting](https://leetcode.cn/problem-list/sorting/) | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) <br> [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) | Core Code Mode | [leetcode912.py](./src/Sorting/leetcode912.py) | $O(N\log N)$ implementation of MergeSort, QuickSort and HeapSort | 
| LeetCode <br> [Sorting](https://leetcode.cn/problem-list/sorting/) | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array) <br> [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array) | Core Code Mode | [leetcode215.py](./src/Sorting/leetcode215.py) | $O(N)$ implementation of QuickSelect Method, inspired by QuickSort |
| LeetCode | [LCR 170. 交易逆序对的总数](https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/) | Core Code Mode | [leetcodeLCR170.py](./src/Sorting/leetcodeLCR170.py) | inspired by MergeSort and taught by Teacher [Zuo](https://www.bilibili.com/video/BV13g41157hK?t=3685.5&p=4) |
| LeetCode <br> [Sorting](https://leetcode.cn/problem-list/sorting/) | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) <br> [56. 合并区间](https://leetcode.cn/problems/merge-intervals/) | Core Code Mode | [leetcode56.py](./src/Sorting/leetcode56.py) | Directly use `list.sort(key=..., reverse=...)` and lambda function to quickly sort the [int,int] |
| LeetCode <br> [Sorting](https://leetcode.cn/problem-list/sorting/) | [179. Largest Number](https://leetcode.com/problems/largest-number/) <br> [179. 最大数](https://leetcode.cn/problems/largest-number/) | Core Code Mode | [leetcode179.py](./src/Sorting/leetcode179.py) | Use `cmp_to_key` in advanced function tool `functools` and two-parameter lambda function to skillfully implement "cmp" function in `key` parameter |
| NowCoder <br> [面试TOP101](https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=295) | [BM17. 二分查找-I](https://www.nowcoder.com/practice/d3df40bd23594118b57554129cadf47b?tpId=295&tqId=1499549&sourceUrl=%2Fexam%2Foj%3FquestionJobId%3D10%26subTabName%3Donline_coding_page) | Core Code Mode | [nowcoderBM17.py](./src/Sorting/nowcoderBM17.py) | bisection method |
| NowCoder <br> [面试TOP101](https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=295) | [BM18. 二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=295&tqId=23256&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AC%2594%25E9%259D%25A2%25E8%25AF%2595%25E7%25AF%2587%26topicId%3D295) | Core Code Mode | [nowcoderBM18.py](./src/Sorting/nowcoderBM18.py) | reframe the problem and treat the 2D array as a Binary Search Tree(BST) |
| NowCoder <br> [面试TOP101](https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=295) | [BM19. 寻找峰值](https://www.nowcoder.com/practice/fcf87540c4f347bcb4cf720b5b350c76?tpId=295&tqId=2227748&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AC%2594%25E9%259D%25A2%25E8%25AF%2595%25E7%25AF%2587%26topicId%3D295) | Core Code Mode | [nowcoderBM19.py](./src/Sorting/nowcoderBM19.py) | bisection method, given the changing tendency |
| NowCoder <br> [面试TOP101](https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=295) | [BM20. 数组中的逆序对](https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=295&tqId=23260&sourceUrl=%2Fexam%2Foj%3FquestionJobId%3D10%26subTabName%3Donline_coding_page) | Core Code Mode | [nowcoderBM20.py](./src/Sorting/nowcoderBM20.py) | same as [LeetCode LCR 170](https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/) |
| NowCoder <br> [面试TOP101](https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=295) | [BM21. 旋转数组的最小数字](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=295&tqId=23269&sourceUrl=%2Fexam%2Foj%3FquestionJobId%3D10%26subTabName%3Donline_coding_page) | Core Code Mode | [nowcoderBM21.py](./src/Sorting/nowcoderBM21.py) | bisection method, only one side comparation |
| NowCoder <br> [面试TOP101](https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=295) | [BM22. 比较版本号](https://www.nowcoder.com/practice/2b317e02f14247a49ffdbdba315459e7?tpId=295&tqId=1024572&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AC%2594%25E9%259D%25A2%25E8%25AF%2595%25E7%25AF%2587%26topicId%3D295) | Core Code Mode | [nowcoderBM22.py](./src/Sorting/nowcoderBM22.py) | `str.split()` |


> to be done: leetcode148
---

## 🔗 Linked List

| Platform | Problem | Problem Style | Solution | Solution Description |
| :--- | :--- | :--- |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [2. 两数相加](https://leetcode.cn/problems/add-two-numbers) | Core Code Mode | [leetcode2.py](./src/LinkedList/leetcode2.py) | 链表基本操作 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [19. 删除链表的倒数第N个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list) | Core Code Mode | [leetcode19.py](./src/LinkedList/leetcode19.py) | 双指针，正数倒数转换 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists) | Core Code Mode | [leetcode21.py](./src/LinkedList//leetcode21.py) | 虚拟头节点，链表合并 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists) | Core Code Mode | [leetcode23.py](./src/LinkedList/leetcode23.py) | 堆，实现一个包装类重载节点的小于魔法方法`__lt__` | 
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs) | Core Code Mode | [leetcode24.py](./src/LinkedList/leetcode24.py) | 虚拟头节点 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [25. K个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group) | Core Code Mode | [leetcode25.py](./src/LinkedList/leetcode25.py) | 链表的翻转 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [61. 旋转链表](https://leetcode.cn/problems/rotate-list/) | Core Code Mode | [leetcode61.py](./src/LinkedList/leetcode61.py) | 虚拟头节点 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [82. 删除排序链表中的重复元素II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii) | Core Code Mode | [leetcode82.py](./src/LinkedList/leetcode82.py) | 虚拟头节点 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list) | Core Code Mode | [leetcode83.py](./src/LinkedList/leetcode83.py) | 虚拟头节点 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [86. 分隔链表](https://leetcode.cn/problems/partition-list) | Core Code Mode | [leetcode86.py](./src/LinkedList/leetcode86.py) | 链表的连接关系变换 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [92. 反转链表II](https://leetcode.cn/problems/reverse-linked-list-ii) | Core Code Mode | [leetcode92.py](./src/LinkedList/leetcode92.py) | 虚拟头节点，链表的翻转 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [138. 随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer) | Core Code Mode | [leetcode138.py](./src/LinkedList/leetcode138.py) | 左神上课讲过额外空间O(1)的方法 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle) | Core Code Mode | [leetcode141.py](./src/LinkedList/leetcode141.py) | 快慢指针 |
| LeetCode <br> [LinkedList](https://leetcode.cn/problem-list/linked-list/) | [142. 环形链表II](https://leetcode.cn/problems/linked-list-cycle-ii) | Core Code Mode | [leetcode142.py](./src/LinkedList/leetcode142.py) | 快慢指针固定套路，记住 |




---

## 🌳 Binary Tree

| Platform | Problem | Solution |
| :--- | :--- | :--- |
| | | |
