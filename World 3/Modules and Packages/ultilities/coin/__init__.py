def double(price=0, formatt=False):
    ans = price * 2
    return ans if formatt is False else coin(ans)


def half(price=0, formatt=False):
    ans = price / 2
    return ans if formatt is False else coin(ans)


def up(price=0, up=0, formatt=False):
    ans = price + (price * up / 100)
    return ans if formatt is False else coin(ans)


def down(price=0, off=0, formatt=False):
    ans = price - (price * off / 100)
    return ans if formatt is False else coin(ans)


def coin(price=0, cifrao="R$"):
    return f"{cifrao}{price:>.2f}".replace(".", ",")


def resum(price=0, upp=0, off=0, formatt=False):
    print("-" * 30)
    print("Values Convertion".center(30))
    print("-" * 30)
    print(f"The double is: \t{double(price, formatt)}")
    print(f"The half is: \t\t{half(price, formatt)}")
    print(f"The 19% is: \t\t{up(price, upp, formatt)}")
    print(f"The 28% is: \t\t{down(price, off, formatt)}")
    print("-" * 30)
