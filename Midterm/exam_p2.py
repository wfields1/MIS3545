import string
alpha_list = string.ascii_lowercase

def load_wordlist(file_name):
    '''
    '''
    print('Loading word list from file...')
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

def is_a_valid_word(word_list, word):
    '''    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_joke_string():
    """
    Returns: an article in encrypted text.
    """
    f = open("joke.txt", "r", encoding = 'utf-8') #can't read the apostrophe without this
    joke = str(f.read())
    f.close()
    return joke

WORDLIST_FILENAME = 'words.txt'


class Text(object):

    def __init__(self, text):
        '''
        Initializes a Text object
        '''
        self.text = text
        self.valid_words = load_wordlist(WORDLIST_FILENAME)

    def get_text(self):
        '''
        Returns: self.text
        '''
        return self.text

    def get_valid_words(self):
        '''
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def create_moved_dict(self, move):
        moved_dict = {}
        for location in range(len(alpha_list)):
            location_updated = location + move
            if location_updated >= 26:
                location_updated = location_updated - 26
            moved_dict[alpha_list[location]] = alpha_list[location_updated]
        return moved_dict

    def apply_move(self, move):
        word_updated = ''
        upper_case = False
        dict_updated = self.create_moved_dict(move)
        if move < 0:
            print('Move must be greater than 0')
            return False
        if move > 26:
            print('Move must be less than 26')
            return False
        for character in self.text:
            if character.iscapital():
                upper_case = True
                character = character.lower()
                character = dict_updated[character]
            elif upper_case:
                character = character.upper()
            upper_case = False
        return(word_updated)





        '''
        Applies the cipher to self.text with the input move       

        move: an integer, 0 <= move < 26

        Returns: the text (string) in which every character is moved
             down the alphabet by the input move
        '''
        pass  # delete this line and replace with your code here


class PlainText(Text):

    def __init__(self, text, move):
        self.text = text
        self.move = move
        text.__init__(self,self.text)

    def get_move(self):
        return self.move

    def get_encrypting_dict(self):
        return self.create_moved_dict(self.move)

    def get_encrypted_text(self):
        return self.apply_move(self.move)

    def change_move(self, move):
        self.move = move


class CipherText(Text):

    def __init__(self, text):
        self.text = text
        text.__init__(self, self.text)

    ### YOU NEED TO MODIFY THIS METHOD ###
    def decrypt_text(self):
        if ' ' in self.text:
            alpha_list_updated = {}
            word_updated = 0
            words = self.text.split()
            for attempt in range(len(alpha_list)):
                for word in words:
                    word_attempt = text(word)
                    word_updated


        '''
        Decrypt self.text by trying every possible move value
        and find the "best" one. We will define "best" as the move that
        creates the maximum number of real words when we use apply_move(move)
        on the text. If s is the original move value used to encrypt
        the text, then we would expect 26 - s to be the best move value 
        for decrypting it.

        Returns: a tuple of the best move value used to decrypt the text
        and the decrypted  text using that move value. Check out the
        test case in main function below.

        '''
        pass  # delete this line and replace with your code here


def decrypt_joke():
    joke = CipherText(get_joke_string())
    return joke.decrypt_text()

def main():
    # Example test case (PlainText)
    plaintext = PlainText('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_encrypted_text())

    # Example test case (CipherText)
    ciphertext = CipherText('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_text())

    print(decrypt_joke())

if __name__ == '__main__':
    main()
