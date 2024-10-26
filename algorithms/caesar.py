from algorithms.cipher import Cipher

class CaesarCipher(Cipher):
    def __init__(self, shifts, block_size=4):
        super().__init__()
        self.shifts = [int(shift) for shift in shifts]  
        self.block_size = block_size

    
    def encrypt(self, plaintext):
        plaintext = self._preprocess_text(plaintext)
        blocks = self._split_into_blocks(plaintext, self.block_size)  # Розбиваємо на блоки
        alphabet = self._get_alphabet(plaintext)
        result = []

        shift_len = len(self.shifts)

        for block in blocks:
            block_result = []
            for i, char in enumerate(block):
                if char in alphabet:
                    shift = self.shifts[i % shift_len]  
                    index = (self._get_index(char, alphabet) + shift) % len(alphabet)
                    encrypted_char = self._convert_to_char(index, alphabet)  
                    block_result.append(encrypted_char)
                else:
                    block_result.append(char)  

            result.append(''.join(block_result))

        return ''.join(result)

   
