class Identifier:
    def validate_identifier(self, s: str) -> bool:
        if len(s) == 0:
            return False

        if not self.valid_s(s[0]):
            return False

        for ch in s[1:]:
            if not self.valid_f(ch):
                return False

        if 1 <= len(s) <= 6:
            return True
        
        return False

    def valid_s(self, ch: str) -> bool:
        return ch.isalpha()

    def valid_f(self, ch: str) -> bool:
        return ch.isalnum()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Use: python identifier.py <string>")
    else:
        id = Identifier()
        if id.validate_identifier(sys.argv[1]):
            print("Valid")
        else:
            print("Invalid")


