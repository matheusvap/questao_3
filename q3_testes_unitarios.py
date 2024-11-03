import unittest
from aes_decrypt import aes_decrypt_ecb

class TestAESDecryptECB(unittest.TestCase):
    
    def setUp(self):
        # Configurações comuns aos testes
        self.correct_key = "thisisasecretkey"  # Chave correta de 128 bits
        self.encrypted_hex = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"  # Código hexadecimal de teste
        self.expected_output = "Sistemas Embarcados"  # Saída esperada após decodificação

    def test_decrypt_valid_hex(self):
        """Teste de decodificação com chave e código válidos"""
        result = aes_decrypt_ecb(self.encrypted_hex, self.correct_key)
        self.assertEqual(result, self.expected_output)

    def test_decrypt_invalid_key(self):
        """Teste de decodificação com chave incorreta"""
        invalid_key = "wrongsecretkey!"  # Chave incorreta
        with self.assertRaises(ValueError):
            aes_decrypt_ecb(self.encrypted_hex, invalid_key)

    def test_decrypt_invalid_hex(self):
        """Teste com código hexadecimal inválido"""
        invalid_hex = "thisisnotvalidhex"
        with self.assertRaises(ValueError):
            aes_decrypt_ecb(invalid_hex, self.correct_key)

    def test_decrypt_short_key(self):
        """Teste com chave menor que 128 bits"""
        short_key = "shortkey"  # Chave muito curta
        with self.assertRaises(ValueError):
            aes_decrypt_ecb(self.encrypted_hex, short_key)

    def test_decrypt_long_key(self):
        """Teste com chave maior que 128 bits"""
        long_key = "thiskeyistoolongforaes"  # Chave muito longa
        with self.assertRaises(ValueError):
            aes_decrypt_ecb(self.encrypted_hex, long_key)

# Executar os testes
if __name__ == "__main__":
    unittest.main()