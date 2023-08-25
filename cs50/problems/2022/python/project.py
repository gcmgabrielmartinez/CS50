#submit50 cs50/problems/2022/python/project
#Gabriel Calvo Martinez, Brazil, Rio de Janeiro

def main():

    try:
        paper = input("Investment paper: ").strip().title()
        if paper not in ["Treasury Bill", "Treasury Note"]:
            raise ValueError

        yield_rate = float(input("Yield rate: "))
        if yield_rate < 0:
            raise ValueError

        elif paper == "Treasury Bill":
            coupon_rate = None

        elif paper == "Treasury Note":
            coupon_rate = input("Coupon rate: ")
            if coupon_rate == "":
                coupon_rate = yield_rate
            else:
                coupon_rate = float(coupon_rate)
                if coupon_rate < 0:
                    #print("here")
                    raise ValueError
        else:
            print("here")
            raise ValueError

        maturity = float(input("Maturity: "))
        if maturity < 0:
            raise ValueError
        face_value = 1000

        example2 = {"paper": paper, "yield_rate": yield_rate, "coupon_rate": coupon_rate, "maturity": maturity, "face_value":face_value}

    except ValueError:
        exit("Invalid Value")

    price = present_value(**example2)
    duration = maccauly_duration(**example2)
    duration_m = modified_duration(**example2)

    example2["price"] = price
    example2["duration"] = duration
    example2["mod_duration"] = duration_m

    if example2["paper"] == "Treasury Bill":
        print(f"For a {example2['paper'] } of face value of {example2['face_value']}:\n - yield rate: {example2['yield_rate']}\n - maturity: {example2['maturity']}\n - price: {example2['price']}\n - duration: {example2['duration']}\n - modified duration: {example2['mod_duration']}")
    elif example2["paper"] == "Treasury Note":
        print(f"For a {example2['paper']} of face value of {example2['face_value']}:\n - yield rate: {example2['yield_rate']}\n - coupon rate: {example2['coupon_rate']}\n - maturity: {example2['maturity']}\n - price: {example2['price']}\n - duration: {example2['duration']}\n - modified duration: {example2['mod_duration']}")
    else:
        print("Invalid financial asset")



def present_value(yield_rate = 0.05, maturity = 1, coupon_rate = None, face_value = 1000, paper = "Treasury Bill"):
    if paper == "Treasury Bill":
        return round(face_value /pow(1 + yield_rate, maturity), 2)

    elif paper == "Treasury Note":
        yield_rate = pow(1+yield_rate, 0.5) - 1
        if coupon_rate == None:
            coupon_rate = yield_rate
        else:
            coupon_rate = pow(1 + coupon_rate, 0.5) - 1

        return round(face_value/pow(1 + yield_rate, maturity*2) + face_value*coupon_rate/yield_rate*(1 - 1/pow(1 + yield_rate, maturity*2)), 2)
    else:
        print("Class not supported")


def maccauly_duration(yield_rate = 0.05, maturity = 1, coupon_rate = None, face_value = 1000, paper = "Treasury Bill"):
    if paper == "Treasury Bill":
        return round(maturity, 2)

    elif paper == "Treasury Note":
        yield_rate = pow(1+yield_rate, 0.5) - 1
        if coupon_rate == None:
            coupon_rate = yield_rate
        else:
            coupon_rate = pow(1+coupon_rate, 0.5) - 1
        return round((1 + yield_rate)/(yield_rate*2) - (1 + yield_rate + maturity*2*(yield_rate - coupon_rate))/ (2*coupon_rate*(pow(1 + yield_rate, maturity*2)-1) + 2*yield_rate), 2)
    else:
        return "Class not supported"


def modified_duration(yield_rate = 0.05, maturity = 1, coupon_rate = None, face_value = 1000, paper = "Treasury Bill"):
    duration = maccauly_duration(yield_rate, maturity, coupon_rate, face_value, paper)
    if paper == "Treasury Bill":
        return round(duration/(1+yield_rate), 2)
    elif paper == "Treasury Note":
        return round(duration/pow(1+yield_rate, 0.5), 2)
    else:
        return "Class not supported"


if __name__ == "__main__":
    main()