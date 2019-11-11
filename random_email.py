import random, string
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains):  #called fourth
    return random.choice(domains)

def get_random_name(letters, length):   #called third
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(n, length):  #called second
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(n)]

def main():  #called first
    print(generate_random_emails(10, 7))

if __name__ == "__main__":
    main()