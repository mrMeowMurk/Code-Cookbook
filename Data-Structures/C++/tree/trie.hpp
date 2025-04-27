#ifndef TRIE_HPP
#define TRIE_HPP

#include <string>
#include <unordered_map>
#include <vector>
#include <memory>

/**
 * @class TrieNode
 * @brief A node in the Trie data structure.
 * 
 * Each node represents a character in a word and contains a map of child nodes.
 */
class TrieNode {
public:
    std::unordered_map<char, std::shared_ptr<TrieNode>> children;
    bool is_end_of_word;
    int word_count;

    TrieNode() : is_end_of_word(false), word_count(0) {}
};

/**
 * @class Trie
 * @brief A Trie (prefix tree) implementation.
 * 
 * A Trie is a tree-like data structure used to store and retrieve strings.
 * It is particularly efficient for operations like:
 * - Inserting a string
 * - Searching for a string
 * - Finding all strings with a given prefix
 */
class Trie {
private:
    std::shared_ptr<TrieNode> root;

    /**
     * @brief Get the node corresponding to the last character of the prefix.
     * 
     * @param prefix The prefix to traverse.
     * @return std::shared_ptr<TrieNode> The node at the end of the prefix, or nullptr if not found.
     */
    std::shared_ptr<TrieNode> get_node(const std::string& prefix) const {
        auto current = root;
        for (char c : prefix) {
            if (current->children.find(c) == current->children.end()) {
                return nullptr;
            }
            current = current->children[c];
        }
        return current;
    }

    /**
     * @brief Collect all words starting from the given node.
     * 
     * @param node The current node.
     * @param prefix The current prefix.
     * @param words The vector to collect words in.
     */
    void collect_words(std::shared_ptr<TrieNode> node, const std::string& prefix, std::vector<std::string>& words) const {
        if (node->is_end_of_word) {
            words.push_back(prefix);
        }

        for (const auto& [c, child] : node->children) {
            collect_words(child, prefix + c, words);
        }
    }

public:
    /**
     * @brief Default constructor.
     */
    Trie() : root(std::make_shared<TrieNode>()) {}

    /**
     * @brief Insert a word into the Trie.
     * 
     * @param word The word to be inserted.
     */
    void insert(const std::string& word) {
        auto current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                current->children[c] = std::make_shared<TrieNode>();
            }
            current = current->children[c];
        }
        current->is_end_of_word = true;
        current->word_count++;
    }

    /**
     * @brief Search for a word in the Trie.
     * 
     * @param word The word to search for.
     * @return true if the word exists in the Trie, false otherwise.
     */
    bool search(const std::string& word) const {
        auto node = get_node(word);
        return node != nullptr && node->is_end_of_word;
    }

    /**
     * @brief Check if any word in the Trie starts with the given prefix.
     * 
     * @param prefix The prefix to check for.
     * @return true if any word starts with the prefix, false otherwise.
     */
    bool starts_with(const std::string& prefix) const {
        return get_node(prefix) != nullptr;
    }

    /**
     * @brief Get all words in the Trie that start with the given prefix.
     * 
     * @param prefix The prefix to search for.
     * @return std::vector<std::string> A vector of words starting with the prefix.
     */
    std::vector<std::string> get_words_with_prefix(const std::string& prefix) const {
        std::vector<std::string> words;
        auto node = get_node(prefix);
        if (node != nullptr) {
            collect_words(node, prefix, words);
        }
        return words;
    }

    /**
     * @brief Delete a word from the Trie.
     * 
     * @param word The word to delete.
     * @return true if the word was deleted, false if it didn't exist.
     */
    bool remove(const std::string& word) {
        if (!search(word)) {
            return false;
        }

        auto current = root;
        std::vector<std::pair<std::shared_ptr<TrieNode>, char>> stack;

        // Find the node and build a stack of nodes to potentially delete
        for (char c : word) {
            stack.push_back({current, c});
            current = current->children[c];
        }

        // Mark the end node as not a word
        current->is_end_of_word = false;
        current->word_count--;

        // Delete nodes if they have no children and are not end of words
        while (!stack.empty() && !current->is_end_of_word && current->children.empty()) {
            auto [parent, c] = stack.back();
            stack.pop_back();
            parent->children.erase(c);
            current = parent;
        }

        return true;
    }
};

#endif // TRIE_HPP 