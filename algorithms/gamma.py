from algorithms.cipher import Cipher

class GammaCipher(Cipher):
    def __init__(self, key,block_size=4):
        super().__init__()
        self.key = self._preprocess_text(key)  
        self.block_size = block_size

    def encrypt(self, plaintext):
        plaintext = self._preprocess_text(plaintext)
        blocks = self._split_into_blocks(plaintext, self.block_size)  # Розбиваємо на блоки
        alphabet = self._get_alphabet(plaintext)
        result = []

        for block in blocks:
            block_result = []
            for i, char in enumerate(block):
                if char in alphabet:
                    key_char = self.key[i % len(self.key)]  
                    encrypted_char = self._convert_to_char(
                        (self._get_index(char, alphabet) + self._get_index(key_char, alphabet)) % len(alphabet),
                        alphabet  
                    )
                    block_result.append(encrypted_char)
                else:
                    block_result.append(char)

            result.append(''.join(block_result))

        return ''.join(result)
    

   