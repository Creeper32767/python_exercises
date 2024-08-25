import validation

id_number = input("[initialization] 请输入你的身份证号码: ")
id_number_obj = validation.id_card_verification(id_number)

if id_number_obj.check_length():
    print("[info] 身份证号码位数检查通过!")
    print(f"[info] 你是 {id_number_obj.check_city_code()} 人.")
    if id_number_obj.check_verification_number():
        print("[info] 身份证号码校验码检查通过!")
        try:
            call, age = id_number_obj.check_age()
            print(f"[info] 你是一个 {call}, 在当前年份内 {age} 岁.")
        except ValueError:
            print("[error] 你输入了错误的生日!")

    else:
        print("[error] 身份证号码校验码错误!")

else:
    print("[error] 身份证号码位数不为18位!")

input("Finished. Press 'Enter' to exit.")
