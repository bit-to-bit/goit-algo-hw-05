"""Test TASK 1 hash table"""

from hash_table import HashTable

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))  # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

# Тестуємо видалення
print(H.delete("apple"))
print(H.delete("apple"))
print(H.get("apple"))
H.insert("apple", 10)
print(H.get("apple"))  # Виведе: 10
