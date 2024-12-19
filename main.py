import os,time

def banner():
    print("\n***********************************************")
    print("    Electricity Bill Calculate -- TR FAHIM")
    print("***********************************************\n")

def extra_cal(load,main_cal):
    demand_charge=42
    extra_cal_1=(load*demand_charge)
    vat_count = ((main_cal+extra_cal_1)*(5/100))
    total_bill=(main_cal+extra_cal_1+vat_count)
    show_total = round(total_bill, 2)
    vat_ammount_show = round(vat_count, 2)
    
    print(f">> Vat Ammount : {vat_ammount_show}Tk\n>> Demand Charge: {extra_cal_1}Tk")
    print("\n---------------------------------")
    print(f"    Total Bill: {show_total}Tk")
    print("---------------------------------\n")

def cl():
    os.system("cls")

def face_1(use,load,main_cal):
    main_cal = (use*5.26)
    os.system("cls")
    banner()
    time.sleep(3)
    print(f"\n>> Electricity Bill: {round(main_cal, 2)}Tk")
    extra_cal(load,use,main_cal)

def face_2(main_cal):
    os.system("cls")
    banner()
    time.sleep(3)
    print(f"\n>> Electricity Bill: {round(main_cal, 2)}tk")
    
def face_3(main_cal):
    os.system("cls")
    banner()
    time.sleep(3)
    print(f"\n>> Electricity Bill: {round(main_cal, 2)}tk")

def face_4(main_cal):
    os.system("cls")
    banner()
    time.sleep(3)
    print(f"\n>> Electricity Bill: {round(main_cal, 2)}tk")
    
def face_5(main_cal):
    os.system("cls")
    banner()
    time.sleep(3)
    print(f">> Electricity Bill: {round(main_cal, 2)}tk")

def face_6(main_cal): 
    os.system("cls")
    banner()
    time.sleep(3)
    print(f">> Electricity Bill: {round(main_cal, 2)}tk")

def main():
    cal1=(75*5.26)
    cal2=(125*7.2)
    cal3=(100*7.59)
    cal4=(100*8.02)
    cal5=(200*12.67)
    cl()
    banner()
    use = float(input("\nTotal Unit (KWH/Unit): "))
    load = float(input("Demand Load (KW): "))
    main_cal=float()
      
    if use <= 75:
        face_1(use,load, main_cal)
        
    elif use <= 200:
        t_cal = (use-75)
        f_cal = (t_cal*7.2)
        main_cal = (cal1+f_cal)
        face_2(main_cal)
        extra_cal(load, main_cal)
    
    elif use <= 300:
        t_cal = (use-200)
        f_cal = (t_cal*7.59)
        main_cal = (cal1+cal2+f_cal)
        face_3(main_cal)
        extra_cal(load, main_cal)
    
    elif use <= 400:
        t_cal = (use-300)
        f_cal = (t_cal*8.02)
        main_cal = (cal1+cal2+cal3+f_cal)
        face_4(main_cal)
        extra_cal(load, main_cal)
    
    elif use <= 600:
        t_cal = (use-400)
        f_cal = (t_cal*12.67)
        main_cal = (cal1+cal2+cal3+cal4+f_cal)
        face_5(main_cal)
        extra_cal(load, main_cal)
    
    elif use > 600:
        t_cal = (use-600)
        f_cal = (t_cal*14.61)
        main_cal = (cal1+cal2+cal3+cal4+cal5+f_cal)
        face_6(main_cal)
        extra_cal(load, main_cal)
    
    else:
        print("\nSomething Wrong !!")
        
        

if __name__ == "__main__":
    main()
