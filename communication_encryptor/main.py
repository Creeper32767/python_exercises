from coding import encodelongstring, decodelongstring

while True:
    carry_over = input("[initialization] Enter which base system should we use(2 ~ 35): ")
    if carry_over == "":
        carry_over = 16
        break

    elif carry_over.isdigit():
        carry_over = int(carry_over)
        if 2 <= carry_over <= 35:
            break
        else:
            print("[error] Your number is not in valid range.")

    else:
        print("[error] Your input contains other characters besides numbers.")
    print(f"[info] Current value of carry_over is {carry_over}\n")

while True:
    print("+"*20)
    cmd = input("[command] Enter e(ncode)/d(ecode)/q(uit): ")
    if cmd == "e":
        content = input("[content] Input: ")
        print(encodelongstring(content, carry_over))
    elif cmd == "d":
        content = input("[content] Input: ")
        print(decodelongstring(content.upper(), carry_over))
    elif cmd == "q":
        break
    else:
        print("[error] No such command, please try again.")
    print("\n")
