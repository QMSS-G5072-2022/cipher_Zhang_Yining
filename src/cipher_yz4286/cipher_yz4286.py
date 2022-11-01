def cipher(text, shift, encrypt=True):
    """
    Each letter is replaced by a letter some fixed number of positions down the alphabet

    Parameters
    ----------
    text : String
      A string you wish to encrypt or decrypt 
    shift : integer
      A integer that represent the number of position down the alphabet
    encrypt : Booleon
      A true or false value that represents encrypt or decrypt
    
    Returns
    -------
    String
      The new string after encrypt

    Examples
    --------
    >>> cipher('coffee!',1,  encrypt=True)
    oYoY
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text