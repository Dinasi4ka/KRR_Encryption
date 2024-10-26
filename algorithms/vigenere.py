from algorithms.cipher import Cipher

class VigenereCipher(Cipher):
    def __init__(self,key, block_size=4):
        super().__init__()
        self.key = key
        self.block_size = block_size

    def encrypt(self, plaintext):
        plaintext = self._preprocess_text(plaintext)
        blocks = self._split_into_blocks(plaintext, self.block_size)  # Розбиваємо на блоки
        result = []

        for block in blocks:
            block_result = []
            for i, char in enumerate(block):
                if char in self.ukrainian_alphabet or char in self.english_alphabet:
                    alphabet = self._get_alphabet(char)
                    key_char = self.key[i % len(self.key)]
                    shift = self._get_index(key_char, self.ukrainian_alphabet) if key_char in self.ukrainian_alphabet else self._get_index(key_char, self.english_alphabet)

                    char_index = self._get_index(char, alphabet)
                    encrypted_char = self._convert_to_char((char_index + shift) % len(alphabet), alphabet)
                    block_result.append(encrypted_char)
                else:
                    block_result.append(char)

            result.append(''.join(block_result))

        return ''.join(result)

   