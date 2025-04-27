#include <iostream>
#include <vector>
#include <list>
#include <string>

class HashTable {
private:
    std::vector<std::list<std::pair<int, std::string>>> table;
    int size;
    
    int hashFunction(int key) {
        return key % size;
    }
    
public:
    HashTable(int tableSize) : size(tableSize) {
        table.resize(size);
    }
    
    void insert(int key, const std::string& value) {
        int index = hashFunction(key);
        table[index].push_back(std::make_pair(key, value));
    }
    
    std::string search(int key) {
        int index = hashFunction(key);
        
        // Search in the chain
        for (const auto& item : table[index]) {
            if (item.first == key) {
                return item.second;  // Return the value
            }
        }
        
        return "";  // Key not found
    }
};

int main() {
    // Create a hash table
    HashTable hashTable(10);
    
    // Insert some key-value pairs
    hashTable.insert(1, "One");
    hashTable.insert(2, "Two");
    hashTable.insert(11, "Eleven");  // This will cause a collision with key 1
    
    // Search for keys
    std::cout << "Searching for key 1: " << hashTable.search(1) << std::endl;
    std::cout << "Searching for key 2: " << hashTable.search(2) << std::endl;
    std::cout << "Searching for key 11: " << hashTable.search(11) << std::endl;
    std::cout << "Searching for key 3: " << hashTable.search(3) << std::endl;  // Not found
    
    return 0;
} 