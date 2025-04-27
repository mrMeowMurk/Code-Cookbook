/**
 * @file hash_table.hpp
 * @brief Hash Table implementation in C++
 * 
 * A hash table is a data structure that implements an associative array abstract data type,
 * a structure that can map keys to values. It uses a hash function to compute an index into
 * an array of buckets or slots, from which the desired value can be found.
 * 
 * Time Complexity:
 * - Insert: O(1) average case, O(n) worst case
 * - Delete: O(1) average case, O(n) worst case
 * - Search: O(1) average case, O(n) worst case
 * 
 * Space Complexity: O(n)
 */

#ifndef HASH_TABLE_HPP
#define HASH_TABLE_HPP

#include <vector>
#include <list>
#include <stdexcept>
#include <functional>

template<typename K, typename V>
class HashTable {
private:
    struct Entry {
        K key;
        V value;
        
        Entry(const K& key, const V& value) : key(key), value(value) {}
    };

    std::vector<std::list<Entry>> table;
    size_t size;
    size_t count;
    float load_factor;
    std::hash<K> hash_function;

    size_t get_index(const K& key) const {
        return hash_function(key) % size;
    }

    void resize() {
        std::vector<std::list<Entry>> old_table = table;
        size *= 2;
        table = std::vector<std::list<Entry>>(size);
        count = 0;

        for (const auto& bucket : old_table) {
            for (const auto& entry : bucket) {
                insert(entry.key, entry.value);
            }
        }
    }

public:
    /**
     * @brief Default constructor
     * @param initial_size The initial size of the hash table
     * @param load_factor The load factor threshold for resizing
     */
    HashTable(size_t initial_size = 10, float load_factor = 0.75)
        : size(initial_size), count(0), load_factor(load_factor) {
        table = std::vector<std::list<Entry>>(size);
    }

    /**
     * @brief Insert a key-value pair into the hash table
     * @param key The key to insert
     * @param value The value to insert
     */
    void insert(const K& key, const V& value) {
        if (static_cast<float>(count) / size >= load_factor) {
            resize();
        }

        size_t index = get_index(key);
        auto& bucket = table[index];

        // Check if key already exists
        for (auto& entry : bucket) {
            if (entry.key == key) {
                entry.value = value;
                return;
            }
        }

        bucket.emplace_back(key, value);
        count++;
    }

    /**
     * @brief Delete a key-value pair from the hash table
     * @param key The key to delete
     * @return true if the key was deleted, false otherwise
     */
    bool remove(const K& key) {
        size_t index = get_index(key);
        auto& bucket = table[index];

        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->key == key) {
                bucket.erase(it);
                count--;
                return true;
            }
        }

        return false;
    }

    /**
     * @brief Search for a value by key in the hash table
     * @param key The key to search for
     * @return The value associated with the key, or nullptr if not found
     */
    V* search(const K& key) {
        size_t index = get_index(key);
        auto& bucket = table[index];

        for (auto& entry : bucket) {
            if (entry.key == key) {
                return &entry.value;
            }
        }

        return nullptr;
    }

    /**
     * @brief Get the number of key-value pairs in the hash table
     * @return The number of key-value pairs
     */
    size_t get_size() const {
        return count;
    }

    /**
     * @brief Check if the hash table is empty
     * @return true if the hash table is empty, false otherwise
     */
    bool is_empty() const {
        return count == 0;
    }

    /**
     * @brief Remove all key-value pairs from the hash table
     */
    void clear() {
        table = std::vector<std::list<Entry>>(size);
        count = 0;
    }

    /**
     * @brief Get all keys in the hash table
     * @return A vector of all keys
     */
    std::vector<K> keys() const {
        std::vector<K> result;
        for (const auto& bucket : table) {
            for (const auto& entry : bucket) {
                result.push_back(entry.key);
            }
        }
        return result;
    }

    /**
     * @brief Get all values in the hash table
     * @return A vector of all values
     */
    std::vector<V> values() const {
        std::vector<V> result;
        for (const auto& bucket : table) {
            for (const auto& entry : bucket) {
                result.push_back(entry.value);
            }
        }
        return result;
    }

    /**
     * @brief Get all key-value pairs in the hash table
     * @return A vector of (key, value) pairs
     */
    std::vector<std::pair<K, V>> items() const {
        std::vector<std::pair<K, V>> result;
        for (const auto& bucket : table) {
            for (const auto& entry : bucket) {
                result.emplace_back(entry.key, entry.value);
            }
        }
        return result;
    }
};

#endif // HASH_TABLE_HPP 