# -*- coding: utf-8 -*-
"""
Courtesy 
https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python#:~:text=size%20of%20children.-,class%20BstNode%3A,-def%20__init__(

Requires that the each node of tree has attributes: self.left, self.right, self.key and self.value
Call display(root node) to print tree.
Prints node.key for each node with proper structure.
"""

def display_aux(self):
      """Returns list of strings, width, height, and horizontal coordinate of the root."""
      # No child.
      if self.right is None and self.left is None:
          line = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
          width = len(line)
          height = 1
          middle = width // 2
          return [line], width, height, middle

      # Only left child.
      if self.right is None:
          lines, n, p, x = display_aux(self.left)
          #s = '%s' % self.key
          s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
          u = len(s)
          first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
          second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
          shifted_lines = [line + u * ' ' for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

      # Only right child.
      if self.left is None:
          lines, n, p, x = display_aux(self.right)
          #s = '%s' % self.key
          s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
          u = len(s)
          first_line = s + x * '_' + (n - x) * ' '
          second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
          shifted_lines = [u * ' ' + line for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

      # Two children.
      left, n, p, x = display_aux(self.left)
      right, m, q, y = display_aux(self.right)
      #s = '%s' % self.key
      s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
      second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
      if p < q:
          left += [n * ' '] * (q - p)
      elif q < p:
          right += [m * ' '] * (p - q)
      zipped_lines = zip(left, right)
      lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
      return lines, n + m + u, max(p, q) + 2, n + u // 2

def display(self):
      lines, *_ = display_aux(self)
      for line in lines:
          print(line)
      print()
      
