def valid_amount(amount):
    try:
        amount = float(amount)

        if amount > 0:
            return True
        else:
            return False

    except:
        return False


def valid_text(text):
    if text.strip() != "":
        return True
    else:
        return False